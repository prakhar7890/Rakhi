# -*- coding: utf-8 -*-
import os

def generate_index_html():
    content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <meta name="theme-color" content="#2D1822">
  <meta name="description" content="A secret, interactive, cinematic Rakhi surprise experience crafted by Prakhar for his sister Prerna Gupta.">
  <title>For Prerna • Happy Raksha Bandhan ✨</title>

  <!-- Preconnect to Google Fonts -->
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
  <canvas id="confetti-canvas" aria-hidden="true"></canvas>
  <canvas id="hearts-canvas" aria-hidden="true"></canvas>
  <canvas id="sparkle-cursor-canvas" aria-hidden="true"></canvas>

  <!-- Top Minimalist Story Bar -->
  <header class="top-story-bar" aria-label="Story Header">
    <div class="brand-chip">
      <span class="brand-icon">🌸</span>
      <span class="brand-text">For Prerna • 23</span>
    </div>

    <!-- Subtle Dots Progress Indicator (18 steps) -->
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

      <!-- Easter Egg 1 Button -->
      <button id="easter-egg-1-btn" class="control-pill-btn warning-pill" aria-label="Secret Easter Egg" title="Don't touch this!">
        <span>🚫 Don't touch</span>
      </button>
    </div>
  </header>

  <!-- MAIN STORY VIEWPORT (18 Cinematic Scenes) -->
  <main id="story-viewport" class="story-viewport">

    <!-- ============================================================ -->
    <!-- SCENE 1: SECRET ENTRY                                        -->
    <!-- ============================================================ -->
    <section class="story-screen active dark-scene" id="scene-1" data-scene="1">
      <div class="screen-box cinematic-intro-card">
        <div class="screen-badge glow-badge">
          <span>✨ Chapter 01 • The Beginning</span>
        </div>

        <div class="cinematic-text-stream">
          <p class="cinematic-line c-line-1" id="s1-line-1">"There is someone very special..."</p>
          <p class="cinematic-line c-line-2" id="s1-line-2">"Someone who has been annoying her brother for 23 years."</p>
          <p class="cinematic-line c-line-3 handwriting" id="s1-line-3">"I think you know who I mean."</p>
        </div>

        <div class="screen-action-wrap" id="s1-action-wrap" style="opacity: 0;">
          <button id="btn-scene-1-enter" class="btn-grand-gold pulse-btn">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Enter the surprise</span>
              <span class="btn-sparkle">✨</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 2: NAME CHECK & SCANNING                               -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-2" data-scene="2">
      <div class="screen-box glass-card interactive-card">
        <div class="screen-badge">
          <span>🕵️‍♀️ Chapter 02 • Identity Check</span>
        </div>

        <div class="prompt-header">
          <p class="prompt-sub">Before we begin...</p>
          <h2 class="prompt-title">Tell me your name.</h2>
        </div>

        <form id="form-name-check" class="interactive-form" onsubmit="return false;">
          <div class="input-field-wrap">
            <input 
              type="text" 
              id="input-user-name" 
              class="story-input" 
              placeholder="Enter your name..." 
              autocomplete="off" 
              autocapitalize="words"
              spellcheck="false"
              required
            >
          </div>

          <!-- Scanning Bar Animation -->
          <div class="scanning-terminal-box" id="scanning-terminal" style="display: none;">
            <div class="scan-status-text" id="scan-status-text">Checking identity...</div>
            <div class="scan-progress-bar">
              <div class="scan-bar-fill" id="scan-bar-fill"></div>
            </div>
          </div>

          <div class="validation-feedback" id="name-validation-msg" aria-live="polite"></div>

          <div class="screen-action-wrap" id="name-btn-wrap">
            <button type="submit" id="btn-name-continue" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">
                <span>Confirm Identity</span>
                <span class="btn-arrow">→</span>
              </span>
            </button>
          </div>
        </form>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 3: AGE CHECK & 23 STATS                                -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-3" data-scene="3">
      <div class="screen-box glass-card interactive-card">
        <div class="screen-badge">
          <span>🎂 Chapter 03 • The Milestone</span>
        </div>

        <div class="prompt-header">
          <p class="prompt-sub">One more thing...</p>
          <div class="huge-number-anim" id="age-huge-number">23?</div>
          <h2 class="prompt-title">Is this really the age of my little sister?</h2>
        </div>

        <form id="form-age-check" class="interactive-form" onsubmit="return false;">
          <div class="input-field-wrap age-input-wrap">
            <input 
              type="number" 
              id="input-user-age" 
              class="story-input age-input" 
              placeholder="23" 
              min="1" 
              max="100" 
              autocomplete="off"
              required
            >
          </div>

          <div class="validation-feedback" id="age-validation-msg" aria-live="polite"></div>

          <div class="screen-action-wrap" id="age-btn-wrap">
            <button type="submit" id="btn-age-continue" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">
                <span>Verify Age</span>
                <span class="btn-arrow">→</span>
              </span>
            </button>
          </div>
        </form>

        <!-- 23 Years Sibling Stats Card (Shown on correct) -->
        <div class="stats-badge-grid" id="age-stats-grid" style="display: none;">
          <div class="stat-pill"><span class="stat-num">23</span><span class="stat-lbl">YEARS</span></div>
          <div class="stat-pill"><span class="stat-num">∞</span><span class="stat-lbl">MEMORIES</span></div>
          <div class="stat-pill"><span class="stat-num">∞</span><span class="stat-lbl">ARGUMENTS</span></div>
          <div class="stat-pill highlight-pill"><span class="stat-num">1</span><span class="stat-lbl">SISTER</span></div>
        </div>

        <div class="screen-action-wrap" id="age-success-next-wrap" style="display: none;">
          <button id="btn-age-next" class="btn-grand-gold">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Let's Begin</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 4: THE FIRST TRICK QUESTION                            -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-4" data-scene="4">
      <div class="screen-box glass-card quiz-card">
        <div class="screen-badge">
          <span>🧠 Chapter 04 • The Ultimate Debate</span>
        </div>

        <div class="prompt-header">
          <p class="prompt-sub">Let's see how well you know your brother...</p>
          <h2 class="prompt-title">Who is the better sibling?</h2>
        </div>

        <div class="quiz-options-list" id="s4-options-list">
          <button class="quiz-option-btn" data-key="prerna" data-reaction="Correct. I respect your honesty. 💅">
            <span class="opt-key">A</span>
            <span class="opt-label">Prerna</span>
          </button>
          <button class="quiz-option-btn" data-key="prakhar" data-reaction="Incorrect. But confidence is important. 😇">
            <span class="opt-key">B</span>
            <span class="opt-label">Prakhar</span>
          </button>
          <button class="quiz-option-btn" data-key="obv-prerna" data-reaction="The universe agrees with your supreme ego. 👑">
            <span class="opt-key">C</span>
            <span class="opt-label">Obviously Prerna</span>
          </button>
          <button class="quiz-option-btn" data-key="rigged" data-reaction="You finally understand how this family works. ⚖️😂">
            <span class="opt-key">D</span>
            <span class="opt-label">This question is rigged</span>
          </button>
        </div>

        <div class="quiz-feedback-box" id="s4-feedback-box" style="display: none;">
          <p class="feedback-text handwriting" id="s4-feedback-text"></p>
          <button id="btn-s4-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Next Challenge</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 5: SIBLING RAPID FIRE (7 QUESTIONS SEQUENTIAL)         -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-5" data-scene="5">
      <div class="screen-box glass-card quiz-card">
        <div class="screen-badge">
          <span>⚡ Chapter 05 • Sibling Rapid Fire</span>
        </div>

        <div class="rapid-fire-stage" id="rapid-fire-stage">
          <div class="rapid-step-badge" id="rapid-step-badge">Question 1 of 7</div>
          <h2 class="prompt-title rapid-question-title" id="rapid-question-title">Who gets angry first?</h2>

          <div class="rapid-options-row" id="rapid-options-row">
            <button class="btn-choice-pill" data-choice="prerna">
              <span>Prerna</span>
            </button>
            <button class="btn-choice-pill" data-choice="prakhar">
              <span>Prakhar</span>
            </button>
            <button class="btn-choice-pill" data-choice="both">
              <span>Both / Draw</span>
            </button>
          </div>

          <div class="rapid-feedback-box" id="rapid-feedback-box" style="display: none;">
            <p class="feedback-text handwriting" id="rapid-feedback-text"></p>
            <button id="btn-rapid-next" class="btn-primary-glow">
              <span class="btn-shine"></span>
              <span class="btn-content">
                <span id="rapid-btn-label">Next Question</span>
                <span class="btn-arrow">→</span>
              </span>
            </button>
          </div>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 6: WOULD YOU RATHER                                    -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-6" data-scene="6">
      <div class="screen-box glass-card interactive-card">
        <div class="screen-badge">
          <span>🤔 Chapter 06 • Would You Rather</span>
        </div>

        <div class="prompt-header">
          <p class="prompt-sub">Choose wisely...</p>
          <h2 class="prompt-title">Would you rather...</h2>
        </div>

        <div class="wyr-cards-container" id="wyr-cards-container">
          <div class="wyr-card" id="wyr-card-a" role="button" tabindex="0">
            <span class="wyr-badge">OPTION A</span>
            <p class="wyr-card-text" id="wyr-text-a">"Fight with your brother every day"</p>
          </div>
          <div class="wyr-divider">OR</div>
          <div class="wyr-card" id="wyr-card-b" role="button" tabindex="0">
            <span class="wyr-badge">OPTION B</span>
            <p class="wyr-card-text" id="wyr-text-b">"Admit your brother is right once?"</p>
          </div>
        </div>

        <div class="wyr-feedback-box" id="wyr-feedback-box" style="display: none;">
          <p class="feedback-text handwriting" id="wyr-feedback-text"></p>
          <button id="btn-wyr-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Continue to Memories</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 7: MEMORY GUESSING GAME (BLUR TO CRISP)                -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-7" data-scene="7">
      <div class="screen-box glass-card memory-guess-card">
        <div class="screen-badge">
          <span>🔍 Chapter 07 • Memory Test</span>
        </div>

        <h2 class="prompt-title">Do you remember this?</h2>

        <!-- Blurred Photo Stage -->
        <div class="memory-guess-stage">
          <div class="guess-photo-frame" id="guess-photo-frame">
            <!-- Blurred Ambient Backdrop -->
            <div class="ambient-blurred-bg" style="background-image: url('assets/prerna-1.jpg');"></div>
            <!-- Main Photo (Contain - Uncropped) -->
            <img 
              src="assets/prerna-1.jpg" 
              alt="Memory Guess Photo" 
              class="personal-photo blurred-guess-img" 
              id="guess-img"
              loading="eager"
              onerror="this.onerror=null; this.src='assets/prerna-1-fallback.svg';"
            >
            <div class="guess-overlay" id="guess-overlay">
              <span class="guess-lock-icon">🔒</span>
            </div>
          </div>
        </div>

        <!-- Guess Buttons -->
        <div class="guess-actions-row" id="guess-actions-row">
          <button class="btn-choice-pill" data-guess="yes"><span>YES</span></button>
          <button class="btn-choice-pill" data-guess="obviously"><span>Obviously</span></button>
          <button class="btn-choice-pill" data-guess="no-idea"><span>I have no idea</span></button>
        </div>

        <div class="guess-reveal-box" id="guess-reveal-box" style="display: none;">
          <p class="feedback-text handwriting" id="guess-reveal-text">"Caught you remembering! Dressed up & looking sharp ✨"</p>
          <button id="btn-guess-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>View Full Memory</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 8: PHOTO REVEAL 1 (FULL ASPECT RATIO PRESERVED)        -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-8" data-scene="8">
      <div class="screen-box full-photo-scene-card">
        <div class="screen-badge">
          <span>📸 Chapter 08 • Memory Spotlight</span>
        </div>

        <div class="photo-contain-wrapper">
          <div class="photo-ambient-blur" style="background-image: url('assets/prerna-1.jpg');"></div>
          <div class="photo-frame-pure">
            <img 
              src="assets/prerna-1.jpg" 
              alt="Prerna Memory 1" 
              class="personal-photo" 
              loading="eager"
              onerror="this.onerror=null; this.src='assets/prerna-1-fallback.svg';"
            >
          </div>
        </div>

        <div class="photo-caption-block">
          <h3 class="photo-main-caption handwriting">"Some memories don't need an explanation."</h3>
          <p class="photo-sub-caption">Prerna looking radiant • A bond built over 23 years ❤️</p>
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
    <!-- SCENE 9: MEMORY 2 (PARTNERS IN CRIME)                        -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-9" data-scene="9">
      <div class="screen-box full-photo-scene-card">
        <div class="screen-badge">
          <span>🏰 Chapter 09 • Throwback Expedition</span>
        </div>

        <div class="photo-contain-wrapper">
          <div class="photo-ambient-blur" style="background-image: url('assets/prerna-2.jpg');"></div>
          <div class="photo-frame-pure">
            <img 
              src="assets/prerna-2.jpg" 
              alt="Prerna Memory 2" 
              class="personal-photo" 
              loading="lazy"
              onerror="this.onerror=null; this.src='assets/prerna-2-fallback.svg';"
            >
          </div>
        </div>

        <div class="photo-caption-block">
          <h3 class="photo-main-caption handwriting">"Partners in crime."</h3>
          <p class="photo-sub-caption">Historic monument trips, classic poses, and eternal adventures 📸</p>
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
    <!-- SCENE 10: MEMORY 3 (ARGUMENT CHAMPION & PIZZA)               -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-10" data-scene="10">
      <div class="screen-box full-photo-scene-card">
        <div class="screen-badge">
          <span>🍕 Chapter 10 • The Food Extortion</span>
        </div>

        <div class="photo-contain-wrapper">
          <div class="photo-ambient-blur" style="background-image: url('assets/prerna-3.jpg');"></div>
          <div class="photo-frame-pure">
            <img 
              src="assets/prerna-3.jpg" 
              alt="Prerna Memory 3" 
              class="personal-photo" 
              loading="lazy"
              onerror="this.onerror=null; this.src='assets/prerna-3-fallback.svg';"
            >
          </div>
        </div>

        <div class="photo-caption-block">
          <h3 class="photo-main-caption handwriting">"Professional argument champion."</h3>
          <p class="photo-sub-caption">"What's on your plate is officially my snack tax." 🍟</p>
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
    <!-- SCENE 11: MEMORY 4 (ANNOYING & FAVORITE)                     -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-11" data-scene="11">
      <div class="screen-box full-photo-scene-card">
        <div class="screen-badge">
          <span>🤍 Chapter 11 • Sibling Hug</span>
        </div>

        <div class="photo-contain-wrapper">
          <div class="photo-ambient-blur" style="background-image: url('assets/prerna-6.jpg');"></div>
          <div class="photo-frame-pure">
            <img 
              src="assets/prerna-6.jpg" 
              alt="Prerna Memory 4" 
              class="personal-photo" 
              loading="lazy"
              onerror="this.onerror=null; this.src='assets/prerna-6-fallback.svg';"
            >
          </div>
        </div>

        <div class="photo-caption-block">
          <h3 class="photo-main-caption handwriting">"Annoying since day one... and still my favorite person."</h3>
          <p class="photo-sub-caption">And somehow, you keep getting more amazing every single day 🌟</p>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-scene-11-next" class="btn-primary-glow">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>View The Sibling Report</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 12: BROTHER VS SISTER SCORECARD                        -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-12" data-scene="12">
      <div class="screen-box glass-card scorecard-card">
        <div class="screen-badge">
          <span>📊 Chapter 12 • Official Report</span>
        </div>

        <h2 class="prompt-title">The Official Prerna vs Prakhar Report</h2>
        <p class="prompt-sub">Audited sibling statistics over 23 years:</p>

        <div class="scorecard-grid">
          <!-- Row 1: Arguments -->
          <div class="score-row">
            <span class="score-metric">Arguments</span>
            <div class="score-values">
              <span class="prerna-score">Prerna: <strong id="score-arg-prerna">0</strong></span>
              <span class="vs-label">vs</span>
              <span class="prakhar-score">Prakhar: <strong id="score-arg-prakhar">0</strong></span>
            </div>
          </div>

          <!-- Row 2: Food Stealing -->
          <div class="score-row">
            <span class="score-metric">Food Stealing</span>
            <div class="score-values">
              <span class="prerna-score">Prerna: <strong id="score-food-prerna">0</strong></span>
              <span class="vs-label">vs</span>
              <span class="prakhar-score">Prakhar: <strong id="score-food-prakhar">0</strong></span>
            </div>
          </div>

          <!-- Row 3: Drama -->
          <div class="score-row">
            <span class="score-metric">Drama</span>
            <div class="score-values">
              <span class="prerna-score">Prerna: <strong id="score-drama-prerna">0</strong></span>
              <span class="vs-label">vs</span>
              <span class="prakhar-score">Prakhar: <strong id="score-drama-prakhar">0</strong></span>
            </div>
          </div>

          <!-- Row 4: Caring -->
          <div class="score-row highlight-score-row">
            <span class="score-metric">Caring</span>
            <div class="score-values">
              <span class="prerna-score">Prerna: <strong>∞</strong></span>
              <span class="vs-label">❤️</span>
              <span class="prakhar-score">Prakhar: <strong>∞</strong></span>
            </div>
          </div>
        </div>

        <div class="scorecard-verdict-box">
          <p class="verdict-title handwriting">"Winner: Both of you."</p>
          <p class="verdict-sub">"Unfortunately, you'll still have to tolerate each other forever." 🤝</p>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-scene-12-next" class="btn-grand-gold">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Read Something Beautiful</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 13: SHAYARI (WARM DARK ATMOSPHERE)                     -->
    <!-- ============================================================ -->
    <section class="story-screen dark-scene shayari-scene" id="scene-13" data-scene="13">
      <div class="screen-box shayari-card">
        <div class="screen-badge glow-badge">
          <span>🪔 Chapter 13 • Dil Ki Baat</span>
        </div>

        <!-- Interactive Rakhi Mandala (Click 5 times for Easter Egg 2) -->
        <div class="shayari-mandala-wrap" id="shayari-mandala" title="Tap the Rakhi 🌸">
          <span class="mandala-icon">🪢</span>
        </div>

        <div class="shayari-lines-container" id="shayari-container">
          <p class="shayari-line s-l-1 devanagari-font">"रिश्तों की भी अपनी एक कहानी होती है,<br>हर लड़ाई के पीछे थोड़ी सी नादानी होती है,<br>बहन चाहे कितनी भी दूर क्यों न चली जाए,<br>भाई के दिल में उसकी जगह हमेशा पुरानी होती है।"</p>
          <p class="shayari-line s-l-2 devanagari-font">"कुछ रिश्ते शब्दों से नहीं,<br>बस साथ होने से खास बन जाते हैं।"</p>
          <p class="shayari-line s-l-3 devanagari-font highlight-shayari">"और बहन का रिश्ता...<br>शायद उन्हीं रिश्तों में सबसे खूबसूरत है।"</p>
        </div>

        <div class="easter-egg-toast" id="easter-egg-2-toast" style="display: none;">
          <span>🎉 +100 Sister Points! You found the secret Rakhi tap! 🪢</span>
        </div>

        <div class="screen-action-wrap" id="shayari-action-wrap" style="opacity: 0;">
          <button id="btn-scene-13-next" class="btn-grand-gold">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Personal Message</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 14: PERSONAL MESSAGE (CLICK TO ADVANCE LINES)         -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-14" data-scene="14">
      <div class="screen-box glass-card emotional-msg-card">
        <div class="screen-badge">
          <span>💌 Chapter 14 • From Prakhar</span>
        </div>

        <div class="emotional-sequence" id="emotional-sequence">
          <p class="emo-preface">Okay. No more jokes for a minute...</p>
          <h2 class="emo-salutation handwriting">Prerna...</h2>

          <div class="emo-interactive-lines" id="emo-lines-list">
            <p class="emo-line" data-idx="0">"We've fought."</p>
            <p class="emo-line" data-idx="1">"We've annoyed each other."</p>
            <p class="emo-line" data-idx="2">"We've laughed at the stupidest things."</p>
            <p class="emo-line" data-idx="3">"We've grown up together."</p>
            <p class="emo-line" data-idx="4">"And through everything..."</p>
            <p class="emo-line emo-highlight handwriting" data-idx="5">"I'm genuinely lucky to have you as my sister."</p>
          </div>

          <div class="emo-tap-hint" id="emo-tap-hint">
            <span>(Tap anywhere to reveal next line 🌸)</span>
          </div>

          <div class="screen-action-wrap" id="emo-action-wrap" style="display: none;">
            <button id="btn-scene-14-next" class="btn-primary-glow">
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
    <!-- SCENE 15: THE REALISTIC ANIMATED 3D ENVELOPE                 -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-15" data-scene="15">
      <div class="screen-box glass-card letter-card">
        <div class="screen-badge">
          <span>📮 Chapter 15 • The Sealed Letter</span>
        </div>

        <div class="letter-preface-text">
          <h2 class="letter-title handwriting">There is something I wanted to tell you properly.</h2>
        </div>

        <!-- 3D Interactive Envelope -->
        <div class="envelope-stage" id="envelope-stage">
          <div class="envelope" id="story-envelope" role="button" tabindex="0" aria-label="Open Letter">
            <div class="envelope-back"></div>
            
            <!-- Sliding Letter Paper -->
            <div class="letter-paper" id="story-letter-paper">
              <div class="letter-stamp-top">🌸</div>
              <div class="letter-salutation handwriting">Dear Prerna,</div>
              <div class="letter-content-body handwriting">
                <p>Happy Raksha Bandhan.</p>
                <p>We've spent 23 years annoying each other, arguing over ridiculous things, stealing food, laughing at things nobody else would understand, and making memories along the way.</p>
                <p>I don't always say it, but having you as my sister is something I'm genuinely grateful for.</p>
                <p>No matter how much we argue, no matter where life takes us, you'll always have your brother standing beside you.</p>
                <p>Keep smiling. Keep being yourself. And don't become too sensible, because then I won't recognize you.</p>
                <p class="bold-highlight">Happy Rakhi, Prerna.</p>
              </div>
              <div class="letter-sign-off handwriting">
                <p>Your annoying brother,</p>
                <p class="sign-name">Prakhar ❤️</p>
              </div>
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
            <span class="btn-content">
              <span>Open it 💌</span>
            </span>
          </button>
          
          <button id="btn-scene-15-next" class="btn-grand-gold" style="display: none;">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>One Last Thing</span>
              <span class="btn-arrow">→</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 16: FINAL SUSPENSE (DARK & MINIMALIST)                 -->
    <!-- ============================================================ -->
    <section class="story-screen dark-scene suspense-scene" id="scene-16" data-scene="16">
      <div class="screen-box minimalist-suspense-box">
        <div class="suspense-lines-wrap">
          <h2 class="suspense-line su-1" id="su-line-1">Wait...</h2>
          <p class="suspense-line su-2" id="su-line-2">We're not done.</p>
          <p class="suspense-line su-3 handwriting" id="su-line-3">There's one last thing.</p>
        </div>

        <div class="screen-action-wrap" id="su-action-wrap" style="display: none;">
          <button id="btn-reveal-rakhi-surprise" class="btn-grand-gold pulse-btn">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>Reveal My Rakhi Surprise ✨</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 17: FINAL PHOTO REVEAL (PRERNA-TOGETHER.JPG CONTAINED)  -->
    <!-- ============================================================ -->
    <section class="story-screen" id="scene-17" data-scene="17">
      <div class="screen-box full-photo-scene-card finale-photo-card">
        <div class="screen-badge glow-badge">
          <span>👑 Chapter 17 • Sibling Bond Forever</span>
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
          <h2 class="grand-festive-title handwriting">Happy Raksha Bandhan, Prerna!</h2>
          <p class="grand-milestone-tag">23 years of being an amazing sister.</p>
          <p class="grand-emotional-message">
            "No matter how much we fight... you'll always be my sister."
          </p>
          <p class="grand-love-note handwriting">Love you always ❤️</p>
        </div>

        <div class="screen-action-wrap">
          <button id="btn-scene-17-next" class="btn-grand-gold pulse-btn">
            <span class="btn-shine"></span>
            <span class="btn-content">
              <span>One final surprise ❤️</span>
            </span>
          </button>
        </div>
      </div>
    </section>


    <!-- ============================================================ -->
    <!-- SCENE 18: MUSIC + GRAND FINALE CELEBRATION                   -->
    <!-- ============================================================ -->
    <section class="story-screen finale-celebration-scene" id="scene-18" data-scene="18">
      <div class="screen-box glass-card grand-celebration-card">
        <div class="grand-crown-badge">
          <span>👑✨ Happy Raksha Bandhan ✨👑</span>
        </div>

        <!-- Audio Player Widget (assets/song.mp3) -->
        <div class="music-player-widget" id="music-player-widget">
          <div class="music-info-row">
            <span class="music-note-icon">♪</span>
            <span class="music-title-text" id="music-status-text">Playing your Rakhi surprise</span>
          </div>
          <div class="music-controls-row">
            <button id="btn-audio-play-pause" class="player-btn" aria-label="Play or Pause">❚❚</button>
            <input type="range" id="audio-volume-slider" min="0" max="1" step="0.05" value="0.8" class="volume-slider" aria-label="Volume">
            <button id="btn-audio-mute" class="player-btn" aria-label="Mute or Unmute">🔊</button>
          </div>
          <!-- Hidden Audio Element -->
          <audio id="rakhi-audio-element" src="assets/song.mp3" preload="none"></audio>
        </div>

        <div class="grand-celebration-text">
          <h1 class="grand-festive-title handwriting">Happy Raksha Bandhan, Prerna!</h1>
          <p class="grand-milestone-tag">"My sister. My partner in crime. My permanent headache."</p>
          <p class="grand-emotional-message">
            "And one of the people I'll always protect."
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

        <!-- Easter Egg 1 Toast (if clicked) -->
        <div class="easter-egg-toast" id="easter-egg-1-toast" style="display: none;">
          <span>😂 "I literally told you not to touch it!" +10 Sibling Chaos Points!</span>
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

  <!-- Script -->
  <script src="script.js"></script>
