# -*- coding: utf-8 -*-
from fastapi import FastAPI, Depends, HTTPException, Header, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

from database import engine, Base, get_db
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Rakhi Surprise Answer Collection API",
    description="Interactive answer collection and milestone tracker for Prerna's Rakhi surprise.",
    version="2.0.0"
)

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://127.0.0.1:5500,http://localhost:8000,http://127.0.0.1:8000,http://localhost:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS if os.getenv("ENVIRONMENT") == "production" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "peda2026")

@app.get("/health")
def health_check():
    return {"status": "ok", "app": "Rakhi Surprise API v2", "timestamp": datetime.utcnow().isoformat()}

@app.post("/api/answer", status_code=status.HTTP_200_OK)
def submit_answer(payload: schemas.AnswerCreate, db: Session = Depends(get_db)):
    session_obj = db.query(models.VisitorSession).filter(models.VisitorSession.id == payload.session_id).first()
    if not session_obj:
        session_obj = models.VisitorSession(id=payload.session_id, started_at=datetime.utcnow())
        db.add(session_obj)
        db.commit()

    existing_answer = db.query(models.SessionAnswer).filter(
        models.SessionAnswer.session_id == payload.session_id,
        models.SessionAnswer.question_id == payload.question_id
    ).first()

    if existing_answer:
        existing_answer.answer = payload.answer
        existing_answer.question_text = payload.question_text
    else:
        new_answer = models.SessionAnswer(
            session_id=payload.session_id,
            question_id=payload.question_id,
            question_text=payload.question_text,
            answer=payload.answer,
            created_at=datetime.utcnow()
        )
        db.add(new_answer)

    db.commit()
    return {"status": "success", "message": "Answer/Milestone recorded"}

@app.post("/api/complete", status_code=status.HTTP_200_OK)
def complete_session(payload: schemas.CompleteSession, db: Session = Depends(get_db)):
    session_obj = db.query(models.VisitorSession).filter(models.VisitorSession.id == payload.session_id).first()
    if not session_obj:
        session_obj = models.VisitorSession(id=payload.session_id, started_at=datetime.utcnow())
        db.add(session_obj)

    session_obj.is_completed = True
    session_obj.completed_at = datetime.utcnow()
    db.commit()
    return {"status": "success", "message": "Session completed"}

@app.post("/api/admin/login")
def admin_login(payload: schemas.AdminLogin):
    if payload.password != ADMIN_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    return {"status": "authenticated", "token": "admin-session-authenticated"}

def verify_admin(authorization: str = Header(None)):
    if not authorization or authorization != "Bearer admin-session-authenticated":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return True

@app.get("/api/admin/sessions")
def get_admin_sessions(db: Session = Depends(get_db), auth: bool = Depends(verify_admin)):
    sessions = db.query(models.VisitorSession).order_by(models.VisitorSession.started_at.desc()).all()
    results = []
    for s in sessions:
        results.append({
            "id": s.id,
            "started_at": s.started_at,
            "is_completed": s.is_completed,
            "completed_at": s.completed_at,
            "answers_count": len(s.answers)
        })
    
    total = len(sessions)
    completed = sum(1 for s in sessions if s.is_completed)
    in_progress = total - completed
    total_answers = db.query(models.SessionAnswer).count()

    return {
        "stats": {
            "total_visitors": total,
            "completed": completed,
            "in_progress": in_progress,
            "total_answers": total_answers
        },
        "sessions": results
    }

@app.get("/api/admin/session/{session_id}")
def get_admin_session_detail(session_id: str, db: Session = Depends(get_db), auth: bool = Depends(verify_admin)):
    session_obj = db.query(models.VisitorSession).filter(models.VisitorSession.id == session_id).first()
    if not session_obj:
        raise HTTPException(status_code=404, detail="Session not found")
    
    answers_out = [
        {
            "question_id": a.question_id,
            "question_text": a.question_text,
            "answer": a.answer,
            "created_at": a.created_at
        }
        for a in session_obj.answers
    ]

    return {
        "id": session_obj.id,
        "started_at": session_obj.started_at,
        "is_completed": session_obj.is_completed,
        "completed_at": session_obj.completed_at,
        "answers": answers_out
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
