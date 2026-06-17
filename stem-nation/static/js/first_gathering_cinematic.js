
/* VIS-5D — FIRST GATHERING LIVE CINEMATIC INTERFACE */

(() => {
  "use strict";

  const scene = document.getElementById("fgCinematic");

  if (!scene) {
    return;
  }

  const studentAvatar =
    document.getElementById("fgStudentAvatar");

  const studentName =
    document.getElementById("fgStudentName");

  const arrivalMessage =
    document.getElementById("fgArrivalMessage");

  // PHASE_1B_VISIBLE_SIGNAL_LOGIC
  const signalAssignmentTitle =
    document.getElementById("fgSignalAssignmentTitle");

  const signalAssignmentAdvisor =
    document.getElementById("fgSignalAssignmentAdvisor");

  const FIRST_SIGNAL_KEY = "stemNationFirstSignal";
  const FIRST_ADVISOR_KEY = "stemNationFirstAdvisor";

  const chamberStatus =
    document.getElementById("fgChamberStatus");

  const panels = Array.from(
    document.querySelectorAll(".fg-voice-panel")
  );

  const captionStage =
    document.getElementById("fgCaptionStage");

  const captionSpeaker =
    document.getElementById("fgCaptionSpeaker");

  const captionText =
    document.getElementById("fgVoiceCaption");

  const replayButton =
    document.getElementById("fgReplayButton");

  const captionButton =
    document.getElementById("fgCaptionButton");

  const muteButton =
    document.getElementById("fgMuteButton");

  const door =
    document.getElementById("fgDoorTarget");

  const doorState =
    document.getElementById("fgDoorState");

  const doorAction =
    document.getElementById("fgDoorAction");

  const doorInstruction =
    document.getElementById("fgDoorInstruction");

  const progressNodes = Array.from(
    document.querySelectorAll(".fg-progress-node")
  );

  const particles =
    document.getElementById("fgParticles");


  // VIS-5D-1A-R — IDENTITY RECOGNITION + DOOR ENTRY FOCUS

  const identityCard =
    document.getElementById("fgIdentityCard");

  const portraitConfirmation =
    document.getElementById("fgPortraitConfirmation");

  const avatarChoiceLabel =
    document.getElementById("fgAvatarChoiceLabel");

  function applyRecognitionMetadata(identity) {
    const isCustom =
      Boolean(identity?.customAvatar) ||
      String(identity?.avatarChoice || "")
        .toLowerCase()
        .includes("custom");

    if (portraitConfirmation) {
      portraitConfirmation.textContent =
        isCustom
          ? "Personal portrait confirmed"
          : "Academy portrait confirmed";
    }

    if (avatarChoiceLabel) {
      avatarChoiceLabel.textContent =
        identity?.avatarChoice ||
        (
          isCustom
            ? "Custom Avatar"
            : "Academy Avatar"
        );
    }
  }

  function renderFirstSignalAssignment() {
    let signal = null;

    try {
      signal = JSON.parse(
        window.localStorage.getItem(FIRST_SIGNAL_KEY) || "null"
      );
    } catch (error) {
      signal = null;
    }

    if (!signal || !signal.title || !signal.advisor) {
      signal = {
        id: "crossing",
        title: "Damaged Crossing",
        advisor: "Builder",
        summary:
          "A route has failed after severe weather. People and supplies may be cut off."
      };
    }

    if (signalAssignmentTitle) {
      signalAssignmentTitle.textContent = signal.title;
    }

    if (signalAssignmentAdvisor) {
      signalAssignmentAdvisor.textContent =
        `${signal.advisor} will respond first.`;
    }

    if (arrivalMessage) {
      arrivalMessage.textContent =
        `Assignment received: ${signal.title}.`;
    }

    window.localStorage.setItem(
      FIRST_ADVISOR_KEY,
      signal.advisor
    );
  }

  function beginIdentityRecognition() {
    const identity = resolveIdentity();

    applyIdentity();
    applyRecognitionMetadata(identity);
    renderFirstSignalAssignment();

    if (identityCard) {
      identityCard.classList.add("recognizing");
    }

    chamberStatus.textContent =
      "Identity recognition in progress";

    door.disabled = true;
    door.classList.remove("unlocked");

    doorState.textContent =
      "Identity recognition in progress";

    doorAction.textContent =
      "Please wait";

    doorInstruction.textContent =
      "The Council Hall will open when recognition is complete.";

    window.setTimeout(() => {
      if (identityCard) {
        identityCard.classList.remove("recognizing");
        identityCard.classList.add("recognition-complete");
      }

      chamberStatus.textContent =
        "Identity confirmed";
    }, 1500);

    window.setTimeout(() => {
      scene.classList.add("entry-ready");

      door.disabled = false;
      door.classList.add("unlocked");

      doorState.textContent =
        "Council Hall ready";

      doorAction.textContent =
        "Enter Council Hall";

      doorInstruction.textContent =
        "Your identity is confirmed. Enter when ready.";

      chamberStatus.textContent =
        "Council Hall ready";
    }, 2600);
  }

  const voices = [
    {
      speaker: "Unidentified voice — left signal",
      text:
        "The image changed overnight. " +
        "That boundary was not there before."
    },
    {
      speaker: "Unidentified voice — right signal",
      text:
        "It could be water, shadow, damage, or movement. " +
        "We should not assume."
    },
    {
      speaker: "Unidentified voice — central signal",
      text:
        "If we act too quickly, " +
        "we may lead people the wrong way."
    }
  ];

  const heard = new Set();

  let captionsEnabled = true;
  let muted = false;
  let fallbackTimer = null;

  function safeParse(value) {
    try {
      return JSON.parse(value);
    } catch {
      return null;
    }
  }

  function normalizeAvatarPath(value) {
    if (!value || typeof value !== "string") {
      return "";
    }

    if (
      value.startsWith("/") ||
      value.startsWith("http://") ||
      value.startsWith("https://") ||
      value.startsWith("data:")
    ) {
      return value;
    }

    if (value.startsWith("static/")) {
      return `/${value}`;
    }

    const avatarMatch =
      value.match(/avatar[_-]?(\d+)/i);

    if (avatarMatch) {
      const number =
        String(avatarMatch[1]).padStart(2, "0");

      return (
        "/static/avatars/student_choices/" +
        `avatar_${number}.png`
      );
    }

    return value;
  }

  function extractIdentityObject(value) {
    if (!value || typeof value !== "object") {
      return null;
    }

    const nested =
      value.studentIdentity ||
      value.identity ||
      value.student ||
      value.profile ||
      value;

    const name =
      nested.studentName ||
      nested.displayName ||
      nested.academyName ||
      nested.callsign ||
      nested.callSign ||
      nested.username ||
      nested.name ||
      "";

    const avatarValue =
      nested.avatarPath ||
      nested.avatarImage ||
      nested.studentAvatar ||
      nested.selectedAvatar ||
      nested.avatarChoice ||
      nested.portrait ||
      nested.avatar ||
      "";

    let avatarPath = "";

    if (typeof avatarValue === "string") {
      avatarPath =
        normalizeAvatarPath(avatarValue);
    } else if (
      avatarValue &&
      typeof avatarValue === "object"
    ) {
      avatarPath = normalizeAvatarPath(
        avatarValue.src ||
        avatarValue.path ||
        avatarValue.image ||
        avatarValue.filename ||
        ""
      );
    }

    if (!name && !avatarPath) {
      return null;
    }

    return {
      name: String(name || "").trim(),
      avatarPath
    };
  }

  function scanStorage(storage) {
    const preferredKeys = [
      "stemNationStudentIdentity",
      "stem_nation_student_identity",
      "academyIdentity",
      "studentIdentity",
      "stemNationIdentity"
    ];

    for (const key of preferredKeys) {
      const raw = storage.getItem(key);

      if (!raw) {
        continue;
      }

      const parsed = safeParse(raw);
      const identity =
        extractIdentityObject(parsed);

      if (identity) {
        return identity;
      }
    }

    for (
      let index = 0;
      index < storage.length;
      index += 1
    ) {
      const key = storage.key(index);

      if (!key) {
        continue;
      }

      const raw = storage.getItem(key);

      if (!raw) {
        continue;
      }

      const parsed = safeParse(raw);
      const identity =
        extractIdentityObject(parsed);

      if (identity) {
        return identity;
      }
    }

    return null;
  }

  function readLegacyRenderedIdentity() {
    const nameSelectors = [
      "#studentName",
      "#studentDisplayName",
      "#displayName",
      "#academyName",
      "[data-student-name]",
      ".student-name",
      ".academy-name"
    ];

    const avatarSelectors = [
      "#studentAvatar",
      "#identityAvatar",
      "#academyAvatar",
      "[data-student-avatar]",
      ".student-avatar img",
      ".identity-avatar img"
    ];

    let name = "";
    let avatarPath = "";

    for (const selector of nameSelectors) {
      const element =
        document.querySelector(selector);

      if (
        !element ||
        element.closest("#fgCinematic")
      ) {
        continue;
      }

      const value =
        element.value ||
        element.textContent ||
        "";

      if (String(value).trim()) {
        name = String(value).trim();
        break;
      }
    }

    for (const selector of avatarSelectors) {
      const element =
        document.querySelector(selector);

      if (
        !element ||
        element.closest("#fgCinematic")
      ) {
        continue;
      }

      const value =
        element.currentSrc ||
        element.src ||
        element.dataset?.src ||
        "";

      if (value) {
        avatarPath = value;
        break;
      }
    }

    if (!name && !avatarPath) {
      return null;
    }

    return {
      name,
      avatarPath
    };
  }

  function resolveIdentity() {
    const globalCandidates = [
      window.stemNationStudentIdentity,
      window.studentIdentity,
      window.academyIdentity
    ];

    for (const candidate of globalCandidates) {
      const identity =
        extractIdentityObject(candidate);

      if (identity) {
        return identity;
      }
    }

    const rendered =
      readLegacyRenderedIdentity();

    if (rendered) {
      return rendered;
    }

    const localIdentity =
      scanStorage(window.localStorage);

    if (localIdentity) {
      return localIdentity;
    }

    const sessionIdentity =
      scanStorage(window.sessionStorage);

    if (sessionIdentity) {
      return sessionIdentity;
    }

    return {
      name: "Academy Learner",
      avatarPath:
        "/static/avatars/student_choices/avatar_01.png"
    };
  }

  function applyIdentity() {
    const identity = resolveIdentity();

    const name =
      identity.name ||
      "Academy Learner";

    studentName.textContent = name;

    if (identity.avatarPath) {
      studentAvatar.src =
        identity.avatarPath;
    }

    studentAvatar.alt =
      `${name}'s selected Academy avatar`;

    arrivalMessage.textContent =
      `${name} has arrived at the First Gathering. ` +
      "Three unresolved signals are active.";
  }

  function createParticles() {
    const reducedMotion =
      window.matchMedia(
        "(prefers-reduced-motion: reduce)"
      ).matches;

    const count =
      reducedMotion
        ? 0
        : 28;

    for (
      let index = 0;
      index < count;
      index += 1
    ) {
      const particle =
        document.createElement("span");

      particle.className = "fg-particle";

      particle.style.left =
        `${Math.random() * 100}%`;

      particle.style.top =
        `${60 + Math.random() * 45}%`;

      particle.style.setProperty(
        "--duration",
        `${7 + Math.random() * 9}s`
      );

      particle.style.setProperty(
        "--delay",
        `${Math.random() * -14}s`
      );

      particle.style.setProperty(
        "--drift",
        `${-30 + Math.random() * 60}px`
      );

      particles.appendChild(particle);
    }
  }

  function cancelVoicePlayback() {
    if (fallbackTimer) {
      window.clearTimeout(fallbackTimer);
      fallbackTimer = null;
    }

    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }
  }

  function chooseVoice(index) {
    if (!("speechSynthesis" in window)) {
      return null;
    }

    const available =
      window.speechSynthesis.getVoices();

    if (!available.length) {
      return null;
    }

    const english = available.filter(
      (voice) =>
        /^en/i.test(voice.lang || "")
    );

    const pool =
      english.length
        ? english
        : available;

    return pool[index % pool.length] || null;
  }

  function completeVoice(index) {
    heard.add(index);

    const panel = panels[index];

    panel.classList.remove("active");
    panel.classList.add("complete");

    const state =
      panel.querySelector(".fg-signal-state");

    if (state) {
      state.textContent = "Signal reviewed";
    }

    chamberStatus.textContent =
      `${heard.size} of 3 signals reviewed`;

    updateProgress();

    if (heard.size === voices.length) {
      unlockDoor();
    }
  }

  function speakVoice(index) {
    cancelVoicePlayback();

    const item = voices[index];

    if (
      muted ||
      !("speechSynthesis" in window)
    ) {
      fallbackTimer =
        window.setTimeout(
          () => completeVoice(index),
          1400
        );

      return;
    }

    const utterance =
      new SpeechSynthesisUtterance(item.text);

    const selectedVoice =
      chooseVoice(index);

    if (selectedVoice) {
      utterance.voice = selectedVoice;
    }

    utterance.rate =
      index === 1
        ? 0.92
        : 0.88;

    utterance.pitch =
      index === 0
        ? 0.92
        : index === 1
          ? 1.04
          : 0.84;

    utterance.volume = 0.92;

    utterance.onend = () => {
      completeVoice(index);
    };

    utterance.onerror = () => {
      completeVoice(index);
    };

    window.speechSynthesis.speak(
      utterance
    );
  }

  function activateVoice(index) {
    cancelVoicePlayback();

    panels.forEach((panel) => {
      panel.classList.remove("active");

      const state =
        panel.querySelector(".fg-signal-state");

      if (
        state &&
        !panel.classList.contains("complete")
      ) {
        state.textContent =
          "Unresolved signal";
      }
    });

    const panel = panels[index];
    const item = voices[index];

    panel.classList.add("active");

    const state =
      panel.querySelector(".fg-signal-state");

    if (state) {
      state.textContent = "Signal playing";
    }

    captionSpeaker.textContent =
      item.speaker;

    captionText.textContent =
      item.text;

    chamberStatus.textContent =
      `Listening to signal ${index + 1}`;

    speakVoice(index);
  }

  function updateProgress() {
    const count = heard.size;

    progressNodes.forEach(
      (node, index) => {
        node.classList.remove(
          "active",
          "complete"
        );

        if (index === 0) {
          node.classList.add("complete");
          return;
        }

        if (index === 1) {
          if (count >= 1) {
            node.classList.add("complete");
          } else {
            node.classList.add("active");
          }

          return;
        }

        if (index === 2) {
          if (count === 3) {
            node.classList.add("complete");
          } else if (count >= 1) {
            node.classList.add("active");
          }

          return;
        }

        if (index === 3) {
          if (count === 3) {
            node.classList.remove("locked");
            node.classList.add("active");
          } else {
            node.classList.add("locked");
          }
        }
      }
    );
  }

  function unlockDoor() {
    door.disabled = false;
    door.classList.add("unlocked");

    doorState.textContent =
      "Council Hall access granted";

    doorAction.textContent =
      "Enter Council Hall";

    doorInstruction.textContent =
      "All three voices have been heard. " +
      "The inner chamber is waiting.";

    chamberStatus.textContent =
      "Council Hall unlocked";
  }

  function resetSequence() {
    cancelVoicePlayback();
    heard.clear();

    panels.forEach((panel) => {
      panel.classList.remove(
        "active",
        "complete"
      );

      const state =
        panel.querySelector(".fg-signal-state");

      if (state) {
        state.textContent =
          "Unresolved signal";
      }
    });

    door.disabled = true;
    door.classList.remove("unlocked");

    doorState.textContent =
      "Council Hall locked";

    doorAction.textContent =
      "Listen to all three voices";

    doorInstruction.textContent =
      "Hear all three voices before " +
      "entering Council Hall.";

    captionSpeaker.textContent =
      "An unidentified voice";

    captionText.textContent =
      "Select one of the three signals to listen.";

    chamberStatus.textContent =
      "Chamber active";

    progressNodes.forEach(
      (node, index) => {
        node.classList.remove(
          "active",
          "complete"
        );

        if (index === 0) {
          node.classList.add("complete");
        } else if (index === 1) {
          node.classList.add("active");
        }

        if (index === 3) {
          node.classList.add("locked");
        }
      }
    );
  }

  function enterCouncilHall() {
    if (door.disabled) {
      return;
    }

    cancelVoicePlayback();

    scene.classList.add("transitioning");

    chamberStatus.textContent =
      "Entering Council Hall";

    window.setTimeout(() => {
      window.location.href =
        "/council_stage";
    }, 1120);
  }

  function toggleCaptions() {
    captionsEnabled = !captionsEnabled;

    captionStage.classList.toggle(
      "hidden",
      !captionsEnabled
    );

    captionButton.setAttribute(
      "aria-pressed",
      String(captionsEnabled)
    );

    captionButton.textContent =
      captionsEnabled
        ? "Captions On"
        : "Captions Off";
  }

  function toggleMute() {
    muted = !muted;

    if (muted) {
      cancelVoicePlayback();
    }

    muteButton.setAttribute(
      "aria-pressed",
      String(muted)
    );

    muteButton.textContent =
      muted
        ? "Sound Off"
        : "Sound On";
  }

  panels.forEach((panel, index) => {
    panel.addEventListener(
      "click",
      () => activateVoice(index)
    );
  });

  replayButton.addEventListener(
    "click",
    resetSequence
  );

  captionButton.addEventListener(
    "click",
    toggleCaptions
  );

  muteButton.addEventListener(
    "click",
    toggleMute
  );

  door.addEventListener(
    "click",
    enterCouncilHall
  );

  document.addEventListener(
    "keydown",
    (event) => {
      if (
        event.key === "Enter" &&
        !door.disabled
      ) {
        enterCouncilHall();
      }
    }
  );

  studentAvatar.addEventListener(
    "error",
    () => {
      studentAvatar.src =
        "/static/avatars/student_choices/avatar_01.png";
    }
  );

  createParticles();

  window.setTimeout(
    beginIdentityRecognition,
    120
  );
})();