</body>
</html>
"""
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully generated index.html")

def generate_style_css():
    content = r"""/* ==========================================================================
   RAKHI SURPRISE STORY • 18-SCENE CINEMATIC EXPERIENCE
   Dedicated to Prerna Gupta (23) • Crafted with love by Prakhar
   ========================================================================== */

/* --- 1. CSS Custom Properties / Design Tokens --- */
:root {
  --color-bg-main: #FFFDF9;
  --color-bg-cream: #FAF5EE;
  --color-dark-burgundy: #2D1822;
  --color-dark-surface: #1B0C15;
  
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

  --glass-bg: rgba(255, 255, 255, 0.88);
  --glass-border: rgba(254, 205, 211, 0.55);
  --glass-shadow: 0 20px 50px rgba(136, 19, 55, 0.08), 0 4px 12px rgba(0, 0, 0, 0.03);
  --glass-shadow-hover: 0 26px 60px rgba(136, 19, 55, 0.14);

  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
  --transition-fast: 0.22s cubic-bezier(0.4, 0, 0.2, 1);
}

/* --- 2. CSS Reset & Global Base --- */
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
    radial-gradient(circle at 15% 20%, rgba(252, 231, 243, 0.6) 0%, transparent 45%),
    radial-gradient(circle at 85% 30%, rgba(254, 243, 199, 0.5) 0%, transparent 50%),
    radial-gradient(circle at 50% 80%, rgba(237, 233, 254, 0.55) 0%, transparent 55%),
    radial-gradient(circle at 80% 85%, rgba(255, 237, 213, 0.45) 0%, transparent 40%);
  pointer-events: none;
  z-index: 0;
}

