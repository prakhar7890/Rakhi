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
    title="Rakhi Surprise Answer & Milestone API",
    description="Backend service for Prerna's interactive Rakhi surprise experience.",
    version="2.1.0"
)

frontend_url = os.getenv("FRONTEND_URL", "").strip()
allowed_origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]
if frontend_url:
    allowed_origins.append(frontend_url.rstrip("/"))

is_prod = os.getenv("ENVIRONMENT") == "production"

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins if is_prod else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "peda2026")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/api/answer", status_code=status.HTTP_200_OK)
def submit_answer(payload: schemas.AnswerCreate, db: Session = Depends(get_db)):
    if not payload.session_id or not payload.question_id:
        raise HTTPException(status_code=400, detail="session_id and question_id are required")

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
    return {"status": "success", "message": "Answer recorded successfully"}

@app.post("/api/milestone", status_code=status.HTTP_200_OK)
def submit_milestone(payload: schemas.MilestoneCreate, db: Session = Depends(get_db)):
    if not payload.session_id or not payload.milestone:
        raise HTTPException(status_code=400, detail="session_id and milestone are required")

    session_obj = db.query(models.VisitorSession).filter(models.VisitorSession.id == payload.session_id).first()
    if not session_obj:
        session_obj = models.VisitorSession(id=payload.session_id, started_at=datetime.utcnow())
        db.add(session_obj)
        db.commit()

    existing_milestone = db.query(models.SessionMilestone).filter(
        models.SessionMilestone.session_id == payload.session_id,
        models.SessionMilestone.milestone == payload.milestone
    ).first()

    if not existing_milestone:
        new_milestone = models.SessionMilestone(
            session_id=payload.session_id,
            milestone=payload.milestone,
            created_at=datetime.utcnow()
        )
        db.add(new_milestone)
        db.commit()

    return {"status": "success", "message": "Milestone recorded successfully"}

@app.post("/api/complete", status_code=status.HTTP_200_OK)
def complete_session(payload: schemas.CompleteSession, db: Session = Depends(get_db)):
    session_obj = db.query(models.VisitorSession).filter(models.VisitorSession.id == payload.session_id).first()
    if not session_obj:
        session_obj = models.VisitorSession(id=payload.session_id, started_at=datetime.utcnow())
        db.add(session_obj)

    session_obj.is_completed = True
    session_obj.completed_at = datetime.utcnow()
    db.commit()
    return {"status": "success", "message": "Session marked as completed"}

@app.post("/api/admin/login")
def admin_login(payload: schemas.AdminLogin):
    if payload.password != ADMIN_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid admin credentials")
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
            "answers_count": len(s.answers),
            "milestones_count": len(s.milestones)
        })

    total = len(sessions)
    completed = sum(1 for s in sessions if s.is_completed)
    in_progress = total - completed
    total_answers = db.query(models.SessionAnswer).count()
    total_milestones = db.query(models.SessionMilestone).count()

    return {
        "stats": {
            "total_visitors": total,
            "completed": completed,
            "in_progress": in_progress,
            "total_answers": total_answers,
            "total_milestones": total_milestones
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

    milestones_out = [
        {
            "milestone": m.milestone,
            "created_at": m.created_at
        }
        for m in session_obj.milestones
    ]

    return {
        "id": session_obj.id,
        "started_at": session_obj.started_at,
        "is_completed": session_obj.is_completed,
        "completed_at": session_obj.completed_at,
        "answers": answers_out,
        "milestones": milestones_out
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
