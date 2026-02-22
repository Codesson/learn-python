/* =============================================
   Python Quest — Google Analytics 4 Tracking
   =============================================
   학습 퍼널 분석을 위한 커스텀 이벤트 모듈.
   GA4 Measurement ID: G-XXXXXXXXXX 를 실제 ID로 교체하세요.
   ============================================= */

const Analytics = (() => {
  function send(eventName, params = {}) {
    if (typeof gtag !== "function") return;
    gtag("event", eventName, params);
  }

  // ── 퍼널 단계 1: 앱 시작 ──
  function trackAppStart(mode) {
    send("app_start", {
      learning_mode: mode,
    });
  }

  // ── 퍼널 단계 2: 챕터 선택 ──
  function trackChapterSelect(chapter) {
    send("chapter_select", {
      chapter_id: chapter.id,
      chapter_number: chapter.number,
      chapter_title: chapter.title,
      part: chapter.part,
      part_title: chapter.partTitle,
    });
  }

  // ── 퍼널 단계 3: 섹션 이동 ──
  function trackSectionView(chapter, sectionIdx, totalSections) {
    send("section_view", {
      chapter_id: chapter.id,
      chapter_number: chapter.number,
      section_index: sectionIdx,
      section_total: totalSections,
      section_progress: Math.round(((sectionIdx + 1) / totalSections) * 100),
    });
  }

  // ── 퍼널 단계 4: 코드 실행 ──
  function trackCodeRun(chapter, sectionIdx, success) {
    send("code_run", {
      chapter_id: chapter ? chapter.id : "playground",
      chapter_number: chapter ? chapter.number : 0,
      section_index: sectionIdx,
      run_success: success,
    });
  }

  // ── 퍼널 단계 5: 섹션 완료 ──
  function trackSectionComplete(chapter, sectionIdx, totalSections) {
    send("section_complete", {
      chapter_id: chapter.id,
      chapter_number: chapter.number,
      section_index: sectionIdx,
      section_total: totalSections,
      section_progress: Math.round(((sectionIdx + 1) / totalSections) * 100),
    });
  }

  // ── 퍼널 단계 6: 챕터 완료 ──
  function trackChapterComplete(chapter, totalChapters) {
    send("chapter_complete", {
      chapter_id: chapter.id,
      chapter_number: chapter.number,
      chapter_title: chapter.title,
      part: chapter.part,
      chapters_completed: totalChapters,
    });
  }

  // ── 보조: 연습문제 시도 ──
  function trackExerciseAttempt(chapter, exerciseNumber) {
    send("exercise_attempt", {
      chapter_id: chapter.id,
      chapter_number: chapter.number,
      exercise_number: exerciseNumber,
    });
  }

  // ── 보조: 레벨업 ──
  function trackLevelUp(newLevel, totalXP) {
    send("level_up", {
      new_level: newLevel,
      total_xp: totalXP,
    });
  }

  // ── 보조: 학습 모드 전환 ──
  function trackModeToggle(newMode) {
    send("mode_toggle", {
      new_mode: newMode,
    });
  }

  // ── 보조: "에디터에 넣기" 클릭 ──
  function trackCodeLoad(chapter, sectionIdx) {
    send("code_load_to_editor", {
      chapter_id: chapter ? chapter.id : "unknown",
      section_index: sectionIdx,
    });
  }

  // ── 보조: 진행 초기화 ──
  function trackProgressReset() {
    send("progress_reset", {});
  }

  return {
    trackAppStart,
    trackChapterSelect,
    trackSectionView,
    trackCodeRun,
    trackSectionComplete,
    trackChapterComplete,
    trackExerciseAttempt,
    trackLevelUp,
    trackModeToggle,
    trackCodeLoad,
    trackProgressReset,
  };
})();
