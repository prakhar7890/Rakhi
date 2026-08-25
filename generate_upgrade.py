# -*- coding: utf-8 -*-
"""
Master Upgraded Generator for Prerna's Raksha Bandhan Surprise Interactive Website
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
    for d in [FRONTEND_DIR, FRONTEND_ASSETS, BACKEND_DIR, DASHBOARD_DIR]:
        os.makedirs(d, exist_ok=True)
    if os.path.exists(ROOT_ASSETS):
        for f in os.listdir(ROOT_ASSETS):
            src = os.path.join(ROOT_ASSETS, f)
            dst = os.path.join(FRONTEND_ASSETS, f)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
    print("[OK] Directories verified and assets synchronized")

def generate_index_html():
    content = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <meta name="theme-color" content="#1B0C15">
  <meta name="description" content="An interactive, cinematic Raksha Bandhan surprise mini-game experience crafted by Prakhar for his sister Prerna (Peda).">
  <title>For Peda • Interactive Rakhi Surprise ✨</title>

  <!-- Google Fonts Preconnect & Styles -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Marck+Script&family=Outfit:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Rozha+One&family=Yatra+One&display=swap" rel="stylesheet">

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

  <!-- Top Minimalist Interactive Story Bar -->
  <header class="top-story-bar" role="banner">
    <div class="top-bar-left">
      <div class="brand-chip" id="brand-badge">
        <span class="brand-icon">🌸</span>
        <span class="brand-text">For Peda</span>
      </div>
      <div class="achievement-pill" id="achievement-counter-badge" title="Trophies Unlocked">
        <span class="ach-trophy-icon">🏆</span>
        <span class="ach-count-text" id="ach-count-display">0/7</span>
      </div>
    </div>

    <!-- 27-Step Progress Indicator -->
    <div class="story-progress-indicator" aria-label="Surprise Story Progress">
      <div class="progress-track">
        <div class="progress-bar-fill" id="progress-bar-fill"></div>
      </div>
      <div class="progress-dots-row" id="progress-dots-row"></div>
    </div>

    <div class="top-controls">
      <button id="sound-toggle" class="control-pill-btn" aria-label="Toggle Sound Effects">
        <span class="sound-icon">🔊</span>
        <span class="sound-label">Sound</span>
      </button>
      <button id="easter-egg-1-btn" class="control-pill-btn warning-pill" title="Do Not Touch">
        <span>🚫 Don't touch</span>
      </button>
    </div>
  </header>

  <!-- Achievement Unlock Notification Container -->
  <div id="achievement-toast-container" class="achievement-toast-container" aria-live="polite"></div>

  <!-- Sibling Reaction Toast Notification Container -->
  <div id="reaction-toast-container" class="reaction-toast-container" aria-live="polite"></div>

  <!-- Audio Element for Finale Rakhi Song -->
  <audio id="rakhi-audio-element" preload="auto">
    <source src="assets/song.mp3" type="audio/mpeg">
  </audio>

  <!-- Main Viewport for Interactive Story Screens -->
  <main class="story-viewport" id="story-viewport">

    <!-- ====================================================================
         SCENE 01: INTERACTIVE WAX SEAL SWIPE & DRAG ENVELOPE
         ==================================================================== -->
    <section class="story-screen active dark-scene" id="scene-1" data-scene="1">
      <div class="screen-box opening-mystery-card">
        <div class="screen-badge glow-badge">
          <span>✨ Chapter 01 • The Beginning</span>
        </div>

        <div class="cinematic-text-stream">
          <h1 class="cinematic-line c-line-1" id="s1-line-1">Wait.</h1>
          <p class="cinematic-line c-line-2" id="s1-line-2">Before you enter this experience...</p>
          <h2 class="cinematic-line c-line-3" id="s1-line-3">You must physically break the wax seal.</h2>
        </div>

        <!-- Interactive Wax Seal Envelope Drag/Swipe Stage -->
        <div class="envelope-drag-stage" id="envelope-drag-stage">
          <div class="interactive-envelope-body" id="interactive-envelope-body">
            <div class="env-front-crease"></div>
            <div class="seal-track" id="seal-track">
              <div class="seal-drag-handle" id="seal-drag-handle" draggable="false">
                <span class="seal-letter">P</span>
                <span class="seal-sparkle">✨</span>
              </div>
              <div class="seal-track-hint">
                <span class="track-arrow">➔</span>
                <span class="track-text">Swipe / Drag Seal to Open</span>
                <span class="track-arrow">➔</span>
              </div>
            </div>
          </div>
          <p class="seal-feedback-hint" id="seal-feedback-hint">Drag the seal all the way to the right!</p>
        </div>

        <div class="s1-reveal-msg" id="s1-reveal-msg" style="display: none;">
          <p>💌 Seal broken! Unfolding your surprise...</p>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 02: SIBLING SECURITY SYSTEM SCANNER
         ==================================================================== -->
    <section class="story-screen dark-scene" id="scene-2" data-scene="2">
      <div class="screen-box futuristic-scanner-card">
        <div class="screen-badge tech-badge">
          <span>🛡️ SIBLING SECURITY CLEARANCE v2.4</span>
        </div>

        <h1 class="scene-title tech-title">Identity Verification</h1>
        <p class="scene-subtitle" style="color: #FCE7F3;">Only the official Gadhi is permitted past this point.</p>

        <form id="form-identity-check" class="auth-form-terminal" autocomplete="off">
          <div class="terminal-input-group">
            <label for="input-user-name" class="terminal-label">SCAN SUBJECT NAME:</label>
            <input type="text" id="input-user-name" class="terminal-input tech-input" placeholder="Type your name here..." required autofocus>
          </div>

          <div class="terminal-input-group" id="age-check-step" style="display: none;">
            <label for="input-user-age-sec" class="terminal-label">OFFICIAL SIBLING AGE:</label>
            <input type="number" id="input-user-age-sec" class="terminal-input tech-input" placeholder="Enter age..." min="1" max="100">
          </div>

          <p class="validation-feedback" id="identity-validation-msg" aria-live="polite"></p>

          <div class="screen-action-wrap" id="identity-btn-wrap">
            <button type="submit" id="btn-verify-identity" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content" id="btn-identity-label">Scan Biometrics</span>
            </button>
          </div>
        </form>

        <div class="scanning-terminal-box" id="scanning-terminal" style="display: none;">
          <div class="scan-laser-line"></div>
          <p class="scan-status-text">⚡ SCANNING DNA & DRAMA LEVELS...</p>
          <div class="scan-progress-bar">
            <div class="scan-bar-fill" id="scan-bar-fill"></div>
          </div>
        </div>

        <div class="identity-card-badge" id="identity-card-badge" style="display: none;">
          <div class="id-header">SIBLING ID VERIFIED ✅</div>
          <div class="id-row"><span>NAME:</span> <strong class="text-green">Prerna Gupta</strong></div>
          <div class="id-row"><span>OFFICIAL TITLE:</span> <strong>Maharani Peda Devi</strong></div>
          <div class="id-row"><span>STATUS:</span> <strong>Permanent Headache</strong></div>
          <div class="id-row"><span>CLEARANCE:</span> <strong class="text-green">AUTHORIZED</strong></div>
          <div class="id-footer">👑 Welcome, Peda.</div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 03: LIGHT THE FESTIVE DIYAS (DARK ROOM INTERACTION)
         ==================================================================== -->
    <section class="story-screen dark-scene festive-dark-room" id="scene-3" data-scene="3">
      <div class="screen-box festive-room-box">
        <div class="screen-badge glow-badge">
          <span>🪔 Chapter 03 • Festive Illumination</span>
        </div>

        <h1 class="festive-room-title">Bhena, pehle thoda roshni kar!</h1>
        <p class="festive-room-subtitle" id="diya-instruction-text">Tap on all 5 unlit diyas scattered in the room to illuminate the surprise.</p>

        <div class="diya-counter-badge" id="diya-counter-badge">
          <span>DIYAS LIT: </span><strong id="diyas-lit-count">0</strong> / 5
        </div>

        <!-- Interactive Dark Festive Scene with 5 Tapable Diyas -->
        <div class="festive-interactive-stage" id="festive-diyas-stage">
          <div class="room-ambient-overlay" id="room-ambient-overlay"></div>
          <div class="room-decorations-layer" id="room-decorations-layer">
            <span class="garland-decor g-1">🌸 🌼 🌸 🌼 🌸</span>
            <span class="garland-decor g-2">🌼 🌸 🌼 🌸 🌼</span>
          </div>

          <!-- 5 Tapable Diyas scattered in room -->
          <button class="interactive-diya-btn" id="diya-1" data-diya="1" style="top: 25%; left: 18%;">
            <span class="diya-flame" id="flame-1">🔥</span>
            <span class="diya-base">🪔</span>
          </button>

          <button class="interactive-diya-btn" id="diya-2" data-diya="2" style="top: 20%; right: 20%;">
            <span class="diya-flame" id="flame-2">🔥</span>
            <span class="diya-base">🪔</span>
          </button>

          <button class="interactive-diya-btn" id="diya-3" data-diya="3" style="top: 60%; left: 12%;">
            <span class="diya-flame" id="flame-3">🔥</span>
            <span class="diya-base">🪔</span>
          </button>

          <button class="interactive-diya-btn" id="diya-4" data-diya="4" style="top: 65%; right: 15%;">
            <span class="diya-flame" id="flame-4">🔥</span>
            <span class="diya-base">🪔</span>
          </button>

          <button class="interactive-diya-btn center-diya" id="diya-5" data-diya="5" style="top: 48%; left: 47%;">
            <span class="diya-flame" id="flame-5">🔥</span>
            <span class="diya-base">🪔</span>
          </button>
        </div>

        <div class="diya-completion-card" id="diya-completion-card" style="display: none;">
          <p class="diya-success-msg">✨ Good job, Gadhi! The festival has officially begun.</p>
          <div class="screen-action-wrap">
            <button id="btn-diya-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Continue to Mystery ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 04: FIND THE HIDDEN RAKHI (EXPLORATION GAME)
         ==================================================================== -->
    <section class="story-screen" id="scene-4" data-scene="4">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🔍 Chapter 04 • Secret Detective</span>
        </div>

        <h1 class="scene-title">Find The Hidden Rakhi!</h1>
        <p class="scene-subtitle">A special golden Rakhi is hidden somewhere in this festive scene. Tap around to find it!</p>

        <!-- Decorative Interactive Search Area -->
        <div class="hidden-search-stage" id="hidden-rakhi-search-stage">
          <div class="search-item-dec" id="search-gift-1" style="top: 20%; left: 15%;" title="Festive Gift Box">🎁</div>
          <div class="search-item-dec" id="search-flower-1" style="top: 15%; right: 25%;" title="Marigold Garland">🌼</div>
          <div class="search-item-dec" id="search-sweet-1" style="top: 68%; left: 22%;" title="Sweet Box">🍬</div>
          <div class="search-item-dec" id="search-photo-1" style="top: 30%; right: 12%;" title="Photo Frame">🖼️</div>
          <div class="search-item-dec" id="search-candle-1" style="top: 72%; right: 30%;" title="Candle">🕯️</div>
          <div class="search-item-dec" id="search-diya-decor" style="top: 45%; left: 8%;" title="Diya">🪔</div>

          <!-- The Hidden Clickable Rakhi (Hidden behind flower) -->
          <div class="hidden-target-rakhi" id="hidden-target-rakhi" title="Secret Rakhi">
            <span class="secret-rakhi-sparkle">✨</span>
            <span class="secret-rakhi-icon">🏵️</span>
          </div>
        </div>

        <div class="rakhi-found-banner" id="rakhi-found-banner" style="display: none;">
          <h2 class="rakhi-found-title">🎉 RAKHI FOUND!</h2>
          <p class="rakhi-found-sub">+100 Bhena Points awarded to Detective Peda!</p>
          <div class="screen-action-wrap">
            <button id="btn-found-rakhi-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Solve Photo Jigsaw ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 05: 9-PIECE PHOTO JIGSAW PUZZLE (REAL PHOTO)
         ==================================================================== -->
    <section class="story-screen" id="scene-5" data-scene="5">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🧩 Chapter 05 • Memory Jigsaw</span>
        </div>

        <h1 class="scene-title">Assemble The Memory</h1>
        <p class="scene-subtitle">Tap two tiles to swap their positions and rebuild this classic photo!</p>

        <!-- 3x3 Puzzle Board -->
        <div class="puzzle-board-container">
          <div class="puzzle-grid-9" id="puzzle-grid-9" aria-label="Photo Jigsaw Puzzle">
            <!-- 9 Puzzle Tiles dynamically generated with assets/prerna-1.jpg -->
          </div>
        </div>

        <div class="puzzle-controls-row">
          <button id="btn-puzzle-hint" class="btn-secondary-pill">💡 Hint / Auto-Solve</button>
          <span class="puzzle-moves-counter" id="puzzle-moves-counter">Moves: 0</span>
        </div>

        <div class="puzzle-solved-card" id="puzzle-solved-card" style="display: none;">
          <div class="solved-camera-flash">📸</div>
          <h2 class="solved-caption-title">Memory Unlocked! ✨</h2>
          <p class="solved-caption-text">"Look at that smile. Even after all the fighting, some moments are pure gold."</p>
          <div class="screen-action-wrap">
            <button id="btn-puzzle-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Scratch Golden Secret ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 06: DIGITAL SCRATCH CARD INTERACTION
         ==================================================================== -->
    <section class="story-screen" id="scene-6" data-scene="6">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>✨ Chapter 06 • Golden Scratch Secret</span>
        </div>

        <h1 class="scene-title">Scratch This, Nautanki!</h1>
        <p class="scene-subtitle">Use your finger or mouse to rub and scratch away the gold foil layer.</p>

        <div class="scratch-card-wrapper" id="scratch-card-wrapper">
          <!-- Hidden Message Underneath -->
          <div class="scratch-hidden-content" id="scratch-hidden-content">
            <div class="scratch-gold-icon">👑</div>
            <h2 class="scratch-revealed-text">"You're one of my favorite people."</h2>
            <p class="scratch-revealed-sub">— Even when you're stealing 80% of the snacks.</p>
          </div>

          <!-- Canvas Scratch Layer -->
          <canvas id="scratch-canvas" class="scratch-canvas" width="400" height="240"></canvas>
        </div>

        <div class="scratch-progress-indicator">
          <span>Foil Cleared: </span><strong id="scratch-percent-display">0%</strong>
        </div>

        <div class="scratch-completed-wrap" id="scratch-completed-wrap" style="display: none;">
          <p class="scratch-success-text">SECRET UNLOCKED ❤️</p>
          <div class="screen-action-wrap">
            <button id="btn-scratch-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Open Memory Cards ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 07: 6 MYSTERY 3D MEMORY FLIP CARDS
         ==================================================================== -->
    <section class="story-screen" id="scene-7" data-scene="7">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🃏 Chapter 07 • Sibling Memory Vault</span>
        </div>

        <h1 class="scene-title">Flip The Mystery Cards</h1>
        <p class="scene-subtitle">Tap each card to reveal what's hidden beneath. Discover all 6 to continue!</p>

        <div class="flip-cards-tracker">
          <span>MEMORIES FOUND: </span><strong id="flip-cards-found-count">0</strong> / 6
        </div>

        <!-- 6 Flip Cards Grid -->
        <div class="flip-cards-grid-6" id="flip-cards-grid-6">
          <div class="flip-card-item" data-card="1">
            <div class="flip-card-inner">
              <div class="flip-card-front"><span>?</span></div>
              <div class="flip-card-back">
                <div class="card-icon">🍟</div>
                <div class="card-text">Food Chor detected in 4K!</div>
              </div>
            </div>
          </div>

          <div class="flip-card-item" data-card="2">
            <div class="flip-card-inner">
              <div class="flip-card-front"><span>?</span></div>
              <div class="flip-card-back">
                <div class="card-icon">🎭</div>
                <div class="card-text">Professional Nautanki Specialist.</div>
              </div>
            </div>
          </div>

          <div class="flip-card-item" data-card="3">
            <div class="flip-card-inner">
              <div class="flip-card-front"><span>?</span></div>
              <div class="flip-card-back">
                <div class="card-icon">📸</div>
                <div class="card-text">One of my favorite childhood memories.</div>
              </div>
            </div>
          </div>

          <div class="flip-card-item" data-card="4">
            <div class="flip-card-inner">
              <div class="flip-card-front"><span>?</span></div>
              <div class="flip-card-back">
                <div class="card-icon">💆‍♂️</div>
                <div class="card-text">Permanent Headache, but mine.</div>
              </div>
            </div>
          </div>

          <div class="flip-card-item" data-card="5">
            <div class="flip-card-inner">
              <div class="flip-card-front"><span>?</span></div>
              <div class="flip-card-back">
                <div class="card-icon">😂</div>
                <div class="card-text">Still can't believe you're my sister.</div>
              </div>
            </div>
          </div>

          <div class="flip-card-item" data-card="6">
            <div class="flip-card-inner">
              <div class="flip-card-front"><span>?</span></div>
              <div class="flip-card-back">
                <div class="card-icon">❤️</div>
                <div class="card-text">Heart of gold behind all the daily drama.</div>
              </div>
            </div>
          </div>
        </div>

        <div class="screen-action-wrap" id="flip-cards-next-wrap" style="display: none;">
          <button id="btn-flip-cards-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">Play Matching Game ➔</span>
          </button>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 08: SIBLING MATCHING GAME (PAIRS)
         ==================================================================== -->
    <section class="story-screen" id="scene-8" data-scene="8">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🎮 Chapter 08 • Sibling Match-Up</span>
        </div>

        <h1 class="scene-title">Match The Sibling Pairs</h1>
        <p class="scene-subtitle">Find the 4 matching sibling word pairs by flipping two cards at a time.</p>

        <div class="match-score-bar">
          <span>PAIRS MATCHED: </span><strong id="match-pairs-count">0</strong> / 4
        </div>

        <!-- 8 Cards Matching Grid -->
        <div class="matching-grid-8" id="matching-grid-8">
          <!-- Dynamically populated and shuffled in script.js -->
        </div>

        <div class="matching-complete-banner" id="matching-complete-banner" style="display: none;">
          <p class="match-success-title">🏆 SIBLING COMPATIBILITY: QUESTIONABLY HIGH</p>
          <div class="screen-action-wrap">
            <button id="btn-matching-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Choose Your Path ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 09: CHOOSE YOUR BRANCHING PATH
         ==================================================================== -->
    <section class="story-screen" id="scene-9" data-scene="9">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🧭 Chapter 09 • The Sibling Dilemma</span>
        </div>

        <h1 class="scene-title">Your Bhai Has ₹500.</h1>
        <p class="scene-subtitle">What is the most scientifically accurate brother move?</p>

        <!-- 4 Branching Interactive Choice Cards -->
        <div class="branching-choices-grid" id="branching-choices-grid">
          <button class="branch-choice-card" data-choice="a">
            <span class="branch-icon">💸</span>
            <strong class="branch-label">A: Give it all to Bhena (Peda)</strong>
            <span class="branch-desc">The fairytale sister wish</span>
          </button>

          <button class="branch-choice-card" data-choice="b">
            <span class="branch-icon">🍕</span>
            <strong class="branch-label">B: Buy secret food for himself</strong>
            <span class="branch-desc">Survival instincts activated</span>
          </button>

          <button class="branch-choice-card" data-choice="c">
            <span class="branch-icon">🤫</span>
            <strong class="branch-label">C: Pretend he forgot his wallet</strong>
            <span class="branch-desc">100% effective defense strategy</span>
          </button>

          <button class="branch-choice-card" data-choice="d">
            <span class="branch-icon">🏃‍♂️</span>
            <strong class="branch-label">D: Run away immediately</strong>
            <span class="branch-desc">Cardio + peace of mind</span>
          </button>
        </div>

        <div class="branch-reaction-box" id="branch-reaction-box" style="display: none;">
          <p class="branch-reaction-text" id="branch-reaction-text"></p>
          <div class="screen-action-wrap">
            <button id="btn-branch-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Continue Decision Quiz ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 10: SIBLING DECISION DRAG QUIZ
         ==================================================================== -->
    <section class="story-screen" id="scene-10" data-scene="10">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🎯 Chapter 10 • Drag The Choice</span>
        </div>

        <h1 class="scene-title">What Would Bhai Order?</h1>
        <p class="scene-subtitle">You just said "I'm not hungry." Drag Bhai's true order onto the plate below!</p>

        <!-- Draggable Objects -->
        <div class="food-drag-sources-row" id="food-drag-sources-row">
          <div class="draggable-food-item" id="drag-pizza" data-food="Pizza" draggable="true">
            <span class="food-emoji">🍕</span>
            <span class="food-name">Extra Large Pizza</span>
          </div>
          <div class="draggable-food-item" id="drag-choc" data-food="Chocolate" draggable="true">
            <span class="food-emoji">🍫</span>
            <span class="food-name">Secret Chocolate</span>
          </div>
          <div class="draggable-food-item" id="drag-burger" data-food="Burger" draggable="true">
            <span class="food-emoji">🍔</span>
            <span class="food-name">Extra Fries & Burger</span>
          </div>
        </div>

        <!-- Decision Dropzone Plate -->
        <div class="decision-dropzone-plate" id="decision-dropzone-plate">
          <div class="plate-inner-ring">
            <span class="plate-placeholder-text">🎯 Drag Your Choice Onto The Plate</span>
          </div>
        </div>

        <div class="decision-reaction-card" id="decision-reaction-card" style="display: none;">
          <h2 class="decision-title" id="decision-title">Correct!</h2>
          <p class="decision-sub" id="decision-sub">"Because 5 minutes later, you will eat half of it anyway."</p>
          <div class="screen-action-wrap">
            <button id="btn-decision-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Build Custom Rakhi ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 11: BUILD YOUR OWN RAKHI (CUSTOMIZER)
         ==================================================================== -->
    <section class="story-screen" id="scene-11" data-scene="11">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🎨 Chapter 11 • Rakhi Workshop</span>
        </div>

        <h1 class="scene-title">Build Your Custom Rakhi</h1>
        <p class="scene-subtitle">Design your official Rakhi thread and centerpiece!</p>

        <!-- Live Rakhi Custom Preview -->
        <div class="rakhi-custom-preview-stage" id="rakhi-custom-preview-stage">
          <div class="custom-thread-line" id="preview-thread"></div>
          <div class="custom-center-element" id="preview-center">🏵️</div>
          <div class="custom-jewel-element" id="preview-jewel">✨</div>
        </div>

        <!-- Customization Options -->
        <div class="rakhi-options-container">
          <!-- Thread Color -->
          <div class="custom-option-group">
            <label class="custom-opt-label">1. Thread Color:</label>
            <div class="color-swatches-row">
              <button class="color-swatch-btn active" data-thread="#E11D48" style="background: #E11D48;" title="Scarlet Red"></button>
              <button class="color-swatch-btn" data-thread="#EC4899" style="background: #EC4899;" title="Rose Pink"></button>
              <button class="color-swatch-btn" data-thread="#F59E0B" style="background: #F59E0B;" title="Royal Gold"></button>
              <button class="color-swatch-btn" data-thread="#8B5CF6" style="background: #8B5CF6;" title="Silk Purple"></button>
            </div>
          </div>

          <!-- Center Motif -->
          <div class="custom-option-group">
            <label class="custom-opt-label">2. Center Motif:</label>
            <div class="motif-buttons-row">
              <button class="motif-btn active" data-motif="🏵️">Traditional</button>
              <button class="motif-btn" data-motif="💖">Heart</button>
              <button class="motif-btn" data-motif="⭐">Star</button>
              <button class="motif-btn" data-motif="🌸">Lotus</button>
            </div>
          </div>

          <!-- Decoration -->
          <div class="custom-option-group">
            <label class="custom-opt-label">3. Accent Charm:</label>
            <div class="motif-buttons-row">
              <button class="charm-btn active" data-charm="✨">Glitter</button>
              <button class="charm-btn" data-charm="💎">Diamond</button>
              <button class="charm-btn" data-charm="🪞">Mirror</button>
              <button class="charm-btn" data-charm="👑">Crown</button>
            </div>
          </div>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-assemble-rakhi" class="btn-grand-gold">
            <span class="btn-shine"></span>
            <span class="btn-content">✨ Assemble My Rakhi ✨</span>
          </button>
          <button id="btn-assembled-next" class="btn-primary-glow" style="display: none;">
            <span class="btn-shine"></span>
            <span class="btn-content">Draw for Bhai ➔</span>
          </button>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 12: DIGITAL DRAWING CANVAS FOR BHAI
         ==================================================================== -->
    <section class="story-screen" id="scene-12" data-scene="12">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🖌️ Chapter 12 • Digital Canvas</span>
        </div>

        <h1 class="scene-title">Draw Something For Bhai</h1>
        <p class="scene-subtitle">Doodle a drawing, write a funny message, or sign your sister autograph!</p>

        <!-- Canvas Drawing Box -->
        <div class="drawing-canvas-wrapper">
          <canvas id="doodle-canvas" class="doodle-canvas" width="480" height="260"></canvas>
        </div>

        <div class="drawing-toolbar">
          <div class="color-palette-mini">
            <button class="brush-color-btn active" data-color="#E11D48" style="background: #E11D48;"></button>
            <button class="brush-color-btn" data-color="#F59E0B" style="background: #F59E0B;"></button>
            <button class="brush-color-btn" data-color="#8B5CF6" style="background: #8B5CF6;"></button>
            <button class="brush-color-btn" data-color="#1B0C15" style="background: #1B0C15;"></button>
          </div>
          <button id="btn-canvas-undo" class="btn-secondary-pill">Undo</button>
          <button id="btn-canvas-clear" class="btn-secondary-pill">Clear</button>
          <button id="btn-canvas-done" class="btn-primary-glow" style="padding: 8px 22px; font-size: 0.9rem;">Done 🎨</button>
        </div>

        <div class="drawing-saved-banner" id="drawing-saved-banner" style="display: none;">
          <p class="drawing-success-text">🎉 Masterpiece detected! Archived in the brother vault.</p>
          <div class="screen-action-wrap">
            <button id="btn-drawing-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Test Heart Tolerance ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 13: HEART TOLERANCE METER (RAPID TAP/HOLD)
         ==================================================================== -->
    <section class="story-screen" id="scene-13" data-scene="13">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>💓 Chapter 13 • Sibling Tolerance Meter</span>
        </div>

        <h1 class="scene-title">Brother Tolerance Gauge</h1>
        <p class="scene-subtitle">Repeatedly tap or hold the heart to measure how much you tolerate your Bhai!</p>

        <div class="heart-gauge-container">
          <div class="giant-beating-heart" id="giant-beating-heart">
            <span class="heart-icon-center">❤️</span>
            <div class="heart-pulse-waves"></div>
          </div>

          <div class="heart-meter-track">
            <div class="heart-meter-fill" id="heart-meter-fill"></div>
          </div>
          <div class="heart-percentage-text" id="heart-percentage-text">Tolerance: 0%</div>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-pump-heart" class="btn-grand-gold">
            <span class="btn-shine"></span>
            <span class="btn-content">💓 TAP / PUMP HEART 💓</span>
          </button>
        </div>

        <div class="heart-maxed-card" id="heart-maxed-card" style="display: none;">
          <h2 class="heart-maxed-title">Tolerance Level: Suspiciously High! 📈</h2>
          <p class="heart-maxed-sub">"Okay, I know you love your brother."</p>
          <div class="screen-action-wrap">
            <button id="btn-heart-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Hold To Reveal ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 14: SIBLING LIE DETECTOR & TRUTH SCANNER
         ==================================================================== -->
    <section class="story-screen dark-scene" id="scene-14" data-scene="14">
      <div class="screen-box glass-card">
        <div class="screen-badge glow-badge">
          <span>⚡ Chapter 14 • Sibling Lie Detector</span>
        </div>

        <h1 class="scene-title" style="color: #FDE68A;">Sibling Truth Scanner</h1>
        <p class="scene-subtitle" style="color: #FCE7F3;">Tap the biometric pad below to scan and analyze the unfiltered truth!</p>

        <!-- Biometric Lie Detector Scanner Stage -->
        <div class="truth-scanner-stage" id="truth-scanner-stage">
          <button class="biometric-scanner-pad" id="btn-scan-truth" aria-label="Tap to Scan Truth">
            <div class="scanner-laser-sweep" id="scanner-laser-sweep"></div>
            <span class="scanner-thumb-icon">🖲️</span>
            <span class="scanner-hint-text">TAP TO SCAN TRUTH</span>
          </button>

          <!-- Live Real-Time Diagnostic Feed -->
          <div class="scanner-live-diagnostic" id="scanner-live-diagnostic" style="display: none;">
            <div class="diagnostic-line" id="diag-1">⚡ Analyzing Nautanki Level... <strong style="color: #FBBF24;">99.8% (Critical)</strong></div>
            <div class="diagnostic-line" id="diag-2" style="opacity: 0;">🍕 Checking Food Theft Records... <strong style="color: #F472B6;">100% GUILTY</strong></div>
            <div class="diagnostic-line" id="diag-3" style="opacity: 0;">👑 Calculating Madam Ji Attitude... <strong style="color: #34D399;">OFF THE CHARTS</strong></div>
          </div>
        </div>

        <div class="hold-revealed-card" id="hold-revealed-card" style="display: none;">
          <div class="truth-verified-badge" style="display: inline-block; background: rgba(245, 158, 11, 0.2); border: 1px solid #F59E0B; color: #FDE68A; padding: 4px 14px; border-radius: 999px; font-size: 0.8rem; font-weight: 800; margin-bottom: 12px;">👑 UNFILTERED TRUTH UNLOCKED</div>
          <p class="hold-revealed-p1">"You're annoying..."</p>
          <p class="hold-revealed-p2">"But you're my favorite annoying person in the whole universe."</p>
          <div class="screen-action-wrap">
            <button id="btn-hold-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Trigger Chaos ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 15: SCREEN SHAKE / RAPID TAP CHAOS
         ==================================================================== -->
    <section class="story-screen" id="scene-15" data-scene="15">
      <div class="screen-box glass-card" id="shake-card-box">
        <div class="screen-badge warning-badge">
          <span>🌪️ Chapter 15 • Sibling Turbulence</span>
        </div>

        <h1 class="scene-title">Shake Things Up!</h1>
        <p class="scene-subtitle">Tap rapidly 8 times to shake the screen and clear the sibling energy!</p>

        <div class="shake-interactive-stage">
          <div class="shake-vortex-icon" id="shake-vortex-icon">💥</div>
          <div class="shake-tap-counter">Taps: <strong id="shake-taps-display">0</strong> / 8</div>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-shake-tap" class="btn-grand-gold">
            <span class="btn-shine"></span>
            <span class="btn-content">⚡ TAP RAPIDLY TO SHAKE ⚡</span>
          </button>
        </div>

        <div class="shake-resolved-card" id="shake-resolved-card" style="display: none;">
          <h2 class="shake-resolved-title">Okay okay, Peda! Enough violence. 😂</h2>
          <p class="shake-resolved-sub">Sibling equilibrium successfully restored.</p>
          <div class="screen-action-wrap">
            <button id="btn-shake-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Search Hidden Objects ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 16: FESTIVE HIDDEN OBJECT HUNT (5 ITEMS)
         ==================================================================== -->
    <section class="story-screen" id="scene-16" data-scene="16">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🕵️‍♀️ Chapter 16 • Festive Hunt</span>
        </div>

        <h1 class="scene-title">Find 5 Festive Treasures</h1>
        <p class="scene-subtitle">Find: 🪔 Diya, 🌸 Flower, 🎁 Gift, 🍬 Peda Sweet, 💖 Love Note.</p>

        <div class="hunt-tracker-bar">
          <span>OBJECTS FOUND: </span><strong id="hunt-found-count">0</strong> / 5
        </div>

        <!-- Interactive 5-Item Hunt Stage -->
        <div class="festive-hunt-board" id="festive-hunt-board">
          <button class="hunt-obj-item" data-hunt="1" style="top: 15%; left: 12%;" title="Diya">🪔</button>
          <button class="hunt-obj-item" data-hunt="2" style="top: 25%; right: 18%;" title="Marigold">🌸</button>
          <button class="hunt-obj-item" data-hunt="3" style="top: 70%; left: 18%;" title="Gift Box">🎁</button>
          <button class="hunt-obj-item" data-hunt="4" style="top: 65%; right: 22%;" title="Peda Sweet">🍬</button>
          <button class="hunt-obj-item" data-hunt="5" style="top: 42%; left: 46%;" title="Love Note">💖</button>
        </div>

        <div class="hunt-completed-card" id="hunt-completed-card" style="display: none;">
          <h2 class="hunt-success-title">🎉 Detective Peda has completed the mission!</h2>
          <div class="screen-action-wrap">
            <button id="btn-hunt-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Pick Your Sweet ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 17: OFFICIAL BHENA SWEET PICKER
         ==================================================================== -->
    <section class="story-screen" id="scene-17" data-scene="17">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🍬 Chapter 17 • The Sweet Truth</span>
        </div>

        <h1 class="scene-title">Choose Your Official Sweet</h1>
        <p class="scene-subtitle">Select your favorite Indian sweet from the royal platter:</p>

        <div class="sweets-platter-grid" id="sweets-platter-grid">
          <button class="sweet-card-btn" data-sweet="Peda">
            <span class="sweet-emoji">🟤</span>
            <strong class="sweet-name">Peda</strong>
          </button>
          <button class="sweet-card-btn" data-sweet="Gulab Jamun">
            <span class="sweet-emoji">🌰</span>
            <strong class="sweet-name">Gulab Jamun</strong>
          </button>
          <button class="sweet-card-btn" data-sweet="Rasgulla">
            <span class="sweet-emoji">⚪</span>
            <strong class="sweet-name">Rasgulla</strong>
          </button>
          <button class="sweet-card-btn" data-sweet="Jalebi">
            <span class="sweet-emoji">🥨</span>
            <strong class="sweet-name">Jalebi</strong>
          </button>
          <button class="sweet-card-btn" data-sweet="Kaju Katli">
            <span class="sweet-emoji">🔷</span>
            <strong class="sweet-name">Kaju Katli</strong>
          </button>
        </div>

        <div class="sweet-verdict-box" id="sweet-verdict-box" style="display: none;">
          <p class="sweet-verdict-p1" id="sweet-verdict-p1"></p>
          <p class="sweet-verdict-p2" id="sweet-verdict-p2">"Incorrect. You're still Peda. 👑"</p>
          <div class="screen-action-wrap">
            <button id="btn-sweet-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Pop The Balloons ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 18: POP THE FLOATING BALLOONS (5 BALLOONS)
         ==================================================================== -->
    <section class="story-screen" id="scene-18" data-scene="18">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🎈 Chapter 18 • Balloon Revelations</span>
        </div>

        <h1 class="scene-title">Pop The Floating Balloons</h1>
        <p class="scene-subtitle">Tap each floating balloon to pop it and reveal a brotherly truth!</p>

        <div class="balloons-popped-tracker">
          <span>BALLOONS POPPED: </span><strong id="balloons-popped-count">0</strong> / 5
        </div>

        <!-- 5 Floating Interactive Balloons -->
        <div class="balloons-floating-arena" id="balloons-floating-arena">
          <div class="floating-balloon-item b-1" data-b="1">
            <span class="balloon-icon">🎈</span>
            <span class="balloon-tag">Truth #1</span>
          </div>
          <div class="floating-balloon-item b-2" data-b="2">
            <span class="balloon-icon">🎈</span>
            <span class="balloon-tag">Truth #2</span>
          </div>
          <div class="floating-balloon-item b-3" data-b="3">
            <span class="balloon-icon">🎈</span>
            <span class="balloon-tag">Truth #3</span>
          </div>
          <div class="floating-balloon-item b-4" data-b="4">
            <span class="balloon-icon">🎈</span>
            <span class="balloon-tag">Truth #4</span>
          </div>
          <div class="floating-balloon-item b-5" data-b="5">
            <span class="balloon-icon">🎈</span>
            <span class="balloon-tag">Truth #5</span>
          </div>
        </div>

        <!-- Live Message Log from Popped Balloons -->
        <div class="balloon-popped-messages-log" id="balloon-popped-messages-log"></div>

        <div class="screen-action-wrap" id="balloons-next-wrap" style="display: none;">
          <button id="btn-balloons-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">Open Photo Album ➔</span>
          </button>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 19: DIGITAL INTERACTIVE PHOTO ALBUM (PAGE-TURN & ZOOM)
         ==================================================================== -->
    <section class="story-screen" id="scene-19" data-scene="19">
      <div class="screen-box glass-card full-photo-album-box">
        <div class="screen-badge">
          <span>📖 Chapter 19 • The Official Photo Album</span>
        </div>

        <h1 class="album-cover-title">"THE CHAOTIC LIFE OF A CERTIFIED PEDA"</h1>
        <p class="scene-subtitle">Turn the pages to relive the memories. Double-tap to zoom or use the magnifying glass!</p>

        <!-- Flip Book Container -->
        <div class="photo-album-book" id="photo-album-book">
          <!-- Page 1 -->
          <div class="album-page active" data-page="1">
            <div class="photo-contain-wrapper">
              <div class="photo-ambient-blur" style="background-image: url('assets/prerna-1.jpg');"></div>
              <div class="photo-frame-pure">
                <img src="assets/prerna-1.jpg" alt="Prerna Memory 1" class="personal-photo" loading="lazy">
              </div>
            </div>
            <div class="album-caption-block">
              <h2 class="album-caption-title handwriting">Chapter 1: Partners in Crime</h2>
              <p class="album-caption-sub">"From childhood mischief to lifelong team."</p>
            </div>
          </div>

          <!-- Page 2 -->
          <div class="album-page" data-page="2" style="display: none;">
            <div class="photo-contain-wrapper">
              <div class="photo-ambient-blur" style="background-image: url('assets/prerna-2.jpg');"></div>
              <div class="photo-frame-pure">
                <img src="assets/prerna-2.jpg" alt="Prerna Memory 2" class="personal-photo" loading="lazy">
              </div>
            </div>
            <div class="album-caption-block">
              <h2 class="album-caption-title handwriting">Chapter 2: Professional Argument Specialist</h2>
              <p class="album-caption-sub">"Can argue about anything, anytime, and win."</p>
            </div>
          </div>

          <!-- Page 3 -->
          <div class="album-page" data-page="3" style="display: none;">
            <div class="photo-contain-wrapper">
              <div class="photo-ambient-blur" style="background-image: url('assets/prerna-3.jpg');"></div>
              <div class="photo-frame-pure">
                <img src="assets/prerna-3.jpg" alt="Prerna Memory 3" class="personal-photo" loading="lazy">
              </div>
            </div>
            <div class="album-caption-block">
              <h2 class="album-caption-title handwriting">Chapter 3: Certified Nautanki</h2>
              <p class="album-caption-sub">"Bollywood needs to take lessons from this drama queen."</p>
            </div>
          </div>

          <!-- Page 4 -->
          <div class="album-page" data-page="4" style="display: none;">
            <div class="photo-contain-wrapper">
              <div class="photo-ambient-blur" style="background-image: url('assets/prerna-4.jpg');"></div>
              <div class="photo-frame-pure">
                <img src="assets/prerna-4.jpg" alt="Prerna Memory 4" class="personal-photo" loading="lazy">
              </div>
            </div>
            <div class="album-caption-block">
              <h2 class="album-caption-title handwriting">Chapter 4: Candid Smiles</h2>
              <p class="album-caption-sub">"The sweetest smile in the family."</p>
            </div>
          </div>

          <!-- Page 5 -->
          <div class="album-page" data-page="5" style="display: none;">
            <div class="photo-contain-wrapper">
              <div class="photo-ambient-blur" style="background-image: url('assets/prerna-5.jpg');"></div>
              <div class="photo-frame-pure">
                <img src="assets/prerna-5.jpg" alt="Prerna Memory 5" class="personal-photo" loading="lazy">
              </div>
            </div>
            <div class="album-caption-block">
              <h2 class="album-caption-title handwriting">Chapter 5: Unforgettable Journeys</h2>
              <p class="album-caption-sub">"Growing up together has been the best adventure."</p>
            </div>
          </div>

          <!-- Page 6 -->
          <div class="album-page" data-page="6" style="display: none;">
            <div class="photo-contain-wrapper">
              <div class="photo-ambient-blur" style="background-image: url('assets/prerna-6.jpg');"></div>
              <div class="photo-frame-pure">
                <img src="assets/prerna-6.jpg" alt="Prerna Memory 6" class="personal-photo" loading="lazy">
              </div>
            </div>
            <div class="album-caption-block">
              <h2 class="album-caption-title handwriting">Chapter 6: Sibling Hug</h2>
              <p class="album-caption-sub">"Always here for you, no matter what."</p>
            </div>
          </div>
        </div>

        <!-- Album Navigation Controls -->
        <div class="album-nav-controls">
          <button id="btn-album-prev" class="btn-secondary-pill">◀ Prev Page</button>
          <span class="album-page-indicator" id="album-page-indicator">Page 1 of 6</span>
          <button id="btn-album-next" class="btn-secondary-pill">Next Page ▶</button>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-album-finish" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">Sibling Cup Scoreboard ➔</span>
          </button>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 20: OFFICIAL SIBLING CUP SCOREBOARD
         ==================================================================== -->
    <section class="story-screen" id="scene-20" data-scene="20">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🏆 Chapter 20 • Championship Match</span>
        </div>

        <h1 class="scene-title">Official Sibling Cup</h1>
        <p class="scene-subtitle">Live referee stats recorded from the household battlefield:</p>

        <div class="scorecard-grid">
          <div class="score-row">
            <span class="score-metric">Dramatic Entrances</span>
            <div class="score-values"><span class="prerna-score" id="cup-drama-pr">98</span> <span class="vs-label">vs</span> <span class="prakhar-score" id="cup-drama-p">12</span></div>
          </div>
          <div class="score-row">
            <span class="score-metric">Stubbornness Level</span>
            <div class="score-values"><span class="prerna-score" id="cup-stub-pr">99</span> <span class="vs-label">vs</span> <span class="prakhar-score" id="cup-stub-p">95</span></div>
          </div>
          <div class="score-row">
            <span class="score-metric">Food Stolen from Bhai</span>
            <div class="score-values"><span class="prerna-score" id="cup-food-pr">89%</span> <span class="vs-label">vs</span> <span class="prakhar-score" id="cup-food-p">11%</span></div>
          </div>
          <div class="score-row highlight-score-row">
            <span class="score-metric">Caring for Each Other</span>
            <div class="score-values"><span class="prerna-score">∞</span> <span class="vs-label">vs</span> <span class="prakhar-score">∞</span></div>
          </div>
        </div>

        <div class="scorecard-verdict-box">
          <h2 class="verdict-title">OFFICIAL WINNER: BOTH 🤝</h2>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-scene-20-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">Spin Nickname Machine ➔</span>
          </button>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 21: SISTER NICKNAME SLOT MACHINE (INTERACTIVE LEVER)
         ==================================================================== -->
    <section class="story-screen" id="scene-21" data-scene="21">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🎰 Chapter 21 • Nickname Generator</span>
        </div>

        <h1 class="scene-title">The Sister Slot Machine</h1>
        <p class="scene-subtitle">Pull the golden lever to generate your official sibling title!</p>

        <!-- Slot Machine Unit with Lever -->
        <div class="slot-machine-unit">
          <div class="slot-machine-stage" id="slot-machine-stage">
            <div class="slot-reel" id="reel-1"><span class="reel-val">MAHARANI</span></div>
            <div class="slot-plus">+</div>
            <div class="slot-reel" id="reel-2"><span class="reel-val">PEDA</span></div>
            <div class="slot-plus">+</div>
            <div class="slot-reel" id="reel-3"><span class="reel-val">DEVI</span></div>
          </div>

          <!-- Physical Lever -->
          <div class="slot-lever-container" id="slot-lever-container">
            <div class="slot-lever-arm" id="slot-lever-arm">
              <div class="slot-lever-knob">🔴</div>
            </div>
          </div>
        </div>

        <div class="slot-spins-left">Spins Left: <strong id="slot-spins-count">3</strong></div>

        <div class="screen-action-wrap">
          <button id="btn-spin-slot" class="btn-grand-gold">
            <span class="btn-shine"></span>
            <span class="btn-content">🎰 PULL LEVER / SPIN 🎰</span>
          </button>
        </div>

        <div class="slot-result-badge" id="slot-result-badge" style="display: none;">
          <h2 class="slot-title handwriting" id="slot-result-title">MAHARANI PEDA DEVI</h2>
          <p class="slot-sub">CEO, Department of Annoying Bhai</p>
          <div class="screen-action-wrap">
            <button id="btn-slot-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Tie Virtual Rakhi ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 22: VIRTUAL RAKHI THREAD TRACING PHYSICS
         ==================================================================== -->
    <section class="story-screen" id="scene-22" data-scene="22">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🏵️ Chapter 22 • The Sacred Thread</span>
        </div>

        <h1 class="scene-title">Tie The Sacred Rakhi</h1>
        <p class="scene-subtitle">Trace your finger or mouse around the circular mandala to tie the sacred thread!</p>

        <!-- Interactive Thread Circular Drag Stage -->
        <div class="rakhi-drag-stage" id="rakhi-drag-stage">
          <div class="rakhi-thread-svg-wrap">
            <svg class="thread-svg" viewBox="0 0 200 200">
              <circle class="thread-path-bg" cx="100" cy="100" r="80"></circle>
              <circle class="thread-path-fill" id="thread-path-fill" cx="100" cy="100" r="80"></circle>
            </svg>
          </div>
          <div class="rakhi-center-mandala" id="rakhi-center-mandala" title="Tap or Trace Rakhi">
            <span>🏵️</span>
          </div>
        </div>

        <div class="rakhi-trace-progress">
          <span>Thread Traced: </span><strong id="thread-traced-percent">0%</strong>
        </div>

        <div class="screen-action-wrap" id="rakhi-tie-btn-wrap">
          <button id="btn-tie-rakhi-action" class="btn-grand-gold">
            <span class="btn-shine"></span>
            <span class="btn-content">✨ Auto-Tie Sacred Rakhi ✨</span>
          </button>
        </div>

        <div class="rakhi-complete-msg" id="rakhi-complete-msg" style="display: none;">
          <div class="thread-connected-badge">BOND SECURED ❤️</div>
          <h2 class="rakhi-quote handwriting">"A thread of love, laughter, and lifelong protection."</h2>
          <div class="screen-action-wrap">
            <button id="btn-rakhi-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">Read Sister Shayari ➔</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 23: INTERACTIVE HINDI SHAYARI (LOTUS TOUCH DOTS)
         ==================================================================== -->
    <section class="story-screen dark-scene" id="scene-23" data-scene="23">
      <div class="screen-box glass-card shayari-card">
        <div class="screen-badge glow-badge">
          <span>📜 Chapter 23 • Sister Shayari</span>
        </div>

        <div class="shayari-lotus-wrap" id="shayari-mandala-egg" title="Tap the Lotus">
          <span>🪷</span>
        </div>

        <p class="scene-subtitle" style="color: #FCE7F3;">Tap on the glowing dots to reveal each line of poetry:</p>

        <!-- Interactive Shayari Dots -->
        <div class="shayari-dots-row">
          <button class="shayari-dot-btn active" data-sline="1">● 1</button>
          <button class="shayari-dot-btn" data-sline="2">● 2</button>
          <button class="shayari-dot-btn" data-sline="3">● 3</button>
          <button class="shayari-dot-btn" data-sline="4">● 4</button>
        </div>

        <div class="shayari-lines-container">
          <p class="shayari-line devanagari-font" id="sh-line-1">"रिश्ते कई मिले इस दुनिया में..."</p>
          <p class="shayari-line devanagari-font" id="sh-line-2">"कुछ वक्त के साथ बदल गए..."</p>
          <p class="shayari-line devanagari-font" id="sh-line-3">"कुछ दूर होकर भी पास रहे..."</p>
          <p class="shayari-line devanagari-font highlight-shayari" id="sh-line-4">"लेकिन बहन का रिश्ता दिल में हमेशा वहीं रहता है।"</p>
        </div>

        <div class="easter-egg-toast" id="easter-egg-2-toast" style="display: none;">
          <span>🎉 SECRET UNLOCKED: +100 Bhena Points!</span>
        </div>

        <div class="screen-action-wrap" id="shayari-action-wrap" style="display: none;">
          <button id="btn-scene-23-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">Open Secret Drawer ➔</span>
          </button>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 24: SECRET WOODEN DRAWER (PHYSICAL DOWNWARD DRAG)
         ==================================================================== -->
    <section class="story-screen" id="scene-24" data-scene="24">
      <div class="screen-box glass-card">
        <div class="screen-badge warning-badge">
          <span>🔒 Chapter 24 • Classified Drawer</span>
        </div>

        <h1 class="scene-title">The Secret Sibling Drawer</h1>
        <p class="scene-subtitle">Drag the wooden drawer handle downwards to unlock classified secrets!</p>

        <!-- Pullable Physical Wooden Drawer -->
        <div class="drawer-cabinet-stage">
          <div class="drawer-box" id="drawer-pullable">
            <div class="drawer-handle-ring" id="drawer-handle-ring">
              <span class="handle-icon">▼</span>
              <span class="handle-text">PULL DOWN</span>
              <span class="handle-icon">▼</span>
            </div>
            <div class="drawer-label">TOP SECRET • PRAKHAR'S VAULT</div>
          </div>

          <div class="drawer-secret-note" id="drawer-secret-note" style="display: none;">
            <h3 class="note-header handwriting">THINGS PRAKHAR WILL NEVER ADMIT:</h3>
            <ul class="note-list handwriting">
              <li>1. You're actually sometimes right.</li>
              <li>2. I do worry about you when you're away.</li>
              <li>3. You're genuinely fun to hang out with.</li>
              <li>4. Life without your bakbak would be terribly boring.</li>
              <li>5. You're one of the most important people in my life.</li>
            </ul>
            <p class="note-footer handwriting">— Don't show Mom. 🤫</p>
          </div>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-open-drawer" class="btn-grand-gold">
            <span class="btn-shine"></span>
            <span class="btn-content">🔓 Pull Down Drawer Handle 🔓</span>
          </button>
          <button id="btn-drawer-next" class="btn-primary-glow" style="display: none;">
            <span class="btn-shine"></span>
            <span class="btn-content">Assemble Message Puzzle ➔</span>
          </button>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 25: EMOTIONAL MESSAGE 4-PIECE MAGNETIC ASSEMBLY PUZZLE
         ==================================================================== -->
    <section class="story-screen" id="scene-25" data-scene="25">
      <div class="screen-box glass-card">
        <div class="screen-badge">
          <span>🧩 Chapter 25 • Heartfelt Words</span>
        </div>

        <h1 class="scene-title">Assemble The Message</h1>
        <p class="scene-subtitle">Tap each message piece in order to assemble Bhai's heartfelt words:</p>

        <!-- 4 Magnetic Message Fragments -->
        <div class="message-puzzle-pieces" id="message-puzzle-pieces">
          <button class="msg-piece-btn" data-piece="1">"You're not just my sister..."</button>
          <button class="msg-piece-btn" data-piece="2">"You're part of my childhood..."</button>
          <button class="msg-piece-btn" data-piece="3">"My happiest memories..."</button>
          <button class="msg-piece-btn" data-piece="4">"And my life. Happy Rakhi, Bhena. ❤️"</button>
        </div>

        <!-- Assembled Message Target Card -->
        <div class="assembled-message-target" id="assembled-message-target">
          <p class="assembled-placeholder">Tap the pieces above in sequence...</p>
        </div>

        <div class="screen-action-wrap" id="msg-puzzle-next-wrap" style="display: none;">
          <button id="btn-msg-puzzle-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">Read Handwritten Letter ➔</span>
          </button>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 26: 3D HANDWRITTEN LETTER & 10-YEAR TIME CAPSULE
         ==================================================================== -->
    <section class="story-screen" id="scene-26" data-scene="26">
      <div class="screen-box glass-card" style="max-width: 680px;">
        <div class="screen-badge">
          <span>💌 Chapter 26 • A Letter From Prakhar</span>
        </div>

        <h1 class="scene-title">A Letter For Prerna</h1>
        <p class="scene-subtitle">Tap the wax seal to slide out the letter:</p>

        <!-- 3D Letter Envelope -->
        <div class="envelope-stage">
          <div class="envelope" id="story-envelope">
            <div class="envelope-back"></div>
            <div class="letter-paper" id="story-letter-paper">
              <div class="letter-stamp-top">🌸</div>
              <h2 class="letter-salutation handwriting">Dear Peda,</h2>
              <div class="letter-content-body handwriting">
                <p>23 years ago, my life became infinitely more chaotic, infinitely louder, and infinitely better.</p>
                <p>We've fought over the TV remote, stolen each other's food, argued over completely pointless things, and pretended to hate each other for 10 minutes at a time.</p>
                <p>No matter how old we get or where life takes us, <strong class="bold-highlight">you will always have your brother standing right beside you.</strong></p>
              </div>
              <div class="letter-sign-off handwriting">
                <p>Always in your corner,</p>
                <p class="sign-name" id="brother-sig">Prakhar ❤️</p>
              </div>

              <!-- Margin Notes -->
              <span class="margin-note m-n-1">Peda forever!</span>
              <span class="margin-note m-n-2">No refunds on this brother.</span>
            </div>
            <div class="env-flap-left"></div>
            <div class="env-flap-right"></div>
            <div class="env-flap-bottom"></div>
            <div class="env-flap-top"></div>
            <div class="env-wax-seal" id="env-wax-seal" title="Break Seal">
              <div class="seal-inner-circle">P</div>
            </div>
          </div>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-open-letter-trigger" class="btn-grand-gold">
            <span class="btn-shine"></span>
            <span class="btn-content">💌 Break Seal & Slide Letter 💌</span>
          </button>
          <button id="btn-scene-26-next" class="btn-primary-glow" style="display: none;">
            <span class="btn-shine"></span>
            <span class="btn-content">Proceed to Grand Finale ➔</span>
          </button>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SCENE 27: FINAL SUSPENSE & GRAND FINALE CELEBRATION
         ==================================================================== -->
    <section class="story-screen" id="scene-27" data-scene="27">
      <div class="screen-box glass-card grand-celebration-card" id="grand-celebration-card">
        <div class="grand-crown-badge">👑 MAHARANI PEDA DEVI'S GRAND CELEBRATION 👑</div>

        <!-- Sibling Bond Score Gauge -->
        <div class="sibling-bond-score-box">
          <span class="bond-score-label">SIBLING BOND SCORE:</span>
          <span class="bond-score-val" id="bond-score-val">98%</span>
          <p class="bond-score-sub">"Only 2% missing probably because you still owe me food. 🍕"</p>
        </div>

        <!-- Custom Audio Player Widget -->
        <div class="music-player-widget">
          <div class="music-info-row">
            <span class="music-note-icon">♫</span>
            <span class="music-title-text" id="music-status-text">Playing: Ek Hazaaron Mein Meri Behna Hai</span>
          </div>
          <div class="music-controls-row">
            <button id="btn-audio-play-pause" class="player-btn" title="Play / Pause">❚❚</button>
            <input type="range" id="audio-volume-slider" class="volume-slider" min="0" max="1" step="0.05" value="0.85" title="Volume">
            <button id="btn-audio-mute" class="player-btn" title="Mute">🔊</button>
          </div>
        </div>

        <!-- 100% UNTOUCHED, UNCONTAINED & FULL PERSONAL TOGETHER PHOTO -->
        <div class="photo-contain-wrapper gold-border-frame" id="together-photo-wrapper">
          <div class="photo-ambient-blur" style="background-image: url('assets/prerna-together.jpg');"></div>
          <div class="photo-frame-pure">
            <img src="assets/prerna-together.jpg" alt="Prerna & Prakhar Together" id="together-photo-img" class="personal-photo" loading="lazy">
          </div>
        </div>

        <!-- Grand Celebration Headings -->
        <h1 class="grand-festive-title">HAPPY RAKSHA BANDHAN!</h1>
        <h2 class="grand-sister-name handwriting">Prerna (Peda) ❤️</h2>
        <p class="grand-milestone-tag">"23 Years. Countless Memories. One Irreplaceable Sister."</p>

        <p class="grand-emotional-message">"No matter how old we get or where life takes us, you will always be my favorite sister."</p>
        <p class="grand-love-note handwriting">Love you always, Bhena! 🌸</p>
        <p class="grand-sign-text handwriting">— Your annoying brother, Prakhar ✨</p>

        <!-- Interactive Celebration Actions -->
        <div class="grand-actions-bar">
          <button id="btn-cannon-more" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">🎉 Fire Confetti Cannon</span>
          </button>

          <button id="btn-diya-bless" class="btn-grand-gold">
            <span class="btn-shine"></span>
            <span class="btn-content">🪔 Light Festive Diya</span>
          </button>

          <button id="btn-download-keepsake" class="btn-secondary-pill">
            <span>📥 Download Keepsake Card</span>
          </button>
        </div>

        <div class="blessing-toast-box" id="blessing-toast-box" style="display: none;">
          <span class="toast-diya-flame">🪔</span>
          <span class="toast-text handwriting">"May your year be filled with happiness, success, good food, and 0 arguments with Bhai!"</span>
        </div>

        <!-- Easter Egg Toasts -->
        <div class="easter-egg-toast" id="easter-egg-1-toast" style="display: none;">
          <span>🎉 "I literally told you not to touch it! +10 Sibling Chaos Points!"</span>
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
            <span>↺ Relive the entire interactive story from the beginning</span>
          </button>
        </div>
      </div>
    </section>

  </main>

  <!-- Transparent Privacy Notice -->
  <footer class="privacy-notice-bar" aria-label="Privacy Note">
    <p>Your answers & milestone achievements in this interactive surprise are saved so your brother can see them later ❤️</p>
  </footer>

  <!-- Script -->
  <script src="script.js"></script>
</body>
</html>
"""
    for path in [os.path.join(FRONTEND_DIR, "index.html"), os.path.join(BASE_DIR, "index.html")]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    print("[OK] Generated upgraded index.html in frontend/ and root")

