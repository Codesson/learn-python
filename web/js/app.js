/* =============================================
   Python Quest — Main Application
   ============================================= */

const STORAGE_KEY = "python-quest-progress";
const XP_PER_SECTION = 10;
const XP_PER_EXERCISE = 25;
const XP_PER_CHAPTER = 50;
const XP_PER_LEVEL = 100;

const MODE_KEY = "python-quest-mode";
const JS_LINE_PATTERN = /^JS[\s:의와에]|JavaScript|Node\.js|\(JS[\s:의와에)]/;

// ── State ──────────────────────────────────────
const state = {
  pyodide: null,
  editor: null,
  currentChapter: null,
  currentSectionIdx: 0,
  sidebarOpen: true,
  mode: localStorage.getItem(MODE_KEY) || "python",
  progress: loadProgress(),
};

function loadProgress() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) return JSON.parse(saved);
  } catch (e) { /* ignore */ }
  return { xp: 0, completedSections: [], completedChapters: [], streak: 0, lastDate: null };
}

function saveProgress() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state.progress));
  } catch (e) { /* ignore */ }
}

// ── Initialization ─────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  applyMode(state.mode);
  initEditor();
  buildChapterList();
  bindEvents();
  updateStats();
  initPyodide();
});

async function initPyodide() {
  const bar = document.getElementById("load-progress");
  const status = document.getElementById("load-status");

  try {
    bar.style.width = "20%";
    status.textContent = "Pyodide 로딩 중...";

    state.pyodide = await loadPyodide({
      indexURL: "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/",
    });

    bar.style.width = "70%";
    status.textContent = "Python 환경 설정 중...";

    state.pyodide.runPython(`
import sys
import io
`);

    bar.style.width = "100%";
    status.textContent = "준비 완료!";

    await sleep(400);
    const loadingScreen = document.getElementById("loading-screen");
    loadingScreen.classList.add("fade-out");
    setTimeout(() => loadingScreen.remove(), 600);

    showIntro();
  } catch (err) {
    status.textContent = "Pyodide 로딩 실패 — 새로고침 해 주세요";
    console.error("Pyodide load error:", err);

    bar.style.width = "100%";
    bar.style.background = "var(--red)";

    await sleep(1500);
    const loadingScreen = document.getElementById("loading-screen");
    loadingScreen.classList.add("fade-out");
    setTimeout(() => loadingScreen.remove(), 600);

    showIntro();
  }
}

function showIntro() {
  const intro = document.getElementById("intro-screen");
  intro.classList.remove("hidden");

  const jsCheck = document.getElementById("intro-js-check");
  jsCheck.checked = state.mode === "js";

  document.getElementById("btn-start").addEventListener("click", () => {
    applyMode(jsCheck.checked ? "js" : "python");
    intro.classList.add("fade-out");
    document.getElementById("app").classList.remove("hidden");

    setTimeout(() => {
      intro.remove();
      state.editor.refresh();
    }, 500);

    const contentSections = getContentSections();
    if (contentSections.length === 0) {
      loadChapter(CHAPTERS_DATA[0]);
    }

    setTimeout(() => state.editor.refresh(), 150);
  });
}

// ── Mode Toggle ────────────────────────────────
function applyMode(mode) {
  state.mode = mode;
  localStorage.setItem(MODE_KEY, mode);
  document.body.classList.toggle("mode-python", mode === "python");
  document.body.classList.toggle("mode-js", mode === "js");

  const icon = document.getElementById("mode-toggle-icon");
  const label = document.getElementById("mode-toggle-label");
  const btn = document.getElementById("btn-mode-toggle");
  if (icon && label && btn) {
    icon.textContent = mode === "js" ? "🔀" : "🐣";
    label.textContent = mode === "js" ? "JS 비교" : "Python";
    btn.classList.toggle("js-mode", mode === "js");
  }

  if (state.currentChapter) renderSection();
}

function toggleMode() {
  applyMode(state.mode === "js" ? "python" : "js");
  const msg = state.mode === "js"
    ? "🔀 JS 개발자 모드: JavaScript와 비교하며 학습합니다"
    : "🐣 순수 Python 모드: 파이썬에 집중합니다";
  showToast(msg, "");
}

