# -*- coding: utf-8 -*-
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AnswerCreate(BaseModel):
    session_id: str
    question_id: str
    question_text: str
    answer: str
    timestamp: Optional[str] = None

class CompleteSession(BaseModel):
    session_id: str
    completed_at: Optional[str] = None

class AdminLogin(BaseModel):
    password: str

class AnswerOut(BaseModel):
    question_id: str
    question_text: str
    answer: str
    created_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True

class SessionOut(BaseModel):
    id: str
    started_at: datetime
    is_completed: bool
    completed_at: Optional[datetime] = None
    answers_count: int = 0

    class Config:
        from_attributes = True
        orm_mode = True

class SessionDetailOut(BaseModel):
    id: str
    started_at: datetime
    is_completed: bool
    completed_at: Optional[datetime] = None
    answers: List[AnswerOut] = []

    class Config:
        from_attributes = True
        orm_mode = True
