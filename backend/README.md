# ⚡ Rakhi Surprise FastAPI Backend & Supabase Service

FastAPI service designed for deployment on **Render Free Web Service** with **Supabase PostgreSQL**.

---

## 🛠️ Tech Stack
- **FastAPI**: Asynchronous Python API framework.
- **SQLAlchemy 2.0**: Database ORM supporting SQLite (development) and PostgreSQL (production).
- **psycopg2-binary**: PostgreSQL driver for Supabase.
- **Pydantic V2**: Data schema validation.

---

## ⚙️ Environment Variables (`.env`)

Create a `.env` file for local development:
```env
DATABASE_URL=sqlite:///./rakhi_answers.db
ADMIN_PASSWORD=peda2026
FRONTEND_URL=http://localhost:5500
ENVIRONMENT=development
```

For Render production:
```env
DATABASE_URL=postgresql://postgres:[PASSWORD]@[HOST]:5432/postgres
ADMIN_PASSWORD=your_secure_password
FRONTEND_URL=https://your-project.vercel.app
ENVIRONMENT=production
```

---

## 🚀 Exact Production Deployment Sequence

1. **Deploy Backend**: Deploy `backend/` to Render with `DATABASE_URL`, `ADMIN_PASSWORD`, and `ENVIRONMENT=production`.
2. **Deploy Frontend**: Deploy frontend static site to Vercel.
3. **Obtain Vercel URL**: Copy your live Vercel URL (e.g. `https://your-project.vercel.app`).
4. **Set FRONTEND_URL on Render**: In Render Dashboard → Environment, add `FRONTEND_URL=https://your-project.vercel.app`.
5. **Redeploy / Restart Render**: Restart the Render service to apply the CORS origin setting.
6. **Test Requests**: Verify that `POST /api/answer` and `POST /api/milestone` from the frontend succeed with `200 OK`.

---

## 🚀 Render Service Configuration
- **Root Directory**: `backend`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

---

## 🧪 Testing Backend
Run the automated test suite:
```bash
python test_api.py
```
Outputs:
```text
[TEST PASS] GET /health returns status: ok
[TEST PASS] POST /api/answer handles initial insert and duplicate updates
[TEST PASS] POST /api/milestone records milestone and prevents duplicate errors
[TEST PASS] POST /api/complete marks session as finished
[TEST PASS] Admin authentication and session details verified
[TEST PASS] PostgreSQL URI normalization logic verified
```
