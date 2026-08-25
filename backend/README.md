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

## 🚀 Render Deployment Settings
- **Root Directory**: `backend`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

---

## 🧪 Testing Backend
Run the automated test suite:
```bash
python test_api.py
```