function isJsLine(text) {
  return JS_LINE_PATTERN.test(text.trim());
}

function initEditor() {
  state.editor = CodeMirror(document.getElementById("editor-container"), {
    value: '# 코드를 작성하고 ▶ 실행 버튼을 눌러보세요!\nprint("Hello, Python Quest!")\n',
    mode: "python",
    theme: "dracula",
    lineNumbers: true,
    matchBrackets: true,
    autoCloseBrackets: true,
    indentUnit: 4,
    tabSize: 4,
    indentWithTabs: false,
    lineWrapping: true,
    extraKeys: {
      "Ctrl-Enter": runCode,
      "Cmd-Enter": runCode,
      "Ctrl-/": "toggleComment",
      "Cmd-/": "toggleComment",
    },
  });
}

// ── Chapter List ───────────────────────────────
function buildChapterList() {
  const container = document.getElementById("chapter-list");
  let currentPart = 0;

  CHAPTERS_DATA.forEach((ch) => {
    if (ch.part !== currentPart) {
      currentPart = ch.part;
      const group = document.createElement("div");
      group.className = "part-group";
      group.innerHTML = `<div class="part-header">${ch.partIcon} Part ${ch.part}: ${ch.partTitle}</div>`;
      container.appendChild(group);
    }

    const item = document.createElement("div");
    item.className = "chapter-item";
    item.dataset.id = ch.id;

    const isCompleted = state.progress.completedChapters.includes(ch.id);
    if (isCompleted) item.classList.add("completed");

    item.innerHTML = `
      <span class="ch-num">${ch.number}.</span>
      <span class="ch-name">${ch.title}</span>
      <span class="ch-status">${isCompleted ? "✅" : "○"}</span>
    `;

    item.addEventListener("click", () => loadChapter(ch));
    container.lastElementChild.appendChild(item);
  });
}

// ── Load Chapter ───────────────────────────────
function loadChapter(chapter) {
  state.currentChapter = chapter;
  state.currentSectionIdx = 0;

  document.getElementById("chapter-badge").textContent = `CH.${String(chapter.number).padStart(2, "0")}`;
  document.getElementById("chapter-title").textContent = chapter.title;

  document.querySelectorAll(".chapter-item").forEach((el) => {
    el.classList.toggle("active", el.dataset.id === chapter.id);
  });

  renderSection();
  updateSectionNav();

  if (window.innerWidth <= 900) {
    toggleSidebar(false);
  }
}

function getContentSections() {
  if (!state.currentChapter) return [];
  if (state.mode === "python") {
    return state.currentChapter.sections.filter((s) => s.type !== "comparison");
  }
  return state.currentChapter.sections;
}

