# -*- coding: utf-8 -*-
"""
Master Project Builder for Raksha Bandhan Surprise for Prerna (Peda)
Crafted with love by Prakhar
"""
import os
import shutil
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
FRONTEND_ASSETS = os.path.join(FRONTEND_DIR, "assets")
ROOT_ASSETS = os.path.join(BASE_DIR, "assets")
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
DASHBOARD_DIR = os.path.join(BASE_DIR, "dashboard")


def setup_directories():
    os.makedirs(FRONTEND_DIR, exist_ok=True)
    os.makedirs(FRONTEND_ASSETS, exist_ok=True)
    os.makedirs(BACKEND_DIR, exist_ok=True)
    os.makedirs(DASHBOARD_DIR, exist_ok=True)

    # Sync assets
    if os.path.exists(ROOT_ASSETS):
        for item in os.listdir(ROOT_ASSETS):
            s = os.path.join(ROOT_ASSETS, item)
            d = os.path.join(FRONTEND_ASSETS, item)
            if os.path.isfile(s) and not os.path.exists(d):
                shutil.copy2(s, d)
    print("✓ Directories & Assets synced")

def generate_index_html():
    content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <meta name="theme-color" content="#1B0C15">
  <meta name="description" content="A secret, interactive, cinematic Rakhi surprise experience crafted by Prakhar for his sister Prerna (Peda).">
  <title>For Peda • Happy Raksha Bandhan ✨</title>

  <!-- Google Fonts Preconnect & Styles -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Marck+Script&family=Outfit:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Rozha+One&family=Yatra+One&display=swap" rel="stylesheet">

  <!-- GSAP CDN for smooth animations -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>

  <!-- Stylesheet -->
  <link rel="stylesheet" href="style.css">