/* --- 3. Interactive Canvas Layers --- */
#bg-canvas,
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
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  background: rgba(255, 253, 249, 0.78);
  border-bottom: 1px solid rgba(254, 205, 211, 0.4);
}

.brand-chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.9);
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

/* Subtle Progress Track & 18 Dots */
.story-progress-indicator {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  max-width: 360px;
  width: 100%;
  margin: 0 14px;
}

.progress-track {
  width: 100%;
  height: 3px;
  background: rgba(225, 29, 72, 0.1);
  border-radius: 999px;
  overflow: hidden;
  position: relative;
}

.progress-bar-fill {
  width: 5.55%;
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
  gap: 2px;
}

.prog-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: rgba(136, 19, 55, 0.2);
  transition: all 0.3s ease;
}

.prog-dot.completed {
  background: var(--color-pink-deep);
}

.prog-dot.active {
  background: var(--color-gold-main);
  transform: scale(1.5);
  box-shadow: 0 0 8px rgba(245, 158, 11, 0.7);
}

.top-controls {
  display: flex;
  align-items: center;
  gap: 8px;
}

.control-pill-btn {
  background: rgba(255, 255, 255, 0.9);
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
  padding-top: 70px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-bottom: 24px;
}

.story-screen {
  display: none;
  opacity: 0;
  width: 100%;
  min-height: calc(100vh - 94px);
  padding: 16px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.story-screen.active {
  display: flex;
  opacity: 1;
  animation: screen-fade-in 0.55s var(--ease-smooth) forwards;
}

.story-screen.slide-in-right {
  animation: screen-slide-right 0.55s var(--ease-smooth) forwards;
}

.story-screen.slide-in-left {
  animation: screen-slide-left 0.55s var(--ease-smooth) forwards;
}

.dark-scene {
  background: radial-gradient(circle at 50% 50%, #2D1822 0%, #150910 100%);
  color: #FFFFFF;
}

@keyframes screen-fade-in {
  from { opacity: 0; transform: scale(0.96) translateY(12px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}

@keyframes screen-slide-right {
  from { opacity: 0; transform: translateX(45px) scale(0.97); }
  to { opacity: 1; transform: translateX(0) scale(1); }
}

@keyframes screen-slide-left {
  from { opacity: 0; transform: translateX(-45px) scale(0.97); }
  to { opacity: 1; transform: translateX(0) scale(1); }
}

/* --- 6. Reusable Card & Header Styles --- */
.screen-box {
  width: min(100%, 680px);
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
  padding: clamp(26px, 5vw, 44px) clamp(18px, 4vw, 36px);
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
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid rgba(225, 29, 72, 0.18);
  color: var(--color-rose-dark);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.4px;
  margin-bottom: 20px;
  box-shadow: 0 4px 12px rgba(225, 29, 72, 0.06);
}

.glow-badge {
  background: rgba(245, 158, 11, 0.15);
  border-color: rgba(245, 158, 11, 0.45);
  color: #FDE68A;
  box-shadow: 0 0 16px rgba(245, 158, 11, 0.25);
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
  padding: 15px 36px;
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
  box-shadow: 0 16px 38px rgba(225, 29, 72, 0.45), 0 0 0 1px rgba(255, 255, 255, 0.4) inset;
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
  gap: 10px;
}

.btn-grand-gold {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #F59E0B 0%, #D97706 50%, #B45309 100%);
  color: #FFFFFF;
  font-family: var(--font-primary);
  font-size: 1.15rem;
  font-weight: 700;
  padding: 16px 42px;
  border-radius: 999px;
  border: 2px solid #FDE68A;
  cursor: pointer;
  box-shadow: 0 15px 35px rgba(217, 119, 6, 0.4), 0 0 25px rgba(251, 191, 36, 0.4);
  overflow: hidden;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast);
}

.btn-grand-gold:hover {
  transform: translateY(-3px) scale(1.03);
  box-shadow: 0 20px 45px rgba(217, 119, 6, 0.5), 0 0 35px rgba(251, 191, 36, 0.6);
}

.btn-secondary-pill {
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(225, 29, 72, 0.2);
  color: var(--color-rose-dark);
  font-family: var(--font-primary);
  font-weight: 600;
  font-size: 0.95rem;
  padding: 12px 24px;
  border-radius: 999px;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(225, 29, 72, 0.08);
  transition: all var(--transition-fast);
}

.btn-secondary-pill:hover {
  background: #FFFFFF;
  border-color: var(--color-pink-deep);
  transform: translateY(-2px);
}

.btn-choice-pill {
  background: rgba(255, 255, 255, 0.9);
  border: 1.5px solid rgba(225, 29, 72, 0.18);
  padding: 12px 22px;
  border-radius: 999px;
  font-family: var(--font-primary);
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-text-main);
  cursor: pointer;
  transition: all var(--transition-fast);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
}

.btn-choice-pill:hover {
  background: #FFFFFF;
  border-color: var(--color-pink-deep);
  transform: translateY(-2px) scale(1.03);
  box-shadow: 0 8px 20px rgba(225, 29, 72, 0.15);
}

.screen-action-wrap {
  margin-top: 28px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: opacity 0.5s ease;
}

/* --- 8. SCENE 1: SECRET ENTRY --- */
.cinematic-intro-card {
  padding: 60px 20px;
}

.cinematic-text-stream {
  margin-bottom: 34px;
}

.cinematic-line {
  line-height: 1.4;
  margin-bottom: 14px;
  opacity: 0;
}

.c-line-1 {
  font-family: var(--font-heading);
  font-size: clamp(2.2rem, 6vw, 3.4rem);
  color: #FDE68A;
}

.c-line-2 {
  font-size: clamp(1.2rem, 3.5vw, 1.6rem);
  color: #FCE7F3;
  font-weight: 500;
}

.c-line-3 {
  font-size: clamp(2rem, 5.5vw, 2.8rem);
  color: #F59E0B;
  font-weight: 700;
}

/* --- 9. SCENE 2 & 3: INPUTS, SCANNING & STATS --- */
.prompt-header {
  margin-bottom: 24px;
}

.prompt-sub {
  font-size: 1.15rem;
  color: var(--color-text-muted);
  margin-bottom: 6px;
}

.prompt-title {
  font-family: var(--font-heading);
  font-size: clamp(1.8rem, 5vw, 2.5rem);
  color: var(--color-rose-dark);
  font-weight: 700;
  line-height: 1.25;
}

.interactive-form {
  max-width: 440px;
  margin: 0 auto;
}

.input-field-wrap {
  position: relative;
  margin-bottom: 12px;
}

.story-input {
  width: 100%;
  padding: 16px 24px;
  background: rgba(255, 255, 255, 0.95);
  border: 2px solid rgba(225, 29, 72, 0.2);
  border-radius: 18px;
  font-family: var(--font-primary);
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--color-text-main);
  text-align: center;
  outline: none;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
  transition: all var(--transition-fast);
}

.story-input:focus {
  border-color: var(--color-pink-deep);
  box-shadow: 0 0 0 4px rgba(219, 39, 119, 0.15), 0 8px 25px rgba(225, 29, 72, 0.12);
  background: #FFFFFF;
}

.scanning-terminal-box {
  background: #1B0C15;
  border-radius: 14px;
  padding: 14px 18px;
  color: #34D399;
  font-family: monospace;
  font-size: 0.95rem;
  margin-bottom: 12px;
  text-align: left;
}

.scan-progress-bar {
  width: 100%;
  height: 8px;
  background: rgba(255, 255, 255, 0.15);
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

.huge-number-anim {
  font-size: clamp(3.5rem, 9vw, 5.5rem);
  font-family: var(--font-heading);
  font-weight: 700;
  color: var(--color-pink-deep);
  margin-bottom: 6px;
  animation: float-ambient 3s ease-in-out infinite alternate;
}

.age-input-wrap {
  max-width: 180px;
  margin: 0 auto 12px;
}

.age-input {
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: 2px;
}

.validation-feedback {
  min-height: 28px;
  font-size: 1.15rem;
  font-weight: 600;
  margin: 8px 0 14px;
}

.validation-feedback.error {
  color: #DC2626;
  animation: shake 0.4s ease;
}

.validation-feedback.success {
  color: #059669;
  font-family: var(--font-handwriting);
  font-size: 1.6rem;
  font-weight: 700;
}

.stats-badge-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
  gap: 12px;
  margin-top: 24px;
  animation: pop-in 0.45s var(--ease-spring);
}

.stat-pill {
  background: #FFFFFF;
  border: 1.5px solid rgba(225, 29, 72, 0.15);
  border-radius: 16px;
  padding: 12px 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.04);
}

