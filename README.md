# 🌸 A Secret Surprise For Prerna (Peda) ✨

A premium, cinematic, highly interactive Raksha Bandhan story & game experience handcrafted by her brother **Prakhar** for **Prerna Gupta (Age 23)**.

---

## 🚀 Project Overview & Architecture

```text
rakhi-surprise/
├── frontend/                     # Standalone high-performance HTML/CSS/JS frontend
│   ├── index.html                # 27 sequential full-screen interactive scenes
│   ├── style.css                 # Cinematic glassmorphism & responsive UI design
│   ├── script.js                 # 27-scene story router, sound synth & particle engine
│   └── assets/
│       ├── prerna-1.jpg          # Original high-res memory photo 1 (Uncropped)
│       ├── prerna-2.jpg          # Original high-res memory photo 2 (Uncropped)
│       ├── prerna-3.jpg          # Original high-res memory photo 3 (Uncropped)
│       ├── prerna-4.jpg          # Original high-res memory photo 4 (Uncropped)
│       ├── prerna-5.jpg          # Original high-res memory photo 5 (Uncropped)
│       ├── prerna-6.jpg          # Original high-res memory photo 6 (Uncropped)
│       ├── prerna-together.jpg   # Finale together portrait (Uncropped)
│       └── song.mp3              # Local Rakhi song ("Ek Hazaaron Mein Meri Behna Hai")
├── backend/                      # Python FastAPI backend for collecting Prerna's answers
│   ├── main.py                   # REST API endpoints & CORS handler
│   ├── database.py               # SQLite / SQLAlchemy engine configuration
│   ├── models.py                 # VisitorSession & SessionAnswer data models
│   ├── schemas.py                # Pydantic validation schemas
│   ├── requirements.txt          # Python dependencies
│   ├── .env.example              # Example environment configuration
│   └── .env                      # Local environment configuration
├── dashboard/                    # Private brother's admin monitoring dashboard
│   └── index.html                # Live Q&A transcript & stats monitor
├── .gitignore                    # Git ignore file for secrets and databases
└── README.md                     # Comprehensive documentation
```

---

## 🎬 The 27 Sequential Interactive Scenes

1. **Scene 01: Opening Mystery Envelope** — Golden particles, mystery envelope click & dramatic unfold.
2. **Scene 02: Sibling Security System** — Futuristic terminal scanner verifying name (*Prerna / Prerna Gupta*) and age (*23*).
3. **Scene 03: Funny Age Scene ("23?!")** — *"Itni badi ho gayi? Behave karna seekha?"* with humorous sibling reactions.
4. **Scene 04: Sibling Intelligence Test™** — 10 rapid-fire questions (1 on screen at a time) with witty reactions and answer recording.
5. **Scene 05: Would You Rather** — 4 pairs of 3D choice dilemma cards.
6. **Scene 06: Memory Machine 3000** — Sci-fi glitch scanline & camera shutter loading extraction.
7. **Scenes 07–12: The Memory Journey (6 Photos)** — Uncropped photos 1–6 with ambient blurred backdrops and captions (*Partners in Crime, Argument Specialists, Certified Nautanki, Candid Smiles, Some Memories, Sibling Hug*).
8. **Scene 13: Official Sibling Cup Scoreboard** — Sports live counters (Drama, Stubbornness, Food stealing, Caring ∞ vs ∞) -> Winner: Both.
9. **Scene 14: Brother's Roast Mode** — Warning alert + 5 roast cards with affectionate Indian sibling banter.
10. **Scene 15: Sister Nickname Generator** — Slot machine with 3 spinning reels stopping on *MAHARANI PEDA DEVI - CEO Department of Annoying Bhai*.
11. **Scene 16: 23 Things About My Bhena** — Interactive card stepping through 23 traits with a full grid preview.
12. **Scene 17: Star Compliment Game** — Night sky with 7 glowing clickable stars unlocking heartfelt truths.
13. **Scene 18: Rakhi Thread Interaction** — Virtual sacred thread tied around circular SVG Rakhi mandala.
14. **Scene 19: Original Hindi Shayari** — Dark warm burgundy ambiance with original poetry and Easter Egg 2.
15. **Scene 20: The Secret Drawer** — Pullable wooden drawer revealing *"Things Prakhar Will Never Admit"*.
16. **Scene 21: Fake System Error** — Glitch error: *"Prerna is apparently too important. Continuing emotional damage..."*
17. **Scene 22: Emotional Transition** — Minimalist, click-to-advance text: *"Okay, Bhena... I've always been lucky to have you as my sister."*
18. **Scene 23: 3D Handwritten Letter** — Wax seal breaks, envelope opens, sliding handwritten letter from Prakhar with margin notes.
19. **Scene 24: Future Time Capsule** — Message from Prakhar set 10 years in the future.
20. **Scene 25: Final Suspense** — Timed pauses leading to `[ REVEAL MY RAKHI SURPRISE ❤️ ]`.
21. **Scene 26: Final Photo Reveal** — Uncropped together portrait (`assets/prerna-together.jpg`) with gold glowing frame.
22. **Scene 27: Finale Celebration & Song** — `assets/song.mp3` custom music player, golden fireworks, confetti cannon, heart bubble spawns, Diya lighting, and downloadable PNG Keepsake Card.

---

## 🥚 5 Secret Easter Eggs

1. **Top Bar Button (`🚫 Don't touch`)**: Confetti explosion + *"I literally told you not to! +10 Sibling Chaos Points!"*
2. **Scene 19 (Shayari)**: Tap Rakhi mandala 5 times -> *"SECRET UNLOCKED: +100 Bhena Points"*
3. **Scene 27 (Finale)**: Click together photo repeatedly -> Spawns animated floating heart bubbles with gentle chime audio.
4. **Keyboard Key `P`**: Press `P` -> *"P detected. Obviously this website belongs to the Peda."*
5. **Scene 23 (Letter)**: Click brother signature -> *"Yes, I made all of this instead of doing something productive."*

---

## 🛡️ Critical Photo Rule Verified

- **100% Uncropped (`object-fit: contain !important;`)**: All personal photos preserve their natural dimensions without face-cropping, using ambient blurred duplicates behind them.

---

## ⚡ Local Setup & Execution

### 1. Frontend (Instant Play)
Open `index.html` (or `frontend/index.html`) directly in any web browser!

### 2. Backend & Admin Dashboard (Optional for Answer Tracking)
```bash
# 1. Navigate to backend directory
cd backend

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run FastAPI server
uvicorn main:app --reload --port 8000
```
- Open `dashboard/index.html` in your browser.
- Login with password: `peda2026` (configurable via `.env`).
- View all answers given by Prerna in real time!

---

*Handcrafted with ❤️ by Prakhar for his sister Prerna (Peda).*