def generate_style_css():
    content = r"""/* ==========================================================================
   RAKHI SURPRISE STORY • UPGRADED 27-SCENE INTERACTIVE CINEMATIC EXPERIENCE
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

  --glass-bg: rgba(255, 255, 255, 0.92);
  --glass-border: rgba(254, 205, 211, 0.65);
  --glass-shadow: 0 20px 50px rgba(136, 19, 55, 0.08), 0 4px 12px rgba(0, 0, 0, 0.03);
  --glass-shadow-hover: 0 26px 60px rgba(136, 19, 55, 0.16);

  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
  --transition-fast: 0.22s cubic-bezier(0.4, 0, 0.2, 1);
}

/* --- 2. Reset & Global Styles --- */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
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

body::before {
  content: '';
  position: fixed;
  inset: 0;
  background: 
    radial-gradient(circle at 15% 20%, rgba(252, 231, 243, 0.7) 0%, transparent 45%),
    radial-gradient(circle at 85% 30%, rgba(254, 243, 199, 0.6) 0%, transparent 50%),
    radial-gradient(circle at 50% 80%, rgba(237, 233, 254, 0.6) 0%, transparent 55%),
    radial-gradient(circle at 80% 85%, rgba(255, 237, 213, 0.55) 0%, transparent 40%);
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
  height: 62px;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 80;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  background: rgba(255, 253, 249, 0.85);
  border-bottom: 1px solid rgba(254, 205, 211, 0.45);
}

.top-bar-left {
  display: flex;
  align-items: center;
  gap: 8px;
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

.achievement-pill {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  background: #FEF3C7;
  border: 1px solid #F59E0B;
  padding: 5px 10px;
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 800;
  color: #B45309;
}

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
  height: 4px;
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

/* --- 5. Achievement & Reaction Toast System --- */
.achievement-toast-container, .reaction-toast-container {
  position: fixed;
  top: 72px;
  right: 20px;
  z-index: 120;
  display: flex;
  flex-direction: column;
  gap: 10px;
  pointer-events: none;
}

.achievement-toast {
  background: rgba(18, 7, 14, 0.95);
  border: 2px solid #F59E0B;
  border-radius: 16px;
  padding: 12px 18px;
  color: #FFFFFF;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), 0 0 20px rgba(245, 158, 11, 0.35);
  display: flex;
  align-items: center;
  gap: 12px;
  max-width: 320px;
  animation: toast-slide-in 0.5s var(--ease-spring) forwards;
}

.achievement-toast .ach-icon { font-size: 1.8rem; }
.achievement-toast .ach-title { font-size: 0.75rem; font-weight: 800; color: #F59E0B; text-transform: uppercase; }
.achievement-toast .ach-name { font-size: 0.95rem; font-weight: 700; color: #FFFFFF; }

.reaction-toast {
  background: #FFFFFF;
  border: 1.5px solid var(--color-pink-deep);
  border-radius: 999px;
  padding: 10px 20px;
  color: var(--color-rose-dark);
  font-weight: 700;
  font-size: 0.92rem;
  box-shadow: 0 8px 25px rgba(225, 29, 72, 0.2);
  animation: toast-slide-in 0.4s var(--ease-spring) forwards;
}

@keyframes toast-slide-in {
  from { opacity: 0; transform: translateX(50px) scale(0.9); }
  to { opacity: 1; transform: translateX(0) scale(1); }
}

/* --- 6. Main Story Viewport & Screens Architecture --- */
.story-viewport {
  position: relative;
  z-index: 10;
  width: 100%;
  min-height: 100vh;
  padding-top: 70px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-bottom: 40px;
}

.story-screen {
  display: none;
  opacity: 0;
  width: 100%;
  min-height: calc(100vh - 110px);
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

/* --- 7. Reusable Card & Header Styles --- */
.screen-box {
  width: min(100%, 740px);
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
  padding: clamp(24px, 5vw, 40px) clamp(16px, 4vw, 32px);
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
  margin-bottom: 16px;
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

.scene-title {
  font-size: clamp(1.8rem, 5vw, 2.5rem);
  font-weight: 700;
  color: var(--color-rose-dark);
  margin-bottom: 6px;
  line-height: 1.25;
}

.dark-scene .scene-title {
  color: #FDE68A;
}

.scene-subtitle {
  font-size: 0.98rem;
  color: var(--color-text-muted);
  margin-bottom: 20px;
  font-weight: 500;
}

.handwriting { font-family: var(--font-handwriting); }
.devanagari-font { font-family: var(--font-devanagari); }

/* --- 8. Buttons Design System --- */
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
  font-size: 1.1rem;
  font-weight: 700;
  padding: 15px 36px;
  border-radius: 999px;
  border: 2px solid #FDE68A;
  cursor: pointer;
  box-shadow: 0 15px 35px rgba(217, 119, 6, 0.4), 0 0 25px rgba(251, 191, 36, 0.35);
  overflow: hidden;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast);
}

.btn-grand-gold:hover {
  transform: translateY(-2px) scale(1.03);
  box-shadow: 0 20px 45px rgba(217, 119, 6, 0.5);
}

.btn-secondary-pill {
  background: rgba(255, 255, 255, 0.95);
  border: 1px solid rgba(225, 29, 72, 0.2);
  color: var(--color-rose-dark);
  font-family: var(--font-primary);
  font-weight: 600;
  font-size: 0.92rem;
  padding: 10px 20px;
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

.screen-action-wrap {
  margin-top: 24px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
}

/* --- 9. SCENE 01: PHYSICAL WAX SEAL SWIPE/DRAG ENVELOPE --- */
.envelope-drag-stage {
  margin: 30px auto;
  max-width: 440px;
  perspective: 1000px;
}

.interactive-envelope-body {
  position: relative;
  width: 100%;
  height: 220px;
  background: linear-gradient(135deg, #FFE4E6 0%, #FECDD3 100%);
  border: 2px solid rgba(225, 29, 72, 0.3);
  border-radius: 20px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.env-front-crease {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 0;
  border-top: 110px solid #FDA4AF;
  border-left: 220px solid transparent;
  border-right: 220px solid transparent;
  z-index: 1;
}

.seal-track {
  position: relative;
  z-index: 10;
  width: 85%;
  height: 64px;
  background: rgba(18, 7, 14, 0.6);
  border: 2px dashed rgba(245, 158, 11, 0.6);
  border-radius: 999px;
  display: flex;
  align-items: center;
  padding: 4px;
  user-select: none;
  touch-action: none;
}

.seal-track-hint {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  color: #FDE68A;
  font-size: 0.85rem;
  font-weight: 700;
  pointer-events: none;
}

.seal-drag-handle {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: radial-gradient(circle, #E11D48 0%, #9F1239 100%);
  border: 2px solid #FDE68A;
  box-shadow: 0 6px 20px rgba(225, 29, 72, 0.6), 0 0 15px rgba(245, 158, 11, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #FFFFFF;
  font-family: var(--font-handwriting);
  font-size: 1.4rem;
  font-weight: 700;
  cursor: grab;
  position: relative;
  z-index: 15;
  touch-action: none;
}

.seal-drag-handle:active { cursor: grabbing; transform: scale(1.08); }
.seal-feedback-hint { color: #FCE7F3; font-size: 0.85rem; margin-top: 12px; font-style: italic; }

/* --- 10. SCENE 02: SIBLING SECURITY SYSTEM --- */
.futuristic-scanner-card {
  background: rgba(18, 7, 14, 0.95);
  border: 1.5px solid rgba(52, 211, 153, 0.35);
  border-radius: 28px;
  padding: 36px 24px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba(52, 211, 153, 0.15);
}

.terminal-input-group { margin-bottom: 16px; text-align: left; max-width: 440px; margin-left: auto; margin-right: auto; }
.terminal-label { display: block; font-family: monospace; font-size: 0.85rem; color: #34D399; margin-bottom: 6px; }
.tech-input { width: 100%; padding: 12px 16px; border-radius: 12px; background: rgba(15, 23, 42, 0.85); border: 2px solid rgba(52, 211, 153, 0.4); color: #34D399; font-family: monospace; font-size: 1rem; }
.tech-input:focus { outline: none; border-color: #34D399; box-shadow: 0 0 15px rgba(52, 211, 153, 0.35); }

.scanning-terminal-box {
  position: relative;
  background: #0B0409;
  border: 1px solid rgba(52, 211, 153, 0.25);
  border-radius: 14px;
  padding: 18px;
  color: #34D399;
  font-family: monospace;
  font-size: 0.92rem;
  margin: 18px auto;
  max-width: 440px;
  overflow: hidden;
}

.scan-laser-line {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: #34D399;
  box-shadow: 0 0 12px #34D399;
  animation: laser-sweep 1.5s infinite ease-in-out;
}

@keyframes laser-sweep {
  0% { top: 0; }
  50% { top: 100%; }
  100% { top: 0; }
}

.scan-progress-bar { width: 100%; height: 8px; background: rgba(255, 255, 255, 0.12); border-radius: 999px; margin-top: 8px; overflow: hidden; }
.scan-bar-fill { width: 0%; height: 100%; background: #34D399; border-radius: 999px; transition: width 1.2s ease-in-out; }

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
}

.id-header { font-weight: 800; color: #34D399; text-align: center; font-size: 1.1rem; margin-bottom: 12px; }
.id-row { display: flex; justify-content: space-between; padding: 4px 0; color: #E2E8F0; font-size: 0.95rem; }
.text-green { color: #34D399; }
.id-footer { text-align: center; font-size: 1.5rem; color: #FDE68A; margin-top: 14px; }

/* --- 11. SCENE 03: LIGHT THE DIYAS IN DARK ROOM --- */
.festive-dark-room {
  position: relative;
  transition: background 1.2s ease;
}

.festive-dark-room.room-illuminated {
  background: radial-gradient(circle at 50% 50%, #3B1224 0%, #15050F 100%);
}

.diya-counter-badge {
  display: inline-block;
  background: rgba(245, 158, 11, 0.15);
  border: 1px solid #F59E0B;
  color: #FDE68A;
  padding: 4px 16px;
  border-radius: 999px;
  font-size: 0.9rem;
  font-weight: 700;
  margin-bottom: 16px;
}

.festive-interactive-stage {
  position: relative;
  width: min(92vw, 540px);
  height: 280px;
  background: rgba(0, 0, 0, 0.4);
  border: 1.5px solid rgba(245, 158, 11, 0.25);
  border-radius: 24px;
  margin: 0 auto 16px;
  overflow: hidden;
}

.room-decorations-layer {
  position: absolute;
  inset: 0;
  opacity: 0.2;
  transition: opacity 1.2s ease;
  pointer-events: none;
}

.festive-dark-room.room-illuminated .room-decorations-layer { opacity: 1; }
.garland-decor { position: absolute; font-size: 1.4rem; letter-spacing: 4px; }
.g-1 { top: 8px; left: 10px; }
.g-2 { bottom: 8px; right: 10px; }

.interactive-diya-btn {
  position: absolute;
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 2.2rem;
  transition: transform var(--transition-fast);
}

.interactive-diya-btn:hover { transform: scale(1.18); }
.diya-flame { font-size: 1.4rem; opacity: 0; filter: drop-shadow(0 0 12px rgba(245, 158, 11, 0.9)); transition: opacity 0.4s ease, transform 0.4s var(--ease-spring); }
.interactive-diya-btn.lit .diya-flame { opacity: 1; animation: flame-flicker 1.2s infinite alternate; }
.interactive-diya-btn.lit { filter: drop-shadow(0 0 20px rgba(245, 158, 11, 0.8)); }

@keyframes flame-flicker {
  0% { transform: scale(1) translateY(0); }
  50% { transform: scale(1.12) translateY(-2px); }
  100% { transform: scale(0.95) translateY(1px); }
}

.diya-success-msg { font-size: 1.35rem; color: #FDE68A; font-weight: 700; }

/* --- 12. SCENE 04: FIND THE HIDDEN RAKHI --- */
.hidden-search-stage {
  position: relative;
  width: min(92vw, 540px);
  height: 280px;
  background: radial-gradient(circle, #FFFDF9 0%, #FEF3C7 100%);
  border: 2px dashed rgba(225, 29, 72, 0.25);
  border-radius: 24px;
  margin: 16px auto;
  overflow: hidden;
}

.search-item-dec {
  position: absolute;
  font-size: 2.5rem;
  cursor: pointer;
  transition: transform 0.2s var(--ease-spring);
}

.search-item-dec:hover { transform: scale(1.2) rotate(8deg); }

.hidden-target-rakhi {
  position: absolute;
  top: 14%;
  right: 23%;
  z-index: 5;
  font-size: 2.8rem;
  cursor: pointer;
  animation: pulse-subtle 2s infinite ease-in-out;
}

.secret-rakhi-sparkle { position: absolute; top: -6px; right: -6px; font-size: 1.2rem; }
.rakhi-found-title { font-size: 2.2rem; color: var(--color-pink-deep); }
.rakhi-found-sub { font-size: 1rem; color: var(--color-rose-dark); font-weight: 700; }

/* --- 13. SCENE 05: 9-PIECE PHOTO JIGSAW PUZZLE --- */
.puzzle-board-container {
  width: 300px;
  height: 300px;
  margin: 16px auto;
  perspective: 800px;
}

.puzzle-grid-9 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  width: 100%;
  height: 100%;
  gap: 3px;
  background: #1B0C15;
  padding: 3px;
  border-radius: 16px;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.puzzle-tile {
  position: relative;
  width: 100%;
  height: 100%;
  background-image: url('assets/prerna-1.jpg');
  background-size: 300px 300px;
  background-repeat: no-repeat;
  border-radius: 6px;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.puzzle-tile:hover { transform: scale(1.04); z-index: 5; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }
.puzzle-tile.selected { border: 2.5px solid #F59E0B; transform: scale(1.08); z-index: 10; box-shadow: 0 0 15px #F59E0B; }

.puzzle-controls-row { display: flex; align-items: center; justify-content: center; gap: 16px; margin-top: 12px; }
.puzzle-moves-counter { font-size: 0.9rem; font-weight: 700; color: var(--color-text-muted); }
.solved-camera-flash { font-size: 2.8rem; }
.solved-caption-title { font-size: 1.8rem; color: var(--color-rose-dark); }
.solved-caption-text { font-size: 1.1rem; color: var(--color-text-muted); font-style: italic; }

/* --- 14. SCENE 06: DIGITAL SCRATCH CARD --- */
.scratch-card-wrapper {
  position: relative;
  width: min(92vw, 400px);
  height: 240px;
  margin: 16px auto;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.scratch-hidden-content {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);
  border: 2px solid #F59E0B;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
  text-align: center;
  z-index: 1;
}

.scratch-gold-icon { font-size: 2.5rem; margin-bottom: 8px; }
.scratch-revealed-text { font-size: 1.6rem; color: #881337; font-weight: 700; line-height: 1.3; }
.scratch-revealed-sub { font-size: 0.95rem; color: #B45309; font-weight: 600; margin-top: 4px; }

.scratch-canvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  z-index: 2;
  cursor: crosshair;
  touch-action: none;
}

.scratch-progress-indicator { font-size: 0.9rem; font-weight: 700; color: var(--color-rose-dark); margin-top: 10px; }
.scratch-success-text { font-size: 1.8rem; font-weight: 800; color: var(--color-pink-deep); }

/* --- 15. SCENE 07: 6 3D MEMORY FLIP CARDS --- */
.flip-cards-tracker { font-size: 0.9rem; font-weight: 800; color: var(--color-rose-dark); margin-bottom: 16px; }
.flip-cards-grid-6 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 12px;
  max-width: 520px;
  margin: 0 auto;
}

.flip-card-item {
  height: 140px;
  perspective: 1000px;
  cursor: pointer;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.6s var(--ease-spring);
  transform-style: preserve-3d;
}

.flip-card-item.flipped .flip-card-inner { transform: rotateY(180deg); }

.flip-card-front, .flip-card-back {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 12px;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.06);
}

.flip-card-front {
  background: linear-gradient(135deg, #FFE4E6 0%, #FECDD3 100%);
  border: 1.5px solid rgba(225, 29, 72, 0.25);
  font-family: var(--font-heading);
  font-size: 2.2rem;
  color: var(--color-pink-deep);
  font-weight: 700;
}

.flip-card-back {
  background: #FFFDF9;
  border: 1.5px solid #F59E0B;
  transform: rotateY(180deg);
}

.flip-card-back .card-icon { font-size: 1.8rem; margin-bottom: 4px; }
.flip-card-back .card-text { font-size: 0.8rem; font-weight: 700; color: var(--color-rose-dark); line-height: 1.25; }

/* --- 16. SCENE 08: SIBLING MATCHING GAME --- */
.match-score-bar { font-size: 0.9rem; font-weight: 800; color: var(--color-pink-deep); margin-bottom: 14px; }
.matching-grid-8 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
  max-width: 480px;
  margin: 0 auto;
}

.match-card-tile {
  height: 90px;
  perspective: 800px;
  cursor: pointer;
}

.match-tile-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.4s var(--ease-spring);
  transform-style: preserve-3d;
}

.match-card-tile.flipped .match-tile-inner,
.match-card-tile.matched .match-tile-inner { transform: rotateY(180deg); }

.match-tile-front, .match-tile-back {
  position: absolute;
  inset: 0;
  border-radius: 12px;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6px;
  font-weight: 700;
  font-size: 0.9rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.match-tile-front { background: #FFE4E6; border: 1.5px solid rgba(225, 29, 72, 0.2); color: var(--color-pink-deep); font-size: 1.4rem; }
.match-tile-back { background: #FEF3C7; border: 1.5px solid #F59E0B; transform: rotateY(180deg); color: #881337; text-align: center; }
.match-card-tile.matched .match-tile-back { background: #D1FAE5; border-color: #10B981; color: #065F46; }
.match-success-title { font-size: 1.5rem; font-weight: 800; color: #10B981; }

/* --- 17. SCENE 09 & 10: BRANCHING CHOICES & DECISION DRAG --- */
.branching-choices-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
  max-width: 540px;
  margin: 16px auto;
}

.branch-choice-card {
  background: #FFFFFF;
  border: 1.5px solid rgba(225, 29, 72, 0.18);
  border-radius: 18px;
  padding: 16px 14px;
  cursor: pointer;
  text-align: left;
  transition: all var(--transition-fast);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04);
}

.branch-choice-card:hover { transform: translateY(-3px) scale(1.02); border-color: var(--color-pink-deep); box-shadow: 0 8px 25px rgba(225, 29, 72, 0.15); }
.branch-icon { font-size: 1.8rem; margin-bottom: 6px; display: block; }
.branch-label { font-size: 0.95rem; color: var(--color-rose-dark); display: block; margin-bottom: 2px; }
.branch-desc { font-size: 0.78rem; color: var(--color-text-muted); }
.branch-reaction-text { font-size: 1.35rem; font-weight: 700; color: var(--color-pink-deep); margin-top: 14px; }

.food-drag-sources-row { display: flex; justify-content: center; gap: 12px; margin: 16px 0; flex-wrap: wrap; }
.draggable-food-item {
  background: #FFFFFF;
  border: 1.5px solid #F59E0B;
  border-radius: 14px;
  padding: 10px 14px;
  cursor: grab;
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 700;
  font-size: 0.9rem;
  color: var(--color-rose-dark);
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  touch-action: none;
}

.draggable-food-item:active { cursor: grabbing; transform: scale(1.08); }
.decision-dropzone-plate {
  width: min(90vw, 360px);
  height: 120px;
  background: #FFFDF9;
  border: 2px dashed var(--color-pink-deep);
  border-radius: 20px;
  margin: 16px auto;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 12px;
  transition: all 0.3s ease;
}

.decision-dropzone-plate.drag-over { background: #FCE7F3; border-color: #F59E0B; transform: scale(1.04); }
.plate-placeholder-text { font-size: 0.92rem; font-weight: 700; color: var(--color-text-muted); }
.decision-title { font-size: 1.8rem; color: var(--color-pink-deep); }
.decision-sub { font-size: 1.05rem; color: var(--color-rose-dark); }

/* --- 18. SCENE 11: RAKHI WORKSHOP CUSTOMIZER --- */
.rakhi-custom-preview-stage {
  position: relative;
  width: 240px;
  height: 120px;
  background: #FFF1F2;
  border: 1.5px solid rgba(225, 29, 72, 0.2);
  border-radius: 20px;
  margin: 14px auto;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.custom-thread-line { position: absolute; width: 100%; height: 6px; background: #E11D48; border-radius: 999px; }
.custom-center-element { position: relative; z-index: 2; font-size: 3rem; }
.custom-jewel-element { position: absolute; top: 12px; right: 40px; z-index: 3; font-size: 1.4rem; }

.rakhi-options-container { max-width: 440px; margin: 0 auto; text-align: left; }
.custom-option-group { margin-bottom: 12px; }
.custom-opt-label { font-size: 0.85rem; font-weight: 700; color: var(--color-rose-dark); display: block; margin-bottom: 6px; }
.color-swatches-row, .motif-buttons-row { display: flex; gap: 8px; }
.color-swatch-btn { width: 32px; height: 32px; border-radius: 50%; border: 2px solid #FFFFFF; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.15); }
.color-swatch-btn.active { outline: 2.5px solid #1B0C15; transform: scale(1.15); }
.motif-btn, .charm-btn { background: #FFFFFF; border: 1px solid rgba(225, 29, 72, 0.2); padding: 6px 12px; border-radius: 999px; font-size: 0.82rem; font-weight: 600; cursor: pointer; }
.motif-btn.active, .charm-btn.active { background: var(--color-pink-deep); color: #FFFFFF; border-color: var(--color-pink-deep); }

/* --- 19. SCENE 12: DIGITAL DRAWING CANVAS --- */
.drawing-canvas-wrapper {
  width: min(92vw, 480px);
  height: 260px;
  margin: 0 auto;
  border-radius: 18px;
  overflow: hidden;
  border: 2px solid rgba(225, 29, 72, 0.25);
  background: #FFFFFF;
  box-shadow: 0 10px 30px rgba(0,0,0,0.06);
}

.doodle-canvas { width: 100%; height: 100%; cursor: crosshair; touch-action: none; }
.drawing-toolbar { display: flex; align-items: center; justify-content: center; gap: 10px; margin-top: 12px; flex-wrap: wrap; }
.color-palette-mini { display: flex; gap: 6px; }
.brush-color-btn { width: 26px; height: 26px; border-radius: 50%; border: 2px solid #FFFFFF; cursor: pointer; }
.brush-color-btn.active { transform: scale(1.2); outline: 2px solid #F59E0B; }
.drawing-success-text { font-size: 1.35rem; color: var(--color-pink-deep); font-weight: 700; }

/* --- 20. SCENE 13 & 14: HEART GAUGE & SIBLING TRUTH SCANNER --- */
.heart-gauge-container { margin: 20px auto; max-width: 320px; text-align: center; }
.giant-beating-heart { position: relative; font-size: 5rem; margin-bottom: 12px; display: inline-block; cursor: pointer; }
.heart-meter-track { width: 100%; height: 14px; background: rgba(225, 29, 72, 0.12); border-radius: 999px; overflow: hidden; margin-bottom: 8px; }
.heart-meter-fill { width: 0%; height: 100%; background: linear-gradient(90deg, #F472B6 0%, #E11D48 100%); border-radius: 999px; transition: width 0.15s ease; }
.heart-percentage-text { font-size: 1.1rem; font-weight: 800; color: var(--color-pink-deep); }
.heart-maxed-title { font-size: 1.8rem; color: var(--color-pink-deep); }
.heart-maxed-sub { font-size: 1.05rem; color: var(--color-rose-dark); }

/* Biometric Sibling Truth Scanner */
.truth-scanner-stage {
  margin: 20px auto;
  max-width: 440px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.biometric-scanner-pad {
  position: relative;
  width: 140px;
  height: 140px;
  border-radius: 28px;
  background: radial-gradient(circle, #2D0D1E 0%, #15050F 100%);
  border: 2.5px solid #F59E0B;
  box-shadow: 0 0 25px rgba(245, 158, 11, 0.4), inset 0 0 15px rgba(245, 158, 11, 0.2);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  overflow: hidden;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast);
}

.biometric-scanner-pad:hover {
  transform: scale(1.05);
  box-shadow: 0 0 35px rgba(245, 158, 11, 0.6);
}

.biometric-scanner-pad:active {
  transform: scale(0.96);
}

.scanner-laser-sweep {
  display: none;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: #34D399;
  box-shadow: 0 0 16px #34D399;
  animation: laser-sweep 1.2s infinite ease-in-out;
  z-index: 5;
}

.biometric-scanner-pad.scanning .scanner-laser-sweep {
  display: block;
}

.scanner-thumb-icon {
  font-size: 3rem;
  margin-bottom: 4px;
  animation: pulse-subtle 2s infinite ease-in-out;
}

.scanner-hint-text {
  font-size: 0.72rem;
  font-weight: 800;
  color: #FDE68A;
  letter-spacing: 0.8px;
}

.scanner-live-diagnostic {
  background: rgba(18, 7, 14, 0.95);
  border: 1.5px solid rgba(245, 158, 11, 0.35);
  border-radius: 14px;
  padding: 14px 18px;
  width: 100%;
  text-align: left;
  font-family: monospace;
  font-size: 0.92rem;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
}

.diagnostic-line {
  margin-bottom: 6px;
  color: #E2E8F0;
  transition: opacity 0.4s ease, transform 0.4s ease;
}

.diagnostic-line:last-child {
  margin-bottom: 0;
}

.hold-revealed-p1 { font-size: 1.6rem; color: #FDE68A; font-weight: 700; margin-bottom: 6px; }
.hold-revealed-p2 { font-size: 1.8rem; color: #F472B6; font-weight: 800; }

/* --- 21. SCENE 15, 16 & 17: SHAKE, HUNT & SWEET PICKER --- */
.shake-interactive-stage { margin: 20px auto; text-align: center; }
.shake-vortex-icon { font-size: 4rem; animation: float-ambient 1.5s infinite alternate; }
.shake-tap-counter { font-size: 1.2rem; font-weight: 800; color: var(--color-rose-dark); margin-top: 8px; }
.shake-resolved-title { font-size: 1.8rem; color: var(--color-pink-deep); }
.shake-resolved-sub { font-size: 1.05rem; color: var(--color-rose-dark); }

.hunt-tracker-bar { font-size: 0.9rem; font-weight: 800; color: var(--color-pink-deep); margin-bottom: 12px; }
.festive-hunt-board {
  position: relative;
  width: min(92vw, 500px);
  height: 260px;
  background: radial-gradient(circle, #FFFDF9 0%, #FEF3C7 100%);
  border: 2px dashed rgba(225, 29, 72, 0.2);
  border-radius: 20px;
  margin: 0 auto 14px;
  overflow: hidden;
}
.hunt-obj-item { position: absolute; background: none; border: none; font-size: 2.4rem; cursor: pointer; transition: transform 0.2s var(--ease-spring); }
.hunt-obj-item:hover { transform: scale(1.3) rotate(12deg); }
.hunt-obj-item.found { opacity: 0.3; pointer-events: none; filter: grayscale(1); }
.hunt-success-title { font-size: 1.6rem; color: var(--color-pink-deep); font-weight: 800; }

.sweets-platter-grid { display: flex; justify-content: center; gap: 12px; margin: 20px auto; flex-wrap: wrap; max-width: 480px; }
.sweet-card-btn { background: #FFFFFF; border: 2px solid rgba(225, 29, 72, 0.15); border-radius: 16px; padding: 14px 18px; cursor: pointer; text-align: center; transition: all var(--transition-fast); }
.sweet-card-btn:hover { transform: translateY(-4px) scale(1.05); border-color: var(--color-pink-deep); box-shadow: 0 8px 20px rgba(225, 29, 72, 0.15); }
.sweet-emoji { font-size: 2rem; display: block; margin-bottom: 4px; }
.sweet-name { font-size: 0.95rem; color: var(--color-rose-dark); }
.sweet-verdict-p1 { font-size: 1.4rem; color: var(--color-rose-dark); font-weight: 700; }
.sweet-verdict-p2 { font-size: 2rem; color: var(--color-pink-deep); font-weight: 800; }

/* --- 22. SCENE 18 & 19: BALLOON POPPING & PHOTO ALBUM FLIP BOOK --- */
.balloons-popped-tracker { font-size: 0.9rem; font-weight: 800; color: var(--color-pink-deep); margin-bottom: 12px; }
.balloons-floating-arena {
  position: relative;
  width: min(92vw, 500px);
  height: 220px;
  background: linear-gradient(180deg, #FDF4FF 0%, #FFF1F2 100%);
  border: 1.5px solid rgba(225, 29, 72, 0.2);
  border-radius: 20px;
  margin: 0 auto 12px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: space-around;
}

.floating-balloon-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  animation: float-ambient 2s infinite alternate ease-in-out;
  transition: transform var(--transition-fast);
}

.floating-balloon-item:hover { transform: scale(1.2); }
.floating-balloon-item.popped { display: none; }
.floating-balloon-item .balloon-icon { font-size: 3rem; }
.floating-balloon-item .balloon-tag { font-size: 0.72rem; font-weight: 800; color: var(--color-rose-dark); }

.balloon-popped-messages-log {
  max-width: 480px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 8px;
  text-align: left;
}

.balloon-log-item {
  background: #FFFFFF;
  border-left: 4px solid var(--color-pink-deep);
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 0.92rem;
  font-weight: 600;
  color: var(--color-rose-dark);
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  animation: pop-in 0.3s var(--ease-spring);
}

/* Digital Photo Album (Page-Turn) */
.full-photo-album-box { max-width: 820px; }
.album-cover-title { font-family: var(--font-heading); font-size: clamp(1.6rem, 4vw, 2.2rem); color: var(--color-rose-dark); margin-bottom: 4px; }
.photo-album-book { position: relative; margin: 16px auto; width: 100%; min-height: 480px; }

.photo-contain-wrapper {
  position: relative;
  width: min(90vw, 760px);
  height: min(54vh, 440px);
  margin: 0 auto 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 16px 45px rgba(0, 0, 0, 0.15);
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

.album-caption-title { font-size: 2rem; color: var(--color-rose-dark); }
.album-caption-sub { font-size: 0.95rem; color: var(--color-text-muted); font-weight: 600; }
.album-nav-controls { display: flex; align-items: center; justify-content: center; gap: 16px; margin: 14px 0; }
.album-page-indicator { font-size: 0.88rem; font-weight: 700; color: var(--color-text-light); }

/* --- 23. SCENE 20, 21 & 22: SCOREBOARD, SLOT MACHINE & THREAD TRACING --- */
.scorecard-grid { display: flex; flex-direction: column; gap: 8px; max-width: 460px; margin: 18px auto; }
.score-row { background: #FFFFFF; border: 1.5px solid rgba(225, 29, 72, 0.15); border-radius: 14px; padding: 12px 18px; display: flex; align-items: center; justify-content: space-between; }
.score-metric { font-weight: 700; color: var(--color-rose-dark); }
.score-values { font-weight: 700; display: flex; gap: 6px; }
.prerna-score { color: var(--color-pink-deep); }
.prakhar-score { color: #2563EB; }
.vs-label { color: var(--color-text-light); font-size: 0.8rem; }
.highlight-score-row { border-color: #F59E0B; background: linear-gradient(135deg, #FFFDF9 0%, #FEF3C7 100%); }
.verdict-title { font-size: 1.8rem; color: var(--color-pink-deep); margin-top: 12px; }

.slot-machine-unit { display: flex; align-items: center; justify-content: center; gap: 16px; margin: 20px auto; }
.slot-machine-stage { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; justify-content: center; }
.slot-reel { background: #1B0C15; border: 2px solid #F59E0B; border-radius: 16px; padding: 14px 12px; min-width: 130px; color: #FDE68A; font-weight: 800; font-size: 1.05rem; box-shadow: 0 0 15px rgba(245, 158, 11, 0.25); text-align: center; }
.slot-plus { font-size: 1.3rem; font-weight: 800; color: var(--color-pink-deep); }
.slot-lever-container { height: 100px; display: flex; align-items: flex-start; cursor: pointer; }
.slot-lever-arm { width: 10px; height: 70px; background: #94A3B8; border-radius: 999px; position: relative; transform-origin: bottom center; transition: transform 0.3s ease; }
.slot-lever-knob { position: absolute; top: -14px; left: -10px; font-size: 1.5rem; }
.slot-spins-left { font-size: 0.85rem; font-weight: 700; color: var(--color-text-light); }
.slot-result-badge { background: #FEF3C7; border: 2px solid #F59E0B; border-radius: 20px; padding: 16px; max-width: 440px; margin: 16px auto; }
.slot-title { font-size: 2.2rem; color: #B45309; }
.slot-sub { font-weight: 700; color: var(--color-rose-dark); }

/* Virtual Thread Tracing */
.rakhi-drag-stage { position: relative; width: 200px; height: 200px; margin: 20px auto; display: flex; align-items: center; justify-content: center; }
.rakhi-center-mandala { position: relative; z-index: 5; width: 80px; height: 80px; border-radius: 50%; background: radial-gradient(circle, #F59E0B 0%, #B45309 100%); display: flex; align-items: center; justify-content: center; font-size: 2.8rem; box-shadow: 0 0 25px rgba(245, 158, 11, 0.5); cursor: pointer; }
.rakhi-thread-svg-wrap { position: absolute; inset: 0; pointer-events: none; }
.thread-svg { width: 100%; height: 100%; }
.thread-path-bg { fill: none; stroke: rgba(225, 29, 72, 0.15); stroke-width: 6; }
.thread-path-fill { fill: none; stroke: #E11D48; stroke-width: 6; stroke-dasharray: 502.65; stroke-dashoffset: 502.65; transition: stroke-dashoffset 0.1s linear; }
.rakhi-trace-progress { font-size: 0.88rem; font-weight: 700; color: var(--color-rose-dark); }
.thread-connected-badge { display: inline-block; background: #E11D48; color: #FFFFFF; font-weight: 800; padding: 4px 16px; border-radius: 999px; font-size: 0.85rem; margin-bottom: 8px; }
.rakhi-quote { font-size: 1.45rem; color: var(--color-rose-dark); margin-bottom: 6px; }

/* --- 24. SCENE 23, 24 & 25: SHAYARI, DRAWER & MESSAGE PUZZLE --- */
.shayari-lotus-wrap { width: 64px; height: 64px; border-radius: 50%; background: radial-gradient(circle, #F59E0B 0%, #B45309 100%); margin: 0 auto 16px; display: flex; align-items: center; justify-content: center; font-size: 2rem; box-shadow: 0 0 25px rgba(245, 158, 11, 0.5); cursor: pointer; }
.shayari-dots-row { display: flex; justify-content: center; gap: 10px; margin-bottom: 16px; }
.shayari-dot-btn { background: rgba(255, 255, 255, 0.15); border: 1px solid rgba(245, 158, 11, 0.4); color: #FDE68A; padding: 6px 14px; border-radius: 999px; font-weight: 700; cursor: pointer; }
.shayari-dot-btn.active { background: #F59E0B; color: #1B0C15; }
.shayari-lines-container { display: flex; flex-direction: column; gap: 14px; max-width: 540px; margin: 0 auto; min-height: 160px; }
.shayari-line { font-size: clamp(1.2rem, 3.6vw, 1.5rem); color: #FDE68A; opacity: 0; transform: translateY(10px); transition: all 0.6s ease; }
.shayari-line.revealed { opacity: 1; transform: translateY(0); }
.highlight-shayari { color: #F472B6; font-size: clamp(1.35rem, 4vw, 1.7rem); }

/* Wooden Drawer */
.drawer-cabinet-stage { perspective: 1000px; margin: 18px auto; max-width: 440px; }
.drawer-box { background: #78350F; border: 3px solid #B45309; border-radius: 16px; padding: 24px 20px; cursor: grab; box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15); transition: transform 0.4s var(--ease-spring); touch-action: none; }
.drawer-box:active { cursor: grabbing; }
.drawer-handle-ring { font-size: 1.2rem; color: #FDE68A; font-weight: 800; letter-spacing: 2px; }
.drawer-label { display: inline-block; background: #B91C1C; color: #FFFFFF; font-size: 0.72rem; font-weight: 800; padding: 3px 10px; border-radius: 4px; margin-top: 6px; }
.drawer-secret-note { background: #FFFDF9; border: 1.5px solid rgba(225, 29, 72, 0.15); border-radius: 16px; padding: 20px; margin-top: 14px; text-align: left; box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1); }
.note-header { font-size: 1.35rem; font-weight: 700; color: #BE123C; margin-bottom: 10px; }
.note-list { list-style: none; font-size: 1.2rem; color: #3B1C28; line-height: 1.45; }
.note-footer { font-size: 1.2rem; color: #881337; margin-top: 10px; text-align: right; }

/* Message Puzzle */
.message-puzzle-pieces { display: flex; flex-direction: column; gap: 8px; max-width: 460px; margin: 16px auto; }
.msg-piece-btn { background: #FFFFFF; border: 1.5px solid rgba(225, 29, 72, 0.2); border-radius: 12px; padding: 12px 16px; font-weight: 700; color: var(--color-rose-dark); cursor: pointer; text-align: left; transition: all var(--transition-fast); }
.msg-piece-btn:hover { background: #FFF1F2; border-color: var(--color-pink-deep); transform: translateX(4px); }
.msg-piece-btn.assembled { opacity: 0.4; pointer-events: none; text-decoration: line-through; }
.assembled-message-target { min-height: 120px; background: #FEF3C7; border: 2px dashed #F59E0B; border-radius: 16px; padding: 18px; max-width: 460px; margin: 14px auto; font-family: var(--font-handwriting); font-size: 1.45rem; color: #78350F; line-height: 1.4; text-align: left; }

/* --- 25. SCENE 26 & 27: 3D LETTER & GRAND FINALE --- */
.envelope-stage { perspective: 1200px; width: 100%; max-width: 480px; margin: 10px auto 24px; }
.envelope { position: relative; width: min(100%, 420px); height: 270px; background: #FFF1F2; border-radius: 12px; box-shadow: 0 16px 40px rgba(136, 19, 55, 0.15); margin: 0 auto; cursor: pointer; }
.envelope-back { position: absolute; inset: 0; background: #FFE4E6; border-radius: 12px; }
.letter-paper { position: absolute; top: 10px; left: 6%; width: 88%; min-height: 250px; background: #FFFDF9; border: 1px solid rgba(225, 29, 72, 0.12); border-radius: 8px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08); padding: 22px; text-align: left; z-index: 2; transform: translateY(0); transition: transform 0.8s var(--ease-spring), min-height 0.8s var(--ease-spring); }
.letter-stamp-top { position: absolute; top: 10px; right: 14px; font-size: 1.4rem; }
.letter-salutation { font-size: 1.8rem; color: var(--color-rose-dark); margin-bottom: 8px; }
.letter-content-body { font-size: 1.2rem; line-height: 1.45; color: #3B1C28; margin-bottom: 12px; }
.letter-content-body p { margin-bottom: 8px; }
.bold-highlight { font-weight: 700; color: var(--color-pink-deep); }
.letter-sign-off { font-size: 1.2rem; color: var(--color-rose-dark); }
.sign-name { font-weight: 700; cursor: pointer; display: inline-block; }
.margin-note { position: absolute; background: #FEF3C7; border: 1px dashed #F59E0B; color: #B45309; font-size: 0.95rem; padding: 2px 8px; border-radius: 6px; transform: rotate(-4deg); }
.m-n-1 { top: 28%; right: -12px; }
.m-n-2 { bottom: 15%; right: -8px; }
.env-flap-left { position: absolute; bottom: 0; left: 0; width: 0; height: 0; border-bottom: 270px solid #FECDD3; border-right: 210px solid transparent; border-bottom-left-radius: 12px; z-index: 3; pointer-events: none; }
.env-flap-right { position: absolute; bottom: 0; right: 0; width: 0; height: 0; border-bottom: 270px solid #FDA4AF; border-left: 210px solid transparent; border-bottom-right-radius: 12px; z-index: 3; pointer-events: none; }
.env-flap-bottom { position: absolute; bottom: 0; left: 0; width: 0; height: 0; border-bottom: 150px solid #F472B6; border-left: 210px solid transparent; border-right: 210px solid transparent; border-bottom-left-radius: 12px; border-bottom-right-radius: 12px; z-index: 4; pointer-events: none; opacity: 0.9; }
.env-flap-top { position: absolute; top: 0; left: 0; width: 0; height: 0; border-top: 150px solid #FB7185; border-left: 210px solid transparent; border-right: 210px solid transparent; border-top-left-radius: 12px; border-top-right-radius: 12px; transform-origin: top center; transform: rotateX(0deg); z-index: 5; transition: transform 0.6s ease, z-index 0.6s step-end; }
.env-wax-seal { position: absolute; top: 125px; left: 50%; transform: translate(-50%, -50%); width: 50px; height: 50px; background: radial-gradient(circle, #E11D48 0%, #9F1239 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 6px 16px rgba(159, 18, 57, 0.4); z-index: 6; cursor: pointer; }
.seal-inner-circle { width: 38px; height: 38px; border: 1px dashed rgba(255, 255, 255, 0.5); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: var(--font-handwriting); font-size: 0.95rem; font-weight: 700; color: #FFFFFF; }
.envelope.is-open .env-flap-top { transform: rotateX(180deg); z-index: 1; transition: transform 0.6s ease, z-index 0.1s step-start; }
.envelope.is-open .env-wax-seal { opacity: 0; pointer-events: none; }
.envelope.is-open .letter-paper { transform: translateY(-140px); min-height: 440px; z-index: 10; box-shadow: 0 25px 60px rgba(136, 19, 55, 0.25); }

/* Grand Finale Celebration */
.grand-celebration-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.96) 0%, rgba(254, 243, 199, 0.88) 100%);
  border: 2.5px solid rgba(245, 158, 11, 0.5);
  box-shadow: 0 30px 70px rgba(245, 158, 11, 0.25), 0 0 40px rgba(251, 191, 36, 0.3);
  max-width: 740px;
}

.grand-crown-badge { font-size: 1.1rem; font-weight: 800; color: var(--color-gold-deep); margin-bottom: 12px; }
.sibling-bond-score-box { background: #FEF3C7; border: 1.5px solid #F59E0B; border-radius: 16px; padding: 12px 18px; margin: 0 auto 16px; max-width: 440px; }
.bond-score-label { font-size: 0.82rem; font-weight: 800; color: #B45309; text-transform: uppercase; }
.bond-score-val { font-size: 1.8rem; font-weight: 800; color: #E11D48; margin-left: 8px; }
.bond-score-sub { font-size: 0.85rem; color: #78350F; font-weight: 600; margin-top: 4px; }

.music-player-widget { background: rgba(255, 255, 255, 0.92); border: 1.5px solid rgba(245, 158, 11, 0.35); border-radius: 18px; padding: 12px 18px; margin: 0 auto 18px; max-width: 440px; box-shadow: 0 6px 20px rgba(0, 0, 0, 0.05); }
.music-info-row { display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 6px; font-size: 0.88rem; font-weight: 700; color: var(--color-rose-dark); }
.music-note-icon { font-size: 1.1rem; color: var(--color-pink-deep); animation: float-ambient 2s infinite alternate; }
.music-controls-row { display: flex; align-items: center; justify-content: center; gap: 12px; }
.player-btn { background: var(--color-pink-soft); border: 1px solid rgba(225, 29, 72, 0.2); color: var(--color-rose-dark); width: 34px; height: 34px; border-radius: 50%; cursor: pointer; font-weight: 700; display: flex; align-items: center; justify-content: center; }
.volume-slider { width: 100px; accent-color: var(--color-pink-deep); cursor: pointer; }

.gold-border-frame { border: 3px solid #F59E0B; border-radius: 16px; }
.grand-festive-title { font-size: clamp(2.2rem, 5.5vw, 3.4rem); color: var(--color-rose-dark); line-height: 1.15; margin-top: 14px; margin-bottom: 4px; }
.grand-sister-name { font-size: clamp(2rem, 5vw, 2.8rem); color: var(--color-pink-deep); margin-bottom: 6px; }
.grand-milestone-tag { font-size: clamp(1rem, 2.8vw, 1.25rem); font-weight: 700; color: var(--color-gold-deep); margin-bottom: 6px; }
.grand-emotional-message { font-size: 1rem; color: var(--color-text-muted); font-style: italic; margin-bottom: 6px; }
.grand-love-note { font-size: clamp(1.7rem, 4.5vw, 2.4rem); color: var(--color-pink-deep); margin-bottom: 4px; }
.grand-sign-text { font-size: 1.05rem; color: var(--color-text-muted); margin-bottom: 20px; }
.grand-actions-bar { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-bottom: 16px; }
.blessing-toast-box { background: rgba(255, 255, 255, 0.95); border: 1.5px solid rgba(245, 158, 11, 0.4); border-radius: 16px; padding: 12px 18px; max-width: 460px; margin: 0 auto 12px; }
.toast-diya-flame { font-size: 1.8rem; }
.toast-text { font-size: 1.3rem; font-weight: 700; color: var(--color-rose-dark); }
.easter-egg-toast { background: rgba(255, 255, 255, 0.95); border: 2px solid #F59E0B; color: var(--color-rose-dark); font-weight: 700; padding: 10px 18px; border-radius: 999px; margin: 12px auto 0; display: inline-block; }
.replay-wrap { margin-top: 14px; }
.replay-link-btn { background: none; border: none; color: var(--color-text-light); font-size: 0.9rem; font-weight: 600; cursor: pointer; text-decoration: underline; }

.privacy-notice-bar { position: fixed; bottom: 0; left: 0; right: 0; padding: 6px 16px; background: rgba(255, 253, 249, 0.75); backdrop-filter: blur(8px); text-align: center; font-size: 0.76rem; color: var(--color-text-light); z-index: 70; border-top: 1px solid rgba(225, 29, 72, 0.1); pointer-events: none; }

/* --- 26. Keyframe Animations --- */
@keyframes pop-in { from { opacity: 0; transform: scale(0.9); } to { opacity: 1; transform: scale(1); } }
@keyframes shine-sweep { 0% { left: -100%; } 25%, 100% { left: 140%; } }
@keyframes float-ambient { from { transform: translateY(0); } to { transform: translateY(-8px); } }
@keyframes pulse-subtle { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.1); } }

/* --- 27. Responsive & Accessibility --- */
@media (max-width: 640px) {
  .top-story-bar { padding: 0 12px; height: 56px; }
  .story-viewport { padding-top: 62px; padding-bottom: 40px; }
  .glass-card { border-radius: 22px; padding: 20px 14px; }
  .photo-contain-wrapper { height: 44vh; }
  .envelope { height: 220px; }
  .envelope.is-open .letter-paper { transform: translateY(-90px); min-height: 380px; padding: 16px; }
  .letter-content-body { font-size: 1.05rem; }
  .slot-reel { min-width: 85px; font-size: 0.88rem; padding: 10px 4px; }
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
    print("[OK] Generated upgraded style.css in frontend/ and root")

def generate_script_js():
    content = r"""/**
 * RAKHI SURPRISE STORY • 27-SCENE INTERACTIVE ENGINE (UPGRADED)
 * Dedicated to Prerna Gupta (Peda, Age 23) • Built with love by Prakhar
 */