.stat-num {
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--color-rose-dark);
}

.stat-lbl {
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--color-text-light);
  letter-spacing: 0.5px;
}

.highlight-pill {
  border-color: #F59E0B;
  background: #FEF3C7;
}

.highlight-pill .stat-num {
  color: #B45309;
}

/* --- 10. SCENE 4 & 5: TRICK QUESTION & RAPID FIRE --- */
.quiz-options-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-width: 480px;
  margin: 0 auto;
}

.quiz-option-btn {
  background: rgba(255, 255, 255, 0.92);
  border: 1.5px solid rgba(225, 29, 72, 0.16);
  border-radius: 18px;
  padding: 14px 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 14px;
  text-align: left;
  font-family: var(--font-primary);
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--color-text-main);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
  transition: all var(--transition-fast);
}

.opt-key {
  width: 32px;
  height: 32px;
  border-radius: 10px;
  background: rgba(225, 29, 72, 0.08);
  color: var(--color-rose-dark);
  font-weight: 700;
  font-size: 0.88rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: all var(--transition-fast);
}

.quiz-option-btn:hover {
  background: #FFFFFF;
  border-color: var(--color-pink-deep);
  transform: translateX(4px);
  box-shadow: 0 8px 20px rgba(225, 29, 72, 0.12);
}