</head>
<body class="theme-cinematic">

  <!-- Interactive Canvas Layers -->
  <canvas id="bg-canvas" aria-hidden="true"></canvas>
  <canvas id="fireworks-canvas" aria-hidden="true"></canvas>
  <canvas id="confetti-canvas" aria-hidden="true"></canvas>
  <canvas id="hearts-canvas" aria-hidden="true"></canvas>
  <canvas id="sparkle-cursor-canvas" aria-hidden="true"></canvas>

  <!-- Top Minimalist Story Bar -->
  <header class="top-story-bar" aria-label="Story Header">
    <div class="brand-chip">
      <span class="brand-icon">🌸</span>
      <span class="brand-text">For Peda • 23</span>
    </div>

    <!-- Subtle Cinematic Progress Dots Indicator -->
    <nav class="story-progress-indicator" id="story-progress-indicator" aria-label="Story Progress">
      <div class="progress-track">
        <div class="progress-bar-fill" id="progress-bar-fill"></div>
      </div>
      <div class="progress-dots-row" id="progress-dots-row"></div>
    </nav>

    <div class="top-controls">
      <button id="sound-toggle" class="control-pill-btn" aria-label="Toggle Sound Effects" title="Toggle sound effects">
        <span class="sound-icon">🔊</span>
        <span class="sound-label">Sound</span>
      </button>

      <!-- Easter Egg 1: Don't touch this -->
      <button id="easter-egg-1-btn" class="control-pill-btn warning-pill" aria-label="Secret Easter Egg" title="Don't click this!">
        <span>🚫 Don't touch</span>
      </button>
    </div>
  </header>

  <!-- MAIN STORY VIEWPORT (27 Interactive Cinematic Scenes) -->
  <main id="story-viewport" class="story-viewport">

    <!-- ============================================================ -->
    <!-- SCENE 1: OPENING MYSTERY ENVELOPE                            -->
    <!-- ============================================================ -->
    <section class="story-screen active dark-scene" id="scene-1" data-scene="1">
      <div class="screen-box opening-mystery-card">
        <div class="screen-badge glow-badge">
          <span>✨ Secret Delivery • Chapter 01</span>
        </div>

        <div class="cinematic-text-stream">
          <p class="cinematic-line c-line-1" id="s1-line-1">"Attention..."</p>
          <p class="cinematic-line c-line-2" id="s1-line-2">"Ek bahut important insaan ke liye message hai."</p>
          <p class="cinematic-line c-line-3 handwriting" id="s1-line-3">"Sirf ek certified Peda hi ise khol sakta hai."</p>
        </div>

        <!-- Mystery Envelope -->
        <div class="mystery-envelope-wrap" id="mystery-envelope-box">
          <div class="mystery-envelope-icon pulse-glow">💌</div>
        </div>

        <div class="screen-action-wrap" id="s1-action-wrap" style="opacity: 0;">
          <button id="btn-scene-1-enter" class="btn-grand-gold pulse-btn">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>OPEN THE MYSTERY</span>
              <span class="btn-sparkle">💌</span>
            </span>
          </button>
        </div>

        <div class="s1-reveal-msg handwriting" id="s1-reveal-msg" style="display: none;">
          <p>"Chal Bhena... Ab dekhte hain tere liye kya banaya hai." ✨</p>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 2: SECRET IDENTITY SCANNER                             -->
    <!-- ============================================================ -->
    <section class="story-screen dark-scene" id="scene-2" data-scene="2">
      <div class="screen-box futuristic-scanner-card">
        <div class="screen-badge tech-badge">
          <span>🛡️ SIBLING SECURITY SYSTEM • STATUS: UNKNOWN</span>
        </div>

        <div class="prompt-header">
          <p class="prompt-sub">Identity Verification Required</p>
          <h2 class="prompt-title tech-title">"Naam batao, Gadhi."</h2>
        </div>

        <form id="form-identity-check" class="interactive-form" onsubmit="return false;">
          <div class="input-field-wrap">
            <input 
              type="text" 
              id="input-user-name" 
              class="story-input tech-input" 
              placeholder="Enter your name..." 
              autocomplete="off" 
              autocapitalize="words"
              spellcheck="false"
              required
            >
          </div>

          <div class="input-field-wrap" id="age-check-step" style="display: none;">
            <p class="prompt-sub tech-sub" style="margin-top: 14px;">"Age batao, Peda."</p>
            <input 
              type="number" 
              id="input-user-age-sec" 
              class="story-input tech-input" 
              placeholder="Enter your age (e.g. 23)..." 
              min="1" 
              max="100" 
              autocomplete="off"
            >
          </div>

          <!-- Scanning Bar Animation -->
          <div class="scanning-terminal-box" id="scanning-terminal" style="display: none;">
            <div class="scan-status-text" id="scan-status-text">SCANNING SIBLING DATABASE...</div>
            <div class="scan-progress-bar">
              <div class="scan-bar-fill" id="scan-bar-fill"></div>
            </div>
          </div>

          <!-- Identity Card Result -->
          <div class="identity-card-badge" id="identity-card-badge" style="display: none;">
            <div class="id-header">IDENTITY CONFIRMED</div>
            <div class="id-row"><span>CODENAME:</span> <strong>PEDA</strong></div>
            <div class="id-row"><span>RELATIONSHIP:</span> <strong>BHENA ❤️</strong></div>
            <div class="id-row"><span>AGE:</span> <strong>23</strong></div>
            <div class="id-row"><span>ACCESS:</span> <strong class="text-green">GRANTED</strong></div>
            <div class="id-footer handwriting">"Thik hai, tu hi hai." 🌸</div>
          </div>

          <div class="validation-feedback" id="identity-validation-msg" aria-live="polite"></div>

          <div class="screen-action-wrap" id="identity-btn-wrap">
            <button type="submit" id="btn-identity-continue" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">
                <span id="btn-identity-label">Scan Identity</span>
                <span class="btn-arrow">→</span>
              </span>
            </button>
          </div>
        </form>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 3: FUNNY AGE SCENE ("23?!")                            -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-3" data-scene="3">
      <div class="screen-box glass-card interactive-card">
        <div class="screen-badge">
          <span>🎂 Milestone Check • Age 23</span>
        </div>

        <div class="prompt-header">
          <div class="huge-number-anim" id="age-huge-number">23?!</div>
          <h2 class="prompt-title">"Itni badi ho gayi?"</h2>
          <p class="prompt-sub" style="margin-top: 8px;">"Behave karna seekha?"</p>
        </div>

        <div class="age-interactive-choices" id="age-choices-row">
          <button class="btn-choice-pill" data-ans="yes"><span>YES</span></button>
          <button class="btn-choice-pill" data-ans="no"><span>NO</span></button>
          <button class="btn-choice-pill" data-ans="working"><span>Still working on it</span></button>
        </div>

        <div class="age-reaction-box" id="age-reaction-box" style="display: none;">
          <p class="feedback-text handwriting" id="age-reaction-text"></p>
          <button id="btn-age-continue-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Take Sibling Test</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 4: SIBLING INTELLIGENCE TEST (10 QUESTIONS)            -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-4" data-scene="4">
      <div class="screen-box glass-card quiz-card">
        <div class="screen-badge">
          <span>🧠 SIBLING INTELLIGENCE TEST™</span>
        </div>

        <div class="rapid-fire-stage" id="quiz-fire-stage">
          <div class="rapid-step-badge" id="quiz-step-badge">Question 1 of 10</div>
          <h2 class="prompt-title rapid-question-title" id="quiz-question-title">Who is the better sibling?</h2>

          <div class="quiz-options-list" id="quiz-options-list">
            <!-- Dynamically populated per question -->
          </div>

          <div class="quiz-feedback-box" id="quiz-feedback-box" style="display: none;">
            <p class="feedback-text handwriting" id="quiz-feedback-text"></p>
            <button id="btn-quiz-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">
                <span id="quiz-btn-label">Next Question</span>
                <span class="btn-arrow">→</span>
              </span>
            </button>
          </div>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 5: WOULD YOU RATHER (4 PAIRS)                          -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-5" data-scene="5">
      <div class="screen-box glass-card interactive-card">
        <div class="screen-badge">
          <span>🤔 Sibling Dilemma • Would You Rather</span>
        </div>

        <div class="prompt-header">
          <div class="rapid-step-badge" id="wyr-step-badge">Pair 1 of 4</div>
          <h2 class="prompt-title">Would you rather...</h2>
        </div>

        <div class="wyr-cards-container" id="wyr-cards-container">
          <div class="wyr-card" id="wyr-card-a" role="button" tabindex="0">
            <span class="wyr-badge">OPTION A</span>
            <p class="wyr-card-text" id="wyr-text-a">Fight with Bhai every day</p>
          </div>
          <div class="wyr-divider">OR</div>
          <div class="wyr-card" id="wyr-card-b" role="button" tabindex="0">
            <span class="wyr-badge">OPTION B</span>
            <p class="wyr-card-text" id="wyr-text-b">Admit Bhai is right once?</p>
          </div>
        </div>

        <div class="wyr-feedback-box" id="wyr-feedback-box" style="display: none;">
          <p class="feedback-text handwriting" id="wyr-feedback-text"></p>
          <button id="btn-wyr-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span id="wyr-btn-label">Next Dilemma</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 6: MEMORY MACHINE 3000                                 -->
    <!-- ============================================================ -->
    <section class="story-screen dark-scene" id="scene-6" data-scene="6">
      <div class="screen-box memory-machine-box">
        <div class="screen-badge tech-badge">
          <span>⚡ MEMORY MACHINE 3000</span>
        </div>

        <div class="prompt-header">
          <h2 class="prompt-title tech-title">"Let's recover some dangerous memories."</h2>
          <p class="prompt-sub" style="color: #FDE68A;">Archived sibling moments ready for extraction...</p>
        </div>

        <div class="machine-terminal-graphic" id="machine-graphic">
          <div class="machine-lens">
            <span class="lens-icon">📷</span>
          </div>
          <div class="machine-status-msg" id="machine-status-msg">STANDBY FOR EXTRACTION</div>
        </div>

        <div class="screen-action-wrap" id="machine-start-wrap">
          <button id="btn-start-machine" class="btn-grand-gold pulse-btn">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>START MEMORY MACHINE</span>
              <span class="btn-sparkle">⚡</span>
            </span>
          </button>
        </div>

        <!-- Recovered Photo Interactive Prompt -->
        <div class="memory-guess-substage" id="machine-recovered-stage" style="display: none;">
          <div class="recovered-badge">MEMORY RECOVERED</div>
          <h3 class="recovered-prompt">"Do you remember this?"</h3>
          
          <div class="guess-actions-row">
            <button class="btn-choice-pill" data-mguess="obviously"><span>Obviously</span></button>
            <button class="btn-choice-pill" data-mguess="forget"><span>How could I forget?</span></button>
            <button class="btn-choice-pill" data-mguess="maybe"><span>Maybe...</span></button>
            <button class="btn-choice-pill" data-mguess="why"><span>Bhai, why do you have this?</span></button>
          </div>

          <div class="machine-reaction-feedback" id="machine-reaction-box" style="display: none;">
            <p class="feedback-text handwriting" id="machine-reaction-text"></p>
            <button id="btn-enter-memory-journey" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">
                <span>Enter Memory Vault</span>
                <span class="btn-arrow">→</span>
              </span>
            </button>
          </div>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 7: MEMORY #01 (PARTNERS IN CRIME)                      -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-7" data-scene="7">
      <div class="screen-box full-photo-scene-card">
        <div class="screen-badge">
          <span>📸 MEMORY #01 • The Peda Special</span>
        </div>

        <div class="photo-contain-wrapper">
          <div class="photo-ambient-blur" style="background-image: url('assets/prerna-1.jpg');"></div>
          <div class="photo-frame-pure">
            <img 
              src="assets/prerna-1.jpg" 
              alt="Memory 1 - Partners in Crime" 
              class="personal-photo" 
              loading="eager"
              onerror="this.onerror=null; this.src='assets/prerna-1-fallback.svg';"
            >
          </div>
        </div>

        <div class="photo-caption-block">
          <h3 class="photo-main-caption handwriting">"Partners in crime."</h3>
          <p class="photo-sub-caption">Looking royal & radiant • The official Peda of the family ❤️</p>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-scene-7-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Next Memory</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 8: MEMORY #02 (ARGUMENT SPECIALISTS)                   -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-8" data-scene="8">
      <div class="screen-box full-photo-scene-card">
        <div class="screen-badge">
          <span>🏰 MEMORY #02 • Historic Throwback</span>
        </div>

        <div class="photo-contain-wrapper">
          <div class="photo-ambient-blur" style="background-image: url('assets/prerna-2.jpg');"></div>
          <div class="photo-frame-pure">
            <img 
              src="assets/prerna-2.jpg" 
              alt="Memory 2 - Professional Argument Specialists" 
              class="personal-photo" 
              loading="lazy"
              onerror="this.onerror=null; this.src='assets/prerna-2-fallback.svg';"
            >
          </div>
        </div>

        <div class="photo-caption-block">
          <h3 class="photo-main-caption handwriting">"Professional argument specialists."</h3>
          <p class="photo-sub-caption">Historic monument trips, classic poses, and eternal banter 📸</p>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-scene-8-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Next Memory</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 9: MEMORY #03 (CERTIFIED NAUTANKI)                     -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-9" data-scene="9">
      <div class="screen-box full-photo-scene-card">
        <div class="screen-badge">
          <span>🍕 MEMORY #03 • Food Chor Detected</span>
        </div>

        <div class="photo-contain-wrapper">
          <div class="photo-ambient-blur" style="background-image: url('assets/prerna-3.jpg');"></div>
          <div class="photo-frame-pure">
            <img 
              src="assets/prerna-3.jpg" 
              alt="Memory 3 - Certified Nautanki" 
              class="personal-photo" 
              loading="lazy"
              onerror="this.onerror=null; this.src='assets/prerna-3-fallback.svg';"
            >
          </div>
        </div>

        <div class="photo-caption-block">
          <h3 class="photo-main-caption handwriting">"Certified Nautanki."</h3>
          <p class="photo-sub-caption">"What's on your plate is officially my snack tax, Madam Ji." 🍟</p>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-scene-9-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Next Memory</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 10: MEMORY #04 (STILL MY FAVORITE GADHI)               -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-10" data-scene="10">
      <div class="screen-box full-photo-scene-card">
        <div class="screen-badge">
          <span>🌸 MEMORY #04 • Candid Smiles</span>
        </div>

        <div class="photo-contain-wrapper">
          <div class="photo-ambient-blur" style="background-image: url('assets/prerna-4.jpg');"></div>
          <div class="photo-frame-pure">
            <img 
              src="assets/prerna-4.jpg" 
              alt="Memory 4 - Still My Favorite Gadhi" 
              class="personal-photo" 
              loading="lazy"
              onerror="this.onerror=null; this.src='assets/prerna-4-fallback.svg';"
            >
          </div>
        </div>

        <div class="photo-caption-block">
          <h3 class="photo-main-caption handwriting">"Still my favorite Gadhi."</h3>
          <p class="photo-sub-caption">The sweetest smiles behind the most chaotic arguments ✨</p>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-scene-10-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Next Memory</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 11: MEMORY #05 (SOME MEMORIES...)                      -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-11" data-scene="11">
      <div class="screen-box full-photo-scene-card">
        <div class="screen-badge">
          <span>✨ MEMORY #05 • Pure Moments</span>
        </div>

        <div class="photo-contain-wrapper">
          <div class="photo-ambient-blur" style="background-image: url('assets/prerna-5.jpg');"></div>
          <div class="photo-frame-pure">
            <img 
              src="assets/prerna-5.jpg" 
              alt="Memory 5 - Some Memories Don't Need an Explanation" 
              class="personal-photo" 
              loading="lazy"
              onerror="this.onerror=null; this.src='assets/prerna-5-fallback.svg';"
            >
          </div>
        </div>

        <div class="photo-caption-block">
          <h3 class="photo-main-caption handwriting">"Some memories don't need an explanation."</h3>
          <p class="photo-sub-caption">23 years of laughter, drama, and growing up side-by-side 🌟</p>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-scene-11-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Next Memory</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 12: MEMORY #06 (SOMEHOW, YOU'RE STILL MY BHENA)        -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-12" data-scene="12">
      <div class="screen-box full-photo-scene-card">
        <div class="screen-badge">
          <span>🤍 MEMORY #06 • The Sibling Hug</span>
        </div>

        <div class="photo-contain-wrapper">
          <div class="photo-ambient-blur" style="background-image: url('assets/prerna-6.jpg');"></div>
          <div class="photo-frame-pure">
            <img 
              src="assets/prerna-6.jpg" 
              alt="Memory 6 - Somehow You're Still My Bhena" 
              class="personal-photo" 
              loading="lazy"
              onerror="this.onerror=null; this.src='assets/prerna-6-fallback.svg';"
            >
          </div>
        </div>

        <div class="photo-caption-block">
          <h3 class="photo-main-caption handwriting">"Somehow, you're still my Bhena."</h3>
          <p class="photo-sub-caption">And truth is... I wouldn't trade you for anything in the world ❤️</p>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-scene-12-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>View Sibling Scoreboard</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 13: THE OFFICIAL SIBLING CUP SCOREBOARD                -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-13" data-scene="13">
      <div class="screen-box glass-card scorecard-card">
        <div class="screen-badge">
          <span>🏆 THE OFFICIAL SIBLING CUP</span>
        </div>

        <h2 class="prompt-title">PRERNA VS PRAKHAR</h2>
        <p class="prompt-sub">Official 23-Year Performance Audit:</p>

        <div class="scorecard-grid" id="sibling-cup-grid">
          <div class="score-row"><span class="score-metric">Drama</span><div class="score-values"><span class="prerna-score">Prerna: <strong id="cup-drama-p">0</strong></span><span class="vs-label">vs</span><span class="prakhar-score">Prakhar: <strong id="cup-drama-pr">0</strong></span></div></div>
          <div class="score-row"><span class="score-metric">Stubbornness</span><div class="score-values"><span class="prerna-score">Prerna: <strong id="cup-stub-p">0</strong></span><span class="vs-label">vs</span><span class="prakhar-score">Prakhar: <strong id="cup-stub-pr">0</strong></span></div></div>
          <div class="score-row"><span class="score-metric">Food Stealing</span><div class="score-values"><span class="prerna-score">Prerna: <strong id="cup-food-p">0</strong></span><span class="vs-label">vs</span><span class="prakhar-score">Prakhar: <strong id="cup-food-pr">0</strong></span></div></div>
          <div class="score-row"><span class="score-metric">Arguments</span><div class="score-values"><span class="prerna-score">Prerna: <strong id="cup-arg-p">0</strong></span><span class="vs-label">vs</span><span class="prakhar-score">Prakhar: <strong id="cup-arg-pr">0</strong></span></div></div>
          <div class="score-row"><span class="score-metric">Laziness</span><div class="score-values"><span class="prerna-score">Prerna: <strong id="cup-lazy-p">0</strong></span><span class="vs-label">vs</span><span class="prakhar-score">Prakhar: <strong id="cup-lazy-pr">0</strong></span></div></div>
          <div class="score-row highlight-score-row"><span class="score-metric">Caring</span><div class="score-values"><span class="prerna-score">Prerna: <strong>∞</strong></span><span class="vs-label">❤️</span><span class="prakhar-score">Prakhar: <strong>∞</strong></span></div></div>
          <div class="score-row"><span class="score-metric">Making Mom Angry</span><div class="score-values"><span class="prerna-score">Prerna: <strong id="cup-mom-p">0</strong></span><span class="vs-label">vs</span><span class="prakhar-score">Prakhar: <strong id="cup-mom-pr">0</strong></span></div></div>
          <div class="score-row highlight-score-row"><span class="score-metric">Secret Teamwork</span><div class="score-values"><span class="prerna-score">Prerna: <strong>100%</strong></span><span class="vs-label">🤝</span><span class="prakhar-score">Prakhar: <strong>100%</strong></span></div></div>
        </div>

        <div class="scorecard-verdict-box">
          <p class="verdict-title handwriting">"WINNER: BOTH"</p>
          <p class="verdict-sub">"Unfortunately, you're stuck with each other. Lifetime contract: ACTIVE." 🤝</p>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-scene-13-next" class="btn-grand-gold">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Activate Roast Mode</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 14: ROAST MODE                                         -->
    <!-- ============================================================ -->
    <section class="story-screen dark-scene" id="scene-14" data-scene="14">
      <div class="screen-box roast-mode-box">
        <div class="screen-badge warning-badge">
          <span>⚠️ WARNING: SIBLING ROASTING DETECTED</span>
        </div>

        <!-- Warning Stage -->
        <div id="roast-warning-stage">
          <h2 class="prompt-title" style="color: #F87171;">"The following content contains unnecessary sibling roasting."</h2>
          <p class="prompt-sub" style="color: #FCE7F3; margin: 16px 0 24px;">Proceed at your own risk, Madam Ji.</p>
          <button id="btn-start-roast" class="btn-grand-gold pulse-btn">
            <span class="btn-shine"></span>
            <span class="btn-content"><span>Continue 😈</span></span>
          </button>
        </div>

        <!-- Active Roast Cards -->
        <div id="roast-active-stage" style="display: none;">
          <div class="roast-card-stack" id="roast-card-display">
            <div class="roast-icon">🔥</div>
            <p class="roast-text handwriting" id="roast-text-content">"23 years old and still stealing food from my plate."</p>
          </div>

          <div class="screen-action-wrap" style="gap: 12px;">
            <button id="btn-roast-next-item" class="btn-choice-pill"><span>Next Roast 🔥</span></button>
            <button id="btn-roast-finish" class="btn-primary-glow" style="display: none;">
              <span class="btn-shine"></span>
              <span class="btn-content"><span>Okay, Roasting Complete</span><span class="btn-arrow">→</span></span>
            </button>
          </div>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 15: THE SISTER NICKNAME GENERATOR                      -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-15" data-scene="15">
      <div class="screen-box glass-card slot-machine-card">
        <div class="screen-badge">
          <span>🎰 THE OFFICIAL SISTER NAME GENERATOR</span>
        </div>

        <p class="prompt-sub">Spinning family registry databases...</p>
        <h2 class="prompt-title">What is your true official title?</h2>

        <!-- Slot Machine Reels -->
        <div class="slot-machine-stage" id="slot-stage">
          <div class="slot-reel" id="reel-1"><span class="reel-val">MAHARANI</span></div>
          <div class="slot-plus">+</div>
          <div class="slot-reel" id="reel-2"><span class="reel-val">PEDA</span></div>
          <div class="slot-plus">+</div>
          <div class="slot-reel" id="reel-3"><span class="reel-val">DEVI</span></div>
        </div>

        <div class="slot-result-badge" id="slot-result-badge" style="display: none;">
          <h3 class="slot-title handwriting">"MAHARANI PEDA DEVI"</h3>
          <p class="slot-sub">CEO • Department of Annoying Bhai 👑</p>
          <p class="slot-note">"Congratulations. Your identity has been permanently updated in the family records."</p>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-spin-slot" class="btn-grand-gold pulse-btn">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>GENERATE MY OFFICIAL NAME 🎰</span>
            </span>
          </button>

          <button id="btn-slot-next" class="btn-primary-glow" style="display: none;">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>23 Things About You</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 16: 23 THINGS ABOUT MY BHENA                           -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-16" data-scene="16">
      <div class="screen-box glass-card twenty-three-card">
        <div class="screen-badge">
          <span>✨ AGE 23 SPECIAL • 23 REASONS</span>
        </div>

        <h2 class="prompt-title">23 Things About My Bhena</h2>
        <p class="prompt-sub">A genuine catalogue of 23 years:</p>

        <div class="traits-carousel-box" id="traits-carousel-box">
          <div class="trait-num-badge" id="trait-num-badge">01</div>
          <p class="trait-text handwriting" id="trait-text">Funny</p>
        </div>

        <div class="traits-progress-counter" id="traits-counter">1 of 23</div>

        <div class="screen-action-wrap" style="gap: 10px;">
          <button id="btn-trait-next" class="btn-choice-pill"><span>Next Reason 🌸</span></button>
          <button id="btn-trait-all" class="btn-secondary-pill"><span>Show All 23</span></button>
          <button id="btn-trait-finish" class="btn-primary-glow" style="display: none;">
            <span class="btn-shine"></span>
            <span class="btn-content"><span>Star Compliments</span><span class="btn-arrow">→</span></span>
          </button>
        </div>

        <div class="all-23-grid" id="all-23-grid" style="display: none;"></div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 17: STAR COMPLIMENT GAME (NIGHT SKY)                   -->
    <!-- ============================================================ -->
    <section class="story-screen dark-scene star-game-scene" id="scene-17" data-scene="17">
      <div class="screen-box star-game-box">
        <div class="screen-badge glow-badge">
          <span>✨ Celestial Vault • Tap The Stars</span>
        </div>

        <h2 class="prompt-title" style="color: #FDE68A;">"Tap the stars."</h2>
        <p class="prompt-sub" style="color: #FCE7F3;">7 secret brotherly truths hidden in the night sky:</p>

        <!-- Interactive Constellation Sky -->
        <div class="night-sky-board" id="night-sky-board">
          <button class="glow-star-btn" data-star="1" style="top: 15%; left: 18%;">★</button>
          <button class="glow-star-btn" data-star="2" style="top: 25%; left: 75%;">★</button>
          <button class="glow-star-btn" data-star="3" style="top: 48%; left: 32%;">★</button>
          <button class="glow-star-btn" data-star="4" style="top: 55%; left: 82%;">★</button>
          <button class="glow-star-btn" data-star="5" style="top: 75%; left: 22%;">★</button>
          <button class="glow-star-btn" data-star="6" style="top: 78%; left: 68%;">★</button>
          <button class="glow-star-btn highlight-star" data-star="7" style="top: 38%; left: 52%;">✨</button>
        </div>

        <div class="star-revealed-msg-card" id="star-revealed-card">
          <p class="star-msg-text handwriting" id="star-msg-text">Tap any glowing star above...</p>
        </div>

        <div class="stars-unlocked-status" id="stars-unlocked-status">0 of 7 stars discovered</div>

        <div class="screen-action-wrap" id="star-finish-wrap" style="display: none;">
          <button id="btn-star-next" class="btn-grand-gold pulse-btn">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Tie Virtual Rakhi</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 18: RAKHI THREAD DRAG INTERACTION                      -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-18" data-scene="18">
      <div class="screen-box glass-card rakhi-thread-card">
        <div class="screen-badge">
          <span>🪢 Sacred Bond • Rakhi Interaction</span>
        </div>

        <h2 class="prompt-title">Tie The Sacred Rakhi</h2>
        <p class="prompt-sub">Click or drag the thread around the mandala:</p>

        <!-- Interactive Rakhi Mandala -->
        <div class="rakhi-drag-stage" id="rakhi-drag-stage">
          <div class="rakhi-center-mandala" id="rakhi-center-mandala" title="Click to tie thread 🌸">
            <span class="rakhi-art">🪢</span>
          </div>
          <div class="rakhi-thread-svg-wrap">
            <svg class="thread-svg" viewBox="0 0 200 200">
              <circle class="thread-path-bg" cx="100" cy="100" r="80"></circle>
              <circle class="thread-path-fill" id="thread-path-fill" cx="100" cy="100" r="80"></circle>
            </svg>
          </div>
        </div>

        <div class="rakhi-status-box" id="rakhi-status-box">
          <button id="btn-tie-rakhi-action" class="btn-secondary-pill">
            <span>Tie The Thread 🪢</span>
          </button>
        </div>

        <div class="rakhi-complete-msg" id="rakhi-complete-msg" style="display: none;">
          <div class="thread-connected-badge">THREAD CONNECTED ❤️</div>
          <p class="rakhi-quote handwriting">"Some bonds don't need Wi-Fi. They just need two idiots who grew up together."</p>
          <p class="rakhi-wishing handwriting">"Happy Rakhi, Bhena." 🌸</p>

          <button id="btn-rakhi-next" class="btn-primary-glow" style="margin-top: 16px;">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Read Dil Ki Baat (Shayari)</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 19: ORIGINAL SHAYARI SCENE                             -->
    <!-- ============================================================ -->
    <section class="story-screen dark-scene shayari-scene" id="scene-19" data-scene="19">
      <div class="screen-box shayari-card">
        <div class="screen-badge glow-badge">
          <span>🪔 Dil Ki Baat • Original Poetry</span>
        </div>

        <div class="shayari-mandala-wrap" id="shayari-mandala-egg" title="Tap the Rakhi 🌸 (Easter Egg #2)">
          <span class="mandala-icon">🪢</span>
        </div>

        <div class="shayari-lines-container" id="shayari-container">
          <p class="shayari-line s-l-1 devanagari-font">"रिश्ते कई मिले इस दुनिया में,<br>कुछ वक्त के साथ बदल गए..."</p>
          <p class="shayari-line s-l-2 devanagari-font">"कुछ दूर होकर भी पास रहे,<br>लेकिन बहन का रिश्ता... दिल में हमेशा वहीं रहता है।"</p>
          <p class="shayari-line s-l-3 devanagari-font">"पेडा है, पगली है, थोड़ी सी नटखट भी है,<br>कभी मेरी headache, कभी मेरी जान भी है।"</p>
          <p class="shayari-line s-l-4 devanagari-font highlight-shayari">"लड़ते हैं दोनों, ये तो रोज़ की कहानी है,<br>पर सच कहूँ Bhena, तू मेरी सबसे खास निशानी है।"</p>
        </div>

        <div class="easter-egg-toast" id="easter-egg-2-toast" style="display: none;">
          <span>🎉 +100 Bhena Points! You found the secret Rakhi tap! 🪢</span>
        </div>

        <div class="screen-action-wrap" id="shayari-action-wrap" style="opacity: 0;">
          <button id="btn-scene-19-next" class="btn-grand-gold">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Open The Secret Drawer</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 20: THE SECRET DRAWER                                  -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-20" data-scene="20">
      <div class="screen-box glass-card secret-drawer-card">
        <div class="screen-badge">
          <span>🗄️ Top Secret • Private Archive</span>
        </div>

        <h2 class="prompt-title">"I found something you probably shouldn't see."</h2>
        <p class="prompt-sub">Classified brotherly admissions:</p>

        <!-- Wooden Drawer -->
        <div class="drawer-cabinet-stage" id="drawer-cabinet-stage">
          <div class="drawer-box" id="drawer-pullable">
            <div class="drawer-handle" id="drawer-handle">═════</div>
            <span class="drawer-label">CONFIDENTIAL</span>
          </div>

          <!-- Revealed Note -->
          <div class="drawer-secret-note" id="drawer-secret-note" style="display: none;">
            <div class="note-header handwriting">THINGS PRAKHAR WILL NEVER ADMIT:</div>
            <ul class="note-list handwriting">
              <li>1. You're sometimes right.</li>
              <li>2. I do worry about you.</li>
              <li>3. You're actually fun to hang out with.</li>
              <li>4. I would miss you if you moved away.</li>
              <li>5. You're important to me.</li>
              <li>6. Don't tell anyone I wrote this.</li>
            </ul>
            <div class="note-footer handwriting">(Especially Mom. 🤫)</div>
          </div>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-open-drawer" class="btn-grand-gold pulse-btn">
            <span class="btn-shine"></span>
            <span class="btn-content"><span>OPEN DRAWER 🗄️</span></span>
          </button>

          <button id="btn-drawer-next" class="btn-primary-glow" style="display: none;">
            <span class="btn-shine"></span>
            <span class="btn-content"><span>Continue</span><span class="btn-arrow">→</span></span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 21: FAKE SYSTEM ERROR                                  -->
    <!-- ============================================================ -->
    <section class="story-screen dark-scene system-error-scene" id="scene-21" data-scene="21">
      <div class="screen-box glitch-terminal-box">
        <div class="screen-badge tech-badge" style="background: rgba(239, 68, 68, 0.2); border-color: #EF4444; color: #FCA5A5;">
          <span>⚠️ SYSTEM ERROR 0x8849</span>
        </div>

        <div class="glitch-text-wrapper">
          <h2 class="glitch-title">SYSTEM ERROR</h2>
          <p class="glitch-line">Too many sibling memories detected in buffer.</p>
          <div class="error-progress-bar">
            <div class="error-bar-fill" id="error-bar-fill"></div>
          </div>
          <div class="error-diagnosis" id="error-diagnosis" style="display: none;">
            <p class="diag-text">DIAGNOSIS: <span class="highlight-p">Prerna is apparently too important.</span></p>
            <p class="diag-sub">Recovery successful. Continuing emotional damage...</p>
          </div>
        </div>

        <div class="screen-action-wrap" id="error-next-wrap" style="display: none;">
          <button id="btn-error-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content"><span>Resume Story</span><span class="btn-arrow">→</span></span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 22: EMOTIONAL TRANSITION                               -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-22" data-scene="22">
      <div class="screen-box glass-card emotional-msg-card">
        <div class="screen-badge">
          <span>💌 From Prakhar • A Real Moment</span>
        </div>

        <div class="emotional-sequence" id="emotional-sequence">
          <p class="emo-preface">"Okay, Bhena."</p>
          <p class="emo-preface" style="margin-bottom: 14px;">"Mazak bahut kar liya. Ab sach mein ek baat bolni hai."</p>

          <div class="emo-interactive-lines" id="emo-lines-list">
            <p class="emo-line" data-idx="0">"We've fought."</p>
            <p class="emo-line" data-idx="1">"We've annoyed each other."</p>
            <p class="emo-line" data-idx="2">"We've laughed at the stupidest things."</p>
            <p class="emo-line" data-idx="3">"We've grown up together."</p>
            <p class="emo-line" data-idx="4">"And through all of it..."</p>
            <p class="emo-line emo-highlight handwriting" data-idx="5">"I've always been lucky to have you as my sister."</p>
          </div>

          <div class="emo-tap-hint" id="emo-tap-hint">
            <span>(Tap anywhere to reveal next line 🌸)</span>
          </div>

          <div class="screen-action-wrap" id="emo-action-wrap" style="display: none;">
            <button id="btn-scene-22-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">
                <span>Open The Letter</span>
                <span class="btn-sparkle">💌</span>
              </span>
            </button>
          </div>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 23: INTERACTIVE 3D LETTER                              -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-23" data-scene="23">
      <div class="screen-box glass-card letter-card">
        <div class="screen-badge">
          <span>📮 Handwritten Letter • Prakhar</span>
        </div>

        <div class="letter-preface-text">
          <h2 class="letter-title handwriting">"One thing I don't say often enough."</h2>
        </div>

        <!-- 3D Interactive Envelope -->
        <div class="envelope-stage" id="envelope-stage">
          <div class="envelope" id="story-envelope" role="button" tabindex="0" aria-label="Open Letter">
            <div class="envelope-back"></div>
            
            <!-- Sliding Letter Paper -->
            <div class="letter-paper" id="story-letter-paper">
              <div class="letter-stamp-top">🌸</div>
              <div class="letter-salutation handwriting">Dear Bhena,</div>
              <div class="letter-content-body handwriting">
                <p>Happy Raksha Bandhan.</p>
                <p>We've spent 23 years annoying each other, arguing over ridiculous things, stealing food, laughing at things nobody else would understand, and making memories along the way.</p>
                <p>I don't always say it, but having you as my sister is something I'm genuinely grateful for.</p>
                <p>No matter how much we argue, no matter where life takes us, you'll always have your brother standing beside you.</p>
                <p>Keep smiling. Keep being yourself. And don't become too sensible, because then I won't recognize you.</p>
                <p class="bold-highlight">Happy Rakhi, Bhena.</p>
              </div>
              <div class="letter-sign-off handwriting">
                <p>Your annoying brother,</p>
                <p class="sign-name" id="brother-sig" title="Click me! (Easter Egg #5)">Prakhar ❤️</p>
              </div>

              <!-- Floating Margin Notes -->
              <div class="margin-note m-n-1 handwriting" id="m-n-1">"I actually mean this."</div>
              <div class="margin-note m-n-2 handwriting" id="m-n-2">"Don't get emotional."</div>
              <div class="margin-note m-n-3 handwriting" id="m-n-3">"Seriously."</div>
            </div>

            <!-- Envelope Flaps & Wax Seal -->
            <div class="env-flap-left"></div>
            <div class="env-flap-right"></div>
            <div class="env-flap-bottom"></div>
            <div class="env-flap-top" id="env-flap-top"></div>
            
            <div class="env-wax-seal" id="env-wax-seal" title="Click to break seal">
              <div class="seal-inner-circle">
                <span>P & P</span>
              </div>
            </div>
          </div>
        </div>

        <div class="screen-action-wrap letter-action-wrap">
          <button id="btn-open-letter-trigger" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content"><span>OPEN LETTER 💌</span></span>
          </button>
          
          <button id="btn-scene-23-next" class="btn-grand-gold" style="display: none;">
            <span class="btn-shine"></span>
            <span class="btn-content"><span>A Message For The Future</span><span class="btn-arrow">→</span></span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 24: FUTURE MESSAGE (10 YEARS FROM NOW)                 -->
    <!-- ============================================================ -->
    <section class="story-screen dark-scene future-msg-scene" id="scene-24" data-scene="24">
      <div class="screen-box future-timecapsule-box">
        <div class="screen-badge tech-badge">
          <span>⏳ TIME CAPSULE • DELIVERY DATE: 10 YEARS FROM NOW</span>
        </div>

        <div class="timecapsule-card">
          <div class="tc-header">MESSAGE FROM: PRAKHAR</div>
          <div class="tc-content handwriting">
            <p>"If you're reading this years later, I hope you're happy.</p>
            <p>I hope you've achieved the things you wanted.</p>
            <p>I hope life has been kind to you.</p>
            <p>And I hope you're still annoying me, because some things should never change.</p>
            <p class="tc-bold">No matter how old we get, you'll always be my Bhena."</p>
          </div>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-scene-24-next" class="btn-grand-gold pulse-btn">
            <span class="btn-shine"></span>
            <span class="btn-content"><span>The Final Surprise</span><span class="btn-arrow">→</span></span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 25: FINAL SUSPENSE                                     -->
    <!-- ============================================================ -->
    <section class="story-screen dark-scene suspense-scene" id="scene-25" data-scene="25">
      <div class="screen-box minimalist-suspense-box">
        <div class="suspense-lines-wrap">
          <h2 class="suspense-line su-1" id="su-line-1">"Wait..."</h2>
          <p class="suspense-line su-2" id="su-line-2">"I forgot something."</p>
          <p class="suspense-line su-3" id="su-line-3">"Actually..."</p>
          <p class="suspense-line su-4 handwriting" id="su-line-4">"There's one last thing."</p>
          <p class="suspense-line su-5 handwriting" id="su-line-5" style="color: #F59E0B; font-size: 2.2rem;">"Ready, Peda?"</p>
        </div>

        <div class="screen-action-wrap" id="su-action-wrap" style="display: none;">
          <button id="btn-reveal-rakhi-surprise" class="btn-grand-gold pulse-btn">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>REVEAL MY RAKHI SURPRISE ❤️</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 26: FINAL PHOTO REVEAL (PRERNA-TOGETHER.JPG CONTAINED) -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-26" data-scene="26">
      <div class="screen-box full-photo-scene-card finale-photo-card">
        <div class="screen-badge glow-badge">
          <span>👑 Chapter 26 • Sibling Bond Forever</span>
        </div>

        <!-- Uncropped Full Together Photo -->
        <div class="photo-contain-wrapper grand-together-wrapper">
          <div class="photo-ambient-blur" style="background-image: url('assets/prerna-together.jpg');"></div>
          <div class="photo-frame-pure gold-border-frame">
            <img 
              src="assets/prerna-together.jpg" 
              alt="Prerna & Prakhar Together" 
              class="personal-photo" 
              id="together-photo-img"
              loading="eager"
              onerror="this.onerror=null; this.src='assets/prerna-together-fallback.svg';"
            >
          </div>
        </div>

        <div class="photo-caption-block">
          <h2 class="grand-festive-title handwriting">HAPPY RAKSHA BANDHAN</h2>
          <h3 class="grand-sister-name handwriting">Prerna</h3>
          <p class="grand-milestone-tag">23 years • Countless memories • One irreplaceable Bhena.</p>
          <p class="grand-emotional-message">
            "No matter where life takes us... You'll always have your brother."
          </p>
          <p class="grand-love-note handwriting">Love you always ❤️</p>
          <p class="grand-sign-text">— <strong>Prakhar</strong></p>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-scene-26-next" class="btn-grand-gold pulse-btn">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Celebrate With Music 🎉</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 27: SONG + FIREWORKS + GRAND FINALE CELEBRATION        -->
    <!-- ============================================================ -->
    <section class="story-screen finale-celebration-scene" id="scene-27" data-scene="27">
      <div class="screen-box glass-card grand-celebration-card">
        <div class="grand-crown-badge">
          <span>👑✨ Happy Raksha Bandhan, Bhena! ✨👑</span>
        </div>

        <!-- Music Player Widget (assets/song.mp3) -->
        <div class="music-player-widget" id="music-player-widget">
          <div class="music-info-row">
            <span class="music-note-icon">♫</span>
            <span class="music-title-text" id="music-status-text">Playing: Ek Hazaaron Mein Meri Behna Hai</span>
          </div>
          <div class="music-controls-row">
            <button id="btn-audio-play-pause" class="player-btn" aria-label="Play or Pause">❚❚</button>
            <input type="range" id="audio-volume-slider" min="0" max="1" step="0.05" value="0.8" class="volume-slider" aria-label="Volume">
            <button id="btn-audio-mute" class="player-btn" aria-label="Mute or Unmute">🔊</button>
          </div>
          <!-- Audio Element (assets/song.mp3) -->
          <audio id="rakhi-audio-element" src="assets/song.mp3" preload="none"></audio>
        </div>

        <div class="grand-celebration-text">
          <h1 class="grand-festive-title handwriting">Happy Raksha Bandhan, Peda!</h1>
          <p class="grand-milestone-tag">"My sister. My partner in crime. My permanent headache."</p>
          <p class="grand-emotional-message">
            "And one of the people I will always protect."
          </p>
          <p class="grand-love-note handwriting">Love you always.</p>
          <p class="grand-sign-text">— <strong>Prakhar ❤️</strong></p>
        </div>

        <!-- Grand Celebration Interactive Actions -->
        <div class="grand-actions-bar">
          <button id="btn-cannon-more" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>More Fireworks & Confetti! 🎉</span>
            </span>
          </button>
          
          <button id="btn-diya-bless" class="btn-secondary-pill">
            <span>Light Sister Diya 🪔</span>
          </button>

          <button id="btn-download-keepsake" class="btn-secondary-pill">
            <span>Save Keepsake Card 💌</span>
          </button>
        </div>

        <!-- Diya Blessing Toast Box -->
        <div class="blessing-toast-box" id="blessing-toast-box" style="display: none;">
          <span class="toast-diya-flame">🪔</span>
          <p class="toast-text handwriting">A sacred diya lit for Prerna's endless health, happiness & joy forever!</p>
        </div>

        <!-- Easter Egg Toast Notifications -->
        <div class="easter-egg-toast" id="easter-egg-1-toast" style="display: none;">
          <span>😂 "I literally told you not to touch it!" +10 Sibling Chaos Points!</span>
        </div>
        <div class="easter-egg-toast" id="easter-egg-4-toast" style="display: none;">
          <span>👑 "P detected. Obviously this website belongs to the Peda."</span>
        </div>
        <div class="easter-egg-toast" id="easter-egg-5-toast" style="display: none;">
          <span>🛠️ "Yes, I made all of this instead of doing something productive."</span>
        </div>

        <!-- Replay from beginning button -->
        <div class="replay-wrap">
          <button id="btn-replay-story" class="replay-link-btn">
            <span>↺ Relive the entire story from the beginning</span>
          </button>
        </div>
      </div>
    </section>

  </main>

  <!-- Transparent Privacy Notice -->
  <footer class="privacy-notice-bar" aria-label="Privacy Note">
    <p>Your answers in this interactive surprise may be saved so your brother can see them later ❤️</p>
  </footer>

  <!-- Script -->
  <script src="script.js"></script>