function renderSection() {
  const ch = state.currentChapter;
  if (!ch) return;

  const sections = getContentSections();
  const section = sections[state.currentSectionIdx];
  if (!section) return;

  const container = document.getElementById("learning-content");
  container.innerHTML = "";

  const block = document.createElement("div");
  block.className = "section-block";
  block.dataset.type = section.type;

  const sectionKey = `${ch.id}:${state.currentSectionIdx}`;
  const isDone = state.progress.completedSections.includes(sectionKey);

  if (section.type === "comparison") {
    block.innerHTML = `
      <div class="section-title">
        <span class="section-check ${isDone ? "done" : ""}" data-key="${sectionKey}">
          ${isDone ? "✅" : "⬜"}
        </span>
        📊 ${section.title}
      </div>
      <div class="comparison-block">${escapeHtml(section.blocks[0]?.content || "")}</div>
    `;
  } else if (section.type === "exercise") {
    let html = `
      <div class="section-title">
        <span class="section-check ${isDone ? "done" : ""}" data-key="${sectionKey}">
          ${isDone ? "✅" : "⬜"}
        </span>
        🏆 ${section.title}
      </div>
    `;
    (section.exercises || []).forEach((ex) => {
      html += `
        <div class="exercise-card">
          <div class="exercise-header">
            <span class="exercise-badge">연습 ${ex.number}</span>
            <span class="exercise-xp">+${XP_PER_EXERCISE} XP</span>
          </div>
          <div class="exercise-desc">${escapeHtml(ex.description)}</div>
          <button class="exercise-try-btn" data-exercise="${ex.number}">도전하기 →</button>
        </div>
      `;
    });
    block.innerHTML = html;
  } else {
    let html = `
      <div class="section-title">
        <span class="section-check ${isDone ? "done" : ""}" data-key="${sectionKey}">
          ${isDone ? "✅" : "⬜"}
        </span>
        ${section.title}
      </div>
    `;
    (section.blocks || []).forEach((b, bi) => {
      if (b.type === "text") {
        html += renderTextBlock(b.content);
      } else if (b.type === "code") {
        const highlighted = hljs.highlight(b.content, { language: "python" }).value;
        html += `
          <div class="content-code-wrapper">
            <pre><code class="language-python">${highlighted}</code></pre>
            <button class="try-btn" data-code-idx="${bi}">에디터에 넣기 →</button>
          </div>
        `;
      }
    });

    if (section.code) {
      html += `
        <div style="margin-top: 16px; text-align: right;">
          <button class="action-btn primary run-section-btn" style="display:inline-flex;">
            ▶ 이 섹션 전체 실행
          </button>
        </div>
      `;
    }
    block.innerHTML = html;
  }

  container.appendChild(block);

  block.querySelectorAll(".try-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const idx = parseInt(btn.dataset.codeIdx);
      const codeBlock = section.blocks[idx];
      if (codeBlock) loadCodeToEditor(codeBlock.content);
    });
  });

  block.querySelectorAll(".run-section-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      if (section.code) {
        loadCodeToEditor(section.code);
        setTimeout(runCode, 200);
      }
    });
  });

  block.querySelectorAll(".exercise-try-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const exNum = btn.dataset.exercise;
      const ex = section.exercises.find((e) => e.number === parseInt(exNum));
      const template = `# 연습 ${exNum}: ${(ex?.description || "").split("\n")[0]}\n# 아래에 코드를 작성하세요!\n\n`;
      loadCodeToEditor(template);
    });
  });

  block.querySelectorAll(".section-check").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.key;
      toggleSectionComplete(key);
    });
  });
}

function updateSectionNav() {
  const sections = getContentSections();
  const total = sections.length;
  const idx = state.currentSectionIdx;

  document.getElementById("section-indicator").textContent = `${idx + 1} / ${total}`;
  document.getElementById("prev-section").disabled = idx === 0;
  document.getElementById("next-section").disabled = idx >= total - 1;
}

// ── Code Execution ─────────────────────────────
async function runCode() {
  if (!state.pyodide) {
    showToast("⏳ Python 엔진이 아직 로딩 중입니다...", "");
    return;
  }

  const code = state.editor.getValue();
  if (!code.trim()) return;

  const terminal = document.getElementById("terminal-output");
  const statusEl = document.getElementById("exec-status");
  const runBtn = document.getElementById("btn-run");

  terminal.innerHTML = "";
  statusEl.textContent = "실행 중...";
  statusEl.className = "exec-status running";
  runBtn.classList.add("running");
  runBtn.innerHTML = "⏳ 실행 중...";

  const codeStr = JSON.stringify(code);

  const setupCode = `
import sys, io

class _QuestStdout(io.StringIO):
    def __init__(self):
        super().__init__()
        self.parts = []
    def write(self, text):
        if text:
            self.parts.append(text)
        return len(text) if text else 0
    def flush(self):
        pass

_old_stdout = sys.stdout
_old_stderr = sys.stderr
_quest_out = _QuestStdout()
_quest_err = _QuestStdout()
sys.stdout = _quest_out
sys.stderr = _quest_err

def input(prompt=""):
    sys.stdout.write(prompt)
    return _quest_input_fn(prompt)

import builtins
builtins.input = input

_quest_exception = None
try:
    exec(${codeStr}, {"__builtins__": __builtins__, "input": input})
except Exception as _e:
    _quest_exception = str(_e)
    import traceback
    _quest_err.parts.append(traceback.format_exc())
finally:
    sys.stdout = _old_stdout
    sys.stderr = _old_stderr
`;

  state.pyodide.globals.set("_quest_input_fn", (prompt) => {
    return window.prompt(prompt || "입력하세요:") || "";
  });

  try {
    state.pyodide.runPython(setupCode);

    const stdout = state.pyodide.globals.get("_quest_out").parts.toJs();
    const stderr = state.pyodide.globals.get("_quest_err").parts.toJs();
    const exception = state.pyodide.globals.get("_quest_exception");

    stdout.forEach((text) => appendTerminal(text, "stdout"));
    stderr.forEach((text) => appendTerminal(text, "stderr"));

    if (exception) {
      statusEl.textContent = "오류 발생";
      statusEl.className = "exec-status error";
    } else {
      statusEl.textContent = "실행 완료";
      statusEl.className = "exec-status success";
      appendTerminal("\n✅ 실행이 완료되었습니다.", "success");
      markCurrentSectionDone();
    }
  } catch (err) {
    appendTerminal(err.message, "stderr");
    statusEl.textContent = "오류 발생";
    statusEl.className = "exec-status error";
  } finally {
    try {
      state.pyodide.runPython(`
try:
    del _quest_out, _quest_err, _quest_exception, _old_stdout, _old_stderr, _quest_input_fn
except:
    pass
`);
    } catch (e) { /* ignore cleanup errors */ }
    runBtn.classList.remove("running");
    runBtn.innerHTML = "▶ 실행";
  }
}

