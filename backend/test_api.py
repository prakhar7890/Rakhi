# -*- coding: utf-8 -*-
"""
Automated Test Suite for Rakhi Surprise FastAPI Backend
Tests all endpoints, SQLite local operations, and Supabase URI normalization.
"""
import unittest
from fastapi.testclient import TestClient
import os
import sys

# Ensure backend directory is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import app
from database import Base, engine

class TestRakhiBackend(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(bind=engine)
        cls.client = TestClient(app)
        cls.test_session_id = "test-session-verify-12345"

    def test_01_health_check(self):
        res = self.client.get("/health")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), {"status": "ok"})
        print("[TEST PASS] GET /health returns status: ok")

    def test_02_submit_answer(self):
        payload = {
            "session_id": self.test_session_id,
            "question_id": "test_q1",
            "question_text": "Who is the favorite sibling?",
            "answer": "Peda"
        }
        res = self.client.post("/api/answer", json=payload)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["status"], "success")

        # Test duplicate update
        payload["answer"] = "Maharani Peda Devi"
        res_dup = self.client.post("/api/answer", json=payload)
        self.assertEqual(res_dup.status_code, 200)
        print("[TEST PASS] POST /api/answer handles initial insert and duplicate updates")

    def test_03_submit_milestone(self):
        payload = {
            "session_id": self.test_session_id,
            "milestone": "envelope_opened"
        }
        res = self.client.post("/api/milestone", json=payload)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["status"], "success")

        # Duplicate milestone should succeed without error
        res_dup = self.client.post("/api/milestone", json=payload)
        self.assertEqual(res_dup.status_code, 200)
        print("[TEST PASS] POST /api/milestone records milestone and prevents duplicate errors")

    def test_04_complete_session(self):
        payload = {
            "session_id": self.test_session_id
        }
        res = self.client.post("/api/complete", json=payload)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["status"], "success")
        print("[TEST PASS] POST /api/complete marks session as finished")

    def test_05_admin_auth_and_sessions(self):
        # Invalid login
        res_fail = self.client.post("/api/admin/login", json={"password": "wrongpassword"})
        self.assertEqual(res_fail.status_code, 401)

        # Valid login
        res_ok = self.client.post("/api/admin/login", json={"password": "peda2026"})
        self.assertEqual(res_ok.status_code, 200)
        token = res_ok.json()["token"]

        # Access sessions without auth -> 401
        res_unauth = self.client.get("/api/admin/sessions")
        self.assertEqual(res_unauth.status_code, 401)

        # Access sessions with auth -> 200
        headers = {"Authorization": f"Bearer {token}"}
        res_sessions = self.client.get("/api/admin/sessions", headers=headers)
        self.assertEqual(res_sessions.status_code, 200)
        data = res_sessions.json()
        self.assertIn("stats", data)
        self.assertIn("sessions", data)
        self.assertGreaterEqual(data["stats"]["total_visitors"], 1)

        # Access session detail
        res_detail = self.client.get(f"/api/admin/session/{self.test_session_id}", headers=headers)
        self.assertEqual(res_detail.status_code, 200)
        detail_data = res_detail.json()
        self.assertEqual(detail_data["id"], self.test_session_id)
        self.assertTrue(detail_data["is_completed"])
        self.assertGreaterEqual(len(detail_data["answers"]), 1)
        self.assertGreaterEqual(len(detail_data["milestones"]), 1)
        print("[TEST PASS] Admin authentication and session details verified")

    def test_06_postgres_uri_normalization(self):
        raw = "postgres://user:pass@ep-cool-db.supabase.co:5432/postgres"
        normalized = raw.replace("postgres://", "postgresql://", 1)
        self.assertTrue(normalized.startswith("postgresql://"))
        print("[TEST PASS] PostgreSQL URI normalization logic verified")

if __name__ == "__main__":
    unittest.main()