</body>
</html>
"""
    # Write to both frontend and root for absolute convenience
    for path in [os.path.join(FRONTEND_DIR, "index.html"), os.path.join(BASE_DIR, "index.html")]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    print("✓ Generated index.html in frontend/ and root")

def generate_style_css():
    content = r"""/* ==========================================================================
   RAKHI SURPRISE STORY • 27-SCENE INTERACTIVE CINEMATIC EXPERIENCE
   Dedicated to Prerna (Peda) • Crafted with love by Prakhar
   ========================================================================== */

/* --- 1. CSS Variables & Design Tokens --- */
:root {
  --color-bg-main: #FFFDF9;
  --color-bg-cream: #FAF5EE;
  --color-dark-burgundy: #1B0C15;
  --color-dark-surface: #12070E;
  
  --color-pink-soft: #FCE7F3;
  --color-pink-mid: #F472B6;
  --color-pink-deep: #DB2777;
  --color-rose-dark: #881337;
  --color-rose-vivid: #E11D48;
  
  --color-peach: #FFEDD5;
  --color-lavender: #EDE9FE;
  --color-gold-light: #FEF3C7;
  --color-gold-main: #F59E0B;
  --color-gold-deep: #B45309;
  
  --color-text-main: #2D1822;
  --color-text-muted: #5E3A4B;
  --color-text-light: #8C6A7B;

  --font-primary: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-body: 'Plus Jakarta Sans', sans-serif;
  --font-heading: 'Playfair Display', Georgia, serif;
  --font-handwriting: 'Caveat', 'Marck Script', cursive;
  --font-devanagari: 'Rozha One', 'Yatra One', serif;

  --glass-bg: rgba(255, 255, 255, 0.9);
  --glass-border: rgba(254, 205, 211, 0.6);
  --glass-shadow: 0 20px 50px rgba(136, 19, 55, 0.08), 0 4px 12px rgba(0, 0, 0, 0.03);
  --glass-shadow-hover: 0 26px 60px rgba(136, 19, 55, 0.15);

  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
  --transition-fast: 0.22s cubic-bezier(0.4, 0, 0.2, 1);
}

/* --- 2. Reset & Global Styles --- */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body {
  width: 100%;
  min-height: 100%;
  overflow-x: hidden;
  background-color: var(--color-bg-main);
  color: var(--color-text-main);
  font-family: var(--font-primary);
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Ambient dynamic background */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background: 
    radial-gradient(circle at 15% 20%, rgba(252, 231, 243, 0.65) 0%, transparent 45%),
    radial-gradient(circle at 85% 30%, rgba(254, 243, 199, 0.55) 0%, transparent 50%),
    radial-gradient(circle at 50% 80%, rgba(237, 233, 254, 0.55) 0%, transparent 55%),
    radial-gradient(circle at 80% 85%, rgba(255, 237, 213, 0.5) 0%, transparent 40%);
  pointer-events: none;
  z-index: 0;
}

/* --- 3. Interactive Canvas Layers --- */
#bg-canvas,
#fireworks-canvas,
#confetti-canvas,
#hearts-canvas,
#sparkle-cursor-canvas {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

#bg-canvas { z-index: 1; }
#fireworks-canvas { z-index: 97; }
#sparkle-cursor-canvas { z-index: 98; }
#hearts-canvas { z-index: 99; }
#confetti-canvas { z-index: 100; }

/* --- 4. Top Minimalist Story Bar --- */
.top-story-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 80;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  background: rgba(255, 253, 249, 0.82);
  border-bottom: 1px solid rgba(254, 205, 211, 0.45);
}

.brand-chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.95);
  padding: 6px 14px;
  border-radius: 999px;
  border: 1px solid rgba(225, 29, 72, 0.15);
  box-shadow: 0 2px 8px rgba(225, 29, 72, 0.05);
}

.brand-icon { font-size: 1rem; }
.brand-text {
  font-family: var(--font-primary);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--color-rose-dark);
}

/* Subtle Progress Track & Dots */
.story-progress-indicator {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  max-width: 380px;
  width: 100%;
  margin: 0 12px;
}

.progress-track {
  width: 100%;
  height: 3px;
  background: rgba(225, 29, 72, 0.1);
  border-radius: 999px;
  overflow: hidden;
}

.progress-bar-fill {
  width: 3.7%;
  height: 100%;
  background: linear-gradient(90deg, #F472B6 0%, #E11D48 50%, #F59E0B 100%);
  border-radius: 999px;
  transition: width 0.45s var(--ease-smooth);
}

.progress-dots-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  gap: 1px;
}

.prog-dot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: rgba(136, 19, 55, 0.2);
  transition: all 0.3s ease;
}

.prog-dot.completed {
  background: var(--color-pink-deep);
}

.prog-dot.active {
  background: var(--color-gold-main);
  transform: scale(1.6);
  box-shadow: 0 0 6px rgba(245, 158, 11, 0.8);
}

.top-controls {
  display: flex;
  align-items: center;
  gap: 8px;
}

.control-pill-btn {
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid rgba(225, 29, 72, 0.18);
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--color-rose-dark);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  transition: all var(--transition-fast);
}

.control-pill-btn:hover {
  background: #FFFFFF;
  border-color: var(--color-pink-deep);
  transform: translateY(-1px);
}

.warning-pill {
  color: #B91C1C;
  border-color: rgba(254, 202, 202, 0.8);
}

/* --- 5. Main Story Viewport & Screens Architecture --- */
.story-viewport {
  position: relative;
  z-index: 10;
  width: 100%;
  min-height: 100vh;
  padding-top: 68px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-bottom: 34px;
}

.story-screen {
  display: none;
  opacity: 0;
  width: 100%;
  min-height: calc(100vh - 102px);
  padding: 16px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.story-screen.active {
  display: flex;
  opacity: 1;
  animation: screen-fade-in 0.5s var(--ease-smooth) forwards;
}

.story-screen.slide-in-right {
  animation: screen-slide-right 0.5s var(--ease-smooth) forwards;
}

.story-screen.slide-in-left {
  animation: screen-slide-left 0.5s var(--ease-smooth) forwards;
}

.dark-scene {
  background: radial-gradient(circle at 50% 50%, #1B0C15 0%, #0F050C 100%);
  color: #FFFFFF;
}

@keyframes screen-fade-in {
  from { opacity: 0; transform: scale(0.96) translateY(12px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}

@keyframes screen-slide-right {
  from { opacity: 0; transform: translateX(40px) scale(0.97); }
  to { opacity: 1; transform: translateX(0) scale(1); }
}

@keyframes screen-slide-left {
  from { opacity: 0; transform: translateX(-40px) scale(0.97); }
  to { opacity: 1; transform: translateX(0) scale(1); }
}

/* --- 6. Reusable Card & Header Styles --- */
.screen-box {
  width: min(100%, 720px);
  margin: 0 auto;
  position: relative;
  text-align: center;
}

.glass-card {
  background: var(--glass-bg);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border: 1.5px solid var(--glass-border);
  border-radius: 28px;
  padding: clamp(24px, 5vw, 42px) clamp(16px, 4vw, 34px);
  box-shadow: var(--glass-shadow);
  position: relative;
  overflow: hidden;
}

.screen-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 16px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.95);
  border: 1px solid rgba(225, 29, 72, 0.18);
  color: var(--color-rose-dark);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.4px;
  margin-bottom: 18px;
  box-shadow: 0 4px 12px rgba(225, 29, 72, 0.06);
}

.glow-badge {
  background: rgba(245, 158, 11, 0.15);
  border-color: rgba(245, 158, 11, 0.45);
  color: #FDE68A;
  box-shadow: 0 0 16px rgba(245, 158, 11, 0.25);
}

.tech-badge {
  background: rgba(52, 211, 153, 0.12);
  border-color: rgba(52, 211, 153, 0.4);
  color: #34D399;
  font-family: monospace;
  letter-spacing: 1px;
}

.warning-badge {
  background: rgba(239, 68, 68, 0.15);
  border-color: rgba(239, 68, 68, 0.4);
  color: #F87171;
}

.handwriting {
  font-family: var(--font-handwriting);
}

.devanagari-font {
  font-family: var(--font-devanagari);
}

/* --- 7. Buttons Design System --- */
.btn-primary-glow {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #E11D48 0%, #DB2777 50%, #9333EA 100%);
  color: #FFFFFF;
  font-family: var(--font-primary);
  font-size: 1.05rem;
  font-weight: 600;
  padding: 14px 34px;
  border-radius: 999px;
  border: none;
  cursor: pointer;
  box-shadow: 0 12px 30px rgba(225, 29, 72, 0.35), 0 0 0 1px rgba(255, 255, 255, 0.25) inset;
  overflow: hidden;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast);
  text-decoration: none;
}

.btn-primary-glow:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 16px 38px rgba(225, 29, 72, 0.45);
}

.btn-primary-glow:active {
  transform: translateY(1px) scale(0.98);
}

.btn-shine {
  position: absolute;
  top: 0;
  left: -100%;
  width: 60%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.35), transparent);
  transform: skewX(-25deg);
  animation: shine-sweep 3.5s infinite ease-in-out;
}

.btn-content {
  position: relative;
  z-index: 2;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.btn-grand-gold {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #F59E0B 0%, #D97706 50%, #B45309 100%);
  color: #FFFFFF;
  font-family: var(--font-primary);
  font-size: 1.12rem;
  font-weight: 700;
  padding: 15px 38px;
  border-radius: 999px;
  border: 2px solid #FDE68A;
  cursor: pointer;
  box-shadow: 0 15px 35px rgba(217, 119, 6, 0.4), 0 0 25px rgba(251, 191, 36, 0.35);
  overflow: hidden;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast);
}

.btn-grand-gold:hover {
  transform: translateY(-2px) scale(1.03);
  box-shadow: 0 20px 45px rgba(217, 119, 6, 0.5), 0 0 35px rgba(251, 191, 36, 0.55);
}

.btn-secondary-pill {
  background: rgba(255, 255, 255, 0.95);
  border: 1px solid rgba(225, 29, 72, 0.2);
  color: var(--color-rose-dark);
  font-family: var(--font-primary);
  font-weight: 600;
  font-size: 0.92rem;
  padding: 11px 22px;
  border-radius: 999px;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(225, 29, 72, 0.08);
  transition: all var(--transition-fast);
}

.btn-secondary-pill:hover {
  background: #FFFFFF;
  border-color: var(--color-pink-deep);
  transform: translateY(-2px);
}

.btn-choice-pill {
  background: rgba(255, 255, 255, 0.95);
  border: 1.5px solid rgba(225, 29, 72, 0.18);
  padding: 12px 20px;
  border-radius: 999px;
  font-family: var(--font-primary);
  font-size: 0.98rem;
  font-weight: 600;
  color: var(--color-text-main);
  cursor: pointer;
  transition: all var(--transition-fast);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
}

.btn-choice-pill:hover {
  background: #FFFFFF;
  border-color: var(--color-pink-deep);
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 8px 20px rgba(225, 29, 72, 0.14);
}

.screen-action-wrap {
  margin-top: 24px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: opacity 0.5s ease;
}

/* --- 8. SCENE 1: OPENING MYSTERY --- */
.opening-mystery-card {
  padding: 50px 20px;
}

.cinematic-text-stream {
  margin-bottom: 28px;
}

.cinematic-line {
  line-height: 1.35;
  margin-bottom: 12px;
  opacity: 0;
}

.c-line-1 {
  font-family: var(--font-heading);
  font-size: clamp(2.4rem, 6.5vw, 3.6rem);
  color: #FDE68A;
}

.c-line-2 {
  font-size: clamp(1.25rem, 3.8vw, 1.65rem);
  color: #FCE7F3;
  font-weight: 500;
}

.c-line-3 {
  font-size: clamp(2rem, 5.5vw, 2.8rem);
  color: #F59E0B;
  font-weight: 700;
}

.mystery-envelope-wrap {
  margin: 16px auto 24px;
}

.mystery-envelope-icon {
  font-size: clamp(4rem, 10vw, 6rem);
  display: inline-block;
  filter: drop-shadow(0 0 25px rgba(245, 158, 11, 0.6));
}

.s1-reveal-msg {
  margin-top: 24px;
  font-size: clamp(1.8rem, 5vw, 2.6rem);
  color: #FDE68A;
  animation: pop-in 0.6s var(--ease-spring);
}

/* --- 9. SCENE 2: FUTURISTIC SCANNER --- */
.futuristic-scanner-card {
  background: rgba(18, 7, 14, 0.95);
  border: 1.5px solid rgba(52, 211, 153, 0.35);
  border-radius: 28px;
  padding: 36px 24px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba(52, 211, 153, 0.15);
}

.tech-title {
  color: #FDE68A;
  font-size: clamp(1.8rem, 5vw, 2.4rem);
}

.tech-input {
  background: rgba(15, 23, 42, 0.85);
  border: 2px solid rgba(52, 211, 153, 0.4);
  color: #34D399;
  font-family: monospace;
}

.tech-input:focus {
  border-color: #34D399;
  box-shadow: 0 0 15px rgba(52, 211, 153, 0.35);
}

.scanning-terminal-box {
  background: #0B0409;
  border: 1px solid rgba(52, 211, 153, 0.25);
  border-radius: 14px;
  padding: 14px 18px;
  color: #34D399;
  font-family: monospace;
  font-size: 0.92rem;
  margin: 14px auto;
  max-width: 440px;
}

.scan-progress-bar {
  width: 100%;
  height: 8px;
  background: rgba(255, 255, 255, 0.12);
  border-radius: 999px;
  margin-top: 8px;
  overflow: hidden;
}

.scan-bar-fill {
  width: 0%;
  height: 100%;
  background: #34D399;
  border-radius: 999px;
  transition: width 1.2s ease-in-out;
}

.identity-card-badge {
  background: #0F050D;
  border: 2px solid #34D399;
  border-radius: 18px;
  padding: 20px;
  max-width: 380px;
  margin: 18px auto;
  text-align: left;
  font-family: monospace;
  box-shadow: 0 0 25px rgba(52, 211, 153, 0.25);
  animation: pop-in 0.5s var(--ease-spring);
}

.id-header {
  font-weight: 800;
  color: #34D399;
  text-align: center;
  font-size: 1.1rem;
  margin-bottom: 12px;
  letter-spacing: 1px;
}

.id-row {
  display: flex;
  justify-content: space-between;
  padding: 4px 0;
  color: #E2E8F0;
  font-size: 0.95rem;
}

.text-green { color: #34D399; }
.id-footer {
  text-align: center;
  font-size: 1.5rem;
  color: #FDE68A;
  margin-top: 14px;
}

/* --- 10. SCENE 3 & 4: FUNNY AGE & INTELLIGENCE TEST --- */
.huge-number-anim {
  font-size: clamp(3.8rem, 10vw, 5.5rem);
  font-family: var(--font-heading);
  font-weight: 700;
  color: var(--color-pink-deep);
  margin-bottom: 4px;
}

.age-interactive-choices {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin: 20px 0;
}

.quiz-options-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: 480px;
  margin: 18px auto;
}

.quiz-opt-item-btn {
  background: rgba(255, 255, 255, 0.95);
  border: 1.5px solid rgba(225, 29, 72, 0.16);
  border-radius: 16px;
  padding: 12px 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 12px;
  text-align: left;
  font-family: var(--font-primary);
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-text-main);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
  transition: all var(--transition-fast);
}

.quiz-opt-item-btn:hover {
  background: #FFFFFF;
  border-color: var(--color-pink-deep);
  transform: translateX(4px);
  box-shadow: 0 8px 20px rgba(225, 29, 72, 0.12);
}

.quiz-opt-key {
  width: 30px;
  height: 30px;
  border-radius: 8px;
  background: rgba(225, 29, 72, 0.08);
  color: var(--color-rose-dark);
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.quiz-feedback-box, .age-reaction-box, .wyr-feedback-box {
  margin-top: 18px;
  animation: pop-in 0.4s var(--ease-spring);
}

.feedback-text {
  font-size: 1.55rem;
  font-weight: 700;
  color: var(--color-rose-dark);
  margin-bottom: 16px;
  line-height: 1.3;
}

.dark-scene .feedback-text {
  color: #FDE68A;
}

/* --- 11. SCENE 5: WOULD YOU RATHER --- */
.wyr-cards-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  margin: 20px 0 12px;
  flex-wrap: wrap;
}

.wyr-card {
  flex: 1 1 240px;
  max-width: 270px;
  background: #FFFFFF;
  border: 2px solid rgba(225, 29, 72, 0.15);
  border-radius: 20px;
  padding: 24px 18px;
  cursor: pointer;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05);
  transition: all var(--transition-fast);
  text-align: center;
}

.wyr-badge {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 800;
  color: var(--color-pink-deep);
  background: var(--color-pink-soft);
  padding: 3px 10px;
  border-radius: 999px;
  margin-bottom: 10px;
}

.wyr-card-text {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--color-rose-dark);
  line-height: 1.35;
}

.wyr-divider {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 1.2rem;
  color: var(--color-gold-deep);
}

.wyr-card:hover, .wyr-card.selected {
  transform: translateY(-4px) scale(1.04);
  border-color: var(--color-pink-deep);
  box-shadow: 0 16px 35px rgba(225, 29, 72, 0.18);
}

/* --- 12. SCENE 6: MEMORY MACHINE 3000 --- */
.machine-terminal-graphic {
  background: #0B0409;
  border: 2px solid #F59E0B;
  border-radius: 24px;
  padding: 28px;
  max-width: 420px;
  margin: 20px auto;
  box-shadow: 0 0 30px rgba(245, 158, 11, 0.25);
}

.machine-lens {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  border: 3px dashed #F59E0B;
  margin: 0 auto 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  animation: spin-slow 12s linear infinite;
}