(function () {
  'use strict';

  // ==========================================================================
  // 0. API CONFIGURATION
  // ==========================================================================
  // In local development (localhost / 127.0.0.1), requests automatically route to
  // http://localhost:8000.
  // In production on Vercel, requests route to Render:
  // https://rakhi-surprise-api.onrender.com
  // ==========================================================================
  const API_CONFIG = {
    BASE_URL: (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1")
      ? "http://localhost:8000"
      : "https://rakhi-surprise-api.onrender.com"
  };

  const TOTAL_SCREENS = 27;
  let currentScreen = 1;
  let isTransitioning = false;

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ==========================================================================
  // 1. SOUND MANAGER (Web Audio API Synthesizer + Zero External Dependencies)
  // ==========================================================================
  const AudioManager = (function () {
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
        osc.frequency.setValueAtTime(420, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(840, ctx.currentTime + 0.08);
        gain.gain.setValueAtTime(0.2, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.08);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.08);
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
          osc.frequency.setValueAtTime(freq, now + i * 0.06);
          gain.gain.setValueAtTime(0, now + i * 0.06);
          gain.gain.linearRampToValueAtTime(0.18, now + i * 0.06 + 0.02);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.06 + 0.4);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + i * 0.06);
          osc.stop(now + i * 0.06 + 0.4);
        });
      } catch (e) {}
    }

    function playBell() {
      if (!isSoundEnabled) return;
      try {
        const ctx = getContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(1174.66, now); // D6
        gain.gain.setValueAtTime(0.22, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.7);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.7);
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
        osc.frequency.setValueAtTime(140, now);
        osc.frequency.exponentialRampToValueAtTime(35, now + 0.09);
        gain.gain.setValueAtTime(0.25, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.09);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.09);
      } catch (e) {}
    }

    function playBalloonPop() {
      if (!isSoundEnabled) return;
      try {
        const ctx = getContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(300, now);
        osc.frequency.exponentialRampToValueAtTime(80, now + 0.06);
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.06);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.06);
      } catch (e) {}
    }

    return { toggleSound, playPop, playChime, playBell, playFanfare, playShutter, playBalloonPop };
  })();

  // ==========================================================================
  // 2. PARTICLE & FIREWORKS CANVAS ENGINE
  // ==========================================================================
  const ParticleManager = (function () {
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
        bgParticles = [];
        for (let i = 0; i < 35; i++) {
          bgParticles.push({
            x: Math.random() * width,
            y: Math.random() * height,
            radius: Math.random() * 2.5 + 1,
            speedY: Math.random() * 0.35 + 0.15,
            opacity: Math.random() * 0.45 + 0.2,
            color: Math.random() > 0.5 ? '#FBBF24' : (Math.random() > 0.5 ? '#F472B6' : '#EDE9FE'),
            angle: Math.random() * Math.PI * 2,
            spin: (Math.random() - 0.5) * 0.02
          });
        }

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

    function createFirework() {
      if (prefersReducedMotion) return;
      const startX = width * (0.2 + Math.random() * 0.6);
      const startY = height;
      fireworksRockets.push({
        x: startX,
        y: startY,
        targetX: width * (0.15 + Math.random() * 0.7),
        targetY: height * (0.15 + Math.random() * 0.4),
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
      if (bgCtx && !prefersReducedMotion) {
        bgCtx.clearRect(0, 0, width, height);
        bgParticles.forEach((p) => {
          p.y += p.speedY;
          p.x += Math.sin(p.angle) * 0.4;
          p.angle += p.spin;
          if (p.y > height + 10) { p.y = -10; p.x = Math.random() * width; }
          bgCtx.save();
          bgCtx.globalAlpha = p.opacity;
          bgCtx.fillStyle = p.color;
          bgCtx.beginPath();
          bgCtx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          bgCtx.fill();
          bgCtx.restore();
        });
      }

      if (cursorCtx && !prefersReducedMotion) {
        cursorCtx.clearRect(0, 0, width, height);
        for (let i = cursorSparkles.length - 1; i >= 0; i--) {
          const sp = cursorSparkles[i];
          sp.x += sp.vx;
          sp.y += sp.vy;
          sp.life -= 0.035;
          if (sp.life <= 0) { cursorSparkles.splice(i, 1); continue; }
          cursorCtx.save();
          cursorCtx.globalAlpha = sp.life;
          cursorCtx.fillStyle = sp.color;
          cursorCtx.beginPath();
          cursorCtx.arc(sp.x, sp.y, sp.size * sp.life, 0, Math.PI * 2);
          cursorCtx.fill();
          cursorCtx.restore();
        }
      }

      if (heartsCtx) {
        heartsCtx.clearRect(0, 0, width, height);
        for (let i = floatingHearts.length - 1; i >= 0; i--) {
          const h = floatingHearts[i];
          h.x += h.vx;
          h.y += h.vy;
          h.opacity -= 0.012;
          if (h.opacity <= 0 || h.y < -30) { floatingHearts.splice(i, 1); continue; }
          heartsCtx.save();
          heartsCtx.globalAlpha = h.opacity;
          heartsCtx.fillStyle = h.color;
          heartsCtx.font = `${h.size}px serif`;
          heartsCtx.fillText('❤️', h.x, h.y);
          heartsCtx.restore();
        }
      }

      if (fireworksCtx && !prefersReducedMotion) {
        fireworksCtx.clearRect(0, 0, width, height);
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
        for (let i = fireworksSparks.length - 1; i >= 0; i--) {
          const s = fireworksSparks[i];
          s.x += s.vx;
          s.y += s.vy;
          s.vy += 0.06;
          s.alpha -= s.decay;
          if (s.alpha <= 0) { fireworksSparks.splice(i, 1); continue; }
          fireworksCtx.save();
          fireworksCtx.globalAlpha = s.alpha;
          fireworksCtx.fillStyle = s.color;
          fireworksCtx.beginPath();
          fireworksCtx.arc(s.x, s.y, 2.2, 0, Math.PI * 2);
          fireworksCtx.fill();
          fireworksCtx.restore();
        }
      }

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
          if (c.life <= 0 || c.y > height + 20) { confettiPieces.splice(i, 1); continue; }
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
  // 3. ACHIEVEMENT MANAGER (7 Hidden Sibling Trophies)
  // ==========================================================================
  const AchievementManager = (function () {
    const unlockedAchievements = new Set();
    const container = document.getElementById('achievement-toast-container');
    const counterDisplay = document.getElementById('ach-count-display');

    const achievementsList = {
      'memory_hunter': { title: 'Memory Hunter', desc: 'Found all 6 flip card memories!' },
      'peda_supreme': { title: 'Peda Supreme', desc: 'Generated royal sister nickname!' },
      'detective_bhena': { title: 'Detective Bhena', desc: 'Found hidden Rakhi & festive items!' },
      'certified_nautanki': { title: 'Certified Nautanki', desc: 'Solved the photo jigsaw puzzle!' },
      'rakhi_master': { title: 'Rakhi Master', desc: 'Customized & tied the sacred Rakhi!' },
      'emotional_damage': { title: 'Emotional Damage', desc: 'Opened secret drawer & letter!' },
      'final_boss': { title: 'Final Boss', desc: 'Completed the entire surprise story!' }
    };

    function unlock(key) {
      if (unlockedAchievements.has(key) || !achievementsList[key]) return;
      unlockedAchievements.add(key);

      if (counterDisplay) {
        counterDisplay.textContent = `${unlockedAchievements.size}/7`;
      }

      AudioManager.playFanfare();
      const ach = achievementsList[key];

      if (container) {
        const toast = document.createElement('div');
        toast.className = 'achievement-toast';
        toast.innerHTML = `
          <div class="ach-icon">🏆</div>
          <div>
            <div class="ach-title">ACHIEVEMENT UNLOCKED</div>
            <div class="ach-name">${ach.title}</div>
          </div>
        `;
        container.appendChild(toast);
        ParticleManager.fireConfetti(window.innerWidth * 0.85, 90, 25);

        setTimeout(() => {
          toast.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          toast.style.opacity = '0';
          toast.style.transform = 'translateX(60px)';
          setTimeout(() => toast.remove(), 400);
        }, 3500);
      }

      AnswerManager.recordMilestone(`achievement_${key}`, ach.title);
    }

    return { unlock, getCount: () => unlockedAchievements.size };
  })();

  // ==========================================================================
  // 4. SIBLING REACTION MANAGER (Randomized Banter Pool)
  // ==========================================================================
  const ReactionManager = (function () {
    const reactions = [
      "Interesting choice, Peda. 😂",
      "Scientists are deeply confused. 🧐",
      "Valid answer, Madam Ji. 💅",
      "Wrong, but confidently wrong. 😇",
      "Classic Gadhi behavior! 🤦‍♂️",
      "Expected. Highly expected.",
      "Mom has been officially notified. 🤫",
      "Brotherhood council approves! 🤝",
      "Suspicious. Very suspicious. 🧐",
      "100% accuracy recorded for once! 🎯"
    ];
    let lastIndex = -1;
    const container = document.getElementById('reaction-toast-container');

    function triggerRandomReaction() {
      let idx;
      do {
        idx = Math.floor(Math.random() * reactions.length);
      } while (idx === lastIndex && reactions.length > 1);
      lastIndex = idx;

      const text = reactions[idx];
      if (container) {
        const toast = document.createElement('div');
        toast.className = 'reaction-toast';
        toast.textContent = text;
        container.appendChild(toast);

        setTimeout(() => {
          toast.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          toast.style.opacity = '0';
          toast.style.transform = 'translateX(40px)';
          setTimeout(() => toast.remove(), 400);
        }, 2800);
      }
    }

    return { triggerRandomReaction };
  })();

  // ==========================================================================
  // 5. ANSWER & MILESTONE MANAGER (FastAPI Backend + Offline Queue)
  // ==========================================================================
  const AnswerManager = (function () {
    const API_BASE = API_CONFIG.BASE_URL;

    let sessionId = sessionStorage.getItem('rakhi_session_id');
    if (!sessionId) {
      sessionId = (typeof crypto !== 'undefined' && crypto.randomUUID)
        ? crypto.randomUUID()
        : 'sess-' + Date.now() + '-' + Math.random().toString(36).substring(2, 9);
      sessionStorage.setItem('rakhi_session_id', sessionId);
    }

    function getOfflineQueue() {
      try {
        const item = localStorage.getItem('rakhi_offline_queue');
        return item ? JSON.parse(item) : [];
      } catch (e) { return []; }
    }

    function saveOfflineQueue(queue) {
      try { localStorage.setItem('rakhi_offline_queue', JSON.stringify(queue)); } catch (e) {}
    }

    async function sendPayload(endpoint, data) {
      if (!API_BASE) return false;
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 6000);
        const res = await fetch(`${API_BASE}${endpoint}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data),
          mode: 'cors',
          signal: controller.signal
        });
        clearTimeout(timeoutId);
        if (!res.ok) {
          const errText = await res.text().catch(() => '');
          console.warn(`API request failed: ${endpoint} (HTTP ${res.status}${errText ? ': ' + errText.substring(0, 100) : ''})`);
          return false;
        }
        return true;
      } catch (e) {
        console.warn(`API request failed: ${endpoint} (${e.name === 'AbortError' ? 'Request timed out' : 'Network/Server unavailable'})`);
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
        const queue = getOfflineQueue();
        if (!queue.some(item => item.type === 'answer' && item.payload.question_id === payload.question_id)) {
          queue.push({ type: 'answer', endpoint: '/api/answer', payload });
          saveOfflineQueue(queue);
        }
      }
    }

    async function recordMilestone(milestoneName) {
      const payload = {
        session_id: sessionId,
        milestone: String(milestoneName)
      };
      const success = await sendPayload('/api/milestone', payload);
      if (!success) {
        const queue = getOfflineQueue();
        if (!queue.some(item => item.type === 'milestone' && item.payload.milestone === payload.milestone)) {
          queue.push({ type: 'milestone', endpoint: '/api/milestone', payload });
          saveOfflineQueue(queue);
        }
      }
    }

    async function recordCompletion() {
      const payload = { session_id: sessionId, completed_at: new Date().toISOString() };
      const success = await sendPayload('/api/complete', payload);
      if (!success) {
        const queue = getOfflineQueue();
        queue.push({ type: 'complete', endpoint: '/api/complete', payload });
        saveOfflineQueue(queue);
      }
    }

    async function retryOfflineQueue() {
      const queue = getOfflineQueue();
      if (queue.length === 0) return;
      const remaining = [];
      for (const item of queue) {
        const ok = await sendPayload(item.endpoint, item.payload);
        if (!ok) remaining.push(item);
      }
      saveOfflineQueue(remaining);
    }

    window.addEventListener('online', retryOfflineQueue);
    setInterval(retryOfflineQueue, 15000);

    return { getSessionId: () => sessionId, recordAnswer, recordMilestone, recordCompletion };
  })();

  // ==========================================================================
  // 6. STORY ROUTER & SCREEN MANAGER
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
      AudioManager.playPop();

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
          targetEl.classList.add(direction === 'next' ? 'slide-in-right' : 'slide-in-left');
          targetEl.style.opacity = '';
          targetEl.style.transform = '';
        }

        currentScreen = targetIndex;
        updateProgress(targetIndex);
        window.location.hash = `scene-${targetIndex}`;
        window.scrollTo({ top: 0, behavior: 'instant' });

        handleSceneActivation(targetIndex);

        setTimeout(() => { isTransitioning = false; }, 350);
      }, 320);
    }

    function handleSceneActivation(index) {
      if (index === 1) startScene1Sequence();
      else if (index === 2) {
        setTimeout(() => {
          const input = document.getElementById('input-user-name');
          if (input) input.focus();
        }, 300);
      } else if (index === 20) startSiblingCupCounters();
      else if (index === 27) {
        triggerGrandCelebration();
        AchievementManager.unlock('final_boss');
        AnswerManager.recordCompletion();
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
  // 7. MINI-GAMES & INTERACTION ENGINES (SCENES 01–27)
  // ==========================================================================

  // --- Scene 01: Physical Wax Seal Swipe / Drag ---
  function startScene1Sequence() {
    const l1 = document.getElementById('s1-line-1');
    const l2 = document.getElementById('s1-line-2');
    const l3 = document.getElementById('s1-line-3');
    const handle = document.getElementById('seal-drag-handle');
    const track = document.getElementById('seal-track');
    const hint = document.getElementById('seal-feedback-hint');
    const revealMsg = document.getElementById('s1-reveal-msg');

    if (l1) l1.style.opacity = '0';
    if (l2) l2.style.opacity = '0';
    if (l3) l3.style.opacity = '0';

    setTimeout(() => { if (l1) { l1.style.transition = 'opacity 0.8s ease'; l1.style.opacity = '1'; } }, 200);
    setTimeout(() => { if (l2) { l2.style.transition = 'opacity 0.8s ease'; l2.style.opacity = '1'; } }, 1200);
    setTimeout(() => { if (l3) { l3.style.transition = 'opacity 0.8s ease'; l3.style.opacity = '1'; } }, 2200);

    let isDragging = false;
    let startX = 0;
    let currentX = 0;
    let isOpened = false;

    function onStart(e) {
      if (isOpened) return;
      isDragging = true;
      startX = e.type.includes('touch') ? e.touches[0].clientX : e.clientX;
    }

    function onMove(e) {
      if (!isDragging || isOpened || !track || !handle) return;
      const clientX = e.type.includes('touch') ? e.touches[0].clientX : e.clientX;
      const maxDrag = track.clientWidth - handle.clientWidth - 8;
      currentX = Math.max(0, Math.min(maxDrag, clientX - startX));
      handle.style.transform = `translateX(${currentX}px)`;

      if (currentX >= maxDrag * 0.85) {
        completeSealOpen();
      }
    }

    function onEnd() {
      if (!isDragging || isOpened || !handle) return;
      isDragging = false;
      if (currentX < 120) {
        handle.style.transition = 'transform 0.3s var(--ease-spring)';
        handle.style.transform = 'translateX(0px)';
        if (hint) hint.textContent = "Arre Peda, itna bhi difficult nahi hai. Drag all the way right! 😂";
        setTimeout(() => { handle.style.transition = ''; }, 300);
      }
    }

    function completeSealOpen() {
      isOpened = true;
      isDragging = false;
      AudioManager.playChime();
      ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.5, 45);
      if (revealMsg) revealMsg.style.display = 'block';
      if (hint) hint.style.display = 'none';

      setTimeout(() => {
        StoryRouter.goToScreen(2, 'next');
      }, 1200);
    }

    if (handle) {
      handle.addEventListener('mousedown', onStart);
      handle.addEventListener('touchstart', onStart, { passive: true });
      window.addEventListener('mousemove', onMove);
      window.addEventListener('touchmove', onMove, { passive: true });
      window.addEventListener('mouseup', onEnd);
      window.addEventListener('touchend', onEnd);
      handle.onclick = completeSealOpen; // Graceful fallback
    }
  }

  // --- Scene 02: Sibling Security System Scanner ---
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
            AudioManager.playPop();
            AnswerManager.recordAnswer('sec_name', 'Identity Name', nameInput.value.trim());
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
          }
        } else {
          const ageVal = ageInput.value.trim();
          if (ageVal === '23') {
            feedback.textContent = '';
            if (btnWrap) btnWrap.style.display = 'none';
            if (terminal) terminal.style.display = 'block';
            AudioManager.playPop();
            AnswerManager.recordAnswer('sec_age', 'Identity Age', ageVal);
            setTimeout(() => { if (barFill) barFill.style.width = '100%'; }, 100);

            setTimeout(() => {
              if (terminal) terminal.style.display = 'none';
              if (idBadge) idBadge.style.display = 'block';
              AudioManager.playChime();
              ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.4, 30);
              setTimeout(() => { StoryRouter.goToScreen(3, 'next'); }, 1800);
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

  // --- Scene 03: Light The Festive Diyas (Dark Room) ---
  let litDiyas = new Set();
  function setupScene3() {
    const diyas = document.querySelectorAll('.interactive-diya-btn');
    const countDisplay = document.getElementById('diyas-lit-count');
    const room = document.getElementById('scene-3');
    const completionCard = document.getElementById('diya-completion-card');
    const btnNext = document.getElementById('btn-diya-next');

    diyas.forEach((diya) => {
      diya.addEventListener('click', function () {
        const id = this.getAttribute('data-diya');
        if (litDiyas.has(id)) return;
        litDiyas.add(id);
        this.classList.add('lit');
        AudioManager.playBell();

        if (countDisplay) countDisplay.textContent = litDiyas.size;
        ParticleManager.fireConfetti(this.offsetLeft + 20, this.offsetTop, 15, ['#F59E0B', '#FBBF24', '#FEF3C7']);

        if (litDiyas.size >= 5) {
          if (room) room.classList.add('room-illuminated');
          AudioManager.playFanfare();
          if (completionCard) completionCard.style.display = 'block';
          ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 50);
          AnswerManager.recordMilestone('diyas_lit', 'Lit all 5 Diyas');
        }
      });
    });

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        StoryRouter.goToScreen(4, 'next');
      });
    }
  }

  // --- Scene 04: Find The Hidden Rakhi ---
  function setupScene4() {
    const target = document.getElementById('hidden-target-rakhi');
    const banner = document.getElementById('rakhi-found-banner');
    const btnNext = document.getElementById('btn-found-rakhi-next');
    let isFound = false;

    if (target) {
      target.addEventListener('click', () => {
        if (isFound) return;
        isFound = true;
        AudioManager.playFanfare();
        ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 45);
        if (banner) banner.style.display = 'block';
        AchievementManager.unlock('detective_bhena');
        AnswerManager.recordMilestone('rakhi_found', 'Found hidden Rakhi');
      });
    }

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        StoryRouter.goToScreen(5, 'next');
      });
    }
  }

  // --- Scene 05: 9-Piece Photo Jigsaw Puzzle ---
  function setupScene5() {
    const grid = document.getElementById('puzzle-grid-9');
    const movesDisplay = document.getElementById('puzzle-moves-counter');
    const hintBtn = document.getElementById('btn-puzzle-hint');
    const solvedCard = document.getElementById('puzzle-solved-card');
    const btnNext = document.getElementById('btn-puzzle-next');

    // 3x3 positions: index 0 to 8
    let tilesState = [4, 0, 7, 2, 1, 5, 8, 3, 6]; // Shuffled initial state
    let selectedTile = null;
    let moves = 0;
    let isSolved = false;

    function renderPuzzle() {
      if (!grid) return;
      grid.innerHTML = '';
      tilesState.forEach((val, pos) => {
        const tile = document.createElement('div');
        tile.className = 'puzzle-tile';
        const row = Math.floor(val / 3);
        const col = val % 3;
        tile.style.backgroundPosition = `-${col * 100}px -${row * 100}px`;
        tile.setAttribute('data-pos', pos);

        tile.onclick = () => {
          if (isSolved) return;
          AudioManager.playPop();
          if (selectedTile === null) {
            selectedTile = pos;
            tile.classList.add('selected');
          } else {
            // Swap tiles
            const temp = tilesState[selectedTile];
            tilesState[selectedTile] = tilesState[pos];
            tilesState[pos] = temp;
            moves++;
            if (movesDisplay) movesDisplay.textContent = `Moves: ${moves}`;
            selectedTile = null;
            renderPuzzle();
            checkSolved();
          }
        };
        grid.appendChild(tile);
      });
    }

    function checkSolved() {
      const solved = tilesState.every((val, pos) => val === pos);
      if (solved && !isSolved) {
        isSolved = true;
        AudioManager.playShutter();
        AudioManager.playFanfare();
        ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 50);
        if (solvedCard) solvedCard.style.display = 'block';
        AchievementManager.unlock('certified_nautanki');
        AnswerManager.recordMilestone('puzzle_solved', 'Solved 9-piece Photo Jigsaw');
      }
    }

    function autoSolve() {
      tilesState = [0, 1, 2, 3, 4, 5, 6, 7, 8];
      renderPuzzle();
      checkSolved();
    }

    if (hintBtn) hintBtn.onclick = autoSolve;
    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(6, 'next');

    renderPuzzle();
  }

  // --- Scene 06: Digital Scratch Card ---
  function setupScene6() {
    const canvas = document.getElementById('scratch-canvas');
    const display = document.getElementById('scratch-percent-display');
    const completeWrap = document.getElementById('scratch-completed-wrap');
    const btnNext = document.getElementById('btn-scratch-next');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let isDrawing = false;
    let clearedCount = 0;
    let isComplete = false;

    // Fill foil
    ctx.fillStyle = '#D97706';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    // Draw pattern
    ctx.fillStyle = '#F59E0B';
    ctx.font = 'bold 20px "Plus Jakarta Sans", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('✨ RUB / SCRATCH HERE ✨', canvas.width / 2, canvas.height / 2);

    function scratch(e) {
      if (!isDrawing || isComplete) return;
      const rect = canvas.getBoundingClientRect();
      const x = (e.type.includes('touch') ? e.touches[0].clientX : e.clientX) - rect.left;
      const y = (e.type.includes('touch') ? e.touches[0].clientY : e.clientY) - rect.top;

      ctx.globalCompositeOperation = 'destination-out';
      ctx.beginPath();
      ctx.arc(x, y, 24, 0, Math.PI * 2);
      ctx.fill();

      clearedCount++;
      if (clearedCount % 8 === 0) {
        AudioManager.playPop();
        const percent = Math.min(100, Math.floor(clearedCount / 3.5));
        if (display) display.textContent = `${percent}%`;

        if (percent >= 60 && !isComplete) {
          isComplete = true;
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          if (display) display.textContent = '100%';
          AudioManager.playChime();
          ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 40);
          if (completeWrap) completeWrap.style.display = 'block';
          AnswerManager.recordMilestone('scratch_revealed', 'Revealed scratch secret');
        }
      }
    }

    canvas.addEventListener('mousedown', () => { isDrawing = true; });
    canvas.addEventListener('touchstart', () => { isDrawing = true; }, { passive: true });
    window.addEventListener('mousemove', scratch);
    window.addEventListener('touchmove', scratch, { passive: true });
    window.addEventListener('mouseup', () => { isDrawing = false; });
    window.addEventListener('touchend', () => { isDrawing = false; });

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(7, 'next');
  }

  // --- Scene 07: 6 3D Memory Flip Cards ---
  let flippedCardCount = 0;
  function setupScene7() {
    const cards = document.querySelectorAll('#flip-cards-grid-6 .flip-card-item');
    const tracker = document.getElementById('flip-cards-found-count');
    const nextWrap = document.getElementById('flip-cards-next-wrap');
    const btnNext = document.getElementById('btn-flip-cards-next');

    cards.forEach((card) => {
      card.addEventListener('click', function () {
        if (this.classList.contains('flipped')) return;
        this.classList.add('flipped');
        flippedCardCount++;
        AudioManager.playPop();
        ReactionManager.triggerRandomReaction();

        if (tracker) tracker.textContent = flippedCardCount;
        ParticleManager.fireConfetti(this.offsetLeft + 40, this.offsetTop, 15);

        if (flippedCardCount >= 6) {
          AudioManager.playChime();
          if (nextWrap) nextWrap.style.display = 'flex';
          AchievementManager.unlock('memory_hunter');
          AnswerManager.recordMilestone('memories_found_all', 'Found all 6 memory cards');
        }
      });
    });

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(8, 'next');
  }

  // --- Scene 08: Sibling Matching Game ---
  function setupScene8() {
    const grid = document.getElementById('matching-grid-8');
    const pairsTracker = document.getElementById('match-pairs-count');
    const banner = document.getElementById('matching-complete-banner');
    const btnNext = document.getElementById('btn-matching-next');

    const cardPairs = [
      { text: 'Peda', matchId: 1 },
      { text: 'Gadhi', matchId: 1 },
      { text: 'Food Chor', matchId: 2 },
      { text: 'Bhai', matchId: 2 },
      { text: 'Nautanki', matchId: 3 },
      { text: 'Drama Queen', matchId: 3 },
      { text: 'Partner', matchId: 4 },
      { text: 'In Crime', matchId: 4 }
    ];

    // Shuffle
    cardPairs.sort(() => Math.random() - 0.5);

    let selectedTiles = [];
    let matchedPairs = 0;

    if (grid) {
      grid.innerHTML = '';
      cardPairs.forEach((item) => {
        const tile = document.createElement('div');
        tile.className = 'match-card-tile';
        tile.innerHTML = `
          <div class="match-tile-inner">
            <div class="match-tile-front">?</div>
            <div class="match-tile-back">${item.text}</div>
          </div>
        `;

        tile.onclick = () => {
          if (tile.classList.contains('flipped') || tile.classList.contains('matched') || selectedTiles.length >= 2) return;
          tile.classList.add('flipped');
          AudioManager.playPop();
          selectedTiles.push({ el: tile, matchId: item.matchId });

          if (selectedTiles.length === 2) {
            if (selectedTiles[0].matchId === selectedTiles[1].matchId) {
              // Match!
              AudioManager.playChime();
              selectedTiles[0].el.classList.add('matched');
              selectedTiles[1].el.classList.add('matched');
              matchedPairs++;
              if (pairsTracker) pairsTracker.textContent = matchedPairs;
              ParticleManager.fireConfetti(tile.offsetLeft + 20, tile.offsetTop, 15);
              selectedTiles = [];

              if (matchedPairs >= 4) {
                AudioManager.playFanfare();
                if (banner) banner.style.display = 'block';
                AnswerManager.recordMilestone('matching_completed', 'Matched all sibling pairs');
              }
            } else {
              // Mismatch
              setTimeout(() => {
                selectedTiles[0].el.classList.remove('flipped');
                selectedTiles[1].el.classList.remove('flipped');
                selectedTiles = [];
              }, 800);
            }
          }
        };

        grid.appendChild(tile);
      });
    }

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(9, 'next');
  }

  // --- Scene 09: Choose Your Branching Path ---
  function setupScene9() {
    const choices = document.querySelectorAll('#branching-choices-grid .branch-choice-card');
    const reactionBox = document.getElementById('branch-reaction-box');
    const reactionText = document.getElementById('branch-reaction-text');
    const btnNext = document.getElementById('btn-branch-next');

    const branchOutcomes = {
      'a': "Nice try! But ₹500 is immediately taxed for brotherly peace & Wi-Fi fees. 😂💸",
      'b': "Survival instincts activated! A secret pizza party has commenced. 🍕🤤",
      'c': "Classic defense strategy: 'Paisa? Konsa paisa?' 100% effective. 🤫",
      'd': "Cardio + peace of mind = Sibling Victory. 🏃‍♂️💨"
    };

    choices.forEach((btn) => {
      btn.addEventListener('click', function () {
        const choice = this.getAttribute('data-choice');
        AudioManager.playPop();
        AnswerManager.recordAnswer('branch_500', 'Bhai has 500 dilemma', choice);
        if (reactionBox && reactionText) {
          reactionText.textContent = branchOutcomes[choice];
          reactionBox.style.display = 'block';
        }
      });
    });

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(10, 'next');
  }

  // --- Scene 10: Sibling Decision Drag Quiz ---
  function setupScene10() {
    const draggables = document.querySelectorAll('.draggable-food-item');
    const dropzone = document.getElementById('decision-dropzone-plate');
    const card = document.getElementById('decision-reaction-card');
    const btnNext = document.getElementById('btn-decision-next');

    draggables.forEach((item) => {
      item.addEventListener('dragstart', (e) => {
        e.dataTransfer.setData('text/plain', item.getAttribute('data-food'));
      });
      // Touch tap fallback
      item.addEventListener('click', () => {
        handleFoodDecision(item.getAttribute('data-food'));
      });
    });

    if (dropzone) {
      dropzone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropzone.classList.add('drag-over');
      });
      dropzone.addEventListener('dragleave', () => {
        dropzone.classList.remove('drag-over');
      });
      dropzone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropzone.classList.remove('drag-over');
        const food = e.dataTransfer.getData('text/plain');
        handleFoodDecision(food);
      });
    }

    function handleFoodDecision(food) {
      AudioManager.playChime();
      ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 30);
      AnswerManager.recordAnswer('food_order_decision', 'Order when not hungry', food);
      if (card) card.style.display = 'block';
    }

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(11, 'next');
  }

  // --- Scene 11: Build Your Own Rakhi (Customizer) ---
  function setupScene11() {
    const threadBtns = document.querySelectorAll('.color-swatch-btn');
    const motifBtns = document.querySelectorAll('.motif-btn');
    const charmBtns = document.querySelectorAll('.charm-btn');
    const previewThread = document.getElementById('preview-thread');
    const previewCenter = document.getElementById('preview-center');
    const previewJewel = document.getElementById('preview-jewel');
    const btnAssemble = document.getElementById('btn-assemble-rakhi');
    const btnNext = document.getElementById('btn-assembled-next');

    let selectedThread = '#E11D48';
    let selectedMotif = '🏵️';
    let selectedCharm = '✨';

    threadBtns.forEach((btn) => {
      btn.onclick = () => {
        threadBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        selectedThread = btn.getAttribute('data-thread');
        if (previewThread) previewThread.style.background = selectedThread;
        AudioManager.playPop();
      };
    });

    motifBtns.forEach((btn) => {
      btn.onclick = () => {
        motifBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        selectedMotif = btn.getAttribute('data-motif');
        if (previewCenter) previewCenter.textContent = selectedMotif;
        AudioManager.playPop();
      };
    });

    charmBtns.forEach((btn) => {
      btn.onclick = () => {
        charmBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        selectedCharm = btn.getAttribute('data-charm');
        if (previewJewel) previewJewel.textContent = selectedCharm;
        AudioManager.playPop();
      };
    });

    if (btnAssemble) {
      btnAssemble.onclick = () => {
        AudioManager.playFanfare();
        ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.4, 45);
        if (btnAssemble) btnAssemble.style.display = 'none';
        if (btnNext) btnNext.style.display = 'inline-flex';
        AchievementManager.unlock('rakhi_master');
        AnswerManager.recordAnswer('custom_rakhi', 'Custom Rakhi Design', `${selectedThread} + ${selectedMotif} + ${selectedCharm}`);
      };
    }

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(12, 'next');
  }

  // --- Scene 12: Digital Drawing Canvas for Bhai ---
  function setupScene12() {
    const canvas = document.getElementById('doodle-canvas');
    const colorBtns = document.querySelectorAll('.brush-color-btn');
    const undoBtn = document.getElementById('btn-canvas-undo');
    const clearBtn = document.getElementById('btn-canvas-clear');
    const doneBtn = document.getElementById('btn-canvas-done');
    const banner = document.getElementById('drawing-saved-banner');
    const btnNext = document.getElementById('btn-drawing-next');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let isDrawing = false;
    let strokeColor = '#E11D48';
    let history = [];

    function saveState() {
      history.push(canvas.toDataURL());
    }

    colorBtns.forEach((btn) => {
      btn.onclick = () => {
        colorBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        strokeColor = btn.getAttribute('data-color');
        AudioManager.playPop();
      };
    });

    function startDraw(e) {
      isDrawing = true;
      saveState();
      draw(e);
    }

    function draw(e) {
      if (!isDrawing) return;
      const rect = canvas.getBoundingClientRect();
      const x = (e.type.includes('touch') ? e.touches[0].clientX : e.clientX) - rect.left;
      const y = (e.type.includes('touch') ? e.touches[0].clientY : e.clientY) - rect.top;

      ctx.lineWidth = 4;
      ctx.lineCap = 'round';
      ctx.strokeStyle = strokeColor;
      ctx.lineTo(x, y);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(x, y);
    }

    function stopDraw() {
      if (!isDrawing) return;
      isDrawing = false;
      ctx.beginPath();
    }

    canvas.addEventListener('mousedown', startDraw);
    canvas.addEventListener('touchstart', startDraw, { passive: true });
    window.addEventListener('mousemove', draw);
    window.addEventListener('touchmove', draw, { passive: true });
    window.addEventListener('mouseup', stopDraw);
    window.addEventListener('touchend', stopDraw);

    if (clearBtn) {
      clearBtn.onclick = () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        history = [];
        AudioManager.playPop();
      };
    }

    if (undoBtn) {
      undoBtn.onclick = () => {
        if (history.length > 0) {
          const img = new Image();
          img.src = history.pop();
          img.onload = () => {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(img, 0, 0);
          };
          AudioManager.playPop();
        }
      };
    }

    if (doneBtn) {
      doneBtn.onclick = () => {
        AudioManager.playChime();
        ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 30);
        if (banner) banner.style.display = 'block';
        AnswerManager.recordMilestone('doodle_drawn', 'Doodled on Canvas');
      };
    }

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(13, 'next');
  }

  // --- Scene 13: Heart Tolerance Meter ---
  let heartPumps = 0;
  function setupScene13() {
    const pumpBtn = document.getElementById('btn-pump-heart');
    const giantHeart = document.getElementById('giant-beating-heart');
    const fillBar = document.getElementById('heart-meter-fill');
    const textDisplay = document.getElementById('heart-percentage-text');
    const maxedCard = document.getElementById('heart-maxed-card');
    const btnNext = document.getElementById('btn-heart-next');

    function pumpHeart() {
      heartPumps++;
      AudioManager.playPop();
      ParticleManager.spawnFloatingHeart();
      const percent = Math.min(100, heartPumps * 10);

      if (fillBar) fillBar.style.width = `${percent}%`;
      if (textDisplay) textDisplay.textContent = `Tolerance: ${percent}%`;

      if (percent >= 100 && maxedCard && maxedCard.style.display !== 'block') {
        AudioManager.playFanfare();
        ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 45);
        maxedCard.style.display = 'block';
        if (pumpBtn) pumpBtn.style.display = 'none';
        AnswerManager.recordMilestone('heart_tolerance_maxed', 'Tolerated brother 100%');
      }
    }

    if (pumpBtn) pumpBtn.onclick = pumpHeart;
    if (giantHeart) giantHeart.onclick = pumpHeart;
    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(14, 'next');
  }

  // --- Scene 14: Sibling Lie Detector & Truth Scanner ---
  function setupScene14() {
    const scanBtn = document.getElementById('btn-scan-truth');
    const diagBox = document.getElementById('scanner-live-diagnostic');
    const diag2 = document.getElementById('diag-2');
    const diag3 = document.getElementById('diag-3');
    const revealedCard = document.getElementById('hold-revealed-card');
    const btnNext = document.getElementById('btn-hold-next');
    let isScanned = false;

    if (scanBtn) {
      scanBtn.onclick = () => {
        if (isScanned) return;
        isScanned = true;
        scanBtn.classList.add('scanning');
        AudioManager.playPop();
        if (diagBox) diagBox.style.display = 'block';

        setTimeout(() => {
          AudioManager.playBell();
          if (diag2) { diag2.style.opacity = '1'; }
        }, 700);

        setTimeout(() => {
          AudioManager.playBell();
          if (diag3) { diag3.style.opacity = '1'; }
        }, 1400);

        setTimeout(() => {
          scanBtn.classList.remove('scanning');
          AudioManager.playFanfare();
          ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 45);
          if (revealedCard) revealedCard.style.display = 'block';
          AnswerManager.recordMilestone('truth_scanned');
        }, 2200);
      };
    }

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(15, 'next');
  }

  // --- Scene 15: Screen Shake / Rapid Tap Chaos ---
  let shakeTaps = 0;
  function setupScene15() {
    const btn = document.getElementById('btn-shake-tap');
    const cardBox = document.getElementById('shake-card-box');
    const display = document.getElementById('shake-taps-display');
    const resolved = document.getElementById('shake-resolved-card');
    const btnNext = document.getElementById('btn-shake-next');

    if (btn) {
      btn.onclick = () => {
        shakeTaps++;
        AudioManager.playPop();
        if (display) display.textContent = Math.min(8, shakeTaps);

        if (cardBox) {
          cardBox.style.animation = 'none';
          void cardBox.offsetWidth;
          cardBox.style.animation = 'pop-in 0.2s ease';
        }

        if (shakeTaps >= 8 && resolved && resolved.style.display !== 'block') {
          AudioManager.playChime();
          ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 40);
          resolved.style.display = 'block';
          if (btn) btn.style.display = 'none';
          AnswerManager.recordMilestone('shake_completed', 'Shook screen 8 times');
        }
      };
    }

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(16, 'next');
  }

  // --- Scene 16: Festive Hidden Object Hunt (5 Items) ---
  let huntFound = new Set();
  function setupScene16() {
    const items = document.querySelectorAll('#festive-hunt-board .hunt-obj-item');
    const countDisplay = document.getElementById('hunt-found-count');
    const card = document.getElementById('hunt-completed-card');
    const btnNext = document.getElementById('btn-hunt-next');

    items.forEach((item) => {
      item.onclick = function () {
        const id = this.getAttribute('data-hunt');
        if (huntFound.has(id)) return;
        huntFound.add(id);
        this.classList.add('found');
        AudioManager.playBell();

        if (countDisplay) countDisplay.textContent = huntFound.size;
        ParticleManager.fireConfetti(this.offsetLeft + 20, this.offsetTop, 15);

        if (huntFound.size >= 5) {
          AudioManager.playFanfare();
          if (card) card.style.display = 'block';
          AchievementManager.unlock('detective_bhena');
          AnswerManager.recordMilestone('hunt_5_found', 'Found all 5 festive hunt items');
        }
      };
    });

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(17, 'next');
  }

  // --- Scene 17: Official Bhena Sweet Picker ---
  function setupScene17() {
    const buttons = document.querySelectorAll('#sweets-platter-grid .sweet-card-btn');
    const verdictBox = document.getElementById('sweet-verdict-box');
    const p1 = document.getElementById('sweet-verdict-p1');
    const btnNext = document.getElementById('btn-sweet-next');

    buttons.forEach((btn) => {
      btn.onclick = function () {
        const sweet = this.getAttribute('data-sweet');
        AudioManager.playPop();
        if (p1) p1.textContent = `You chose ${sweet}...`;
        if (verdictBox) verdictBox.style.display = 'block';
        AchievementManager.unlock('peda_supreme');
        AnswerManager.recordAnswer('official_sweet_choice', 'Favorite Indian Sweet', sweet);
      };
    });

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(18, 'next');
  }

  // --- Scene 18: Pop The Floating Balloons ---
  let poppedCount = 0;
  const balloonMessages = [
    "🎈 Bhai remembers: Every single TV argument you started!",
    "🎈 Bhai appreciates: How you always support me behind my back.",
    "🎈 Bhai will never admit: You're actually pretty cool.",
    "🎈 Bhai promise: Always right here for you forever.",
    "🎈 Bhai wish: May all your dreams come true this year!"
  ];

  function setupScene18() {
    const balloons = document.querySelectorAll('#balloons-floating-arena .floating-balloon-item');
    const countDisplay = document.getElementById('balloons-popped-count');
    const log = document.getElementById('balloon-popped-messages-log');
    const nextWrap = document.getElementById('balloons-next-wrap');
    const btnNext = document.getElementById('btn-balloons-next');

    balloons.forEach((b, idx) => {
      b.onclick = function () {
        if (this.classList.contains('popped')) return;
        this.classList.add('popped');
        poppedCount++;
        AudioManager.playBalloonPop();

        if (countDisplay) countDisplay.textContent = poppedCount;
        ParticleManager.fireConfetti(this.offsetLeft + 20, this.offsetTop, 20);

        if (log) {
          const item = document.createElement('div');
          item.className = 'balloon-log-item';
          item.textContent = balloonMessages[idx];
          log.appendChild(item);
        }

        if (poppedCount >= 5) {
          AudioManager.playFanfare();
          if (nextWrap) nextWrap.style.display = 'flex';
          AnswerManager.recordMilestone('balloons_5_popped', 'Popped all 5 balloons');
        }
      };
    });

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(19, 'next');
  }

  // --- Scene 19: Digital Interactive Photo Album (Page-Turn) ---
  let albumCurrentPage = 1;
  const TOTAL_PAGES = 6;

  function setupScene19() {
    const prevBtn = document.getElementById('btn-album-prev');
    const nextBtn = document.getElementById('btn-album-next');
    const indicator = document.getElementById('album-page-indicator');
    const finishBtn = document.getElementById('btn-album-finish');

    function showAlbumPage(pg) {
      document.querySelectorAll('#photo-album-book .album-page').forEach((p) => {
        p.style.display = 'none';
        p.classList.remove('active');
      });
      const target = document.querySelector(`#photo-album-book .album-page[data-page="${pg}"]`);
      if (target) {
        target.style.display = 'block';
        target.classList.add('active');
        AudioManager.playPop();
      }
      if (indicator) indicator.textContent = `Page ${pg} of ${TOTAL_PAGES}`;
    }

    if (prevBtn) {
      prevBtn.onclick = () => {
        if (albumCurrentPage > 1) {
          albumCurrentPage--;
          showAlbumPage(albumCurrentPage);
        }
      };
    }

    if (nextBtn) {
      nextBtn.onclick = () => {
        if (albumCurrentPage < TOTAL_PAGES) {
          albumCurrentPage++;
          showAlbumPage(albumCurrentPage);
        }
      };
    }

    if (finishBtn) finishBtn.onclick = () => StoryRouter.goToScreen(20, 'next');
  }

  // --- Scene 20: Official Sibling Cup Scoreboard ---
  function startSiblingCupCounters() {
    const btnNext = document.getElementById('btn-scene-20-next');
    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(21, 'next');
  }

  // --- Scene 21: Sister Nickname Slot Machine ---
  let slotSpins = 3;
  function setupScene21() {
    const btnSpin = document.getElementById('btn-spin-slot');
    const lever = document.getElementById('slot-lever-container');
    const reel1 = document.querySelector('#reel-1 .reel-val');
    const reel2 = document.querySelector('#reel-2 .reel-val');
    const reel3 = document.querySelector('#reel-3 .reel-val');
    const countDisplay = document.getElementById('slot-spins-count');
    const badge = document.getElementById('slot-result-badge');
    const btnNext = document.getElementById('btn-slot-next');

    const names1 = ["MAHARANI", "CHOTI DON", "CERTIFIED", "PROFESSIONAL"];
    const names2 = ["PEDA", "GADHI", "DRAMA QUEEN", "FOOD CHOR"];
    const names3 = ["DEVI", "JI", "SPECIALIST", "HEADACHE"];

    function spin() {
      if (slotSpins <= 0) return;
      slotSpins--;
      if (countDisplay) countDisplay.textContent = slotSpins;
      AudioManager.playChime();

      let ticks = 0;
      const interval = setInterval(() => {
        if (reel1) reel1.textContent = names1[Math.floor(Math.random() * names1.length)];
        if (reel2) reel2.textContent = names2[Math.floor(Math.random() * names2.length)];
        if (reel3) reel3.textContent = names3[Math.floor(Math.random() * names3.length)];
        AudioManager.playPop();
        ticks++;

        if (ticks > 12) {
          clearInterval(interval);
          if (reel1) reel1.textContent = "MAHARANI";
          if (reel2) reel2.textContent = "PEDA";
          if (reel3) reel3.textContent = "DEVI";

          AudioManager.playFanfare();
          ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 45);
          if (badge) badge.style.display = 'block';
          if (btnSpin && slotSpins <= 0) btnSpin.disabled = true;
          AchievementManager.unlock('peda_supreme');
          AnswerManager.recordMilestone('slot_spun', 'Generated Maharani Peda Devi');
        }
      }, 100);
    }

    if (btnSpin) btnSpin.onclick = spin;
    if (lever) lever.onclick = spin;
    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(22, 'next');
  }

  // --- Scene 22: Virtual Rakhi Thread Tracing ---
  function setupScene22() {
    const btnTie = document.getElementById('btn-tie-rakhi-action');
    const mandala = document.getElementById('rakhi-center-mandala');
    const threadFill = document.getElementById('thread-path-fill');
    const completeMsg = document.getElementById('rakhi-complete-msg');
    const tieWrap = document.getElementById('rakhi-tie-btn-wrap');
    const btnNext = document.getElementById('btn-rakhi-next');

    function completeRakhi() {
      AudioManager.playFanfare();
      if (threadFill) threadFill.style.strokeDashoffset = '0';
      if (tieWrap) tieWrap.style.display = 'none';
      if (completeMsg) completeMsg.style.display = 'block';
      ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.4, 50);
      AchievementManager.unlock('rakhi_master');
      AnswerManager.recordMilestone('rakhi_tied', 'Tied Virtual Rakhi');
    }

    if (btnTie) btnTie.onclick = completeRakhi;
    if (mandala) mandala.onclick = completeRakhi;
    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(23, 'next');
  }

  // --- Scene 23: Interactive Hindi Shayari ---
  function setupScene23() {
    const dots = document.querySelectorAll('.shayari-dot-btn');
    const mandalaEgg = document.getElementById('shayari-mandala-egg');
    const toast2 = document.getElementById('easter-egg-2-toast');
    const actionWrap = document.getElementById('shayari-action-wrap');
    const btnNext = document.getElementById('btn-scene-23-next');
    let revealedLines = 0;
    let mandalaTaps = 0;

    dots.forEach((dot) => {
      dot.onclick = function () {
        const lineNum = this.getAttribute('data-sline');
        const lineEl = document.getElementById(`sh-line-${lineNum}`);
        if (lineEl && !lineEl.classList.contains('revealed')) {
          lineEl.classList.add('revealed');
          this.classList.add('active');
          revealedLines++;
          AudioManager.playBell();

          if (revealedLines >= 4 && actionWrap) {
            actionWrap.style.display = 'flex';
            AnswerManager.recordMilestone('shayari_read', 'Revealed all 4 Shayari lines');
          }
        }
      };
    });

    if (mandalaEgg) {
      mandalaEgg.onclick = () => {
        mandalaTaps++;
        AudioManager.playPop();
        if (mandalaTaps >= 5 && toast2) {
          toast2.style.display = 'inline-block';
          AudioManager.playFanfare();
        }
      };
    }

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(24, 'next');
  }

  // --- Scene 24: Secret Wooden Drawer Drag ---
  function setupScene24() {
    const btnOpen = document.getElementById('btn-open-drawer');
    const drawer = document.getElementById('drawer-pullable');
    const note = document.getElementById('drawer-secret-note');
    const btnNext = document.getElementById('btn-drawer-next');

    function openDrawer() {
      AudioManager.playChime();
      if (drawer) drawer.style.transform = 'translateY(25px)';
      if (btnOpen) btnOpen.style.display = 'none';
      if (note) note.style.display = 'block';
      if (btnNext) btnNext.style.display = 'inline-flex';
      ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 35);
      AchievementManager.unlock('emotional_damage');
      AnswerManager.recordMilestone('drawer_opened', 'Opened classified drawer');
    }

    if (btnOpen) btnOpen.onclick = openDrawer;
    if (drawer) drawer.onclick = openDrawer;
    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(25, 'next');
  }

  // --- Scene 25: Emotional Message 4-Piece Puzzle ---
  let assembledPieceIndex = 0;
  function setupScene25() {
    const pieces = document.querySelectorAll('#message-puzzle-pieces .msg-piece-btn');
    const target = document.getElementById('assembled-message-target');
    const nextWrap = document.getElementById('msg-puzzle-next-wrap');
    const btnNext = document.getElementById('btn-msg-puzzle-next');

    pieces.forEach((btn) => {
      btn.onclick = function () {
        if (this.classList.contains('assembled')) return;
        this.classList.add('assembled');
        assembledPieceIndex++;
        AudioManager.playPop();

        if (target) {
          if (assembledPieceIndex === 1) target.innerHTML = '';
          const p = document.createElement('p');
          p.textContent = this.textContent;
          target.appendChild(p);
        }

        if (assembledPieceIndex >= 4) {
          AudioManager.playFanfare();
          if (nextWrap) nextWrap.style.display = 'flex';
          AnswerManager.recordMilestone('message_puzzle_assembled', 'Assembled message fragments');
        }
      };
    });

    if (btnNext) btnNext.onclick = () => StoryRouter.goToScreen(26, 'next');
  }

  // --- Scene 26: 3D Handwritten Letter ---
  function setupScene26() {
    const envelope = document.getElementById('story-envelope');
    const waxSeal = document.getElementById('env-wax-seal');
    const openBtn = document.getElementById('btn-open-letter-trigger');
    const nextBtn = document.getElementById('btn-scene-26-next');
    const brotherSig = document.getElementById('brother-sig');
    const toast5 = document.getElementById('easter-egg-5-toast');
    let isOpen = false;

    function openEnvelope() {
      if (isOpen) return;
      isOpen = true;
      AudioManager.playChime();
      if (envelope) envelope.classList.add('is-open');
      if (openBtn) openBtn.style.display = 'none';
      if (nextBtn) nextBtn.style.display = 'inline-flex';
      ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.45, 45);
      AchievementManager.unlock('emotional_damage');
      AnswerManager.recordMilestone('letter_opened', 'Opened 3D Handwritten Letter');
    }

    if (envelope) envelope.onclick = openEnvelope;
    if (waxSeal) waxSeal.onclick = (e) => { e.stopPropagation(); openEnvelope(); };
    if (openBtn) openBtn.onclick = openEnvelope;

    if (brotherSig) {
      brotherSig.onclick = (e) => {
        e.stopPropagation();
        AudioManager.playPop();
        if (toast5) {
          toast5.style.display = 'inline-block';
          setTimeout(() => { toast5.style.display = 'none'; }, 4000);
        }
      };
    }

    if (nextBtn) nextBtn.onclick = () => StoryRouter.goToScreen(27, 'next');
  }

  // --- Scene 27: Finale Celebration & Song ---
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
        AudioManager.playFanfare();
      });
    }

    function pause() {
      if (!audioEl) return;
      audioEl.pause();
      isPlaying = false;
      if (playPauseBtn) playPauseBtn.textContent = '▶';
      if (statusText) statusText.textContent = 'Paused';
    }

    function toggle() { if (isPlaying) pause(); else play(); }

    function init() {
      if (playPauseBtn) playPauseBtn.onclick = toggle;
      if (volumeSlider && audioEl) {
        volumeSlider.oninput = (e) => { audioEl.volume = parseFloat(e.target.value); };
      }
      if (muteBtn && audioEl) {
        muteBtn.onclick = () => {
          audioEl.muted = !audioEl.muted;
          muteBtn.textContent = audioEl.muted ? '🔇' : '🔊';
        };
      }
    }

    return { init, play, pause };
  })();

  function triggerGrandCelebration() {
    AudioManager.playFanfare();
    MusicPlayer.play();
    ParticleManager.startFireworks();
    const w = window.innerWidth;
    const h = window.innerHeight;
    ParticleManager.fireConfetti(w * 0.2, h * 0.5, 90);
    ParticleManager.fireConfetti(w * 0.8, h * 0.5, 90);
    setTimeout(() => ParticleManager.fireConfetti(w * 0.5, h * 0.35, 120), 450);
  }

  function setupScene27() {
    const btnCannon = document.getElementById('btn-cannon-more');
    const btnDiya = document.getElementById('btn-diya-bless');
    const btnDownload = document.getElementById('btn-download-keepsake');
    const btnReplay = document.getElementById('btn-replay-story');
    const toastBox = document.getElementById('blessing-toast-box');
    const togetherPhoto = document.getElementById('together-photo-img');

    if (btnCannon) btnCannon.onclick = triggerGrandCelebration;

    if (btnDiya) {
      btnDiya.onclick = () => {
        AudioManager.playBell();
        if (toastBox) toastBox.style.display = toastBox.style.display === 'none' ? 'block' : 'none';
        ParticleManager.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.5, 35);
      };
    }

    if (togetherPhoto) {
      togetherPhoto.onclick = (e) => {
        AudioManager.playPop();
        ParticleManager.spawnFloatingHeart(e.clientX, e.clientY);
      };
    }

    // Easter Egg 1 Button
    const egg1Btn = document.getElementById('easter-egg-1-btn');
    const egg1Toast = document.getElementById('easter-egg-1-toast');
    if (egg1Btn) {
      egg1Btn.onclick = () => {
        AudioManager.playPop();
        ParticleManager.fireConfetti(window.innerWidth * 0.8, 60, 25);
        if (egg1Toast) {
          egg1Toast.style.display = 'inline-block';
          setTimeout(() => { egg1Toast.style.display = 'none'; }, 4000);
        }
      };
    }

    // Easter Egg 4: Keyboard 'P'
    window.addEventListener('keydown', (e) => {
      if (e.key === 'p' || e.key === 'P') {
        const egg4Toast = document.getElementById('easter-egg-4-toast');
        if (egg4Toast) {
          AudioManager.playPop();
          egg4Toast.style.display = 'inline-block';
          setTimeout(() => { egg4Toast.style.display = 'none'; }, 4000);
        }
      }
    });

    if (btnDownload) btnDownload.onclick = downloadKeepsakeCard;

    if (btnReplay) {
      btnReplay.onclick = () => {
        AudioManager.playChime();
        MusicPlayer.pause();
        StoryRouter.goToScreen(1, 'prev');
      };
    }
  }

  function downloadKeepsakeCard() {
    AudioManager.playPop();
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
  // 8. GLOBAL DOM READY INITIALIZATION
  // ==========================================================================
  document.addEventListener('DOMContentLoaded', () => {
    ParticleManager.init();
    MusicPlayer.init();
    StoryRouter.init();

    const soundToggle = document.getElementById('sound-toggle');
    if (soundToggle) soundToggle.addEventListener('click', AudioManager.toggleSound);

    setupScene2();
    setupScene3();
    setupScene4();
    setupScene5();
    setupScene6();
    setupScene7();
    setupScene8();
    setupScene9();
    setupScene10();
    setupScene11();
    setupScene12();
    setupScene13();
    setupScene14();
    setupScene15();
    setupScene16();
    setupScene17();
    setupScene18();
    setupScene19();
    setupScene21();
    setupScene22();
    setupScene23();
    setupScene24();
    setupScene25();
    setupScene26();
    setupScene27();
  });
})();
"""
    for path in [os.path.join(FRONTEND_DIR, "script.js"), os.path.join(BASE_DIR, "script.js")]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    print("[OK] Generated upgraded script.js in frontend/ and root")

def generate_backend():
    database_py = """# -*- coding: utf-8 -*-
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

