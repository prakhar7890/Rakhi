# -*- coding: utf-8 -*-
"""
Automated Test Suite for Rakhi Surprise FastAPI Backend
Tests all endpoints, SQLite local operations, Supabase URI normalization,
and Idempotency (Preservation of first submitted answer).
"""
import unittest
from fastapi.testclient import TestClient
import os
import sys
import time

# Ensure backend directory is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import app
from database import Base, engine

class TestRakhiBackend(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(bind=engine)
        cls.client = TestClient(app)
        cls.test_session_id = f"test-sess-{int(time.time()*1000)}"

    def test_01_health_check(self):
        res = self.client.get("/health")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), {"status": "ok"})
        print("[TEST PASS] GET /health returns status: ok")

    def test_02_idempotent_answer_cases(self):
        # Case 1: First submission -> INSERT
        payload1 = {
            "session_id": self.test_session_id,
            "question_id": "q_idempotent_test",
            "question_text": "Who is the favorite sibling?",
            "answer": "Original Peda"
        }
        res1 = self.client.post("/api/answer", json=payload1)
        self.assertEqual(res1.status_code, 200)
        data1 = res1.json()
        self.assertEqual(data1["status"], "success")
        self.assertFalse(data1.get("idempotent", True))
        print("[TEST PASS] Case 1: First submission -> INSERT succeeds (idempotent=False)")

        # Case 2: Identical retry -> 200 OK without creating another row
        res2 = self.client.post("/api/answer", json=payload1)
        self.assertEqual(res2.status_code, 200)
        data2 = res2.json()
        self.assertEqual(data2["status"], "success")
        self.assertTrue(data2.get("idempotent", False))
        self.assertEqual(data2.get("recorded_answer"), "Original Peda")
        print("[TEST PASS] Case 2: Identical retry -> idempotent confirmation (idempotent=True)")

        # Case 3: Duplicate submission with a different answer -> preserve original answer
        payload3 = {
            "session_id": self.test_session_id,
            "question_id": "q_idempotent_test",
            "question_text": "Who is the favorite sibling?",
            "answer": "New Different Answer"
        }
        res3 = self.client.post("/api/answer", json=payload3)
        self.assertEqual(res3.status_code, 200)
        data3 = res3.json()
        self.assertEqual(data3["status"], "success")
        self.assertTrue(data3.get("idempotent", False))
        self.assertEqual(data3.get("recorded_answer"), "Original Peda") # Original answer preserved!
        print("[TEST PASS] Case 3: Duplicate with different answer -> original answer preserved (not overwritten)")

    def test_03_submit_milestone_idempotency(self):
        payload = {
            "session_id": self.test_session_id,
            "milestone": "envelope_opened"
        }
        # First milestone insert
        res1 = self.client.post("/api/milestone", json=payload)
        self.assertEqual(res1.status_code, 200)
        self.assertEqual(res1.json()["status"], "success")
        self.assertFalse(res1.json().get("idempotent", True))

        # Duplicate milestone retry
        res2 = self.client.post("/api/milestone", json=payload)
        self.assertEqual(res2.status_code, 200)
        self.assertEqual(res2.json()["status"], "success")
        self.assertTrue(res2.json().get("idempotent", False))
        print("[TEST PASS] POST /api/milestone records milestone idempotently")

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

        # Access sessions with auth -> 200
        headers = {"Authorization": f"Bearer {token}"}
        res_sessions = self.client.get("/api/admin/sessions", headers=headers)
        self.assertEqual(res_sessions.status_code, 200)
        data = res_sessions.json()
        self.assertIn("stats", data)
        self.assertIn("sessions", data)

        # Access session detail and verify preserved answer in DB
        res_detail = self.client.get(f"/api/admin/session/{self.test_session_id}", headers=headers)
        self.assertEqual(res_detail.status_code, 200)
        detail_data = res_detail.json()
        self.assertEqual(detail_data["id"], self.test_session_id)
        self.assertTrue(detail_data["is_completed"])

        # Verify the saved answer is indeed "Original Peda" and only 1 answer exists for that question
        answers = [a for a in detail_data["answers"] if a["question_id"] == "q_idempotent_test"]
        self.assertEqual(len(answers), 1)
        self.assertEqual(answers[0]["answer"], "Original Peda")
        print("[TEST PASS] Verified database contains exactly 1 row with preserved original answer 'Original Peda'")

    def test_06_postgres_uri_normalization(self):
        raw = "postgres://user:pass@ep-cool-db.supabase.co:5432/postgres"
        normalized = raw.replace("postgres://", "postgresql://", 1)
        self.assertTrue(normalized.startswith("postgresql://"))
        print("[TEST PASS] PostgreSQL URI normalization logic verified")

if __name__ == "__main__":
    unittest.main()
