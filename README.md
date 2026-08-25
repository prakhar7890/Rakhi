# 🌸 A Secret Surprise For Prerna (Peda) • Production Deployment Guide ✨

A premium, cinematic, 27-scene interactive Raksha Bandhan story & game experience handcrafted with love by **Prakhar** for his sister **Prerna Gupta (Peda, Age 23)**.

---

## 🏛️ System Architecture

```text
                                GitHub (prakhar7890/Rakhi)
                                            |
                         +------------------+------------------+
                         |                                     |
                         v                                     v
                  Vercel Frontend                       Render Backend
             (Static HTML / CSS / JS)                  (FastAPI + Uvicorn)
                         |                                     |
                         |                                     v
                         +---------------------------> Supabase PostgreSQL
                              (Async Answer &             (DATABASE_URL)
                             Milestone Logging)
```

- **Frontend**: [Vercel](https://vercel.com) (High performance static hosting from `frontend/` or repository root).
- **Backend**: [Render](https://render.com) (FastAPI Python Web Service running on free tier with health checks).
- **Database**: [Supabase](https://supabase.com) (Managed cloud PostgreSQL database).
- **Admin Dashboard**: `dashboard/` (Private brother portal with live stats and chronological milestone timeline).

---

## 📂 Repository Structure

```text
Rakhi/
├── frontend/                     # Static frontend for Vercel
│   ├── index.html                # 27 sequential interactive scenes
│   ├── style.css                 # Cinematic glassmorphism styles & animations
│   ├── script.js                 # Story engine, audio synthesizer & offline queue
│   └── assets/
│       ├── prerna-1.jpg          # Original high-res memory photo 1 (Uncropped)
│       ├── prerna-2.jpg          # Original high-res memory photo 2 (Uncropped)
│       ├── prerna-3.jpg          # Original high-res memory photo 3 (Uncropped)
│       ├── prerna-4.jpg          # Original high-res memory photo 4 (Uncropped)
│       ├── prerna-5.jpg          # Original high-res memory photo 5 (Uncropped)
│       ├── prerna-6.jpg          # Original high-res memory photo 6 (Uncropped)
│       ├── prerna-together.jpg   # Finale together portrait (Uncropped)
│       └── song.mp3              # Local Rakhi song ("Ek Hazaaron Mein Meri Behna Hai")
│
├── backend/                      # Python FastAPI backend
│   ├── main.py                   # REST API endpoints & CORS middleware
│   ├── database.py               # SQLite & Supabase PostgreSQL connection engine
│   ├── models.py                 # VisitorSession, SessionAnswer, SessionMilestone
│   ├── schemas.py                # Pydantic validation schemas
│   ├── requirements.txt          # Python dependencies
│   ├── test_api.py               # Automated test suite for backend & database
│   ├── .env.example              # Environment variables template
│   └── README.md                 # Backend-specific instructions
│
├── dashboard/                    # Private brother's admin dashboard
│   ├── index.html                # HTML layout & modal timeline
│   ├── style.css                 # Dashboard theme
│   └── script.js                 # Dashboard authentication & data fetching
│
├── vercel.json                   # Vercel static routing configuration
├── .gitignore                    # Git ignore file (excludes secrets & .db files)
└── README.md                     # Master documentation
```

---

## 💻 Local Development Setup

### 1. Run the Frontend Locally
```bash
# Using Python HTTP server:
python -m http.server 5500
# Then open http://localhost:5500 in your browser
```

### 2. Run the Backend Locally
```bash
cd backend
python -m venv venv

# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
- API Docs: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/health`

### 3. Open Admin Dashboard
Open `dashboard/index.html` in your browser and enter admin password: `peda2026`.

---

## 🚀 Production Deployment Sequence (Step-by-Step)

Follow this exact 6-step sequence to deploy backend, database, and frontend smoothly with strict CORS protection:

```text
Step 1: Deploy Backend (Render) & Supabase Database
                      ↓
Step 2: Deploy Frontend (Vercel)
                      ↓
Step 3: Obtain Live Vercel URL
                      ↓
Step 4: Set FRONTEND_URL on Render Environment Variables
                      ↓
Step 5: Redeploy / Restart Render Web Service
                      ↓
Step 6: Test Frontend ➔ Backend API Requests
```

---

### Step 1: Deploy Backend to Render & Connect Supabase
1. **Set Up Supabase Database**:
   - Go to [supabase.com](https://supabase.com) and create a free project.
   - Go to **Project Settings** → **Database**, find your **Connection string (URI mode)**.
   - Copy the URI (format: `postgresql://postgres:[YOUR-PASSWORD]@[YOUR-HOST]:5432/postgres`).
2. **Deploy Render Web Service**:
   - Go to [render.com](https://render.com) and click **New +** → **Web Service**.
   - Connect your GitHub repository: `prakhar7890/Rakhi`.
   - Configure:
     - **Name**: `rakhi-surprise-api`
     - **Root Directory**: `backend`
     - **Runtime**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
     - **Instance Type**: `Free`
   - Add initial **Environment Variables**:
     | Variable | Value |
     |---|---|
     | `DATABASE_URL` | `postgresql://postgres:[YOUR-PASSWORD]@[YOUR-HOST]:5432/postgres` |
     | `ADMIN_PASSWORD` | `your_secure_admin_password` |
     | `ENVIRONMENT` | `production` |
   - Click **Create Web Service**.
   - Copy your Render backend URL (e.g., `https://rakhi-surprise-api.onrender.com`).
   - Verify health: Visit `https://rakhi-surprise-api.onrender.com/health` in your browser ➔ `{"status":"ok"}`.

---

### Step 2: Deploy Frontend to Vercel
1. In `frontend/script.js` (and `script.js`), configure `API_CONFIG.BASE_URL` with your Render URL:
   ```javascript
   const API_CONFIG = {
     BASE_URL: (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1")
       ? "http://localhost:8000"
       : "https://rakhi-surprise-api.onrender.com" // <-- Paste your Render URL here
   };
   ```
2. Commit and push:
   ```bash
   git add .
   git commit -m "Configure live Render backend URL"
   git push origin main
   ```
3. Go to [vercel.com](https://vercel.com) and click **Add New...** → **Project**.
4. Import `prakhar7890/Rakhi`.
5. Configuration:
   - **Framework Preset**: `Other`
   - **Root Directory**: `frontend` (or `./`)
   - **Build Command**: *(Leave empty)*
   - **Output Directory**: *(Leave empty)*
6. Click **Deploy**.

---

### Step 3: Obtain Live Vercel URL
Once deployment completes, copy your live Vercel URL from the Vercel dashboard:
- Example: `https://rakhi-surprise.vercel.app` (or custom domain).

---

### Step 4: Set `FRONTEND_URL` on Render
1. Go back to your [Render Dashboard](https://dashboard.render.com).
2. Select your `rakhi-surprise-api` service → **Environment**.
3. Add the new environment variable:
   | Variable | Value |
   |---|---|
   | `FRONTEND_URL` | `https://rakhi-surprise.vercel.app` |
4. Click **Save Changes**.

---

### Step 5: Redeploy / Restart Render Service
- Click **Manual Deploy** → **Deploy latest commit** (or **Restart Service**) on Render to apply the CORS origin setting.

---

### Step 6: Test Frontend ➔ Backend API Requests
1. Open your live Vercel website: `https://rakhi-surprise.vercel.app`.
2. Complete Scene 1 (open envelope) and Scene 2 (verify name/age).
3. Open DevTools (**F12** → **Network tab**) and verify `POST /api/answer` and `POST /api/milestone` return HTTP `200 OK`.
4. Open the live admin dashboard (`https://rakhi-surprise.vercel.app/dashboard` or `dashboard/index.html`), enter your `ADMIN_PASSWORD`, and verify that Prerna's live session and answers appear in real time!

---

## 🛡️ Offline Queue & Sleep Resilience

When deployed on Render's free tier, the backend may sleep after 15 minutes of inactivity:
- The website uses **non-blocking asynchronous fetch** with a 6-second timeout.
- If Render is asleep or cold-starting, answers and milestones are automatically queued in `localStorage` (`rakhi_offline_queue`).
- The frontend automatically retries and flushes the queue when connection is established (`window.online` and periodic 15s background checks).
- Prerna will **never** see an error or lag during the surprise experience.

---

## 🔒 Security Summary
- **Zero Credentials Committed**: `.env`, `*.db`, and bytecode files are strictly gitignored.
- **Admin Authentication**: Admin endpoints require HTTP Bearer tokens validated against `ADMIN_PASSWORD`.
- **CORS Protection**: In production, CORS restricts API access strictly to your `FRONTEND_URL`.
- **No Absolute Paths**: All asset references use clean relative paths.

---

## 🧪 Testing
Run the automated test suite locally:
```bash
cd backend
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