function appendTerminal(text, className) {
  const terminal = document.getElementById("terminal-output");
  const span = document.createElement("span");
  span.className = `term-line ${className}`;
  span.textContent = text;
  terminal.appendChild(span);
  terminal.scrollTop = terminal.scrollHeight;
}

function loadCodeToEditor(code) {
  state.editor.setValue(code);
  state.editor.focus();
  showToast("📝 코드가 에디터에 로드되었습니다!", "");
}

// ── Progress / XP System ───────────────────────
function markCurrentSectionDone() {
  if (!state.currentChapter) return;
  const key = `${state.currentChapter.id}:${state.currentSectionIdx}`;
  if (state.progress.completedSections.includes(key)) return;

  state.progress.completedSections.push(key);
  addXP(XP_PER_SECTION);
  checkChapterCompletion();
  saveProgress();
  updateStats();
  renderSection();
}

function toggleSectionComplete(key) {
  const idx = state.progress.completedSections.indexOf(key);
  if (idx >= 0) {
    state.progress.completedSections.splice(idx, 1);
  } else {
    state.progress.completedSections.push(key);
    addXP(XP_PER_SECTION);
  }
  checkChapterCompletion();
  saveProgress();
  updateStats();
  renderSection();
}

function checkChapterCompletion() {
  if (!state.currentChapter) return;
  const ch = state.currentChapter;
  const sections = getContentSections();
  const allDone = sections.every((_, i) =>
    state.progress.completedSections.includes(`${ch.id}:${i}`)
  );

  if (allDone && !state.progress.completedChapters.includes(ch.id)) {
    state.progress.completedChapters.push(ch.id);
    addXP(XP_PER_CHAPTER);
    showToast(`🎉 ${ch.title} 챕터 완료! +${XP_PER_CHAPTER} XP`, "achievement");

    const item = document.querySelector(`.chapter-item[data-id="${ch.id}"]`);
    if (item) {
      item.classList.add("completed");
      item.querySelector(".ch-status").textContent = "✅";
    }
  }
}

function addXP(amount) {
  const oldLevel = Math.floor(state.progress.xp / XP_PER_LEVEL) + 1;
  state.progress.xp += amount;
  const newLevel = Math.floor(state.progress.xp / XP_PER_LEVEL) + 1;

  if (amount <= XP_PER_SECTION) {
    showToast(`⭐ +${amount} XP`, "xp");
  }

  if (newLevel > oldLevel) {
    showLevelUp(newLevel);
  }

  updateStreak();
  saveProgress();
}