.machine-status-msg {
  font-family: monospace;
  font-size: 0.95rem;
  color: #34D399;
  letter-spacing: 1px;
}

.recovered-badge {
  display: inline-block;
  background: #34D399;
  color: #0B0409;
  font-weight: 800;
  padding: 4px 14px;
  border-radius: 999px;
  font-family: monospace;
  margin-bottom: 10px;
}

.recovered-prompt {
  font-size: 1.4rem;
  color: #FDE68A;
  margin-bottom: 16px;
}

.guess-actions-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-bottom: 14px;
}

/* --- 13. SCENES 7–12: FULL UNTOUCHED PERSONAL PHOTOS (CONTAINED) --- */
.full-photo-scene-card {
  padding: 20px 14px;
  max-width: 920px;
}

.photo-contain-wrapper {
  position: relative;
  width: min(92vw, 860px);
  height: min(60vh, 520px);
  margin: 0 auto 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
  background: #1B0C15;
}

.photo-ambient-blur {
  position: absolute;
  inset: -20px;
  background-size: cover;
  background-position: center;
  filter: blur(28px) brightness(0.75);
  opacity: 0.55;
  z-index: 1;
}

.photo-frame-pure {
  position: relative;
  z-index: 2;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
}

.personal-photo {
  max-width: 100%;
  max-height: 100%;
  width: auto;
  height: auto;
  object-fit: contain !important;
  border-radius: 12px;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);
  display: block;
}

.gold-border-frame {
  border: 3px solid #F59E0B;
  border-radius: 16px;
}

.photo-caption-block {
  margin-top: 14px;
  text-align: center;
}

.photo-main-caption {
  font-size: clamp(1.8rem, 4.5vw, 2.5rem);
  color: var(--color-rose-dark);
  font-weight: 700;
  line-height: 1.25;
  margin-bottom: 4px;
}

.photo-sub-caption {
  font-size: 0.95rem;
  color: var(--color-text-muted);
  font-weight: 600;
}

/* --- 14. SCENE 13: SIBLING CUP SCOREBOARD --- */
.scorecard-grid {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: 480px;
  margin: 20px auto;
}

.score-row {
  background: #FFFFFF;
  border: 1.5px solid rgba(225, 29, 72, 0.15);
  border-radius: 14px;
  padding: 12px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
}

.score-metric {
  font-weight: 700;
  color: var(--color-rose-dark);
  font-size: 1rem;
}

.score-values {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
  font-size: 0.92rem;
}

.prerna-score { color: var(--color-pink-deep); }
.prakhar-score { color: #2563EB; }
.vs-label { color: var(--color-text-light); font-size: 0.78rem; }

.highlight-score-row {
  border-color: #F59E0B;
  background: linear-gradient(135deg, #FFFDF9 0%, #FEF3C7 100%);
}

.scorecard-verdict-box {
  margin: 16px auto 6px;
}

.verdict-title {
  font-size: 2rem;
  color: var(--color-pink-deep);
  font-weight: 700;
}

.verdict-sub {
  font-size: 0.95rem;
  color: var(--color-text-muted);
  font-weight: 600;
}

/* --- 15. SCENE 14: ROAST MODE --- */
.roast-card-stack {
  background: #2D1420;
  border: 2px solid #F87171;
  border-radius: 24px;
  padding: 36px 24px;
  max-width: 480px;
  margin: 20px auto;
  box-shadow: 0 16px 40px rgba(239, 68, 68, 0.2);
}

.roast-icon {
  font-size: 3rem;
  margin-bottom: 12px;
}

.roast-text {
  font-size: clamp(1.6rem, 4.5vw, 2.2rem);
  color: #FDE68A;
  line-height: 1.35;
}

/* --- 16. SCENE 15: NICKNAME SLOT MACHINE --- */
.slot-machine-stage {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin: 24px auto;
  flex-wrap: wrap;
}

.slot-reel {
  background: #1B0C15;
  border: 2px solid #F59E0B;
  border-radius: 16px;
  padding: 16px 14px;
  min-width: 140px;
  color: #FDE68A;
  font-weight: 800;
  font-size: 1.1rem;
  box-shadow: 0 0 15px rgba(245, 158, 11, 0.25);
}

.slot-plus {
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--color-pink-deep);
}

.slot-result-badge {
  background: #FEF3C7;
  border: 2px solid #F59E0B;
  border-radius: 20px;
  padding: 18px;
  max-width: 440px;
  margin: 18px auto;
  animation: pop-in 0.5s var(--ease-spring);
}

.slot-title {
  font-size: 2.2rem;
  color: #B45309;
}

.slot-sub {
  font-weight: 700;
  color: var(--color-rose-dark);
  font-size: 0.95rem;
}

.slot-note {
  font-size: 0.85rem;
  color: #78350F;
  margin-top: 6px;
}

/* --- 17. SCENE 16: 23 THINGS --- */
.traits-carousel-box {
  background: #FFFFFF;
  border: 2px solid rgba(225, 29, 72, 0.2);
  border-radius: 24px;
  padding: 34px 20px;
  max-width: 420px;
  margin: 20px auto 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
}

.trait-num-badge {
  display: inline-block;
  font-size: 1rem;
  font-weight: 800;
  color: var(--color-pink-deep);
  background: var(--color-pink-soft);
  padding: 4px 14px;
  border-radius: 999px;
  margin-bottom: 12px;
}

.trait-text {
  font-size: clamp(2rem, 5.5vw, 2.8rem);
  color: var(--color-rose-dark);
  line-height: 1.25;
}

.traits-progress-counter {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--color-text-light);
}

.all-23-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
  gap: 8px;
  margin-top: 20px;
  max-height: 280px;
  overflow-y: auto;
  padding: 10px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 16px;
}

.grid-trait-chip {
  background: #FFF1F2;
  border: 1px solid rgba(225, 29, 72, 0.15);
  border-radius: 10px;
  padding: 8px 6px;
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--color-rose-dark);
}

/* --- 18. SCENE 17: STAR COMPLIMENT GAME --- */
.night-sky-board {
  position: relative;
  width: min(90vw, 480px);
  height: 240px;
  margin: 16px auto;
  background: radial-gradient(circle, #2D1420 0%, #0F050C 100%);
  border-radius: 20px;
  border: 1.5px solid rgba(245, 158, 11, 0.35);
  overflow: hidden;
}

.glow-star-btn {
  position: absolute;
  background: none;
  border: none;
  color: #FDE68A;
  font-size: 1.8rem;
  cursor: pointer;
  transition: transform var(--transition-fast), filter var(--transition-fast);
  filter: drop-shadow(0 0 8px rgba(245, 158, 11, 0.8));
}

.glow-star-btn:hover, .glow-star-btn.discovered {
  transform: scale(1.4);
  color: #F59E0B;
  filter: drop-shadow(0 0 16px rgba(245, 158, 11, 1));
}

.highlight-star {
  font-size: 2.2rem;
  color: #F472B6;
}

.star-revealed-msg-card {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(245, 158, 11, 0.3);
  border-radius: 16px;
  padding: 16px 20px;
  max-width: 440px;
  margin: 0 auto 10px;
  min-height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.star-msg-text {
  font-size: 1.45rem;
  color: #FDE68A;
  line-height: 1.35;
}

.stars-unlocked-status {
  font-size: 0.85rem;
  color: #FCE7F3;
  font-weight: 600;
}

/* --- 19. SCENE 18: RAKHI THREAD INTERACTION --- */
.rakhi-drag-stage {
  position: relative;
  width: 200px;
  height: 200px;
  margin: 20px auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

.rakhi-center-mandala {
  position: relative;
  z-index: 5;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: radial-gradient(circle, #F59E0B 0%, #B45309 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.8rem;
  box-shadow: 0 0 25px rgba(245, 158, 11, 0.5);
  cursor: pointer;
  transition: transform 0.2s var(--ease-spring);
}

.rakhi-center-mandala:active {
  transform: scale(1.15) rotate(15deg);
}

.rakhi-thread-svg-wrap {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.thread-svg {
  width: 100%;
  height: 100%;
}

.thread-path-bg {
  fill: none;
  stroke: rgba(225, 29, 72, 0.15);
  stroke-width: 6;
}

.thread-path-fill {
  fill: none;
  stroke: #E11D48;
  stroke-width: 6;
  stroke-dasharray: 502;
  stroke-dashoffset: 502;
  transition: stroke-dashoffset 1s ease-in-out;
}

.thread-connected-badge {
  display: inline-block;
  background: #E11D48;
  color: #FFFFFF;
  font-weight: 800;
  padding: 4px 16px;
  border-radius: 999px;
  font-size: 0.85rem;
  margin-bottom: 12px;
}

.rakhi-quote {
  font-size: 1.45rem;
  color: var(--color-rose-dark);
  margin-bottom: 8px;
}

.rakhi-wishing {
  font-size: 1.8rem;
  color: var(--color-pink-deep);
}

/* --- 20. SCENE 19: SHAYARI --- */
.shayari-card {
  padding: 40px 20px;
}

.shayari-mandala-wrap {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: radial-gradient(circle, #F59E0B 0%, #B45309 100%);
  margin: 0 auto 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  box-shadow: 0 0 25px rgba(245, 158, 11, 0.5);
  cursor: pointer;
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.shayari-mandala-wrap:active {
  transform: scale(1.25) rotate(20deg);
}

.shayari-lines-container {
  display: flex;
  flex-direction: column;
  gap: 16px;
  max-width: 560px;
  margin: 0 auto;
}

.shayari-line {
  font-size: clamp(1.2rem, 3.6vw, 1.55rem);
  line-height: 1.55;
  color: #FDE68A;
  opacity: 0;
  transform: translateY(12px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}

.shayari-line.revealed {
  opacity: 1;
  transform: translateY(0);
}

.highlight-shayari {
  color: #F472B6;
  font-size: clamp(1.35rem, 4vw, 1.75rem);
  margin-top: 6px;
}

.easter-egg-toast {
  background: rgba(255, 255, 255, 0.95);
  border: 2px solid #F59E0B;
  color: var(--color-rose-dark);
  font-weight: 700;
  padding: 10px 18px;
  border-radius: 999px;
  margin: 16px auto 0;
  display: inline-block;
  animation: pop-in 0.4s var(--ease-spring);
  box-shadow: 0 8px 25px rgba(245, 158, 11, 0.3);
}

/* --- 21. SCENE 20: SECRET DRAWER --- */
.drawer-cabinet-stage {
  perspective: 1000px;
  margin: 20px auto;
  max-width: 440px;
}

.drawer-box {
  background: #78350F;
  border: 3px solid #B45309;
  border-radius: 16px;
  padding: 24px 20px;
  cursor: pointer;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
  transition: transform 0.6s var(--ease-spring);
}

.drawer-handle {
  font-size: 1.6rem;
  color: #FDE68A;
  letter-spacing: 2px;
}

.drawer-label {
  display: inline-block;
  background: #B91C1C;
  color: #FFFFFF;
  font-size: 0.72rem;
  font-weight: 800;
  padding: 3px 10px;
  border-radius: 4px;
  margin-top: 6px;
}

.drawer-secret-note {
  background: #FFFDF9;
  border: 1.5px solid rgba(225, 29, 72, 0.15);
  border-radius: 16px;
  padding: 24px;
  margin-top: 14px;
  text-align: left;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
  animation: pop-in 0.5s var(--ease-spring);
}

.note-header {
  font-size: 1.4rem;
  font-weight: 700;
  color: #BE123C;
  margin-bottom: 12px;
}

.note-list {
  list-style: none;
  font-size: 1.25rem;
  color: #3B1C28;
  line-height: 1.5;
}

.note-footer {
  font-size: 1.3rem;
  color: #881337;
  margin-top: 12px;
  text-align: right;
}

/* --- 22. SCENE 21: FAKE SYSTEM ERROR --- */
.glitch-terminal-box {
  background: #0D040A;
  border: 2px solid #EF4444;
  border-radius: 24px;
  padding: 36px 20px;
  max-width: 480px;
  margin: 0 auto;
  box-shadow: 0 0 35px rgba(239, 68, 68, 0.3);
}

.glitch-title {
  font-family: monospace;
  font-size: clamp(2rem, 5vw, 2.8rem);
  color: #EF4444;
  letter-spacing: 2px;
  margin-bottom: 10px;
}

.glitch-line {
  font-family: monospace;
  color: #FCA5A5;
  font-size: 0.95rem;
  margin-bottom: 18px;
}

.error-progress-bar {
  width: 100%;
  height: 10px;
  background: rgba(255, 255, 255, 0.15);
  border-radius: 999px;
  overflow: hidden;
  margin: 14px 0;
}

.error-bar-fill {
  width: 0%;
  height: 100%;
  background: #EF4444;
  border-radius: 999px;
  transition: width 1.2s ease-in-out;
}

.diag-text {
  font-family: monospace;
  font-size: 1.1rem;
  color: #34D399;
  margin: 14px 0 6px;
}

.highlight-p {
  color: #FDE68A;
  font-weight: 700;
}

.diag-sub {
  font-size: 0.88rem;
  color: #E2E8F0;
}

/* --- 23. SCENE 22 & 23: EMOTIONAL MESSAGE & 3D LETTER --- */
.emo-preface {
  font-size: 1.15rem;
  color: var(--color-text-muted);
  line-height: 1.4;
}

.emo-interactive-lines {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: 520px;
  margin: 20px auto;
  min-height: 220px;
}

.emo-line {
  font-size: clamp(1.15rem, 3.2vw, 1.45rem);
  color: var(--color-text-main);
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.emo-line.revealed {
  opacity: 1;
  transform: translateY(0);
}

.emo-highlight {
  font-size: clamp(1.7rem, 4.8vw, 2.4rem);
  color: var(--color-pink-deep);
  margin-top: 8px;
}

.emo-tap-hint {
  font-size: 0.85rem;
  color: var(--color-text-light);
  font-style: italic;
}

/* 3D Envelope */
.envelope-stage {
  perspective: 1200px;
  width: 100%;
  max-width: 480px;
  margin: 10px auto 24px;
}

.envelope {
  position: relative;
  width: min(100%, 420px);
  height: 270px;
  background: #FFF1F2;
  border-radius: 12px;
  box-shadow: 0 16px 40px rgba(136, 19, 55, 0.15);
  margin: 0 auto;
  cursor: pointer;
}

.envelope-back {
  position: absolute;
  inset: 0;
  background: #FFE4E6;
  border-radius: 12px;
}

.letter-paper {
  position: absolute;
  top: 10px;
  left: 6%;
  width: 88%;
  min-height: 250px;
  background: #FFFDF9;
  border: 1px solid rgba(225, 29, 72, 0.12);
  border-radius: 8px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  padding: 22px;
  text-align: left;
  z-index: 2;
  transform: translateY(0);
  transition: transform 0.8s var(--ease-spring), min-height 0.8s var(--ease-spring), box-shadow 0.8s ease;
  overflow: visible;
}

.letter-stamp-top {
  position: absolute;
  top: 10px;
  right: 14px;
  font-size: 1.4rem;
}

.letter-salutation {
  font-size: 1.8rem;
  color: var(--color-rose-dark);
  margin-bottom: 8px;
}

.letter-content-body {
  font-size: 1.2rem;
  line-height: 1.45;
  color: #3B1C28;
  margin-bottom: 12px;
}

.letter-content-body p { margin-bottom: 8px; }
.bold-highlight { font-weight: 700; color: var(--color-pink-deep); }
.letter-sign-off { font-size: 1.2rem; color: var(--color-rose-dark); }
.sign-name { font-weight: 700; cursor: pointer; display: inline-block; }

.margin-note {
  position: absolute;
  background: #FEF3C7;
  border: 1px dashed #F59E0B;
  color: #B45309;
  font-size: 0.95rem;
  padding: 2px 8px;
  border-radius: 6px;
  transform: rotate(-4deg);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
}

.m-n-1 { top: 28%; right: -12px; }
.m-n-2 { top: 58%; left: -10px; transform: rotate(3deg); }
.m-n-3 { bottom: 15%; right: -8px; }

.env-flap-left {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 0;
  border-bottom: 270px solid #FECDD3;
  border-right: 210px solid transparent;
  border-bottom-left-radius: 12px;
  z-index: 3;
  pointer-events: none;
}

.env-flap-right {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 0;
  height: 0;
  border-bottom: 270px solid #FDA4AF;
  border-left: 210px solid transparent;
  border-bottom-right-radius: 12px;
  z-index: 3;
  pointer-events: none;
}

.env-flap-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 0;
  border-bottom: 150px solid #F472B6;
  border-left: 210px solid transparent;
  border-right: 210px solid transparent;
  border-bottom-left-radius: 12px;
  border-bottom-right-radius: 12px;
  z-index: 4;
  pointer-events: none;
  opacity: 0.9;
}

.env-flap-top {
  position: absolute;
  top: 0;
  left: 0;
  width: 0;
  height: 0;
  border-top: 150px solid #FB7185;
  border-left: 210px solid transparent;
  border-right: 210px solid transparent;
  border-top-left-radius: 12px;
  border-top-right-radius: 12px;
  transform-origin: top center;
  transform: rotateX(0deg);
  z-index: 5;
  transition: transform 0.6s ease, z-index 0.6s step-end;
}

.env-wax-seal {
  position: absolute;
  top: 125px;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 50px;
  height: 50px;
  background: radial-gradient(circle, #E11D48 0%, #9F1239 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 16px rgba(159, 18, 57, 0.4);
  z-index: 6;
  cursor: pointer;
  transition: transform var(--transition-fast), opacity 0.4s ease;
}

.seal-inner-circle {
  width: 38px;
  height: 38px;
  border: 1px dashed rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-handwriting);
  font-size: 0.95rem;
  font-weight: 700;
  color: #FFFFFF;
}

.envelope.is-open .env-flap-top {
  transform: rotateX(180deg);
  z-index: 1;
  transition: transform 0.6s ease, z-index 0.1s step-start;
}

.envelope.is-open .env-wax-seal {
  opacity: 0;
  pointer-events: none;
}

.envelope.is-open .letter-paper {
  transform: translateY(-140px);
  min-height: 440px;
  z-index: 10;
  box-shadow: 0 25px 60px rgba(136, 19, 55, 0.25);
}

/* --- 24. SCENE 24 & 25: FUTURE MESSAGE & SUSPENSE --- */
.timecapsule-card {
  background: rgba(18, 7, 14, 0.95);
  border: 2px solid #F59E0B;
  border-radius: 24px;
  padding: 32px 24px;
  max-width: 500px;
  margin: 20px auto;
  text-align: left;
  box-shadow: 0 0 30px rgba(245, 158, 11, 0.2);
}

.tc-header {
  font-family: monospace;
  font-size: 0.88rem;
  color: #34D399;
  margin-bottom: 16px;
}

.tc-content {
  font-size: 1.35rem;
  line-height: 1.5;
  color: #FDE68A;
}

.tc-content p { margin-bottom: 12px; }
.tc-bold { font-weight: 700; color: #F472B6; font-size: 1.5rem; }

.minimalist-suspense-box {
  padding: 50px 20px;
}

.suspense-lines-wrap {
  margin-bottom: 30px;
}

.suspense-line {
  color: #FFFFFF;
  line-height: 1.3;
  opacity: 0;
  margin-bottom: 14px;
}

.su-1 {
  font-family: var(--font-heading);
  font-size: clamp(3rem, 8vw, 4.8rem);
  color: #FDE68A;
}

.su-2, .su-3 {
  font-size: clamp(1.4rem, 4vw, 2rem);
  color: #FCE7F3;
}

.su-4 {
  font-size: clamp(2.4rem, 6.5vw, 3.6rem);
  color: #F59E0B;
}

/* --- 25. SCENE 26 & 27: FINALE PHOTO, CELEBRATION & MUSIC --- */
.grand-sister-name {
  font-size: clamp(2rem, 5.5vw, 3rem);
  color: var(--color-pink-deep);
  margin-bottom: 8px;
}

.grand-celebration-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(254, 243, 199, 0.85) 100%);
  border: 2.5px solid rgba(245, 158, 11, 0.5);
  box-shadow: 0 30px 70px rgba(245, 158, 11, 0.25), 0 0 40px rgba(251, 191, 36, 0.3);
  max-width: 700px;
}

.grand-crown-badge {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--color-gold-deep);
  margin-bottom: 14px;
}

.music-player-widget {
  background: rgba(255, 255, 255, 0.92);
  border: 1.5px solid rgba(245, 158, 11, 0.35);
  border-radius: 18px;
  padding: 12px 18px;
  margin: 0 auto 20px;
  max-width: 440px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.05);
}

.music-info-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-bottom: 8px;
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-rose-dark);
}

.music-note-icon {
  font-size: 1.1rem;
  color: var(--color-pink-deep);
  animation: float-ambient 2s infinite alternate;
}

.music-controls-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
}

.player-btn {
  background: var(--color-pink-soft);
  border: 1px solid rgba(225, 29, 72, 0.2);
  color: var(--color-rose-dark);
  width: 34px;
  height: 34px;
  border-radius: 50%;
  cursor: pointer;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all var(--transition-fast);
}

.player-btn:hover {
  background: var(--color-pink-deep);
  color: #FFFFFF;
  transform: scale(1.1);
}

.volume-slider {
  width: 110px;
  accent-color: var(--color-pink-deep);
  cursor: pointer;
}

.grand-festive-title {
  font-size: clamp(2.4rem, 6vw, 3.8rem);
  color: var(--color-rose-dark);
  line-height: 1.15;
  margin-bottom: 8px;
}

.grand-milestone-tag {
  font-size: clamp(1.05rem, 3vw, 1.35rem);
  font-weight: 700;
  color: var(--color-gold-deep);
  margin-bottom: 8px;
}

.grand-emotional-message {
  font-size: 1.05rem;
  color: var(--color-text-muted);
  font-style: italic;
  margin-bottom: 8px;
}

.grand-love-note {
  font-size: clamp(1.8rem, 5vw, 2.6rem);
  color: var(--color-pink-deep);
  margin-bottom: 6px;
}

.grand-sign-text {
  font-size: 1.1rem;
  color: var(--color-text-muted);
  margin-bottom: 22px;
}

.grand-actions-bar {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-bottom: 18px;
}

.blessing-toast-box {
  background: rgba(255, 255, 255, 0.95);
  border: 1.5px solid rgba(245, 158, 11, 0.4);
  border-radius: 16px;
  padding: 12px 18px;
  max-width: 460px;
  margin: 0 auto 14px;
  animation: pop-in 0.4s var(--ease-spring);
}

.toast-diya-flame { font-size: 1.8rem; }
.toast-text {
  font-size: 1.35rem;
  font-weight: 700;
  color: var(--color-rose-dark);
}

.replay-wrap { margin-top: 14px; }
.replay-link-btn {
  background: none;
  border: none;
  color: var(--color-text-light);
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  text-decoration: underline;
  transition: color var(--transition-fast);
}

.replay-link-btn:hover { color: var(--color-rose-dark); }

/* Transparent Privacy Notice */
.privacy-notice-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 6px 16px;
  background: rgba(255, 253, 249, 0.75);
  backdrop-filter: blur(8px);
  text-align: center;
  font-size: 0.76rem;
  color: var(--color-text-light);
  z-index: 70;
  border-top: 1px solid rgba(225, 29, 72, 0.1);
  pointer-events: none;
}

/* --- 26. Keyframe Animations --- */
@keyframes pop-in {
  from { opacity: 0; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1); }
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  20%, 60% { transform: translateX(-8px); }
  40%, 80% { transform: translateX(8px); }
}

