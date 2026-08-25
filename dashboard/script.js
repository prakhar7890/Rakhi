/**
 * PRAKHAR'S ADMIN DASHBOARD CONTROLLER
 */
const API_BASE = (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1")
  ? "http://localhost:8000"
  : "https://YOUR-RENDER-BACKEND.onrender.com";

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
      loginError.textContent = "Invalid password!";
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
        <td><strong>${s.answers_count}</strong> answers • <strong>${s.milestones_count || 0}</strong> milestones</td>
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
