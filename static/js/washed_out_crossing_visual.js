/* ============================================================
   VIS-2B — Corrected Talking + Moving Advisor Prototype
   ============================================================ */

(function () {
  const limit = 3;
  const selected = [];

  const cards = Array.from(document.querySelectorAll("[data-woc-material]"));
  const countEl = document.querySelector("[data-woc-count]");
  const progressFill = document.querySelector("[data-woc-progress-fill]");
  const warning = document.querySelector("[data-woc-warning]");
  const checkpoint = document.querySelector("[data-woc-checkpoint]");
  const explainZone = document.querySelector("[data-woc-explain-zone]");
  const explainList = document.querySelector("[data-woc-explain-list]");
  const testBtn = document.querySelector("[data-woc-test]");
  const resetBtn = document.querySelector("[data-woc-reset]");
  const summary = document.querySelector("[data-woc-summary]");
  const summaryList = document.querySelector("[data-woc-summary-list]");
  const completeBanner = document.querySelector("[data-woc-complete]");
  const stage = document.querySelector(".woc-stage");
  const beginBtn = document.querySelector("[data-woc-begin]");
  const beginOverlay = document.querySelector("[data-woc-begin-overlay]");
  const guardianImg = document.querySelector("[data-woc-guardian-img]");
  let missionStarted = false;

  const advisor = document.querySelector("[data-woc-advisor]");
  const expression = document.querySelector("[data-woc-expression]");
  const speechText = document.querySelector("[data-woc-speech-text]");
  const speakBtn = document.querySelector("[data-woc-speak]");
  const stopSpeechBtn = document.querySelector("[data-woc-stop-speech]");
  const voiceStatus = document.querySelector("[data-woc-voice-status]");

  let currentLine = "";
  let typeTimer = null;

  function line(name, fallback) {
    if (!speechText) return fallback || "";
    const attr = `data-${name.replaceAll("_", "-")}-line`;
    return speechText.getAttribute(attr) || fallback || "";
  }

  function updateVoiceStatus(status, message) {
    if (!voiceStatus) return;
    voiceStatus.classList.remove("ready", "blocked", "unavailable");
    if (status) voiceStatus.classList.add(status);
    voiceStatus.textContent = message;
  }

  function checkVoiceAvailability() {
    if (!("speechSynthesis" in window) || !("SpeechSynthesisUtterance" in window)) {
      updateVoiceStatus("unavailable", "Voice not available in this browser");
      return false;
    }

    updateVoiceStatus("ready", "Voice ready — click Speak Aloud");
    return true;
  }

  function setGuardianImage(state) {
    if (!guardianImg) return;

    const neutral = guardianImg.dataset.neutralSrc || guardianImg.src;
    const alertSrc = guardianImg.dataset.alertSrc || neutral;
    const speakingSrc = guardianImg.dataset.speakingSrc || neutral;
    const successSrc = guardianImg.dataset.successSrc || neutral;

    if (state === "warning") guardianImg.src = alertSrc;
    else if (state === "speaking") guardianImg.src = speakingSrc;
    else if (state === "success") guardianImg.src = successSrc;
    else guardianImg.src = neutral;
  }

  function setAdvisorState(state) {
    setGuardianImage(state);
    if (!advisor) return;

    advisor.classList.remove("speaking", "warning", "success");

    if (state === "speaking") {
      advisor.classList.add("speaking");
      if (expression) expression.textContent = "💬";
    } else if (state === "warning") {
      advisor.classList.add("warning");
      if (expression) expression.textContent = "!";
      stage?.classList.remove("advisor-warning");
      void stage?.offsetWidth;
      stage?.classList.add("advisor-warning");
      setTimeout(() => stage?.classList.remove("advisor-warning"), 520);
    } else if (state === "success") {
      advisor.classList.add("success");
      stage?.classList.add("advisor-success");
      if (expression) expression.textContent = "✓";
    } else {
      if (expression) expression.textContent = "!";
    }
  }

  function typeAdvisor(text, state = "speaking") {
    // VIS-2E guard: do not type before mission begins
    if (!missionStarted) return;
    if (!speechText || !text) return;

    currentLine = text;
    clearInterval(typeTimer);
    speechText.textContent = "";
    speechText.classList.remove("done");
    setAdvisorState(state);

    let i = 0;
    typeTimer = setInterval(() => {
      speechText.textContent = text.slice(0, i + 1);
      i++;

      if (i >= text.length) {
        clearInterval(typeTimer);
        speechText.classList.add("done");

        if (state === "speaking") {
          setTimeout(() => setAdvisorState("idle"), 700);
        }
      }
    }, 24);
  }

  function speakCurrentLine() {
    if (!checkVoiceAvailability()) {
      showWarning("Voice is not available in this browser, but the advisor text still works.");
      return;
    }

    window.speechSynthesis.cancel();

    const text = currentLine || speechText?.textContent || line("intro", "");
    if (!text.trim()) return;

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 0.92;
    utterance.pitch = 0.95;
    utterance.volume = 1;

    setAdvisorState("speaking");

    utterance.onend = () => {
      setAdvisorState("idle");
      updateVoiceStatus("ready", "Voice ready — click Speak Aloud");
    };

    utterance.onerror = () => {
      setAdvisorState("idle");
      updateVoiceStatus("blocked", "Voice blocked — click page, then Speak Aloud");
      showWarning("Voice was blocked by the browser. Click anywhere on the page, then press Speak Aloud again.");
    };

    updateVoiceStatus("ready", "Speaking…");
    window.speechSynthesis.speak(utterance);
  }

  function stopSpeech() {
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }
    updateVoiceStatus("ready", "Voice ready — click Speak Aloud");
    setAdvisorState("idle");
  }

  function setProgress(percent) {
    if (progressFill) progressFill.style.width = `${percent}%`;
  }

  function showWarning(message) {
    if (!warning) return;
    warning.textContent = message;
    warning.classList.remove("active");
    void warning.offsetWidth;
    warning.classList.add("active");
  }

  function advisorWarning(message) {
    showWarning(message);
    typeAdvisor(line("limit_warning", message), "warning");
  }

  function advisorMissingReason(message) {
    showWarning(message);
    typeAdvisor(line("missing_reason", message), "warning");
  }

  function showCheckpoint(message) {
    if (!checkpoint) return;
    checkpoint.textContent = message;
    checkpoint.classList.add("active");
  }

  function buildExplanationFields() {
    if (!explainZone || !explainList) return;

    explainList.innerHTML = "";

    selected.forEach((id, index) => {
      const card = document.querySelector(`[data-woc-material="${id}"]`);
      const label = card ? card.dataset.wocLabel : id;
      const prompt = card ? card.dataset.wocPrompt : "Explain your choice.";

      const wrap = document.createElement("div");
      wrap.className = "woc-explain-card";
      wrap.innerHTML = `
        <label>${index + 1}. ${label}</label>
        <textarea data-woc-explanation="${id}" placeholder="${prompt}"></textarea>
      `;
      explainList.appendChild(wrap);
    });

    explainZone.classList.add("active");
    setProgress(60);
  }

  function updateCards() {
    cards.forEach(card => {
      const id = card.dataset.wocMaterial;
      const idx = selected.indexOf(id);
      const number = card.querySelector("[data-woc-choice-number]");

      card.classList.toggle("selected", idx !== -1);

      if (number) number.textContent = idx !== -1 ? idx + 1 : "";

      if (selected.length >= limit && idx === -1) {
        card.classList.add("locked");
      } else {
        card.classList.remove("locked");
      }
    });

    if (countEl) countEl.textContent = `${selected.length}/${limit}`;
    setProgress(Math.round((selected.length / limit) * 45));

    if (selected.length === 0) {
      showCheckpoint("Observe the damaged crossing. Choose only three priorities.");
      if (missionStarted) {
        typeAdvisor(line("intro", "The crossing is unstable. What should we protect first?"), "speaking");
      }
    } else if (selected.length < limit) {
      showCheckpoint(`Priority ${selected.length} recorded. Choose ${limit - selected.length} more.`);
      typeAdvisor(line("selecting", "Choose carefully. Only three priorities can guide this first survival plan."), "speaking");
    } else {
      showCheckpoint("Three priorities selected. Now explain why each choice matters.");
      typeAdvisor(line("explain", "Now defend your choices. Why do these priorities belong in your top three?"), "speaking");
      buildExplanationFields();
    }
  }

  function handleCardClick(card) {
    const id = card.dataset.wocMaterial;
    const already = selected.indexOf(id);

    if (already !== -1) {
      selected.splice(already, 1);
      explainZone?.classList.remove("active");
      summary?.classList.remove("active");
      completeBanner?.classList.remove("active");
      stage?.classList.remove("advisor-success");
      updateCards();
      return;
    }

    if (selected.length >= limit) {
      advisorWarning("Only three priorities may be selected. Remove one choice before adding another.");
      return;
    }

    selected.push(id);
    updateCards();
  }

  function testPlan() {
    if (selected.length !== limit) {
      advisorWarning("Select exactly three priorities before testing the plan.");
      return;
    }

    const textareas = Array.from(document.querySelectorAll("[data-woc-explanation]"));
    const missing = textareas.filter(t => !t.value.trim());

    if (missing.length) {
      advisorMissingReason("Explain why each selected priority matters before testing the plan.");
      missing[0].focus();
      return;
    }

    summaryList.innerHTML = "";

    textareas.forEach((textarea, index) => {
      const id = textarea.dataset.wocExplanation;
      const card = document.querySelector(`[data-woc-material="${id}"]`);
      const label = card ? card.dataset.wocLabel : id;

      const li = document.createElement("li");
      li.innerHTML = `<strong>${index + 1}. ${label}:</strong> ${textarea.value.trim()}`;
      summaryList.appendChild(li);
    });

    summary.classList.add("active");
    completeBanner.classList.add("active");
    showCheckpoint("Mission checkpoint complete. You selected, explained, and defended your survival priorities.");
    typeAdvisor(line("complete", "Checkpoint complete. You selected, explained, and defended your survival priorities."), "success");
    setProgress(100);
  }

  function resetMission() {
    stopSpeech();
    selected.splice(0, selected.length);
    if (explainList) explainList.innerHTML = "";
    explainZone?.classList.remove("active");
    summary?.classList.remove("active");
    completeBanner?.classList.remove("active");
    warning?.classList.remove("active");
    stage?.classList.remove("advisor-success", "advisor-warning");
    setProgress(0);
    updateCards();
  }

  function beginMission() {
    missionStarted = true;
    stage?.setAttribute("data-woc-mission-started", "true");
    beginOverlay?.classList.add("hidden");
    if (speechText) {
      speechText.textContent = "";
      speechText.classList.remove("done");
    }
    typeAdvisor(line("intro", "The crossing is unstable. What should we protect first?"), "speaking");
  }

  cards.forEach(card => card.addEventListener("click", () => {
    if (!missionStarted) {
      showWarning("Begin the mission first.");
      return;
    }
    handleCardClick(card);
  }));
  testBtn?.addEventListener("click", testPlan);
  resetBtn?.addEventListener("click", resetMission);
  beginBtn?.addEventListener("click", beginMission);
  speakBtn?.addEventListener("click", speakCurrentLine);
  stopSpeechBtn?.addEventListener("click", stopSpeech);

  checkVoiceAvailability();
  updateCards();

  console.log("VIS-2B advisor avatar present:", !!document.querySelector("[data-woc-advisor-avatar]"));
  console.log("VIS-2B speech synthesis available:", "speechSynthesis" in window);
})();