raw_db_url = os.getenv("DATABASE_URL", "sqlite:///./rakhi_answers.db")

# SQLAlchemy 2.0 requires postgresql:// instead of legacy postgres://
if raw_db_url.startswith("postgres://"):
    raw_db_url = raw_db_url.replace("postgres://", "postgresql://", 1)

DATABASE_URL = raw_db_url

if "sqlite" in DATABASE_URL:
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(
        DATABASE_URL,
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True
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
"""
    with open(os.path.join(BACKEND_DIR, "models.py"), "w", encoding="utf-8") as f:
        f.write(models_py)

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

class MilestoneCreate(BaseModel):
    session_id: str
    milestone: str

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

class MilestoneOut(BaseModel):
    milestone: str
    created_at: datetime

    class Config:
        from_attributes = True

class SessionOut(BaseModel):
    id: str
    started_at: datetime
    is_completed: bool
    completed_at: Optional[datetime] = None
    answers_count: int = 0
    milestones_count: int = 0

    class Config:
        from_attributes = True

class SessionDetailOut(BaseModel):
    id: str
    started_at: datetime
    is_completed: bool
    completed_at: Optional[datetime] = None
    answers: List[AnswerOut] = []
    milestones: List[MilestoneOut] = []

    class Config:
        from_attributes = True
"""
    with open(os.path.join(BACKEND_DIR, "schemas.py"), "w", encoding="utf-8") as f:
        f.write(schemas_py)

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
        return {
            "status": "success",
            "message": "Answer already recorded; original answer preserved.",
            "idempotent": True,
            "recorded_answer": existing_answer.answer
        }

    new_answer = models.SessionAnswer(
        session_id=payload.session_id,
        question_id=payload.question_id,
        question_text=payload.question_text,
        answer=payload.answer,
        created_at=datetime.utcnow()
    )
    db.add(new_answer)
    db.commit()

    return {"status": "success", "message": "Answer recorded successfully", "idempotent": False}

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

    if existing_milestone:
        return {
            "status": "success",
            "message": "Milestone already recorded.",
            "idempotent": True
        }

    new_milestone = models.SessionMilestone(
        session_id=payload.session_id,
        milestone=payload.milestone,
        created_at=datetime.utcnow()
    )
    db.add(new_milestone)
    db.commit()

    return {"status": "success", "message": "Milestone recorded successfully", "idempotent": False}

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
"""
    with open(os.path.join(BACKEND_DIR, "main.py"), "w", encoding="utf-8") as f:
        f.write(main_py)

    reqs = """fastapi>=0.100.0
uvicorn>=0.22.0
sqlalchemy>=2.0.0
pydantic>=2.0.0
psycopg2-binary>=2.9.6
python-dotenv>=1.0.0
"""
    with open(os.path.join(BACKEND_DIR, "requirements.txt"), "w", encoding="utf-8") as f:
        f.write(reqs)

    env_file = """# Local Dev Environment
ADMIN_PASSWORD=peda2026
DATABASE_URL=sqlite:///./rakhi_answers.db
ENVIRONMENT=development
FRONTEND_URL=http://localhost:5500
"""
    with open(os.path.join(BACKEND_DIR, ".env"), "w", encoding="utf-8") as f:
        f.write(env_file)

    print("[OK] Generated backend files in backend/")

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
      <div class="stat-card"><div class="stat-val" id="stat-answers">0</div><div class="stat-lbl">Total Milestones & Answers</div></div>
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
            <th>Milestones & Answers</th>
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
      <p id="modal-sub" style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 20px;">Detailed Q&A & Milestone Timeline:</p>
      <div id="qa-container"></div>
    </div>
  </div>

  <script>
    const API_BASE = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')
      ? 'http://localhost:8000'
      : 'https://rakhi-surprise-api.onrender.com';

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

        document.getElementById('stat-visitors').textContent = data.stats.total_visitors;
        document.getElementById('stat-completed').textContent = data.stats.completed;
        document.getElementById('stat-progress').textContent = data.stats.in_progress;
        document.getElementById('stat-answers').textContent = data.stats.total_answers;

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
            <td><strong>${s.answers_count}</strong> items</td>
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

        if (data.milestones && data.milestones.length > 0) {
          const mWrap = document.createElement('div');
          mWrap.style.marginBottom = '18px';
          mWrap.innerHTML = '<h3 style="color: var(--gold); font-size: 0.95rem; margin-bottom: 8px;">🚩 Reached Milestones:</h3>';
          const mList = document.createElement('div');
          mList.style.display = 'flex';
          mList.style.flexWrap = 'wrap';
          mList.style.gap = '6px';
          data.milestones.forEach(m => {
            const mBadge = document.createElement('span');
            mBadge.className = 'badge badge-success';
            mBadge.textContent = '✨ ' + m.milestone.replace(/_/g, ' ');
            mList.appendChild(mBadge);
          });
          mWrap.appendChild(mList);
          container.appendChild(mWrap);
        }

        if (data.answers.length === 0) {
          container.innerHTML += '<p style="color: var(--text-muted);">No answers submitted in this session yet.</p>';
        } else {
          const qHeader = document.createElement('h3');
          qHeader.style.color = 'var(--gold)';
          qHeader.style.fontSize = '0.95rem';
          qHeader.style.marginBottom = '8px';
          qHeader.textContent = '📝 Q&A Responses:';
          container.appendChild(qHeader);

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
    print("[OK] Generated dashboard/index.html")

if __name__ == '__main__':
    setup_directories()
    generate_index_html()
    generate_style_css()
    generate_script_js()
    generate_backend()
    generate_dashboard()
    print("\n=======================================================")
    print("🎉 FULL INTERACTIVE UPGRADE GENERATED SUCCESSFULLY!")
    print("=======================================================")