.quiz-option-btn:hover .opt-key {
  background: var(--color-pink-deep);
  color: #FFFFFF;
}

.quiz-feedback-box, .rapid-feedback-box, .wyr-feedback-box {
  margin-top: 22px;
  animation: pop-in 0.4s var(--ease-spring);
}

.feedback-text {
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--color-rose-dark);
  margin-bottom: 20px;
  line-height: 1.3;
}

/* Rapid Fire Layout */
.rapid-step-badge {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--color-pink-deep);
  text-transform: uppercase;
  letter-spacing: 0.8px;
  margin-bottom: 8px;
}

.rapid-question-title {
  margin-bottom: 24px;
}

.rapid-options-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin-bottom: 12px;
}

/* --- 11. SCENE 6: WOULD YOU RATHER --- */
.wyr-cards-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  margin: 24px 0 12px;
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
  margin-bottom: 12px;
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

/* --- 12. SCENE 7: MEMORY GUESSING GAME --- */
.memory-guess-stage {
  margin: 20px auto;
  display: flex;
  justify-content: center;
}

.guess-photo-frame {
  position: relative;
  width: min(88vw, 420px);
  height: 280px;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
}

.blurred-guess-img {
  filter: blur(18px) brightness(0.9);
  transition: filter 0.8s ease;
}

.guess-photo-frame.revealed .blurred-guess-img {
  filter: blur(0px) brightness(1);
}

.guess-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(45, 24, 34, 0.2);
  transition: opacity 0.5s ease;
}

.guess-lock-icon { font-size: 2.5rem; }

.guess-photo-frame.revealed .guess-overlay {
  opacity: 0;
  pointer-events: none;
}

.guess-actions-row {
  display: flex;
  justify-content: center;
  gap: 12px;
  margin: 16px 0;
  flex-wrap: wrap;
}

/* --- 13. SCENES 8–11: FULL PERSONAL PHOTOS (UNCROPPED OBJECT-FIT: CONTAIN) --- */
.full-photo-scene-card {
  padding: 24px 16px;
  max-width: 900px;
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
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.12);
  background: #2D1822;
}

.photo-ambient-blur {
  position: absolute;
  inset: -20px;
  background-size: cover;
  background-position: center;
  filter: blur(28px) brightness(0.75);
  opacity: 0.5;
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
  padding: 12px;
}

.personal-photo {
  max-width: 100%;
  max-height: 100%;
  width: auto;
  height: auto;
  object-fit: contain !important;
  border-radius: 12px;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.35);
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

/* --- 14. SCENE 12: BROTHER VS SISTER SCORECARD --- */
.scorecard-grid {
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-width: 480px;
  margin: 24px auto;
}

.score-row {
  background: #FFFFFF;
  border: 1.5px solid rgba(225, 29, 72, 0.15);
  border-radius: 16px;
  padding: 14px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
}

.score-metric {
  font-weight: 700;
  color: var(--color-rose-dark);
  font-size: 1.05rem;
}

.score-values {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
  font-size: 0.95rem;
}