@keyframes shine-sweep {
  0% { left: -100%; }
  25%, 100% { left: 140%; }
}

@keyframes pulse-glow {
  0%, 100% { transform: scale(1); filter: drop-shadow(0 0 20px rgba(245, 158, 11, 0.6)); }
  50% { transform: scale(1.08); filter: drop-shadow(0 0 35px rgba(245, 158, 11, 0.9)); }
}

@keyframes float-ambient {
  from { transform: translateY(0) rotate(0deg); }
  to { transform: translateY(-8px) rotate(3deg); }
}

@keyframes spin-slow {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* --- 27. Responsive & Accessibility --- */
@media (max-width: 640px) {
  .top-story-bar {
    padding: 0 12px;
    height: 56px;
  }

  .story-viewport {
    padding-top: 62px;
    padding-bottom: 40px;
  }

  .glass-card {
    border-radius: 22px;
    padding: 22px 14px;
  }

  .photo-contain-wrapper {
    height: 48vh;
  }

  .envelope {
    height: 220px;
  }

  .envelope.is-open .letter-paper {
    transform: translateY(-90px);
    min-height: 380px;
    padding: 16px;
  }

  .letter-content-body {
    font-size: 1.05rem;
  }

  .slot-reel {
    min-width: 90px;
    font-size: 0.9rem;
    padding: 12px 6px;
  }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
"""
    for path in [os.path.join(FRONTEND_DIR, "style.css"), os.path.join(BASE_DIR, "style.css")]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    print("✓ Generated style.css in frontend/ and root")

def generate_script_js():
    content = r"""/**
 * RAKHI SURPRISE STORY • 27-SCENE INTERACTIVE ENGINE
 * Dedicated to Prerna Gupta (Peda, Age 23) • Built with love by Prakhar
 */

(function () {

  'use strict';

  const TOTAL_SCREENS = 27;
  let currentScreen = 1;
  let isTransitioning = false;

  // Check prefers-reduced-motion
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ==========================================================================
  // 1. SESSION MANAGEMENT & ANSWER TRACKER (FastAPI Backend + Offline Queue)
  // ==========================================================================
  const AnswerTracker = (function () {
    const API_BASE = window.location.origin.includes('localhost') || window.location.origin.includes('127.0.0.1')
      ? 'http://127.0.0.1:8000'
      : ''; // In production, same domain or configured URL

    let sessionId = sessionStorage.getItem('rakhi_session_id');
    if (!sessionId) {
      sessionId = (typeof crypto !== 'undefined' && crypto.randomUUID)
        ? crypto.randomUUID()
        : 'sess-' + Date.now() + '-' + Math.random().toString(36).substring(2, 9);
      sessionStorage.setItem('rakhi_session_id', sessionId);
    }

    function getOfflineQueue() {
      try {
        const item = localStorage.getItem('rakhi_offline_answers');
        return item ? JSON.parse(item) : [];
      } catch (e) {
        return [];
      }
    }

    function saveOfflineQueue(queue) {
      try {
        localStorage.setItem('rakhi_offline_answers', JSON.stringify(queue));
      } catch (e) {}
    }

    async function sendPayload(endpoint, data) {
      if (!API_BASE && !window.location.origin.startsWith('http')) return false;
      try {
        const res = await fetch(`${API_BASE}${endpoint}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data),
          mode: 'cors'
        });
        return res.ok;
      } catch (e) {
        return false;
      }
    }

    async function recordAnswer(questionId, questionText, answerText) {
      const payload = {
        session_id: sessionId,
        question_id: String(questionId),
        question_text: String(questionText),
        answer: String(answerText),
        timestamp: new Date().toISOString()
      };

      const success = await sendPayload('/api/answer', payload);
      if (!success) {
        // Save to offline retry queue
        const queue = getOfflineQueue();
        // Prevent local duplicate
        const exists = queue.some(item => item.question_id === payload.question_id);
        if (!exists) {
          queue.push(payload);
          saveOfflineQueue(queue);
        }
      }
    }

    async function recordCompletion() {
      const payload = {
        session_id: sessionId,
        completed_at: new Date().toISOString()
      };
      const success = await sendPayload('/api/complete', payload);
      if (!success) {
        const queue = getOfflineQueue();
        queue.push({ ...payload, is_completion: true });
        saveOfflineQueue(queue);
      }
    }

    async function retryOfflineAnswers() {
      const queue = getOfflineQueue();
      if (queue.length === 0) return;

      const remaining = [];
      for (const item of queue) {
        if (item.is_completion) {
          const ok = await sendPayload('/api/complete', item);
          if (!ok) remaining.push(item);
        } else {
          const ok = await sendPayload('/api/answer', item);
          if (!ok) remaining.push(item);
        }
      }
      saveOfflineQueue(remaining);
    }

    // Attach online event and periodic retry
    window.addEventListener('online', retryOfflineAnswers);
    setInterval(retryOfflineAnswers, 20000);

    return { getSessionId: () => sessionId, recordAnswer, recordCompletion, retryOfflineAnswers };
  })();

  // ==========================================================================
  // 2. SOUND SYNTHESIZER (Web Audio API - Zero External Audio Dependencies)
  // ==========================================================================
  const SoundEngine = (function () {
    let audioCtx = null;
    let isSoundEnabled = true;

    function getContext() {
      if (!audioCtx) {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (AudioContext) audioCtx = new AudioContext();
      }
      if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
      return audioCtx;
    }

    function toggleSound() {
      isSoundEnabled = !isSoundEnabled;
      const toggleBtn = document.getElementById('sound-toggle');
      if (toggleBtn) {
        const icon = toggleBtn.querySelector('.sound-icon');
        const label = toggleBtn.querySelector('.sound-label');
        if (icon) icon.textContent = isSoundEnabled ? '🔊' : '🔇';
        if (label) label.textContent = isSoundEnabled ? 'Sound' : 'Muted';
      }
      if (isSoundEnabled) playPop();
      return isSoundEnabled;
    }

    function playPop() {
      if (!isSoundEnabled) return;
      try {
        const ctx = getContext();
        if (!ctx) return;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(820, ctx.currentTime + 0.07);
        gain.gain.setValueAtTime(0.2, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.07);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.07);
      } catch (e) {}
    }

    function playChime() {
      if (!isSoundEnabled) return;
      try {
        const ctx = getContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
        notes.forEach((freq, i) => {
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, now + i * 0.07);
          gain.gain.setValueAtTime(0, now + i * 0.07);
          gain.gain.linearRampToValueAtTime(0.18, now + i * 0.07 + 0.02);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.07 + 0.45);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + i * 0.07);
          osc.stop(now + i * 0.07 + 0.45);
        });
      } catch (e) {}
    }

    function playFanfare() {
      if (!isSoundEnabled) return;
      try {
        const ctx = getContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const chords = [
          { f: 523.25, t: 0 },
          { f: 659.25, t: 0.1 },
          { f: 783.99, t: 0.2 },
          { f: 1046.50, t: 0.35 },
          { f: 1318.51, t: 0.5 }
        ];
        chords.forEach((note) => {
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(note.f, now + note.t);
          gain.gain.setValueAtTime(0.2, now + note.t);
          gain.gain.exponentialRampToValueAtTime(0.001, now + note.t + 0.8);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + note.t);
          osc.stop(now + note.t + 0.8);
        });
      } catch (e) {}
    }

    function playShutter() {
      if (!isSoundEnabled) return;
      try {
        const ctx = getContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'square';
        osc.frequency.setValueAtTime(120, now);
        osc.frequency.exponentialRampToValueAtTime(40, now + 0.08);
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.08);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.08);
      } catch (e) {}
    }

    return { toggleSound, playPop, playChime, playFanfare, playShutter, getContext };
  })();

  // ==========================================================================
  // 3. PARTICLE, FIREWORKS, CONFETTI & HEARTS CANVAS ENGINE
  // ==========================================================================
  const ParticleEngine = (function () {
    const bgCanvas = document.getElementById('bg-canvas');
    const fireworksCanvas = document.getElementById('fireworks-canvas');
    const confettiCanvas = document.getElementById('confetti-canvas');
    const heartsCanvas = document.getElementById('hearts-canvas');
    const cursorCanvas = document.getElementById('sparkle-cursor-canvas');

    let bgCtx, fireworksCtx, confettiCtx, heartsCtx, cursorCtx;
    let bgParticles = [];
    let fireworksRockets = [];
    let fireworksSparks = [];
    let confettiPieces = [];
    let floatingHearts = [];
    let cursorSparkles = [];
    let width = window.innerWidth;
    let height = window.innerHeight;
    let isFireworksActive = false;

    function resize() {
      width = window.innerWidth;
      height = window.innerHeight;
      if (bgCanvas) { bgCanvas.width = width; bgCanvas.height = height; }
      if (fireworksCanvas) { fireworksCanvas.width = width; fireworksCanvas.height = height; }
      if (confettiCanvas) { confettiCanvas.width = width; confettiCanvas.height = height; }
      if (heartsCanvas) { heartsCanvas.width = width; heartsCanvas.height = height; }
      if (cursorCanvas) { cursorCanvas.width = width; cursorCanvas.height = height; }
    }

    function init() {
      if (bgCanvas) bgCtx = bgCanvas.getContext('2d');
      if (fireworksCanvas) fireworksCtx = fireworksCanvas.getContext('2d');
      if (confettiCanvas) confettiCtx = confettiCanvas.getContext('2d');
      if (heartsCanvas) heartsCtx = heartsCanvas.getContext('2d');
      if (cursorCanvas) cursorCtx = cursorCanvas.getContext('2d');

      resize();
      window.addEventListener('resize', resize);

      if (!prefersReducedMotion) {
        // Celestial background particles
        bgParticles = [];
        for (let i = 0; i < 35; i++) {
          bgParticles.push({
            x: Math.random() * width,
            y: Math.random() * height,
            radius: Math.random() * 3 + 1,
            speedY: Math.random() * 0.35 + 0.15,
            opacity: Math.random() * 0.45 + 0.2,
            color: Math.random() > 0.5 ? '#FBBF24' : (Math.random() > 0.5 ? '#F472B6' : '#EDE9FE'),
            angle: Math.random() * Math.PI * 2,
            spin: (Math.random() - 0.5) * 0.02
          });
        }

        // Sparkle cursor
        window.addEventListener('mousemove', (e) => {
          if (Math.random() > 0.6) return;
          cursorSparkles.push({
            x: e.clientX,
            y: e.clientY,
            vx: (Math.random() - 0.5) * 1.5,
            vy: (Math.random() - 0.5) * 1.5 - 0.4,
            life: 1,
            size: Math.random() * 3 + 1.5,
            color: Math.random() > 0.5 ? '#F59E0B' : '#EC4899'
          });
        }, { passive: true });
      }

      requestAnimationFrame(loop);
    }

    function fireConfetti(originX, originY, count = 75, colors = ['#E11D48', '#F59E0B', '#EC4899', '#8B5CF6', '#10B981', '#FDE68A']) {
      if (prefersReducedMotion) return;
      for (let i = 0; i < count; i++) {
        const angle = Math.random() * Math.PI * 2;
        const velocity = Math.random() * 12 + 6;
        confettiPieces.push({
          x: originX,
          y: originY,
          vx: Math.cos(angle) * velocity,
          vy: Math.sin(angle) * velocity - 3,
          gravity: 0.26,
          drag: 0.94,
          size: Math.random() * 8 + 5,
          color: colors[Math.floor(Math.random() * colors.length)],
          rotation: Math.random() * Math.PI * 2,
          rotationSpeed: (Math.random() - 0.5) * 0.2,
          life: 1,
          decay: Math.random() * 0.012 + 0.008
        });
      }
    }

    function spawnFloatingHeart(x, y) {
      floatingHearts.push({
        x: x || width / 2,
        y: y || height * 0.75,
        vx: (Math.random() - 0.5) * 2,
        vy: -(Math.random() * 2.5 + 2),
        size: Math.random() * 16 + 18,
        opacity: 1,
        color: Math.random() > 0.5 ? '#E11D48' : '#DB2777'
      });
    }

    function createFirework(targetX, targetY) {
      if (prefersReducedMotion) return;
      const startX = width * (0.2 + Math.random() * 0.6);
      const startY = height;
      fireworksRockets.push({
        x: startX,
        y: startY,
        targetX: targetX || width * (0.15 + Math.random() * 0.7),
        targetY: targetY || height * (0.15 + Math.random() * 0.4),
        speed: 12,
        color: Math.random() > 0.5 ? '#F59E0B' : (Math.random() > 0.5 ? '#F472B6' : '#FFFFFF')
      });
    }

    function explodeFirework(x, y, color) {
      const count = 55;
      for (let i = 0; i < count; i++) {
        const angle = (Math.PI * 2 / count) * i + (Math.random() - 0.5) * 0.2;
        const speed = Math.random() * 5 + 2;
        fireworksSparks.push({
          x,
          y,
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed,
          color: color || '#F59E0B',
          alpha: 1,
          decay: Math.random() * 0.015 + 0.01
        });
      }
    }

    function startFireworks() {
      isFireworksActive = true;
      let count = 0;
      const interval = setInterval(() => {
        if (!isFireworksActive || count > 20) {
          clearInterval(interval);
          return;
        }
        createFirework();
        count++;
      }, 700);
    }

    function loop() {
      // 1. Ambient Background Particles
      if (bgCtx && !prefersReducedMotion) {
        bgCtx.clearRect(0, 0, width, height);
        bgParticles.forEach((p) => {
          p.y += p.speedY;
          p.x += Math.sin(p.angle) * 0.4;
          p.angle += p.spin;
          if (p.y > height + 10) {
            p.y = -10;
            p.x = Math.random() * width;
          }

          bgCtx.save();
          bgCtx.globalAlpha = p.opacity;
          bgCtx.fillStyle = p.color;
          bgCtx.beginPath();
          bgCtx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          bgCtx.fill();
          bgCtx.restore();
        });
      }

      // 2. Cursor Sparkles
      if (cursorCtx && !prefersReducedMotion) {
        cursorCtx.clearRect(0, 0, width, height);
        for (let i = cursorSparkles.length - 1; i >= 0; i--) {
          const sp = cursorSparkles[i];
          sp.x += sp.vx;
          sp.y += sp.vy;
          sp.life -= 0.035;

          if (sp.life <= 0) {
            cursorSparkles.splice(i, 1);
            continue;
          }

          cursorCtx.save();
          cursorCtx.globalAlpha = sp.life;
          cursorCtx.fillStyle = sp.color;
          cursorCtx.beginPath();
          cursorCtx.arc(sp.x, sp.y, sp.size * sp.life, 0, Math.PI * 2);
          cursorCtx.fill();
          cursorCtx.restore();
        }
      }

      // 3. Floating Hearts
      if (heartsCtx) {
        heartsCtx.clearRect(0, 0, width, height);
        for (let i = floatingHearts.length - 1; i >= 0; i--) {
          const h = floatingHearts[i];
          h.x += h.vx;
          h.y += h.vy;
          h.opacity -= 0.012;

          if (h.opacity <= 0 || h.y < -30) {
            floatingHearts.splice(i, 1);
            continue;
          }

          heartsCtx.save();
          heartsCtx.globalAlpha = h.opacity;
          heartsCtx.fillStyle = h.color;
          heartsCtx.font = `${h.size}px serif`;
          heartsCtx.fillText('❤️', h.x, h.y);
          heartsCtx.restore();
        }
      }

      // 4. Fireworks Rockets & Sparks
      if (fireworksCtx && !prefersReducedMotion) {
        fireworksCtx.clearRect(0, 0, width, height);

        // Rockets
        for (let i = fireworksRockets.length - 1; i >= 0; i--) {
          const r = fireworksRockets[i];
          const dx = r.targetX - r.x;
          const dy = r.targetY - r.y;
          const dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < 15) {
            explodeFirework(r.x, r.y, r.color);
            fireworksRockets.splice(i, 1);
            continue;
          }

          r.x += (dx / dist) * r.speed;
          r.y += (dy / dist) * r.speed;

          fireworksCtx.save();
          fireworksCtx.fillStyle = r.color;
          fireworksCtx.beginPath();
          fireworksCtx.arc(r.x, r.y, 3, 0, Math.PI * 2);
          fireworksCtx.fill();
          fireworksCtx.restore();
        }

        // Sparks
        for (let i = fireworksSparks.length - 1; i >= 0; i--) {
          const s = fireworksSparks[i];
          s.x += s.vx;
          s.y += s.vy;
          s.vy += 0.06; // gravity
          s.alpha -= s.decay;

          if (s.alpha <= 0) {
            fireworksSparks.splice(i, 1);
            continue;
          }

          fireworksCtx.save();
          fireworksCtx.globalAlpha = s.alpha;
          fireworksCtx.fillStyle = s.color;
          fireworksCtx.beginPath();
          fireworksCtx.arc(s.x, s.y, 2.2, 0, Math.PI * 2);
          fireworksCtx.fill();
          fireworksCtx.restore();
        }
      }

      // 5. Physics Confetti
      if (confettiCtx && !prefersReducedMotion) {
        confettiCtx.clearRect(0, 0, width, height);
        for (let i = confettiPieces.length - 1; i >= 0; i--) {
          const c = confettiPieces[i];
          c.vx *= c.drag;
          c.vy = c.vy * c.drag + c.gravity;
          c.x += c.vx;
          c.y += c.vy;
          c.rotation += c.rotationSpeed;
          c.life -= c.decay;

          if (c.life <= 0 || c.y > height + 20) {
            confettiPieces.splice(i, 1);
            continue;
          }

          confettiCtx.save();
          confettiCtx.globalAlpha = Math.min(1, c.life * 1.5);
          confettiCtx.translate(c.x, c.y);
          confettiCtx.rotate(c.rotation);
          confettiCtx.fillStyle = c.color;
          confettiCtx.fillRect(-c.size / 2, -c.size / 2, c.size, c.size * 0.6);
          confettiCtx.restore();
        }
      }

      requestAnimationFrame(loop);
    }

    return { init, fireConfetti, spawnFloatingHeart, startFireworks };
  })();

  // ==========================================================================
  // 4. MUSIC PLAYER CONTROLLER (assets/song.mp3 with Graceful Fallback)
  // ==========================================================================
  const MusicPlayer = (function () {
    const audioEl = document.getElementById('rakhi-audio-element');
    const playPauseBtn = document.getElementById('btn-audio-play-pause');
    const volumeSlider = document.getElementById('audio-volume-slider');
    const muteBtn = document.getElementById('btn-audio-mute');
    const statusText = document.getElementById('music-status-text');

    let isPlaying = false;

    function play() {
      if (!audioEl) return;
      audioEl.play().then(() => {
        isPlaying = true;
        if (playPauseBtn) playPauseBtn.textContent = '❚❚';
        if (statusText) statusText.textContent = 'Playing: Ek Hazaaron Mein Meri Behna Hai ♫';
      }).catch(() => {
        if (statusText) statusText.textContent = 'Happy Raksha Bandhan, Bhena! ❤️';
        SoundEngine.playFanfare();
      });
    }

    function pause() {
      if (!audioEl) return;
      audioEl.pause();
      isPlaying = false;
      if (playPauseBtn) playPauseBtn.textContent = '▶';
      if (statusText) statusText.textContent = 'Paused';
    }

    function togglePlay() {
      if (isPlaying) pause();
      else play();
    }

    function init() {
      if (playPauseBtn) playPauseBtn.addEventListener('click', togglePlay);

      if (volumeSlider && audioEl) {
        volumeSlider.addEventListener('input', (e) => {
          audioEl.volume = parseFloat(e.target.value);
        });
      }

      if (muteBtn && audioEl) {
        muteBtn.addEventListener('click', () => {
          audioEl.muted = !audioEl.muted;
          muteBtn.textContent = audioEl.muted ? '🔇' : '🔊';
        });
      }

      if (audioEl) {
        audioEl.addEventListener('ended', () => {
          isPlaying = false;
          if (playPauseBtn) playPauseBtn.textContent = '▶';
        });
      }
    }

    return { init, play, pause };
  })();

  // ==========================================================================
  // 5. STORY ROUTER (27-Scene Sequential Navigation Engine)
  // ==========================================================================
  const StoryRouter = (function () {
    const dotsRow = document.getElementById('progress-dots-row');
    const barFill = document.getElementById('progress-bar-fill');

    function buildProgressDots() {
      if (!dotsRow) return;
      dotsRow.innerHTML = '';
      for (let i = 1; i <= TOTAL_SCREENS; i++) {
        const dot = document.createElement('span');
        dot.className = `prog-dot ${i === 1 ? 'active' : ''}`;
        dot.id = `prog-dot-${i}`;
        dot.setAttribute('data-index', i);
        dotsRow.appendChild(dot);
      }
    }

    function updateProgress(targetIndex) {
      if (barFill) {
        const percent = ((targetIndex - 1) / (TOTAL_SCREENS - 1)) * 100;
        barFill.style.width = `${Math.max(3.7, percent)}%`;
      }

      for (let i = 1; i <= TOTAL_SCREENS; i++) {
        const dot = document.getElementById(`prog-dot-${i}`);
        if (dot) {
          dot.className = 'prog-dot';
          if (i < targetIndex) dot.classList.add('completed');
          if (i === targetIndex) dot.classList.add('active');
        }
      }
    }

    function goToScreen(targetIndex, direction = 'next') {
      if (targetIndex < 1 || targetIndex > TOTAL_SCREENS || isTransitioning) return;
      if (targetIndex === currentScreen) return;

      isTransitioning = true;
      SoundEngine.playPop();

      const currentEl = document.getElementById(`scene-${currentScreen}`);
      const targetEl = document.getElementById(`scene-${targetIndex}`);

      if (currentEl) {
        currentEl.style.transition = 'opacity 0.32s ease, transform 0.32s ease';
        currentEl.style.opacity = '0';
        currentEl.style.transform = direction === 'next' ? 'translateX(-30px) scale(0.97)' : 'translateX(30px) scale(0.97)';
      }

      setTimeout(() => {
        if (currentEl) {
          currentEl.classList.remove('active', 'slide-in-right', 'slide-in-left');
          currentEl.style.display = 'none';
        }

        if (targetEl) {
          targetEl.style.display = 'flex';
          targetEl.classList.remove('slide-in-right', 'slide-in-left');
          targetEl.classList.add('active');
          if (direction === 'next') {
            targetEl.classList.add('slide-in-right');
          } else {
            targetEl.classList.add('slide-in-left');
          }
          targetEl.style.opacity = '';
          targetEl.style.transform = '';
        }

        currentScreen = targetIndex;
        updateProgress(targetIndex);
        window.location.hash = `scene-${targetIndex}`;
        window.scrollTo({ top: 0, behavior: 'instant' });

        // Trigger scene activations
        handleSceneActivation(targetIndex);

        setTimeout(() => {
          isTransitioning = false;
        }, 350);
      }, 320);
    }

    function handleSceneActivation(index) {
      if (index === 1) {
        startScene1Sequence();
      } else if (index === 2) {
        setTimeout(() => {
          const input = document.getElementById('input-user-name');
          if (input) input.focus();
        }, 300);
      } else if (index === 13) {
        startSiblingCupScoreboard();
      } else if (index === 19) {
        startShayariSequence();
      } else if (index === 21) {
        startSystemErrorSequence();
      } else if (index === 22) {
        startEmotionalSequence();
      } else if (index === 25) {
        startSuspenseSequence();
      } else if (index === 27) {
        triggerGrandCelebration();
        AnswerTracker.recordCompletion();
      }
    }

    function init() {
      buildProgressDots();

      const hash = window.location.hash;
      if (hash && hash.startsWith('#scene-')) {
        const target = parseInt(hash.replace('#scene-', ''), 10);
        if (!isNaN(target) && target >= 1 && target <= TOTAL_SCREENS) {
          document.querySelectorAll('.story-screen').forEach((s) => {
            s.classList.remove('active');
            s.style.display = 'none';
          });
          const initial = document.getElementById(`scene-${target}`);
          if (initial) {
            initial.style.display = 'flex';
            initial.classList.add('active');
            currentScreen = target;
            updateProgress(target);
            handleSceneActivation(target);
          }
        }
      } else {
        startScene1Sequence();
      }

      window.addEventListener('popstate', () => {
        const h = window.location.hash;
        if (h && h.startsWith('#scene-')) {
          const target = parseInt(h.replace('#scene-', ''), 10);
          if (!isNaN(target) && target >= 1 && target <= TOTAL_SCREENS && target !== currentScreen) {
            goToScreen(target, target > currentScreen ? 'next' : 'prev');
          }
        }
      });
    }

    return { init, goToScreen, getCurrentScreen: () => currentScreen };
  })();

  // ==========================================================================
  // 6. SCENE CONTROLLERS & INTERACTION MODULES
  // ==========================================================================

  // --- Scene 1: Opening Mystery Envelope ---
  function startScene1Sequence() {
    const l1 = document.getElementById('s1-line-1');
    const l2 = document.getElementById('s1-line-2');
    const l3 = document.getElementById('s1-line-3');
    const act = document.getElementById('s1-action-wrap');
    const revealMsg = document.getElementById('s1-reveal-msg');

    if (l1) l1.style.opacity = '0';
    if (l2) l2.style.opacity = '0';
    if (l3) l3.style.opacity = '0';
    if (act) act.style.opacity = '0';

    setTimeout(() => { if (l1) { l1.style.transition = 'opacity 0.8s ease'; l1.style.opacity = '1'; } }, 300);
    setTimeout(() => { if (l2) { l2.style.transition = 'opacity 0.8s ease'; l2.style.opacity = '1'; } }, 1700);
    setTimeout(() => { if (l3) { l3.style.transition = 'opacity 0.8s ease'; l3.style.opacity = '1'; } }, 3100);
    setTimeout(() => {
      if (act) {
        act.style.transition = 'opacity 0.8s ease';
        act.style.opacity = '1';
      }
    }, 4200);

    const btnEnter = document.getElementById('btn-scene-1-enter');
    if (btnEnter) {
      btnEnter.onclick = () => {
        SoundEngine.playChime();
        ParticleEngine.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 40);
        if (revealMsg) revealMsg.style.display = 'block';
        if (act) act.style.display = 'none';

        setTimeout(() => {
          StoryRouter.goToScreen(2, 'next');
        }, 1200);
      };
    }
  }

  // --- Scene 2: Sibling Security System Scanner ---
  function setupScene2() {
    const form = document.getElementById('form-identity-check');
    const nameInput = document.getElementById('input-user-name');
    const ageStep = document.getElementById('age-check-step');
    const ageInput = document.getElementById('input-user-age-sec');
    const feedback = document.getElementById('identity-validation-msg');
    const terminal = document.getElementById('scanning-terminal');
    const barFill = document.getElementById('scan-bar-fill');
    const idBadge = document.getElementById('identity-card-badge');
    const btnWrap = document.getElementById('identity-btn-wrap');
    const btnLabel = document.getElementById('btn-identity-label');

    let isNameConfirmed = false;

    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();

        if (!isNameConfirmed) {
          const val = nameInput.value.trim().toLowerCase();
          if (val === 'prerna' || val === 'prerna gupta') {
            feedback.textContent = '';
            isNameConfirmed = true;
            SoundEngine.playPop();
            AnswerTracker.recordAnswer('sec_name', 'Identity Name', nameInput.value.trim());

            if (ageStep) {
              ageStep.style.display = 'block';
              if (ageInput) ageInput.focus();
            }
            if (btnLabel) btnLabel.textContent = 'Confirm Credentials';
          } else if (val.length === 0) {
            feedback.className = 'validation-feedback error';
            feedback.textContent = 'Naam toh likh pehle, Gadhi!';
          } else {
            feedback.className = 'validation-feedback error';
            feedback.textContent = "Nice try, hacker. Asli Gadhi (Prerna) ko bulao. 🤨";
            nameInput.classList.add('error');
            setTimeout(() => nameInput.classList.remove('error'), 500);
          }
        } else {
          // Verify Age
          const ageVal = ageInput.value.trim();
          if (ageVal === '23') {
            feedback.textContent = '';
            if (btnWrap) btnWrap.style.display = 'none';
            if (terminal) terminal.style.display = 'block';
            SoundEngine.playPop();
            AnswerTracker.recordAnswer('sec_age', 'Identity Age', ageVal);

            setTimeout(() => { if (barFill) barFill.style.width = '100%'; }, 100);

            setTimeout(() => {
              if (terminal) terminal.style.display = 'none';
              if (idBadge) idBadge.style.display = 'block';
              SoundEngine.playChime();
              ParticleEngine.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.4, 30);

              setTimeout(() => {
                StoryRouter.goToScreen(3, 'next');
              }, 1800);
            }, 1400);
          } else if (ageVal.length === 0) {
            feedback.className = 'validation-feedback error';
            feedback.textContent = 'Age batao, Peda!';
          } else {
            feedback.className = 'validation-feedback error';
            feedback.textContent = 'Suspicious age detected. Sachi age batao! 🧐';
          }
        }
      });
    }
  }

  // --- Scene 3: Funny Age Scene ("23?!") ---
  function setupScene3() {
    const buttons = document.querySelectorAll('#age-choices-row .btn-choice-pill');
    const reactionBox = document.getElementById('age-reaction-box');
    const reactionText = document.getElementById('age-reaction-text');
    const btnNext = document.getElementById('btn-age-continue-next');

    buttons.forEach((btn) => {
      btn.addEventListener('click', function () {
        SoundEngine.playPop();
        const ans = this.getAttribute('data-ans');
        let reply = '';

        if (ans === 'yes') reply = "Jhooth bolne ki bhi limit hoti hai, Madam Ji. 🤥💅";
        else if (ans === 'no') reply = "At least honesty toh hai. Respect, Gadhi. 🤝";
        else reply = "Progress report: 23 years and still disappointing. 📉😂";

        AnswerTracker.recordAnswer('age_behavior', 'Behave karna seekha?', ans);

        if (reactionBox && reactionText) {
          reactionText.textContent = reply;
          reactionBox.style.display = 'block';
        }
      });
    });

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        StoryRouter.goToScreen(4, 'next');
      });
    }
  }

  // --- Scene 4: Sibling Intelligence Test (10 Questions) ---
  const intelligenceQuestions = [
    {
      q: "1. Who is the better sibling?",
      opts: ["Prerna", "Prakhar", "Obviously Prerna", "Question hi biased hai"],
      reactions: [
        "Correct. Itna bhi Gadhi nahi hai tu. 💅",
        "Wrong. Confidence 100%. Accuracy questionable. 😇",
        "Scientists are still studying this extreme ego. 👑",
        "Family court has been officially notified. ⚖️😂"
      ]
    },
    {
      q: "2. Who starts arguments over absolutely nothing?",
      opts: ["Prerna", "Prakhar", "Both", "Mom"],
      reactions: [
        "Self-awareness level: legendary! 😂",
        "Nice deflection, Madam Ji. 🤥",
        "A daily household sporting event. 🥊",
        "Don't bring Mom into this or we are both grounded. 🤫"
      ]
    },
    {
      q: "3. Who steals food from the other's plate?",
      opts: ["Prerna (Food Chor)", "Prakhar", "Both", "It's called 'Sibling Tax'"],
      reactions: [
        "Food chor spotted in 4K resolution! 🍟",
        "I only take what is legally my brotherly dividend.",
        "A battle fought at every single meal. 🍕",
        "The universal sister tax law applied! 📜"
      ]
    },
    {
      q: "4. Who is more dramatic?",
      opts: ["Prerna (Drama Queen)", "Prakhar", "Both", "Academy Award winner Peda"],
      reactions: [
        "Oscar nomination pending for daily sibling drama. 🎭",
        "I am pure calm and innocence. 😇",
        "Our living room is basically Bollywood. 🎬",
        "Standing ovation for Maharani Peda Devi! 🏆"
      ]
    },
    {
      q: "5. Who says 'I'm not hungry' and then eats everyone's food?",
      opts: ["Peda", "Gadhi", "Maharani Peda Devi", "All of the above"],
      reactions: [
        "The classic sister extortion move! 🍔",
        "Guilty as charged! 🍟",
        "Royalty demands royal food taxes. 👑",
        "100% accuracy achieved on this question! 🎯"
      ]
    },
    {
      q: "6. Who is more stubborn?",
      opts: ["Prerna", "Prakhar", "Both", "The Wall of China"],
      reactions: [
        "More stubborn than a stubborn mule! 🐴",
        "I call it 'firm leadership'. 🧐",
        "Unstoppable force meets immovable headache. 🧱",
        "Wall of China has got nothing on Peda. 🏛️"
      ]
    },
    {
      q: "7. Who apologizes first after a fight?",
      opts: ["Prerna", "Prakhar", "The one who needs Wi-Fi", "Nobody, we send memes"],
      reactions: [
        "A miracle recorded in sibling history! ✨",
        "Always the mature brother. 😇",
        "Wi-Fi is the ultimate peace treaty! 📶",
        "Sending memes is our official peace diplomacy. 🤝"
      ]
    },
    {
      q: "8. Who is secretly more emotional?",
      opts: ["Prerna", "Prakhar", "Both", "Secret"],
      reactions: [
        "Behind the drama, a pure heart of gold. ❤️",
        "I pretend to be tough, but facts are facts. 🥺",
        "Both of us are softies deep down. 🌸",
        "Some brother-sister secrets remain classified. 🔒"
      ]
    },
    {
      q: "9. Who is Mom's favorite?",
      opts: ["Prerna", "Prakhar", "The dog", "Whoever isn't shouting right now"],
      reactions: [
        "In your dreams, Madam Ji! 😴",
        "Obviously the favorite son. 👑",
        "The dog wins every single time. 🐶",
        "Facts! Peace in the house is Mom's only true favorite. 😂"
      ]
    },
    {
      q: "10. Who would survive longer without talking to the other?",
      opts: ["Prerna", "Prakhar", "0 hours (Impossible)", "Sibling bond too strong"],
      reactions: [
        "Spoiler: You would call in 15 minutes for gossip. 📱",
        "I enjoy the peace... for about 10 minutes. 😂",
        "Neither of us can last a single day without bakbak. 🗣️",
        "Correct! Sibling bond too strong forever. ❤️"
      ]
    }
  ];
  let quizCurrentIndex = 0;

  function renderQuizQuestion(idx) {
    const q = intelligenceQuestions[idx];
    const titleEl = document.getElementById('quiz-question-title');
    const badgeEl = document.getElementById('quiz-step-badge');
    const listEl = document.getElementById('quiz-options-list');
    const feedbackBox = document.getElementById('quiz-feedback-box');
    const btnLabel = document.getElementById('quiz-btn-label');

    if (titleEl) titleEl.textContent = q.q;
    if (badgeEl) badgeEl.textContent = `Question ${idx + 1} of ${intelligenceQuestions.length}`;
    if (feedbackBox) feedbackBox.style.display = 'none';
    if (btnLabel) btnLabel.textContent = idx === intelligenceQuestions.length - 1 ? 'Finish Sibling Test' : 'Next Question';

    if (listEl) {
      listEl.innerHTML = '';
      const letters = ['A', 'B', 'C', 'D'];
      q.opts.forEach((optText, optIdx) => {
        const btn = document.createElement('button');
        btn.className = 'quiz-opt-item-btn';
        btn.innerHTML = `<span class="quiz-opt-key">${letters[optIdx]}</span><span class="quiz-opt-label">${optText}</span>`;
        btn.onclick = () => {
          SoundEngine.playPop();
          AnswerTracker.recordAnswer(`quiz_q${idx + 1}`, q.q, optText);
          const feedbackText = document.getElementById('quiz-feedback-text');
          if (feedbackBox && feedbackText) {
            feedbackText.textContent = q.reactions[optIdx] || "Interesting answer, Peda. 😂";
            feedbackBox.style.display = 'block';
          }
        };
        listEl.appendChild(btn);
      });
    }
  }

  function setupScene4() {
    renderQuizQuestion(0);
    const btnNext = document.getElementById('btn-quiz-next');
    if (btnNext) {
      btnNext.addEventListener('click', () => {
        SoundEngine.playChime();
        if (quizCurrentIndex < intelligenceQuestions.length - 1) {
          quizCurrentIndex++;
          renderQuizQuestion(quizCurrentIndex);
        } else {
          StoryRouter.goToScreen(5, 'next');
        }
      });
    }
  }

  // --- Scene 5: Would You Rather (4 Pairs) ---
  const wyrPairs = [
    {
      badge: "Pair 1 of 4",
      a: "Fight with Bhai every day",
      b: "Admit Bhai is right once?",
      rA: "A true warrior! Sibling arguments are cardio anyway. 🥊😂",
      rB: "Admitting I am right?! A miracle on Raksha Bandhan! 🏆✨"
    },
    {
      badge: "Pair 2 of 4",
      a: "Unlimited chocolate for life",
      b: "Unlimited shopping for life?",
      rA: "Sweet tooth Peda spotted! 🍫😋",
      rB: "Goodbye entire bank account! Maharani Peda Devi is shopping! 🛍️💅"
    },
    {
      badge: "Pair 3 of 4",
      a: "Never argue with Bhai again",
      b: "Never annoy each other again?",
      rA: "Life would be too boring without our arguments. 🤝",
      rB: "Annoying each other is our official love language! 😂❤️"
    },
    {
      badge: "Pair 4 of 4",
      a: "Bhai cooks dinner for you",
      b: "Bhai gives you ₹500 directly?",
      rA: "Order ambulance just in case! 🍳🔥",
      rB: "Straight cash! Peda's business mind is sharp. 💸🤑"
    }
  ];
  let wyrIndex = 0;

  function renderWyrPair(idx) {
    const p = wyrPairs[idx];
    const stepBadge = document.getElementById('wyr-step-badge');
    const textA = document.getElementById('wyr-text-a');
    const textB = document.getElementById('wyr-text-b');
    const feedbackBox = document.getElementById('wyr-feedback-box');
    const btnLabel = document.getElementById('wyr-btn-label');
    const cardA = document.getElementById('wyr-card-a');
    const cardB = document.getElementById('wyr-card-b');

    if (cardA) cardA.classList.remove('selected');
    if (cardB) cardB.classList.remove('selected');
    if (stepBadge) stepBadge.textContent = p.badge;
    if (textA) textA.textContent = p.a;
    if (textB) textB.textContent = p.b;
    if (feedbackBox) feedbackBox.style.display = 'none';
    if (btnLabel) btnLabel.textContent = idx === wyrPairs.length - 1 ? 'Start Memory Machine' : 'Next Dilemma';
  }

  function setupScene5() {
    renderWyrPair(0);
    const cardA = document.getElementById('wyr-card-a');
    const cardB = document.getElementById('wyr-card-b');
    const feedbackBox = document.getElementById('wyr-feedback-box');
    const feedbackText = document.getElementById('wyr-feedback-text');
    const btnNext = document.getElementById('btn-wyr-next');

    function selectCard(card, isOptionA) {
      SoundEngine.playPop();
      if (cardA) cardA.classList.remove('selected');
      if (cardB) cardB.classList.remove('selected');
      card.classList.add('selected');

      const p = wyrPairs[wyrIndex];
      const selectedText = isOptionA ? p.a : p.b;
      const reaction = isOptionA ? p.rA : p.rB;

      AnswerTracker.recordAnswer(`wyr_pair${wyrIndex + 1}`, `Would You Rather ${wyrIndex + 1}`, selectedText);

      if (feedbackBox && feedbackText) {
        feedbackText.textContent = reaction;
        feedbackBox.style.display = 'block';
      }
    }

    if (cardA) cardA.onclick = () => selectCard(cardA, true);
    if (cardB) cardB.onclick = () => selectCard(cardB, false);

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        SoundEngine.playChime();
        if (wyrIndex < wyrPairs.length - 1) {
          wyrIndex++;
          renderWyrPair(wyrIndex);
        } else {
          StoryRouter.goToScreen(6, 'next');
        }
      });
    }
  }

  // --- Scene 6: Memory Machine 3000 ---
  function setupScene6() {
    const btnStart = document.getElementById('btn-start-machine');
    const statusMsg = document.getElementById('machine-status-msg');
    const startWrap = document.getElementById('machine-start-wrap');
    const recoveredStage = document.getElementById('machine-recovered-stage');
    const guessButtons = document.querySelectorAll('#machine-recovered-stage .btn-choice-pill');
    const reactionBox = document.getElementById('machine-reaction-box');
    const reactionText = document.getElementById('machine-reaction-text');
    const btnEnterJourney = document.getElementById('btn-enter-memory-journey');

    if (btnStart) {
      btnStart.addEventListener('click', () => {
        SoundEngine.playShutter();
        if (statusMsg) statusMsg.textContent = "RECOVERING 23-YEAR MEMORY DATA...";

        setTimeout(() => {
          SoundEngine.playChime();
          if (startWrap) startWrap.style.display = 'none';
          if (recoveredStage) recoveredStage.style.display = 'block';
          ParticleEngine.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.4, 30);
        }, 1200);
      });
    }

    guessButtons.forEach((btn) => {
      btn.addEventListener('click', function () {
        SoundEngine.playPop();
        const guess = this.getAttribute('data-mguess');
        let rep = "Caught you remembering! Let's visit all 6 memories. 📸✨";
        if (guess === 'why') rep = "Because archiving Peda's nautanki is my life's mission! 😂📸";

        AnswerTracker.recordAnswer('memory_machine_guess', 'Do you remember this?', guess);

        if (reactionBox && reactionText) {
          reactionText.textContent = rep;
          reactionBox.style.display = 'block';
        }
      });
    });

    if (btnEnterJourney) {
      btnEnterJourney.addEventListener('click', () => {
        StoryRouter.goToScreen(7, 'next');
      });
    }
  }

  // --- Scenes 7–12: Memory Journey ---
  function setupMemoryJourney() {
    const memoryRoutes = [
      { btn: 'btn-scene-7-next', target: 8 },
      { btn: 'btn-scene-8-next', target: 9 },
      { btn: 'btn-scene-9-next', target: 10 },
      { btn: 'btn-scene-10-next', target: 11 },
      { btn: 'btn-scene-11-next', target: 12 },
      { btn: 'btn-scene-12-next', target: 13 }
    ];

    memoryRoutes.forEach((r) => {
      const el = document.getElementById(r.btn);
      if (el) {
        el.addEventListener('click', () => {
          StoryRouter.goToScreen(r.target, 'next');
        });
      }
    });
  }

  // --- Scene 13: Sibling Cup Scoreboard ---
  function startSiblingCupScoreboard() {
    function animateCounter(id, target, duration) {
      const el = document.getElementById(id);
      if (!el) return;
      let start = 0;
      const stepTime = Math.abs(Math.floor(duration / target));
      const timer = setInterval(() => {
        start += 1;
        el.textContent = start;
        if (start >= target) {
          el.textContent = target;
          clearInterval(timer);
        }
      }, stepTime || 20);
    }

    setTimeout(() => { animateCounter('cup-drama-p', 94, 700); animateCounter('cup-drama-pr', 88, 700); }, 150);
    setTimeout(() => { animateCounter('cup-stub-p', 99, 700); animateCounter('cup-stub-pr', 95, 700); }, 400);
    setTimeout(() => { animateCounter('cup-food-p', 86, 700); animateCounter('cup-food-pr', 42, 700); }, 650);
    setTimeout(() => { animateCounter('cup-arg-p', 87, 700); animateCounter('cup-arg-pr', 91, 700); }, 900);
    setTimeout(() => { animateCounter('cup-lazy-p', 78, 700); animateCounter('cup-lazy-pr', 80, 700); }, 1150);
    setTimeout(() => { animateCounter('cup-mom-p', 91, 700); animateCounter('cup-mom-pr', 93, 700); }, 1400);

    const btnNext = document.getElementById('btn-scene-13-next');
    if (btnNext) {
      btnNext.onclick = () => StoryRouter.goToScreen(14, 'next');
    }
  }

  // --- Scene 14: Brother's Roast Mode ---
  const roastList = [
    "23 years old and still stealing food from my plate without shame. 🍟",
    "Professional argument specialist: Can turn a 30-second conversation into a 45-minute national debate. 🎙️",
    "Somehow always right. (According to herself, her mirror, and her supreme ego). 👑",
    "CEO of Bakbak & Home Minister of completely unnecessary opinions. 📢",
    "Certified Peda: Looks innocent, causes 90% of the household chaos. 🌪️"
  ];
  let roastIdx = 0;

  function setupScene14() {
    const btnStart = document.getElementById('btn-start-roast');
    const warningStage = document.getElementById('roast-warning-stage');
    const activeStage = document.getElementById('roast-active-stage');
    const roastText = document.getElementById('roast-text-content');
    const btnNextRoast = document.getElementById('btn-roast-next-item');
    const btnFinish = document.getElementById('btn-roast-finish');

    if (btnStart) {
      btnStart.addEventListener('click', () => {
        SoundEngine.playPop();
        if (warningStage) warningStage.style.display = 'none';
        if (activeStage) activeStage.style.display = 'block';
        if (roastText) roastText.textContent = roastList[0];
      });
    }

    if (btnNextRoast) {
      btnNextRoast.addEventListener('click', () => {
        SoundEngine.playPop();
        roastIdx++;
        if (roastIdx < roastList.length) {
          if (roastText) roastText.textContent = roastList[roastIdx];
        }
        if (roastIdx >= roastList.length - 1) {
          if (btnNextRoast) btnNextRoast.style.display = 'none';
          if (btnFinish) btnFinish.style.display = 'inline-flex';
        }
      });
    }

    if (btnFinish) {
      btnFinish.addEventListener('click', () => {
        StoryRouter.goToScreen(15, 'next');
      });
    }
  }

  // --- Scene 15: Sister Nickname Generator ---
  function setupScene15() {
    const btnSpin = document.getElementById('btn-spin-slot');
    const reel1 = document.querySelector('#reel-1 .reel-val');
    const reel2 = document.querySelector('#reel-2 .reel-val');
    const reel3 = document.querySelector('#reel-3 .reel-val');
    const resultBadge = document.getElementById('slot-result-badge');
    const btnNext = document.getElementById('btn-slot-next');

    const names1 = ["MAHARANI", "CHOTI DON", "CERTIFIED", "PROFESSIONAL", "PERMANENT"];
    const names2 = ["PEDA", "GADHI", "DRAMA QUEEN", "FOOD CHOR", "BAKBAK MACHINE"];
    const names3 = ["DEVI", "JI", "SPECIALIST", "HEADACHE", "EXPERT"];

    if (btnSpin) {
      btnSpin.addEventListener('click', () => {
        SoundEngine.playChime();
        btnSpin.disabled = true;

        let ticks = 0;
        const spinInterval = setInterval(() => {
          if (reel1) reel1.textContent = names1[Math.floor(Math.random() * names1.length)];
          if (reel2) reel2.textContent = names2[Math.floor(Math.random() * names2.length)];
          if (reel3) reel3.textContent = names3[Math.floor(Math.random() * names3.length)];
          SoundEngine.playPop();
          ticks++;

          if (ticks > 14) {
            clearInterval(spinInterval);
            if (reel1) reel1.textContent = "MAHARANI";
            if (reel2) reel2.textContent = "PEDA";
            if (reel3) reel3.textContent = "DEVI";

            SoundEngine.playFanfare();
            ParticleEngine.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 45);

            if (resultBadge) resultBadge.style.display = 'block';
            if (btnSpin) btnSpin.style.display = 'none';
            if (btnNext) btnNext.style.display = 'inline-flex';
          }
        }, 100);
      });
    }

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        StoryRouter.goToScreen(16, 'next');
      });
    }
  }

  // --- Scene 16: 23 Things About My Bhena ---
  const twentyThreeList = [
    "01 — Funny", "02 — Stubborn", "03 — Caring", "04 — Dramatic", "05 — Food thief",
    "06 — Secretly emotional", "07 — Annoying", "08 — Protective", "09 — Strong",
    "10 — Impossible to argue with", "11 — Bakbak expert", "12 — Professional Nautanki",
    "13 — Sweet when she wants to be", "14 — Always has an opinion", "15 — Surprisingly thoughtful",
    "16 — My partner in crime", "17 — Occasionally sensible", "18 — Usually chaotic",
    "19 — Impossible to replace", "20 — Family", "21 — Friend", "22 — My favorite Gadhi", "23 — My Bhena ❤️"
  ];
  let traitIdx = 0;

  function setupScene16() {
    const numBadge = document.getElementById('trait-num-badge');
    const traitText = document.getElementById('trait-text');
    const counterEl = document.getElementById('traits-counter');
    const btnNext = document.getElementById('btn-trait-next');
    const btnAll = document.getElementById('btn-trait-all');
    const btnFinish = document.getElementById('btn-trait-finish');
    const allGrid = document.getElementById('all-23-grid');

    // Populate allGrid
    if (allGrid) {
      allGrid.innerHTML = '';
      twentyThreeList.forEach((item) => {
        const chip = document.createElement('div');
        chip.className = 'grid-trait-chip';
        chip.textContent = item;
        allGrid.appendChild(chip);
      });
    }

    function renderTrait(idx) {
      const parts = twentyThreeList[idx].split(' — ');
      if (numBadge) numBadge.textContent = parts[0];
      if (traitText) traitText.textContent = parts[1];
      if (counterEl) counterEl.textContent = `${idx + 1} of 23`;

      if (idx === twentyThreeList.length - 1) {
        if (btnNext) btnNext.style.display = 'none';
        if (btnFinish) btnFinish.style.display = 'inline-flex';
      }
    }

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        SoundEngine.playPop();
        if (traitIdx < twentyThreeList.length - 1) {
          traitIdx++;
          renderTrait(traitIdx);
        }
      });
    }

    if (btnAll && allGrid) {
      btnAll.addEventListener('click', () => {
        SoundEngine.playChime();
        const isHidden = allGrid.style.display === 'none' || !allGrid.style.display;
        allGrid.style.display = isHidden ? 'grid' : 'none';
        btnAll.textContent = isHidden ? 'Hide Grid' : 'Show All 23';
        if (btnFinish) btnFinish.style.display = 'inline-flex';
      });
    }

    if (btnFinish) {
      btnFinish.addEventListener('click', () => {
        StoryRouter.goToScreen(17, 'next');
      });
    }
  }

  // --- Scene 17: Star Compliment Game ---
  const starMessages = {
    "1": "You're stronger than you realize. 💪",
    "2": "You're more caring than you show. ❤️",
    "3": "You're hilarious when you're not trying. 😂",
    "4": "You make ordinary days memorable. 🌟",
    "5": "You're family, but you're also my friend. 🤝",
    "6": "You're irreplaceable, Peda. ✨",
    "7": "Yes, Gadhi. I actually mean every word of this. 🌸"
  };
  let discoveredStars = new Set();

  function setupScene17() {
    const starButtons = document.querySelectorAll('#night-sky-board .glow-star-btn');
    const statusText = document.getElementById('stars-unlocked-status');
    const msgText = document.getElementById('star-msg-text');
    const finishWrap = document.getElementById('star-finish-wrap');
    const btnNext = document.getElementById('btn-star-next');

    starButtons.forEach((btn) => {
      btn.addEventListener('click', function () {
        SoundEngine.playChime();
        const starId = this.getAttribute('data-star');
        this.classList.add('discovered');
        discoveredStars.add(starId);

        if (msgText) msgText.textContent = starMessages[starId] || "A shining sibling truth! ✨";
        if (statusText) statusText.textContent = `${discoveredStars.size} of 7 stars discovered`;

        if (discoveredStars.size >= 7) {
          if (statusText) statusText.textContent = "All 7 secrets unlocked ✨";
          if (finishWrap) finishWrap.style.display = 'flex';
          ParticleEngine.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 40);
        }
      });
    });

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        StoryRouter.goToScreen(18, 'next');
      });
    }
  }

  // --- Scene 18: Rakhi Thread Interaction ---
  function setupScene18() {
    const btnTie = document.getElementById('btn-tie-rakhi-action');
    const mandala = document.getElementById('rakhi-center-mandala');
    const threadFill = document.getElementById('thread-path-fill');
    const statusBox = document.getElementById('rakhi-status-box');
    const completeMsg = document.getElementById('rakhi-complete-msg');
    const btnNext = document.getElementById('btn-rakhi-next');

    function completeRakhiTie() {
      SoundEngine.playFanfare();
      if (threadFill) threadFill.style.strokeDashoffset = '0';
      if (statusBox) statusBox.style.display = 'none';
      if (completeMsg) completeMsg.style.display = 'block';
      ParticleEngine.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.4, 50, ['#E11D48', '#F59E0B', '#FEF3C7']);
    }

    if (btnTie) btnTie.onclick = completeRakhiTie;
    if (mandala) mandala.onclick = completeRakhiTie;

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        StoryRouter.goToScreen(19, 'next');
      });
    }
  }

  // --- Scene 19: Original Hindi Shayari & Easter Egg 2 ---
  let rakhiTapCount = 0;
  function startShayariSequence() {
    const lines = document.querySelectorAll('#scene-19 .shayari-line');
    const actWrap = document.getElementById('shayari-action-wrap');
    lines.forEach((l) => l.classList.remove('revealed'));
    if (actWrap) actWrap.style.opacity = '0';

    lines.forEach((l, idx) => {
      setTimeout(() => {
        l.classList.add('revealed');
        if (idx === lines.length - 1) {
          SoundEngine.playChime();
          setTimeout(() => {
            if (actWrap) {
              actWrap.style.transition = 'opacity 0.6s ease';
              actWrap.style.opacity = '1';
            }
          }, 800);
        }
      }, (idx + 1) * 1100);
    });

    const btnNext = document.getElementById('btn-scene-19-next');
    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(20, 'next');

    // Easter Egg 2: Tap Rakhi 5 times
    const mandala = document.getElementById('shayari-mandala-egg');
    const toast2 = document.getElementById('easter-egg-2-toast');
    if (mandala) {
      mandala.onclick = () => {
        rakhiTapCount++;
        SoundEngine.playPop();
        ParticleEngine.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.3, 15);
        if (rakhiTapCount >= 5 && toast2) {
          toast2.style.display = 'inline-block';
          SoundEngine.playFanfare();
        }
      };
    }
  }

  // --- Scene 20: Secret Drawer ---
  function setupScene20() {
    const btnOpen = document.getElementById('btn-open-drawer');
    const drawer = document.getElementById('drawer-pullable');
    const note = document.getElementById('drawer-secret-note');
    const btnNext = document.getElementById('btn-drawer-next');

    function openSecretDrawer() {
      SoundEngine.playChime();
      if (drawer) drawer.style.transform = 'translateY(-20px)';
      if (btnOpen) btnOpen.style.display = 'none';
      if (note) note.style.display = 'block';
      if (btnNext) btnNext.style.display = 'inline-flex';
      ParticleEngine.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 30);
    }

    if (btnOpen) btnOpen.onclick = openSecretDrawer;
    if (drawer) drawer.onclick = openSecretDrawer;

    if (btnNext) {
      btnNext.onclick = () => StoryRouter.goToScreen(21, 'next');
    }
  }

  // --- Scene 21: Fake System Error ---
  function startSystemErrorSequence() {
    const barFill = document.getElementById('error-bar-fill');
    const diag = document.getElementById('error-diagnosis');
    const nextWrap = document.getElementById('error-next-wrap');
    const btnNext = document.getElementById('btn-error-next');

    if (barFill) barFill.style.width = '0%';
    if (diag) diag.style.display = 'none';
    if (nextWrap) nextWrap.style.display = 'none';

    setTimeout(() => {
      SoundEngine.playPop();
      if (barFill) barFill.style.width = '100%';
    }, 400);

    setTimeout(() => {
      SoundEngine.playChime();
      if (diag) diag.style.display = 'block';
      if (nextWrap) nextWrap.style.display = 'flex';
    }, 1800);

    if (btnNext) {
      btnNext.onclick = () => StoryRouter.goToScreen(22, 'next');
    }
  }

  // --- Scene 22: Emotional Transition ---
  let emoCurrentIndex = 0;
  function startEmotionalSequence() {
    emoCurrentIndex = 0;
    const lines = document.querySelectorAll('#scene-22 .emo-line');
    const actWrap = document.getElementById('emo-action-wrap');
    const hint = document.getElementById('emo-tap-hint');
    const container = document.getElementById('emotional-sequence');

    lines.forEach((l) => l.classList.remove('revealed'));
    if (actWrap) actWrap.style.display = 'none';
    if (hint) hint.style.display = 'block';

    if (lines[0]) lines[0].classList.add('revealed');

    function revealNextEmoLine() {
      if (emoCurrentIndex < lines.length - 1) {
        emoCurrentIndex++;
        lines[emoCurrentIndex].classList.add('revealed');
        SoundEngine.playPop();

        if (emoCurrentIndex === lines.length - 1) {
          SoundEngine.playChime();
          if (hint) hint.style.display = 'none';
          if (actWrap) actWrap.style.display = 'flex';
        }
      }
    }

    if (container) {
      container.onclick = (e) => {
        if (e.target.closest('#btn-scene-22-next')) return;
        revealNextEmoLine();
      };
    }

    const btnNext = document.getElementById('btn-scene-22-next');
    if (btnNext) {
      btnNext.onclick = () => StoryRouter.goToScreen(23, 'next');
    }
  }

  // --- Scene 23: 3D Handwritten Letter & Easter Egg 5 ---
  function setupScene23() {
    const envelope = document.getElementById('story-envelope');
    const waxSeal = document.getElementById('env-wax-seal');
    const openBtn = document.getElementById('btn-open-letter-trigger');
    const nextBtn = document.getElementById('btn-scene-23-next');
    const brotherSig = document.getElementById('brother-sig');
    const toast5 = document.getElementById('easter-egg-5-toast');
    let isOpen = false;

    function openEnvelope() {
      if (isOpen) return;
      isOpen = true;
      SoundEngine.playChime();

      if (envelope) envelope.classList.add('is-open');
      if (openBtn) openBtn.style.display = 'none';

      ParticleEngine.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 45, ['#F472B6', '#FDA4AF', '#FEF3C7']);

      setTimeout(() => {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
      }, 1200);
    }

    if (envelope) envelope.addEventListener('click', openEnvelope);
    if (waxSeal) waxSeal.addEventListener('click', (e) => { e.stopPropagation(); openEnvelope(); });
    if (openBtn) openBtn.addEventListener('click', openEnvelope);

    // Easter Egg 5: Click brother signature
    if (brotherSig) {
      brotherSig.addEventListener('click', (e) => {
        e.stopPropagation();
        SoundEngine.playPop();
        if (toast5) {
          toast5.style.display = 'inline-block';
          setTimeout(() => { toast5.style.display = 'none'; }, 4000);
        }
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        StoryRouter.goToScreen(24, 'next');
      });
    }
  }

  // --- Scene 24: Future Message ---
  function setupScene24() {
    const btnNext = document.getElementById('btn-scene-24-next');
    if (btnNext) {
      btnNext.addEventListener('click', () => {
        StoryRouter.goToScreen(25, 'next');
      });
    }
  }

  // --- Scene 25: Final Suspense ---
  function startSuspenseSequence() {
    const l1 = document.getElementById('su-line-1');
    const l2 = document.getElementById('su-line-2');
    const l3 = document.getElementById('su-line-3');
    const l4 = document.getElementById('su-line-4');
    const l5 = document.getElementById('su-line-5');
    const act = document.getElementById('su-action-wrap');

    if (l1) l1.style.opacity = '0';
    if (l2) l2.style.opacity = '0';
    if (l3) l3.style.opacity = '0';
    if (l4) l4.style.opacity = '0';
    if (l5) l5.style.opacity = '0';
    if (act) act.style.display = 'none';

    setTimeout(() => { if (l1) { l1.style.transition = 'opacity 0.8s ease'; l1.style.opacity = '1'; } }, 300);
    setTimeout(() => { if (l2) { l2.style.transition = 'opacity 0.8s ease'; l2.style.opacity = '1'; } }, 2000);
    setTimeout(() => { if (l3) { l3.style.transition = 'opacity 0.8s ease'; l3.style.opacity = '1'; } }, 3600);
    setTimeout(() => { if (l4) { l4.style.transition = 'opacity 0.8s ease'; l4.style.opacity = '1'; } }, 5200);
    setTimeout(() => { if (l5) { l5.style.transition = 'opacity 0.8s ease'; l5.style.opacity = '1'; } }, 6800);
    setTimeout(() => {
      if (act) {
        act.style.display = 'flex';
        act.style.animation = 'pop-in 0.6s var(--ease-spring)';
      }
    }, 8000);

    const btnReveal = document.getElementById('btn-reveal-rakhi-surprise');
    if (btnReveal) {
      btnReveal.onclick = () => StoryRouter.goToScreen(26, 'next');
    }
  }

  // --- Scene 26: Final Photo Reveal ---
  function setupScene26() {
    const btnNext = document.getElementById('btn-scene-26-next');
    if (btnNext) {
      btnNext.addEventListener('click', () => {
        StoryRouter.goToScreen(27, 'next');
      });
    }
  }

  // --- Scene 27: Finale Celebration & Song ---
  function triggerGrandCelebration() {
    SoundEngine.playFanfare();
    MusicPlayer.play();
    ParticleEngine.startFireworks();

    const w = window.innerWidth;
    const h = window.innerHeight;

    ParticleEngine.fireConfetti(w * 0.2, h * 0.5, 90);
    ParticleEngine.fireConfetti(w * 0.8, h * 0.5, 90);

    setTimeout(() => {
      ParticleEngine.fireConfetti(w * 0.5, h * 0.35, 120);
    }, 450);

    setTimeout(() => {
      ParticleEngine.fireConfetti(w * 0.35, h * 0.5, 70);
      ParticleEngine.fireConfetti(w * 0.65, h * 0.5, 70);
    }, 900);
  }

  function setupScene27() {
    const btnMore = document.getElementById('btn-cannon-more');
    const btnDiya = document.getElementById('btn-diya-bless');
    const btnDownload = document.getElementById('btn-download-keepsake');
    const btnReplay = document.getElementById('btn-replay-story');
    const toastBox = document.getElementById('blessing-toast-box');
    const togetherPhoto = document.getElementById('together-photo-img');

    if (btnMore) btnMore.addEventListener('click', triggerGrandCelebration);

    if (btnDiya) {
      btnDiya.addEventListener('click', () => {
        SoundEngine.playChime();
        if (toastBox) {
          const isHidden = toastBox.style.display === 'none' || !toastBox.style.display;
          toastBox.style.display = isHidden ? 'block' : 'none';
          if (isHidden) {
            const rect = btnDiya.getBoundingClientRect();
            ParticleEngine.fireConfetti(rect.left + rect.width / 2, rect.top, 35, ['#F59E0B', '#FBBF24', '#FEF3C7']);
          }
        }
      });
    }

    // Easter Egg 3: Clicking photo spawns floating hearts
    if (togetherPhoto) {
      togetherPhoto.addEventListener('click', (e) => {
        SoundEngine.playPop();
        ParticleEngine.spawnFloatingHeart(e.clientX, e.clientY);
      });
    }

    // Easter Egg 1 Button
    const egg1Btn = document.getElementById('easter-egg-1-btn');
    const egg1Toast = document.getElementById('easter-egg-1-toast');
    if (egg1Btn) {
      egg1Btn.addEventListener('click', () => {
        SoundEngine.playPop();
        ParticleEngine.fireConfetti(window.innerWidth * 0.8, 60, 25);
        if (egg1Toast) {
          egg1Toast.style.display = 'inline-block';
          setTimeout(() => { egg1Toast.style.display = 'none'; }, 4000);
        }
      });
    }

    // Easter Egg 4: Keyboard 'P' Key
    window.addEventListener('keydown', (e) => {
      if (e.key === 'p' || e.key === 'P') {
        const egg4Toast = document.getElementById('easter-egg-4-toast');
        if (egg4Toast) {
          SoundEngine.playPop();
          egg4Toast.style.display = 'inline-block';
          setTimeout(() => { egg4Toast.style.display = 'none'; }, 4000);
        }
      }
    });

    if (btnDownload) {
      btnDownload.addEventListener('click', downloadKeepsakeCard);
    }

    if (btnReplay) {
      btnReplay.addEventListener('click', () => {
        SoundEngine.playChime();
        MusicPlayer.pause();
        StoryRouter.goToScreen(1, 'prev');
      });
    }
  }

  function downloadKeepsakeCard() {
    SoundEngine.playPop();
    const canvas = document.createElement('canvas');
    canvas.width = 1200;
    canvas.height = 800;
    const ctx = canvas.getContext('2d');

    const grad = ctx.createLinearGradient(0, 0, 1200, 800);
    grad.addColorStop(0, '#FFF1F2');
    grad.addColorStop(0.5, '#FEF3C7');
    grad.addColorStop(1, '#EDE9FE');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 1200, 800);

    ctx.strokeStyle = '#F59E0B';
    ctx.lineWidth = 12;
    ctx.strokeRect(28, 28, 1144, 744);

    ctx.strokeStyle = '#E11D48';
    ctx.lineWidth = 3;
    ctx.strokeRect(42, 42, 1116, 716);

    ctx.fillStyle = '#881337';
    ctx.font = 'bold 36px "Plus Jakarta Sans", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('✨ A SPECIAL RAKHI KEEPSAKE ✨', 600, 130);

    ctx.fillStyle = '#BE123C';
    ctx.font = 'bold 64px "Playfair Display", Georgia, serif';
    ctx.fillText('Happy Raksha Bandhan, Prerna (Peda)!', 600, 250);

    ctx.fillStyle = '#B45309';
    ctx.font = '600 32px "Plus Jakarta Sans", sans-serif';
    ctx.fillText('23 Years of Being an Amazing Sister', 600, 320);

    ctx.fillStyle = '#4A1525';
    ctx.font = 'italic 28px "Plus Jakarta Sans", sans-serif';
    ctx.fillText('"You may annoy me and steal my food, but you will always be', 600, 430);
    ctx.fillText('one of the most important people in my life."', 600, 480);

    ctx.fillStyle = '#E11D48';
    ctx.font = 'bold 42px "Playfair Display", serif';
    ctx.fillText('Love you always ❤️', 600, 590);

    ctx.fillStyle = '#881337';
    ctx.font = '600 28px "Plus Jakarta Sans", sans-serif';
    ctx.fillText('— Your annoying brother, Prakhar', 600, 660);

    const link = document.createElement('a');
    link.download = 'Rakhi_Surprise_For_Prerna.png';
    link.href = canvas.toDataURL('image/png');
    link.click();
  }

  // ==========================================================================
  // 7. GLOBAL DOM READY INITIALIZATION
  // ==========================================================================
  document.addEventListener('DOMContentLoaded', () => {
    ParticleEngine.init();
    MusicPlayer.init();
    StoryRouter.init();

    const soundToggle = document.getElementById('sound-toggle');
    if (soundToggle) soundToggle.addEventListener('click', SoundEngine.toggleSound);

    setupScene2();
    setupScene3();
    setupScene4();
    setupScene5();
    setupScene6();
    setupMemoryJourney();
    setupScene14();
    setupScene15();
    setupScene16();
    setupScene17();
    setupScene18();
    setupScene20();
    setupScene23();
    setupScene24();
    setupScene26();
    setupScene27();
  });
})();
"""
    for path in [os.path.join(FRONTEND_DIR, "script.js"), os.path.join(BASE_DIR, "script.js")]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    print("✓ Generated script.js in frontend/ and root")

def generate_backend():

    # 1. database.py
    database_py = """# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./rakhi_answers.db")

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""
    with open(os.path.join(BACKEND_DIR, "database.py"), "w", encoding="utf-8") as f:
        f.write(database_py)

    # 2. models.py
    models_py = """# -*- coding: utf-8 -*-
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

    answers = relationship("SessionAnswer", back_populates="session", cascade="all, delete-orphan")

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
"""
    with open(os.path.join(BACKEND_DIR, "models.py"), "w", encoding="utf-8") as f:
        f.write(models_py)

    # 3. schemas.py
    schemas_py = """# -*- coding: utf-8 -*-
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
        orm_mode = True

class SessionOut(BaseModel):
    id: str
    started_at: datetime
    is_completed: bool
    completed_at: Optional[datetime] = None
    answers_count: int = 0

    class Config:
        orm_mode = True

class SessionDetailOut(BaseModel):
    id: str
    started_at: datetime
    is_completed: bool
    completed_at: Optional[datetime] = None
    answers: List[AnswerOut] = []

    class Config:
        orm_mode = True
"""
    with open(os.path.join(BACKEND_DIR, "schemas.py"), "w", encoding="utf-8") as f:
        f.write(schemas_py)

    # 4. main.py
    main_py = """# -*- coding: utf-8 -*-
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
    description="Secure, lightweight answer collection API for Prerna's interactive Rakhi experience.",
    version="1.0.0"
)

# CORS Configuration
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
    return {"status": "ok", "app": "Rakhi Surprise API", "timestamp": datetime.utcnow().isoformat()}

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
    return {"status": "success", "message": "Answer recorded"}

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
"""
    with open(os.path.join(BACKEND_DIR, "main.py"), "w", encoding="utf-8") as f:
        f.write(main_py)

    # 5. requirements.txt
    reqs = """fastapi>=0.100.0
uvicorn>=0.22.0
sqlalchemy>=2.0.0
pydantic>=2.0.0
python-dotenv>=1.0.0
"""
    with open(os.path.join(BACKEND_DIR, "requirements.txt"), "w", encoding="utf-8") as f:
        f.write(reqs)

    # 6. .env.example & .env
    env_example = """# Rakhi Surprise Backend Environment Configuration
ADMIN_PASSWORD=change_this_to_a_secure_password
DATABASE_URL=sqlite:///./rakhi_answers.db
ENVIRONMENT=development
ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:5500,http://localhost:8000,http://127.0.0.1:8000
"""
    with open(os.path.join(BACKEND_DIR, ".env.example"), "w", encoding="utf-8") as f:
        f.write(env_example)
    
    env_file = """# Local Dev Environment
ADMIN_PASSWORD=peda2026
DATABASE_URL=sqlite:///./rakhi_answers.db
ENVIRONMENT=development
ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:5500,http://localhost:8000,http://127.0.0.1:8000
"""
    with open(os.path.join(BACKEND_DIR, ".env"), "w", encoding="utf-8") as f:
        f.write(env_file)

    print("✓ Generated backend (main.py, database.py, models.py, schemas.py, requirements.txt, .env)")

def generate_dashboard():
    content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prakhar's Admin Dashboard • Prerna's Rakhi Journey</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0F0811;
      --card-bg: #1B0E1E;
      --accent: #E11D48;
      --gold: #F59E0B;
      --text: #F8FAFC;
      --text-muted: #94A3B8;
      --border: #331A38;
      --green: #10B981;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Plus Jakarta Sans', sans-serif;
      min-height: 100vh;
      padding: 24px;
    }
    .container { max-width: 1100px; margin: 0 auto; }
    .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 28px; border-bottom: 1px solid var(--border); padding-bottom: 16px; }
    .header h1 { font-family: 'Outfit', sans-serif; font-size: 1.6rem; color: var(--gold); }
    .btn { background: var(--accent); color: #fff; border: none; padding: 10px 20px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: 0.2s; }
    .btn:hover { background: #BE123C; }
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 28px; }
    .stat-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 14px; padding: 20px; text-align: center; }
    .stat-val { font-size: 2.2rem; font-weight: 700; color: var(--gold); margin-bottom: 4px; font-family: 'Outfit', sans-serif; }
    .stat-lbl { font-size: 0.82rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700; }
    .panel { background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 24px; margin-bottom: 24px; }
    .panel h2 { font-size: 1.25rem; margin-bottom: 16px; color: var(--text); }
    table { width: 100%; border-collapse: collapse; text-align: left; }
    th, td { padding: 12px 14px; border-bottom: 1px solid var(--border); font-size: 0.9rem; }
    th { color: var(--text-muted); font-weight: 600; }
    .badge { padding: 4px 10px; border-radius: 999px; font-size: 0.75rem; font-weight: 700; }
    .badge-success { background: rgba(16, 185, 129, 0.2); color: var(--green); }
    .badge-pending { background: rgba(245, 158, 11, 0.2); color: var(--gold); }
    .clickable-row { cursor: pointer; transition: background 0.15s; }
    .clickable-row:hover { background: rgba(225, 29, 72, 0.08); }
    .login-box { max-width: 380px; margin: 80px auto; background: var(--card-bg); border: 1px solid var(--border); padding: 32px; border-radius: 16px; text-align: center; }
    .login-input { width: 100%; padding: 12px 16px; background: #0B040B; border: 1px solid var(--border); border-radius: 8px; color: #fff; margin: 16px 0; font-size: 1rem; }
    .modal { position: fixed; inset: 0; background: rgba(0,0,0,0.8); display: flex; align-items: center; justify-content: center; z-index: 100; padding: 20px; }
    .modal-content { background: var(--card-bg); border: 1px solid var(--border); border-radius: 18px; width: min(100%, 750px); max-height: 85vh; overflow-y: auto; padding: 28px; position: relative; }
    .close-btn { position: absolute; top: 16px; right: 16px; background: none; border: none; color: var(--text-muted); font-size: 1.4rem; cursor: pointer; }
    .qa-card { background: #120714; border: 1px solid var(--border); border-radius: 10px; padding: 14px 16px; margin-bottom: 12px; }
    .qa-q { font-weight: 700; color: var(--gold); font-size: 0.95rem; margin-bottom: 4px; }
    .qa-a { font-size: 1.05rem; color: #fff; }
    .qa-time { font-size: 0.75rem; color: var(--text-muted); margin-top: 4px; text-align: right; }
  </style>
</head>
<body>

  <div id="login-section" class="login-box">
    <h2 style="color: var(--gold); margin-bottom: 8px;">🔐 Brother's Portal</h2>
    <p style="color: var(--text-muted); font-size: 0.9rem;">Enter admin password to view Prerna's journey:</p>
    <input type="password" id="admin-pass" class="login-input" placeholder="Admin password (default: peda2026)">
    <button id="btn-login" class="btn" style="width: 100%;">Unlock Dashboard</button>
    <p id="login-error" style="color: #F87171; font-size: 0.85rem; margin-top: 12px; display: none;">Invalid password!</p>
  </div>

  <div id="dashboard-section" class="container" style="display: none;">
    <div class="header">
      <div>
        <h1>🌸 Prerna's Rakhi Journey • Live Insights</h1>
        <p style="color: var(--text-muted); font-size: 0.85rem;">Monitored live from FastAPI Backend</p>
      </div>
      <div>
        <button id="btn-refresh" class="btn" style="background: #334155; margin-right: 8px;">Refresh</button>
        <button id="btn-logout" class="btn">Logout</button>
      </div>
    </div>

    <!-- Stats Summary Cards -->
    <div class="stats-grid">
      <div class="stat-card"><div class="stat-val" id="stat-visitors">0</div><div class="stat-lbl">Total Visitors</div></div>
      <div class="stat-card"><div class="stat-val" id="stat-completed" style="color: var(--green);">0</div><div class="stat-lbl">Completed</div></div>
      <div class="stat-card"><div class="stat-val" id="stat-progress">0</div><div class="stat-lbl">In Progress</div></div>
      <div class="stat-card"><div class="stat-val" id="stat-answers">0</div><div class="stat-lbl">Total Answers</div></div>
    </div>

    <!-- Sessions List -->
    <div class="panel">
      <h2>Prerna's Interactive Sessions</h2>
      <table>
        <thead>
          <tr>
            <th>Session ID</th>
            <th>Started At</th>
            <th>Status</th>
            <th>Answers Given</th>
            <th>Completed At</th>
          </tr>
        </thead>
        <tbody id="sessions-tbody">
          <tr><td colspan="5" style="text-align: center; color: var(--text-muted);">Loading sessions...</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Session Detail Modal -->
  <div id="detail-modal" class="modal" style="display: none;">
    <div class="modal-content">
      <button class="close-btn" id="btn-close-modal">✕</button>
      <h2 id="modal-title" style="color: var(--gold); margin-bottom: 4px;">Session Details</h2>
      <p id="modal-sub" style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 20px;">Detailed Q&A Timeline:</p>
      <div id="qa-container"></div>
    </div>
  </div>

  <script>
    const API_BASE = window.location.origin.includes('localhost') || window.location.origin.includes('127.0.0.1')
      ? 'http://127.0.0.1:8000'
      : '';

    let authToken = sessionStorage.getItem('admin_token');

    const loginSection = document.getElementById('login-section');
    const dashboardSection = document.getElementById('dashboard-section');
    const btnLogin = document.getElementById('btn-login');
    const adminPassInput = document.getElementById('admin-pass');
    const loginError = document.getElementById('login-error');
    const btnLogout = document.getElementById('btn-logout');
    const btnRefresh = document.getElementById('btn-refresh');
    const detailModal = document.getElementById('detail-modal');
    const btnCloseModal = document.getElementById('btn-close-modal');

    async function checkAuthAndLoad() {
      if (authToken) {
        loginSection.style.display = 'none';
        dashboardSection.style.display = 'block';
        loadDashboardData();
      } else {
        loginSection.style.display = 'block';
        dashboardSection.style.display = 'none';
      }
    }

    async function handleLogin() {
      const pass = adminPassInput.value.trim();
      try {
        const res = await fetch(`${API_BASE}/api/admin/login`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ password: pass })
        });
        if (res.ok) {
          const data = await res.json();
          authToken = data.token || 'admin-session-authenticated';
          sessionStorage.setItem('admin_token', authToken);
          loginError.style.display = 'none';
          checkAuthAndLoad();
        } else {
          loginError.style.display = 'block';
        }
      } catch (e) {
        loginError.textContent = "Cannot connect to backend server. Make sure backend is running!";
        loginError.style.display = 'block';
      }
    }

    async function loadDashboardData() {
      try {
        const res = await fetch(`${API_BASE}/api/admin/sessions`, {
          headers: { 'Authorization': `Bearer ${authToken}` }
        });
        if (!res.ok) {
          if (res.status === 401) {
            authToken = null;
            sessionStorage.removeItem('admin_token');
            checkAuthAndLoad();
          }
          return;
        }
        const data = await res.json();

        // Update stats
        document.getElementById('stat-visitors').textContent = data.stats.total_visitors;
        document.getElementById('stat-completed').textContent = data.stats.completed;
        document.getElementById('stat-progress').textContent = data.stats.in_progress;
        document.getElementById('stat-answers').textContent = data.stats.total_answers;

        // Render sessions
        const tbody = document.getElementById('sessions-tbody');
        tbody.innerHTML = '';
        if (data.sessions.length === 0) {
          tbody.innerHTML = '<tr><td colspan="5" style="text-align: center; color: var(--text-muted);">No sessions recorded yet. Waiting for Prerna to open the site!</td></tr>';
          return;
        }

        data.sessions.forEach(s => {
          const tr = document.createElement('tr');
          tr.className = 'clickable-row';
          const startTime = new Date(s.started_at).toLocaleString();
          const completeTime = s.completed_at ? new Date(s.completed_at).toLocaleString() : '—';
          const statusBadge = s.is_completed
            ? '<span class="badge badge-success">Completed ✨</span>'
            : '<span class="badge badge-pending">In Progress ⏳</span>';

          tr.innerHTML = `
            <td><strong>${s.id.substring(0, 12)}...</strong></td>
            <td>${startTime}</td>
            <td>${statusBadge}</td>
            <td><strong>${s.answers_count}</strong> answers</td>
            <td>${completeTime}</td>
          `;
          tr.onclick = () => openSessionDetail(s.id);
          tbody.appendChild(tr);
        });

      } catch (e) {
        console.error(e);
      }
    }

    async function openSessionDetail(sessionId) {
      try {
        const res = await fetch(`${API_BASE}/api/admin/session/${sessionId}`, {
          headers: { 'Authorization': `Bearer ${authToken}` }
        });
        if (!res.ok) return;
        const data = await res.json();

        document.getElementById('modal-title').textContent = `Session: ${sessionId}`;
        document.getElementById('modal-sub').textContent = `Started: ${new Date(data.started_at).toLocaleString()} | Status: ${data.is_completed ? 'Completed' : 'In Progress'}`;

        const container = document.getElementById('qa-container');
        container.innerHTML = '';
        if (data.answers.length === 0) {
          container.innerHTML = '<p style="color: var(--text-muted);">No answers submitted in this session yet.</p>';
        } else {
          data.answers.forEach(a => {
            const card = document.createElement('div');
            card.className = 'qa-card';
            card.innerHTML = `
              <div class="qa-q">${a.question_text}</div>
              <div class="qa-a">"${a.answer}"</div>
              <div class="qa-time">${new Date(a.created_at).toLocaleTimeString()}</div>
            `;
            container.appendChild(card);
          });
        }
        detailModal.style.display = 'flex';
      } catch (e) {
        console.error(e);
      }
    }

    btnLogin.onclick = handleLogin;
    adminPassInput.onkeydown = (e) => { if (e.key === 'Enter') handleLogin(); };
    btnLogout.onclick = () => {
      authToken = null;
      sessionStorage.removeItem('admin_token');
      checkAuthAndLoad();
    };
    btnRefresh.onclick = loadDashboardData;
    btnCloseModal.onclick = () => { detailModal.style.display = 'none'; };
    window.onclick = (e) => { if (e.target === detailModal) detailModal.style.display = 'none'; };

    checkAuthAndLoad();
  </script>
</body>
</html>
"""
    with open(os.path.join(DASHBOARD_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("✓ Generated dashboard/index.html")

def generate_meta_files():
    # 1. .gitignore
    gitignore = """.env
*.db
__pycache__/
*.pyc
node_modules/
.DS_Store
"""
    with open(os.path.join(BASE_DIR, ".gitignore"), "w", encoding="utf-8") as f:
        f.write(gitignore)

    # 2. README.md
    readme = """# 🌸 A Secret Surprise For Prerna (Peda) ✨

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
"""
    with open(os.path.join(BASE_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)
    print("✓ Generated .gitignore and README.md")

if __name__ == '__main__':
    setup_directories()
    generate_index_html()
    generate_style_css()
    generate_script_js()
    generate_backend()
    generate_dashboard()
    generate_meta_files()
    print("\n=======================================================")
    print("🎉 MASTER PROJECT BUILD COMPLETED SUCCESSFULLY!")
    print("=======================================================")




