# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Boolean, DateTime, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class VisitorSession(Base):
    __tablename__ = "visitor_sessions"

    id = Column(String, primary_key=True, index=True)
    started_at = Column(DateTime, default=datetime.utcnow)
    is_completed = Column(Boolean, default=False)
    completed_at = Column(DateTime, nullable=True)

    answers = relationship("SessionAnswer", back_populates="session", cascade="all, delete-orphan", order_by="SessionAnswer.created_at")
    milestones = relationship("SessionMilestone", back_populates="session", cascade="all, delete-orphan", order_by="SessionMilestone.created_at")

class SessionAnswer(Base):
    __tablename__ = "session_answers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    session_id = Column(String, ForeignKey("visitor_sessions.id"), index=True)
    question_id = Column(String, index=True)
    question_text = Column(String)
    answer = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("session_id", "question_id", name="uq_session_question"),
    )

    session = relationship("VisitorSession", back_populates="answers")

class SessionMilestone(Base):
    __tablename__ = "session_milestones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    session_id = Column(String, ForeignKey("visitor_sessions.id"), index=True)
    milestone = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("session_id", "milestone", name="uq_session_milestone"),
    )

    session = relationship("VisitorSession", back_populates="milestones")