.prerna-score { color: var(--color-pink-deep); }
.prakhar-score { color: #2563EB; }
.vs-label { color: var(--color-text-light); font-size: 0.8rem; }

.highlight-score-row {
  border-color: #F59E0B;
  background: linear-gradient(135deg, #FFFDF9 0%, #FEF3C7 100%);
}

.scorecard-verdict-box {
  margin: 18px auto 8px;
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

/* --- 15. SCENE 13: SHAYARI --- */
.shayari-card {
  padding: 40px 20px;
}

.shayari-mandala-wrap {
  width: 68px;
  height: 68px;
  border-radius: 50%;
  background: radial-gradient(circle, #F59E0B 0%, #B45309 100%);
  margin: 0 auto 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.2rem;
  box-shadow: 0 0 25px rgba(245, 158, 11, 0.5);
  cursor: pointer;
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.shayari-mandala-wrap:active {
  transform: scale(1.3) rotate(20deg);
}

.shayari-lines-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 540px;
  margin: 0 auto;
}

.shayari-line {
  font-size: clamp(1.25rem, 3.8vw, 1.6rem);
  line-height: 1.6;
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
  font-size: clamp(1.4rem, 4.2vw, 1.8rem);
  margin-top: 8px;
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

/* --- 16. SCENE 14: PERSONAL EMOTIONAL MESSAGE --- */
.emo-preface {
  font-size: 1.1rem;
  color: var(--color-text-muted);
  margin-bottom: 4px;
}

.emo-salutation {
  font-size: clamp(2.4rem, 6vw, 3.6rem);
  color: var(--color-rose-dark);
  margin-bottom: 20px;
}

.emo-interactive-lines {
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-width: 520px;
  margin: 0 auto 20px;
  min-height: 220px;
}

.emo-line {
  font-size: clamp(1.15rem, 3.2vw, 1.45rem);
  color: var(--color-text-main);
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.5s ease, transform 0.5s ease;
  line-height: 1.35;
}

.emo-line.revealed {
  opacity: 1;
  transform: translateY(0);
}

.emo-highlight {
  font-size: clamp(1.8rem, 5vw, 2.6rem);
  color: var(--color-pink-deep);
  margin-top: 10px;
}

.emo-tap-hint {
  font-size: 0.85rem;
  color: var(--color-text-light);
  font-style: italic;
}

/* --- 17. SCENE 15: THE REALISTIC 3D ENVELOPE --- */
.envelope-stage {
  perspective: 1200px;
  width: 100%;
  max-width: 480px;
  margin: 10px auto 26px;
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
  overflow: hidden;
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

.letter-content-body p {
  margin-bottom: 8px;
}

.bold-highlight {
  font-weight: 700;
  color: var(--color-pink-deep);
}

.letter-sign-off {
  font-size: 1.2rem;
  color: var(--color-rose-dark);
}

.sign-name { font-weight: 700; }

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

.env-wax-seal:hover {
  transform: translate(-50%, -50%) scale(1.12);
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

/* --- 18. SCENE 16: FINAL SUSPENSE --- */
.minimalist-suspense-box {
  padding: 60px 20px;
}

.suspense-lines-wrap {
  margin-bottom: 32px;
}

.suspense-line {
  color: #FFFFFF;
  line-height: 1.3;
  opacity: 0;
}

.su-1 {
  font-family: var(--font-heading);
  font-size: clamp(3rem, 8vw, 4.8rem);
  color: #FDE68A;
  margin-bottom: 16px;
}

.su-2 {
  font-size: clamp(1.4rem, 4vw, 2rem);
  color: #FCE7F3;
  margin-bottom: 16px;
}

.su-3 {
  font-size: clamp(2.4rem, 6.5vw, 3.6rem);
  color: #F59E0B;
}

/* --- 19. SCENE 17 & 18: FINALE, CELEBRATION & MUSIC PLAYER --- */
.grand-celebration-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(254, 243, 199, 0.8) 100%);
  border: 2.5px solid rgba(245, 158, 11, 0.5);
  box-shadow: 0 30px 70px rgba(245, 158, 11, 0.25), 0 0 40px rgba(251, 191, 36, 0.3);
  max-width: 680px;
}

.grand-crown-badge {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--color-gold-deep);
  margin-bottom: 14px;
}

/* Music Player Widget */
.music-player-widget {
  background: rgba(255, 255, 255, 0.9);
  border: 1.5px solid rgba(245, 158, 11, 0.35);
  border-radius: 18px;
  padding: 12px 18px;
  margin: 0 auto 20px;
  max-width: 420px;
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
  margin-bottom: 10px;
}

.grand-milestone-tag {
  font-size: clamp(1.1rem, 3vw, 1.35rem);
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
  margin-bottom: 24px;
}

.grand-actions-bar {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
}

.blessing-toast-box {
  background: rgba(255, 255, 255, 0.95);
  border: 1.5px solid rgba(245, 158, 11, 0.4);
  border-radius: 16px;
  padding: 12px 18px;
  max-width: 460px;
  margin: 0 auto 16px;
  animation: pop-in 0.4s var(--ease-spring);
}

.toast-diya-flame { font-size: 1.8rem; }
.toast-text {
  font-size: 1.35rem;
  font-weight: 700;
  color: var(--color-rose-dark);
}

.replay-wrap {
  margin-top: 14px;
}

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

.replay-link-btn:hover {
  color: var(--color-rose-dark);
}

/* --- 20. Keyframes & Responsiveness --- */
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
  0%, 100% { box-shadow: 0 15px 35px rgba(217, 119, 6, 0.4), 0 0 25px rgba(251, 191, 36, 0.4); }
  50% { box-shadow: 0 20px 50px rgba(217, 119, 6, 0.7), 0 0 45px rgba(251, 191, 36, 0.8); }
}

@keyframes float-ambient {
  from { transform: translateY(0) rotate(0deg); }
  to { transform: translateY(-8px) rotate(3deg); }
}

@media (max-width: 640px) {
  .top-story-bar {
    padding: 0 12px;
    height: 56px;
  }

  .story-viewport {
    padding-top: 62px;
  }

  .glass-card {
    border-radius: 22px;
    padding: 24px 16px;
  }

  .photo-contain-wrapper {
    height: 46vh;
  }

  .envelope {
    height: 220px;
  }

  .envelope.is-open .letter-paper {
    transform: translateY(-90px);
    min-height: 360px;
    padding: 16px;
  }

  .letter-content-body {
    font-size: 1.05rem;
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
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully generated style.css")


def generate_script_js():
    content = r"""/**
 * RAKHI SURPRISE STORY • 18-SCENE INTERACTION ENGINE
 * Dedicated to Prerna Gupta (Age 23) • Built by Prakhar
 */

(function () {
  'use strict';

  const TOTAL_SCREENS = 18;
  let currentScreen = 1;
  let isTransitioning = false;

  // ==========================================================================
  // 1. SOUND SYNTHESIZER (Web Audio API - Zero External Dependencies)
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
        osc.frequency.exponentialRampToValueAtTime(800, ctx.currentTime + 0.07);
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

    return { toggleSound, playPop, playChime, playFanfare, getContext };
  })();

  // ==========================================================================
  // 2. PARTICLE, CONFETTI & HEARTS ENGINE (Canvas Rendering)
  // ==========================================================================
  const ParticleEngine = (function () {
    const bgCanvas = document.getElementById('bg-canvas');
    const confettiCanvas = document.getElementById('confetti-canvas');
    const heartsCanvas = document.getElementById('hearts-canvas');
    const cursorCanvas = document.getElementById('sparkle-cursor-canvas');

    let bgCtx, confettiCtx, heartsCtx, cursorCtx;
    let bgParticles = [];
    let confettiPieces = [];
    let floatingHearts = [];
    let cursorSparkles = [];
    let width = window.innerWidth;
    let height = window.innerHeight;

    function resize() {
      width = window.innerWidth;
      height = window.innerHeight;
      if (bgCanvas) { bgCanvas.width = width; bgCanvas.height = height; }
      if (confettiCanvas) { confettiCanvas.width = width; confettiCanvas.height = height; }
      if (heartsCanvas) { heartsCanvas.width = width; heartsCanvas.height = height; }
      if (cursorCanvas) { cursorCanvas.width = width; cursorCanvas.height = height; }
    }

    function init() {
      if (bgCanvas) bgCtx = bgCanvas.getContext('2d');
      if (confettiCanvas) confettiCtx = confettiCanvas.getContext('2d');
      if (heartsCanvas) heartsCtx = heartsCanvas.getContext('2d');
      if (cursorCanvas) cursorCtx = cursorCanvas.getContext('2d');

      resize();
      window.addEventListener('resize', resize);

      // Ambient golden stars & soft petals
      bgParticles = [];
      for (let i = 0; i < 30; i++) {
        bgParticles.push({
          x: Math.random() * width,
          y: Math.random() * height,
          radius: Math.random() * 3.5 + 1.5,
          speedY: Math.random() * 0.4 + 0.2,
          speedX: Math.sin(Math.random() * Math.PI) * 0.3,
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
          vy: (Math.random() - 0.5) * 1.5 - 0.5,
          life: 1,
          size: Math.random() * 3 + 1.5,
          color: Math.random() > 0.5 ? '#F59E0B' : '#EC4899'
        });
      }, { passive: true });

      requestAnimationFrame(loop);
    }

    function fireConfetti(originX, originY, count = 80, colors = ['#E11D48', '#F59E0B', '#EC4899', '#8B5CF6', '#10B981', '#FDE68A']) {
      for (let i = 0; i < count; i++) {
        const angle = Math.random() * Math.PI * 2;
        const velocity = Math.random() * 12 + 6;
        confettiPieces.push({
          x: originX,
          y: originY,
          vx: Math.cos(angle) * velocity,
          vy: Math.sin(angle) * velocity - 3,
          gravity: 0.28,
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

    function loop() {
      // 1. Ambient Background Particles
      if (bgCtx) {
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
      if (cursorCtx) {
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

      // 4. Physics Confetti
      if (confettiCtx) {
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

    return { init, fireConfetti, spawnFloatingHeart };
  })();

  // ==========================================================================
  // 3. MUSIC PLAYER CONTROLLER (assets/song.mp3 with Graceful Fallback)
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
        if (statusText) statusText.textContent = 'Playing your Rakhi surprise ♪';
      }).catch(() => {
        // Fallback if song.mp3 is missing
        if (statusText) statusText.textContent = 'Happy Raksha Bandhan, Prerna! ❤️';
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
  // 4. STORY ROUTER (18-Scene Sequential Navigation Engine)
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
        barFill.style.width = `${Math.max(5.5, percent)}%`;
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

        // Trigger scene-specific animations
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
      } else if (index === 3) {
        setTimeout(() => {
          const input = document.getElementById('input-user-age');
          if (input) input.focus();
        }, 300);
      } else if (index === 12) {
        startScorecardCounters();
      } else if (index === 13) {
        startShayariSequence();
      } else if (index === 14) {
        startEmotionalSequence();
      } else if (index === 16) {
        startSuspenseSequence();
      } else if (index === 18) {
        triggerGrandCelebration();
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
  // 5. SCENE SPECIFIC LOGIC & CONTROLLERS
  // ==========================================================================

  // --- Scene 1: Secret Entry Sequence ---
  function startScene1Sequence() {
    const l1 = document.getElementById('s1-line-1');
    const l2 = document.getElementById('s1-line-2');
    const l3 = document.getElementById('s1-line-3');
    const act = document.getElementById('s1-action-wrap');

    if (l1) l1.style.opacity = '0';
    if (l2) l2.style.opacity = '0';
    if (l3) l3.style.opacity = '0';
    if (act) act.style.opacity = '0';

    setTimeout(() => { if (l1) { l1.style.transition = 'opacity 0.8s ease'; l1.style.opacity = '1'; } }, 300);
    setTimeout(() => { if (l2) { l2.style.transition = 'opacity 0.8s ease'; l2.style.opacity = '1'; } }, 1800);
    setTimeout(() => { if (l3) { l3.style.transition = 'opacity 0.8s ease'; l3.style.opacity = '1'; } }, 3200);
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
        ParticleEngine.fireConfetti(window.innerWidth / 2, window.innerHeight / 2, 45);
        StoryRouter.goToScreen(2, 'next');
      };
    }
  }

  // --- Scene 2: Name Check & Scanning ---
  function setupScene2() {
    const form = document.getElementById('form-name-check');
    const input = document.getElementById('input-user-name');
    const feedback = document.getElementById('name-validation-msg');
    const terminal = document.getElementById('scanning-terminal');
    const barFill = document.getElementById('scan-bar-fill');
    const btnWrap = document.getElementById('name-btn-wrap');

    if (form && input) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const val = input.value.trim().toLowerCase();

        if (val === 'prerna' || val === 'prerna gupta') {
          feedback.textContent = '';
          if (btnWrap) btnWrap.style.display = 'none';
          if (terminal) terminal.style.display = 'block';
          SoundEngine.playPop();

          setTimeout(() => { if (barFill) barFill.style.width = '100%'; }, 100);

          setTimeout(() => {
            feedback.className = 'validation-feedback success';
            feedback.textContent = "Identity confirmed. Yep. It's you. 🌸";
            SoundEngine.playChime();
            setTimeout(() => {
              StoryRouter.goToScreen(3, 'next');
            }, 1000);
          }, 1400);

        } else if (val.length === 0) {
          feedback.className = 'validation-feedback error';
          feedback.textContent = 'Please enter your name first!';
        } else {
          feedback.className = 'validation-feedback error';
          feedback.textContent = "Hmm... nice try. I don't think you're Prerna. 🤨";
          input.classList.add('error');
          setTimeout(() => input.classList.remove('error'), 500);
        }
      });
    }
  }

  // --- Scene 3: Age Check & Stats ---
  function setupScene3() {
    const form = document.getElementById('form-age-check');
    const input = document.getElementById('input-user-age');
    const feedback = document.getElementById('age-validation-msg');
    const statsGrid = document.getElementById('age-stats-grid');
    const btnWrap = document.getElementById('age-btn-wrap');
    const successNextWrap = document.getElementById('age-success-next-wrap');
    const btnNext = document.getElementById('btn-age-next');

    if (form && input) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const val = input.value.trim();

        if (val === '23') {
          feedback.className = 'validation-feedback success';
          feedback.textContent = '23 years of arguments, laughter, chaos and memories! 🏆';
          SoundEngine.playChime();
          if (btnWrap) btnWrap.style.display = 'none';
          if (statsGrid) statsGrid.style.display = 'grid';
          if (successNextWrap) successNextWrap.style.display = 'flex';
        } else if (val.length === 0) {
          feedback.className = 'validation-feedback error';
          feedback.textContent = 'Please enter your age!';
        } else {
          feedback.className = 'validation-feedback error';
          feedback.textContent = 'That answer seems suspicious. 🤔';
          input.classList.add('error');
          setTimeout(() => input.classList.remove('error'), 500);
        }
      });
    }

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        StoryRouter.goToScreen(4, 'next');
      });
    }
  }

  // --- Scene 4: The First Trick Question ---
  function setupScene4() {
    const buttons = document.querySelectorAll('#s4-options-list .quiz-option-btn');
    const feedbackBox = document.getElementById('s4-feedback-box');
    const feedbackText = document.getElementById('s4-feedback-text');
    const btnNext = document.getElementById('btn-s4-next');

    buttons.forEach((btn) => {
      btn.addEventListener('click', function () {
        SoundEngine.playPop();
        const reaction = this.getAttribute('data-reaction');
        if (feedbackBox && feedbackText) {
          feedbackText.textContent = reaction;
          feedbackBox.style.display = 'block';
        }
      });
    });

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        StoryRouter.goToScreen(5, 'next');
      });
    }
  }

  // --- Scene 5: Sibling Rapid Fire (7 Questions) ---
  const rapidFireQuestions = [
    { q: "Who gets angry first?", r: "A volcanic temper disguised as innocence. 😂" },
    { q: "Who says 'I'm not hungry' and then eats your food?", r: "The universal sister tax applied instantly! 🍟" },
    { q: "Who is more dramatic?", r: "Academy Award nomination pending for daily sibling drama. 🎭" },
    { q: "Who apologizes first after a fight?", r: "Apologies are hard, but sending memes is our treaty. 🤝" },
    { q: "Who would survive longer without talking to the other?", r: "Spoiler: neither of us can last 24 hours. 📱" },
    { q: "Who is secretly more emotional?", r: "Behind the banter, pure heart. ❤️" },
    { q: "Who is mom's favorite?", r: "Whoever isn't causing chaos in the kitchen right now. 🤫" }
  ];
  let rapidIndex = 0;

  function setupScene5() {
    const qTitle = document.getElementById('rapid-question-title');
    const stepBadge = document.getElementById('rapid-step-badge');
    const choiceButtons = document.querySelectorAll('#rapid-options-row .btn-choice-pill');
    const feedbackBox = document.getElementById('rapid-feedback-box');
    const feedbackText = document.getElementById('rapid-feedback-text');
    const btnNext = document.getElementById('btn-rapid-next');
    const btnLabel = document.getElementById('rapid-btn-label');

    function renderQuestion(idx) {
      if (qTitle) qTitle.textContent = rapidFireQuestions[idx].q;
      if (stepBadge) stepBadge.textContent = `Question ${idx + 1} of ${rapidFireQuestions.length}`;
      if (feedbackBox) feedbackBox.style.display = 'none';
      if (btnLabel) btnLabel.textContent = idx === rapidFireQuestions.length - 1 ? 'Finish Rapid Fire' : 'Next Question';
    }

    choiceButtons.forEach((btn) => {
      btn.addEventListener('click', () => {
        SoundEngine.playPop();
        if (feedbackBox && feedbackText) {
          feedbackText.textContent = rapidFireQuestions[rapidIndex].r;
          feedbackBox.style.display = 'block';
        }
      });
    });

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        SoundEngine.playChime();
        if (rapidIndex < rapidFireQuestions.length - 1) {
          rapidIndex++;
          renderQuestion(rapidIndex);
        } else {
          StoryRouter.goToScreen(6, 'next');
        }
      });
    }
  }

  // --- Scene 6: Would You Rather ---
  function setupScene6() {
    const cardA = document.getElementById('wyr-card-a');
    const cardB = document.getElementById('wyr-card-b');
    const feedbackBox = document.getElementById('wyr-feedback-box');
    const feedbackText = document.getElementById('wyr-feedback-text');
    const btnNext = document.getElementById('btn-wyr-next');

    function selectCard(card, text) {
      SoundEngine.playPop();
      if (cardA) cardA.classList.remove('selected');
      if (cardB) cardB.classList.remove('selected');
      card.classList.add('selected');

      if (feedbackBox && feedbackText) {
        feedbackText.textContent = text;
        feedbackBox.style.display = 'block';
      }
    }

    if (cardA) {
      cardA.addEventListener('click', () => {
        selectCard(cardA, 'A true sibling warrior! Fighting builds character. ⚔️😂');
      });
    }

    if (cardB) {
      cardB.addEventListener('click', () => {
        selectCard(cardB, 'Admitting I am right?! A miracle on Raksha Bandhan! 🏆✨');
      });
    }

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        StoryRouter.goToScreen(7, 'next');
      });
    }
  }

  // --- Scene 7: Memory Guessing Game ---
  function setupScene7() {
    const guessButtons = document.querySelectorAll('#guess-actions-row .btn-choice-pill');
    const photoFrame = document.getElementById('guess-photo-frame');
    const revealBox = document.getElementById('guess-reveal-box');
    const actionsRow = document.getElementById('guess-actions-row');
    const btnNext = document.getElementById('btn-guess-next');

    guessButtons.forEach((btn) => {
      btn.addEventListener('click', () => {
        SoundEngine.playChime();
        if (photoFrame) photoFrame.classList.add('revealed');
        if (actionsRow) actionsRow.style.display = 'none';
        if (revealBox) revealBox.style.display = 'block';
        ParticleEngine.fireConfetti(window.innerWidth / 2, window.innerHeight * 0.4, 40);
      });
    });

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        StoryRouter.goToScreen(8, 'next');
      });
    }
  }

  // --- Scenes 8–11: Photo Memory Progression ---
  function setupPhotoScenesNavigation() {
    const routes = [
      { btn: 'btn-scene-8-next', target: 9 },
      { btn: 'btn-scene-9-next', target: 10 },
      { btn: 'btn-scene-10-next', target: 11 },
      { btn: 'btn-scene-11-next', target: 12 },
      { btn: 'btn-scene-12-next', target: 13 }
    ];

    routes.forEach((r) => {
      const el = document.getElementById(r.btn);
      if (el) {
        el.addEventListener('click', () => {
          StoryRouter.goToScreen(r.target, 'next');
        });
      }
    });
  }

  // --- Scene 12: Brother vs Sister Scorecard Counters ---
  function startScorecardCounters() {
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

    setTimeout(() => { animateCounter('score-arg-prerna', 87, 800); animateCounter('score-arg-prakhar', 91, 800); }, 200);
    setTimeout(() => { animateCounter('score-food-prerna', 63, 800); animateCounter('score-food-prakhar', 42, 800); }, 600);
    setTimeout(() => { animateCounter('score-drama-prerna', 94, 800); animateCounter('score-drama-prakhar', 88, 800); }, 1000);
  }

  // --- Scene 13: Shayari Sequence & Easter Egg 2 ---
  let rakhiTapCount = 0;
  function startShayariSequence() {
    const lines = document.querySelectorAll('.shayari-line');
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
      }, (idx + 1) * 1200);
    });

    const btnNext = document.getElementById('btn-scene-13-next');
    if (btnNext) {
      btnNext.onclick = () => StoryRouter.goToScreen(14, 'next');
    }

    // Easter Egg 2: Tap Rakhi 5 times
    const mandala = document.getElementById('shayari-mandala');
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

  // --- Scene 14: Personal Message (Interactive line reveal on tap) ---
  let emoCurrentIndex = 0;
  function startEmotionalSequence() {
    emoCurrentIndex = 0;
    const lines = document.querySelectorAll('.emo-line');
    const actWrap = document.getElementById('emo-action-wrap');
    const hint = document.getElementById('emo-tap-hint');
    const container = document.getElementById('emotional-sequence');

    lines.forEach((l) => l.classList.remove('revealed'));
    if (actWrap) actWrap.style.display = 'none';
    if (hint) hint.style.display = 'block';

    // Reveal first line immediately
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
        if (e.target.closest('#btn-scene-14-next')) return;
        revealNextEmoLine();
      };
    }

    const btnNext = document.getElementById('btn-scene-14-next');
    if (btnNext) {
      btnNext.onclick = () => StoryRouter.goToScreen(15, 'next');
    }
  }

  // --- Scene 15: 3D Envelope & Handwritten Letter ---
  function setupScene15() {
    const envelope = document.getElementById('story-envelope');
    const waxSeal = document.getElementById('env-wax-seal');
    const openBtn = document.getElementById('btn-open-letter-trigger');
    const nextBtn = document.getElementById('btn-scene-15-next');
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

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        StoryRouter.goToScreen(16, 'next');
      });
    }
  }

  // --- Scene 16: Final Suspense Sequence ---
  function startSuspenseSequence() {
    const l1 = document.getElementById('su-line-1');
    const l2 = document.getElementById('su-line-2');
    const l3 = document.getElementById('su-line-3');
    const act = document.getElementById('su-action-wrap');

    if (l1) l1.style.opacity = '0';
    if (l2) l2.style.opacity = '0';
    if (l3) l3.style.opacity = '0';
    if (act) act.style.display = 'none';

    setTimeout(() => { if (l1) { l1.style.transition = 'opacity 0.8s ease'; l1.style.opacity = '1'; } }, 300);
    setTimeout(() => { if (l2) { l2.style.transition = 'opacity 0.8s ease'; l2.style.opacity = '1'; } }, 2000);
    setTimeout(() => { if (l3) { l3.style.transition = 'opacity 0.8s ease'; l3.style.opacity = '1'; } }, 3800);
    setTimeout(() => {
      if (act) {
        act.style.display = 'flex';
        act.style.animation = 'pop-in 0.6s var(--ease-spring)';
      }
    }, 5200);

    const btnReveal = document.getElementById('btn-reveal-rakhi-surprise');
    if (btnReveal) {
      btnReveal.onclick = () => StoryRouter.goToScreen(17, 'next');
    }
  }

  // --- Scene 17: Final Photo Reveal ---
  function setupScene17() {
    const btnNext = document.getElementById('btn-scene-17-next');
    if (btnNext) {
      btnNext.addEventListener('click', () => {
        StoryRouter.goToScreen(18, 'next');
      });
    }
  }

  // --- Scene 18: Music + Grand Finale Celebration ---
  function triggerGrandCelebration() {
    SoundEngine.playFanfare();
    MusicPlayer.play();

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

  function setupScene18() {
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
    ctx.fillText('Happy Raksha Bandhan, Prerna!', 600, 250);

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
  // 6. GLOBAL DOM READY
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
    setupScene7();
    setupPhotoScenesNavigation();
    setupScene15();
    setupScene17();
    setupScene18();
  });
})();
"""
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully generated script.js")


def generate_readme():
    content = """# 🌸 A Secret Surprise For Prerna ✨ (Happy Raksha Bandhan)

A cinematic, deeply personal, funny, and emotional **18-scene interactive Rakhi story/game experience** dedicated to **Prerna Gupta (Age 23)** from her brother **Prakhar**.

---

## 🎬 The 18 Cinematic Interactive Scenes

Each scene is a full-screen standalone chapter in an interactive story, progressing only as Prerna interacts:

```text
SCENE 01: SECRET ENTRY
Dark warm ambiance with floating golden stars.
"There is someone very special..." → "Someone who has been annoying her brother for 23 years." → "I think you know who I mean." → [ Enter the surprise ✨ ]

SCENE 02: NAME CHECK & SCANNING TERMINAL
"Tell me your name." Input with case-insensitive validation for "Prerna" / "Prerna Gupta".
Animated terminal scan: "Checking identity... ██████████ 100%" → "Identity confirmed. Yep. It's you."

SCENE 03: AGE CHECK & 23 YEARS STATS
Huge animated "23?" → "Is this really the age of my little sister?"
Input "23" unlocks birthday stats: [23 YEARS] [∞ MEMORIES] [∞ ARGUMENTS] [1 SISTER].

SCENE 04: THE FIRST TRICK QUESTION
"Who is the better sibling?" (Prerna / Prakhar / Obviously Prerna / This question is rigged) with witty responses.

SCENE 05: SIBLING RAPID FIRE (7 QUESTIONS)
One question on screen at a time with randomized sibling punchlines:
1. Who gets angry first?
2. Who says "I'm not hungry" and then eats your food?
3. Who is more dramatic?
4. Who apologizes first after a fight?
5. Who would survive longer without talking to the other?
6. Who is secretly more emotional?
7. Who is mom's favorite?

SCENE 06: WOULD YOU RATHER
Dynamic choice cards:
• "Fight with your brother every day" OR "Admit your brother is right once?"
• Selection animation & humorous sibling verdict.

SCENE 07: MEMORY GUESSING GAME
Blurred photo with lock icon → "Do you remember this?" [YES] [Obviously] [I have no idea]
On click, the blur melts away into crisp photo: "Caught you remembering!"

SCENE 08: PHOTO REVEAL 1 (PURE OBJECT-FIT: CONTAIN)
Uncropped personal photo (prerna-1.jpg) with ambient blurred backdrop.
"Some memories don't need an explanation."

SCENE 09: MEMORY 2 (PARTNERS IN CRIME)
Uncropped historic monument trip photo (prerna-2.jpg).
"Partners in crime. Historic expeditions & timeless poses 📸"

SCENE 10: MEMORY 3 (FOOD EXTORTION)
Pizza table treaty memory (prerna-3.jpg).
"Professional argument champion. What's on your plate is officially my snack tax 🍟"

SCENE 11: MEMORY 4 (SIBLING HUG)
Uncropped brother-sister hug (prerna-6.jpg).
"Annoying since day one... and still my favorite person ❤️"

SCENE 12: BROTHER VS SISTER SCORECARD
"The Official Prerna vs Prakhar Report"
Animated live counters ticking up:
• Arguments: Prerna 87 vs Prakhar 91
• Food stealing: Prerna 63 vs Prakhar 42
• Drama: Prerna 94 vs Prakhar 88
• Caring: Prerna ∞ vs Prakhar ∞
"Winner: Both of you. Unfortunately, you'll still have to tolerate each other."

SCENE 13: SHAYARI (DIL KI BAAT)
Warm dark background, golden floating particles, Devanagari font.
Original 3-part Hindi shayari revealed line by line with typewriter/fade animation.
Tap the Rakhi mandala 5 times for Easter Egg #2!

SCENE 14: PERSONAL EMOTIONAL MESSAGE
"Okay. No more jokes for a minute..."
Interactive tap-to-reveal lines:
"We've fought." → "We've annoyed each other." → "We've laughed at the stupidest things." → "We've grown up together." → "I'm genuinely lucky to have you as my sister."

SCENE 15: THE REALISTIC 3D ENVELOPE
3D interactive envelope with "P & P" wax seal.
Clicking breaks seal, opens flap, and slides out handwritten letter from Prakhar.

SCENE 16: FINAL SUSPENSE
Dark minimalist screen with timed pauses:
"Wait..." → 2s pause → "We're not done." → 2s pause → "There's one last thing." → [ Reveal My Rakhi Surprise ✨ ]

SCENE 17: FINAL PHOTO REVEAL
Uncropped together portrait (prerna-together.jpg) with golden glowing frame.
"Happy Raksha Bandhan, Prerna!" → "23 years of being an amazing sister." → "No matter how much we fight... you'll always be my sister." → "Love you always ❤️" → [ One final surprise ❤️ ]

SCENE 18: MUSIC + GRAND FINALE CELEBRATION
Golden fireworks, confetti explosion, floating hearts.
Custom Music Player for assets/song.mp3 (play/pause/volume/mute + Web Audio synth backup).
Interactive Diya lighting, Download Keepsake PNG card, and story replay!
```

---

## 🥚 Secret Easter Eggs

1. **Top Bar Button**: `🚫 Don't touch` → Click triggers: *"I literally told you not to touch it! +10 Sibling Chaos Points! 😂"*
2. **Scene 13 (Shayari)**: Tap the golden Rakhi mandala **5 times** → Unlocks *"+100 Sister Points! You found the secret Rakhi tap! 🪢"*
3. **Scene 18 (Finale)**: Clicking the together photo repeatedly spawns floating animated heart bubbles with soft pop sounds!

---

## 🛡️ Critical Photo Rule

- **Zero Cropping**: All personal photos (`prerna-1.jpg` to `prerna-6.jpg` and `prerna-together.jpg`) use `object-fit: contain !important;` with ambient blurred copies behind them.
- **Aspect Ratio**: Whether portrait or landscape, photos are 100% visible with zero cropped faces or distorted dimensions.

---

## 🚀 How to Run Locally

Open `index.html` directly in any web browser.

---

*Made with ❤️ by Prakhar for Prerna.*
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully generated README.md")

if __name__ == '__main__':
    generate_index_html()
    generate_style_css()
    generate_script_js()
    generate_readme()
    print("ALL FILES GENERATED SUCCESSFULLY!")