function updateStreak() {
  const today = new Date().toISOString().slice(0, 10);
  if (state.progress.lastDate === today) return;

  const yesterday = new Date(Date.now() - 86400000).toISOString().slice(0, 10);
  if (state.progress.lastDate === yesterday) {
    state.progress.streak += 1;
  } else if (state.progress.lastDate !== today) {
    state.progress.streak = 1;
  }
  state.progress.lastDate = today;
}

function updateStats() {
  const p = state.progress;
  const level = Math.floor(p.xp / XP_PER_LEVEL) + 1;
  const xpInLevel = p.xp % XP_PER_LEVEL;

  document.getElementById("level-badge").textContent = `Lv.${level}`;
  document.getElementById("xp-text").textContent = `${xpInLevel} / ${XP_PER_LEVEL} XP`;
  document.getElementById("xp-bar").style.width = `${(xpInLevel / XP_PER_LEVEL) * 100}%`;
  document.getElementById("completed-count").textContent = `✅ ${p.completedSections.length}`;
  document.getElementById("streak-badge").textContent = `🔥 ${p.streak}일`;

  const totalSections = CHAPTERS_DATA.reduce((s, ch) => s + ch.sections.length, 0);
  const pct = totalSections > 0 ? Math.round((p.completedSections.length / totalSections) * 100) : 0;
  document.getElementById("progress-percent").textContent = `${pct}%`;
  document.getElementById("progress-ring").setAttribute("stroke-dasharray", `${pct}, 100`);
}

function resetProgress() {
  if (!confirm("모든 학습 진행 상황(XP, 레벨, 완료 기록)이 초기화됩니다.\n정말 초기화할까요?")) return;

  state.progress = { xp: 0, completedSections: [], completedChapters: [], streak: 0, lastDate: null };
  saveProgress();
  updateStats();

  document.querySelectorAll(".chapter-item.completed").forEach((el) => {
    el.classList.remove("completed");
    el.querySelector(".ch-status").textContent = "○";
  });

  if (state.currentChapter) renderSection();

  showToast("🔄 진행 상황이 초기화되었습니다.", "");
}

// ── Toast & Level-up ───────────────────────────
function showToast(message, type) {
  const container = document.getElementById("toast-container");
  const toast = document.createElement("div");
  toast.className = `toast ${type}`;
  toast.textContent = message;
  container.appendChild(toast);

  setTimeout(() => {
    toast.classList.add("removing");
    setTimeout(() => toast.remove(), 300);
  }, 2500);
}

function showLevelUp(level) {
  const overlay = document.createElement("div");
  overlay.className = "level-up-overlay";
  overlay.innerHTML = `
    <div class="level-up-card">
      <div class="lu-icon">🎊</div>
      <h2>레벨 업!</h2>
      <p>Level ${level} 달성! 대단해요!</p>
    </div>
  `;
  document.body.appendChild(overlay);
  overlay.addEventListener("click", () => {
    overlay.style.animation = "fadeIn 0.3s ease reverse";
    setTimeout(() => overlay.remove(), 300);
  });
  setTimeout(() => {
    if (overlay.parentNode) {
      overlay.style.animation = "fadeIn 0.3s ease reverse";
      setTimeout(() => overlay.remove(), 300);
    }
  }, 3000);
}

// ── Event Bindings ─────────────────────────────
function bindEvents() {
  document.getElementById("sidebar-toggle").addEventListener("click", () => {
    toggleSidebar();
  });

  document.getElementById("btn-run").addEventListener("click", runCode);
  document.getElementById("btn-mode-toggle").addEventListener("click", toggleMode);

  document.getElementById("btn-clear").addEventListener("click", () => {
    state.editor.setValue('# 코드를 작성하세요\n\n');
    state.editor.focus();
  });

  document.getElementById("btn-reset").addEventListener("click", resetProgress);

  document.getElementById("btn-clear-terminal").addEventListener("click", () => {
    document.getElementById("terminal-output").innerHTML = "";
    document.getElementById("exec-status").textContent = "";
    document.getElementById("exec-status").className = "exec-status";
  });

  document.getElementById("prev-section").addEventListener("click", () => {
    if (state.currentSectionIdx > 0) {
      state.currentSectionIdx--;
      renderSection();
      updateSectionNav();
      document.getElementById("learning-content").scrollTop = 0;
    }
  });

  document.getElementById("next-section").addEventListener("click", () => {
    const sections = getContentSections();
    if (state.currentSectionIdx < sections.length - 1) {
      state.currentSectionIdx++;
      renderSection();
      updateSectionNav();
      document.getElementById("learning-content").scrollTop = 0;
    }
  });

  initResizeHandles();
  initKeyboardShortcuts();
}

