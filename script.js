/**
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
  // In production on Vercel, replace "https://YOUR-RENDER-BACKEND.onrender.com" below
  // with your actual live Render Web Service URL!
  // ==========================================================================
  const API_CONFIG = {
    BASE_URL: (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1")
      ? "http://localhost:8000"
      : "https://YOUR-RENDER-BACKEND.onrender.com" // <-- Replace with your Render URL
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
      if (!API_BASE || API_BASE.includes('YOUR-RENDER-BACKEND')) return false;
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