function toggleSidebar(forceOpen) {
  const sidebar = document.getElementById("sidebar");
  const main = document.getElementById("main-content");
  const isWide = window.innerWidth > 900;

  if (typeof forceOpen === "boolean") {
    state.sidebarOpen = forceOpen;
  } else {
    state.sidebarOpen = !state.sidebarOpen;
  }

  if (isWide) {
    sidebar.classList.toggle("collapsed", !state.sidebarOpen);
    main.classList.toggle("expanded", !state.sidebarOpen);
  } else {
    sidebar.classList.toggle("open", state.sidebarOpen);
  }
}

function initResizeHandles() {
  const handle = document.getElementById("resize-handle");
  const leftPanel = document.getElementById("left-panel");
  const rightPanel = document.getElementById("right-panel");

  let startX, startLeftW, startRightW;

  handle.addEventListener("mousedown", (e) => {
    e.preventDefault();
    handle.classList.add("active");
    startX = e.clientX;
    startLeftW = leftPanel.offsetWidth;
    startRightW = rightPanel.offsetWidth;

    const onMove = (e) => {
      const dx = e.clientX - startX;
      const totalW = startLeftW + startRightW;
      const newLeft = Math.max(250, Math.min(totalW - 300, startLeftW + dx));
      leftPanel.style.flex = `0 0 ${newLeft}px`;
      rightPanel.style.flex = `1`;
    };
    const onUp = () => {
      handle.classList.remove("active");
      document.removeEventListener("mousemove", onMove);
      document.removeEventListener("mouseup", onUp);
      state.editor.refresh();
    };
    document.addEventListener("mousemove", onMove);
    document.addEventListener("mouseup", onUp);
  });

  const termHandle = document.getElementById("terminal-resize");
  const editorArea = document.getElementById("editor-area");
  const terminalArea = document.getElementById("terminal-area");

  termHandle.addEventListener("mousedown", (e) => {
    e.preventDefault();
    termHandle.classList.add("active");
    const startY = e.clientY;
    const startEditorH = editorArea.offsetHeight;
    const startTermH = terminalArea.offsetHeight;

    const onMove = (e) => {
      const dy = e.clientY - startY;
      const totalH = startEditorH + startTermH;
      const newEditorH = Math.max(100, Math.min(totalH - 80, startEditorH + dy));
      const newTermH = totalH - newEditorH;
      editorArea.style.flex = `0 0 ${newEditorH}px`;
      terminalArea.style.height = `${newTermH}px`;
    };
    const onUp = () => {
      termHandle.classList.remove("active");
      document.removeEventListener("mousemove", onMove);
      document.removeEventListener("mouseup", onUp);
      state.editor.refresh();
    };
    document.addEventListener("mousemove", onMove);
    document.addEventListener("mouseup", onUp);
  });
}

function initKeyboardShortcuts() {
  document.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
      e.preventDefault();
      runCode();
    }

    if (e.key === "ArrowLeft" && e.altKey) {
      e.preventDefault();
      document.getElementById("prev-section").click();
    }
    if (e.key === "ArrowRight" && e.altKey) {
      e.preventDefault();
      document.getElementById("next-section").click();
    }
  });
}

// ── Helpers ────────────────────────────────────
function renderTextBlock(content) {
  const lines = content.split("\n");
  let html = '<div class="content-text">';
  lines.forEach((line) => {
    const escaped = escapeHtml(line);
    if (isJsLine(line)) {
      html += `<span class="js-hint-line">${escaped}</span>\n`;
    } else {
      html += escaped + "\n";
    }
  });
  html += "</div>";
  return html;
}

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}
