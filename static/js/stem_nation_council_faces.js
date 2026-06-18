/* ============================================================
   VIS-4B — Shared Council Face Strip JS
   ============================================================ */

window.STEMNationCouncilFaces = {
  getCard(advisorName) {
    return document.querySelector(
      `[data-sn-council-advisor="${advisorName}"]`
    );
  },

  clearStates() {
    document.querySelectorAll("[data-sn-council-advisor]").forEach((card) => {
      card.classList.remove(
        "is-active",
        "is-speaking",
        "is-warning",
        "is-success"
      );

      const state = card.querySelector(".sn-council-face-state");
      if (state) state.textContent = "•";
    });
  },

  setState(advisorName, state) {
    const card = this.getCard(advisorName);
    if (!card) return;

    card.classList.remove(
      "is-speaking",
      "is-warning",
      "is-success"
    );

    card.classList.add("is-active");

    const stateElement = card.querySelector(".sn-council-face-state");

    const map = {
      idle: "•",
      speaking: "💬",
      warning: "!",
      success: "✓"
    };

    if (state && state !== "idle") {
      card.classList.add(`is-${state}`);
    }

    if (stateElement) {
      stateElement.textContent = map[state] || "•";
    }
  },

  activate(advisorName) {
    this.clearStates();
    this.setState(advisorName, "speaking");
  }
};
/* ============================================================
   VIS-4D — First Gathering Council Entrance Sequence
   ============================================================ */

(function () {
  const ADVISOR_SEQUENCE = [
    {
      key: "scout",
      name: "Scout",
      verb: "Discover",
      question: "What do we notice?"
    },
    {
      key: "mapkeeper",
      name: "Mapkeeper",
      verb: "Remember",
      question: "What do we know?"
    },
    {
      key: "builder",
      name: "Builder",
      verb: "Create",
      question: "What can we build?"
    },
    {
      key: "healer",
      name: "Healer",
      verb: "Restore",
      question: "What do people need?"
    },
    {
      key: "guardian",
      name: "Guardian",
      verb: "Protect",
      question: "What should we protect?"
    }
  ];

  const wait = (milliseconds) =>
    new Promise((resolve) => window.setTimeout(resolve, milliseconds));

  function createStatusElement(wrapper) {
    let status = wrapper.querySelector(
      "[data-first-gathering-council-status]"
    );

    if (status) return status;

    status = document.createElement("div");
    status.className = "first-gathering-council-status";
    status.setAttribute(
      "data-first-gathering-council-status",
      ""
    );
    status.setAttribute("aria-live", "polite");
    status.setAttribute("aria-atomic", "true");
    status.textContent = "The Inquiry Council is assembling.";

    const strip = wrapper.querySelector("[data-sn-council-strip]");

    if (strip) {
      strip.insertAdjacentElement("afterend", status);
    } else {
      wrapper.appendChild(status);
    }

    return status;
  }

  function resetCards(wrapper) {
    wrapper
      .querySelectorAll("[data-sn-council-advisor]")
      .forEach((card) => {
        card.classList.remove(
          "is-entered",
          "is-introducing",
          "is-active",
          "is-speaking",
          "is-warning",
          "is-success"
        );

        const badge = card.querySelector(
          ".sn-council-face-state"
        );

        if (badge) badge.textContent = "•";
      });
  }

  async function runFirstGatheringCouncilEntrance() {
    const wrapper = document.querySelector(
      "[data-first-gathering-council]"
    );

    if (!wrapper) return;

    const reducedMotion = window.matchMedia(
      "(prefers-reduced-motion: reduce)"
    ).matches;

    const status = createStatusElement(wrapper);

    resetCards(wrapper);
    wrapper.classList.add("is-sequencing");

    if (reducedMotion) {
      wrapper
        .querySelectorAll("[data-sn-council-advisor]")
        .forEach((card) => card.classList.add("is-entered"));

      status.innerHTML =
        "<strong>The Inquiry Council is assembled.</strong> " +
        "Their questions will guide your investigation.";

      status.classList.add("is-complete");
      wrapper.classList.remove("is-sequencing");
      return;
    }

    await wait(350);

    for (const advisor of ADVISOR_SEQUENCE) {
      const card = wrapper.querySelector(
        `[data-sn-council-advisor="${advisor.key}"]`
      );

      if (!card) continue;

      card.classList.add(
        "is-entered",
        "is-introducing",
        "is-active",
        "is-speaking"
      );

      const badge = card.querySelector(
        ".sn-council-face-state"
      );

      if (badge) badge.textContent = "💬";

      status.innerHTML =
        `<strong>${advisor.name} · ${advisor.verb}</strong> — ` +
        `${advisor.question}`;

      await wait(1150);

      card.classList.remove(
        "is-introducing",
        "is-active",
        "is-speaking"
      );

      if (badge) badge.textContent = "•";

      await wait(180);
    }

    wrapper.classList.remove("is-sequencing");

    status.innerHTML =
      "<strong>The Inquiry Council is assembled.</strong> " +
      "They will guide your questions, but the decisions remain yours.";

    status.classList.add("is-complete");

    wrapper
      .querySelectorAll("[data-sn-council-advisor]")
      .forEach((card) => card.classList.add("is-entered"));

    wrapper.dispatchEvent(
      new CustomEvent("stemnation:council-entrance-complete")
    );
  }

  window.STEMNationCouncilFaces =
    window.STEMNationCouncilFaces || {};

  window.STEMNationCouncilFaces.runFirstGatheringEntrance =
    runFirstGatheringCouncilEntrance;

  if (document.readyState === "loading") {
    document.addEventListener(
      "DOMContentLoaded",
      runFirstGatheringCouncilEntrance,
      { once: true }
    );
  } else {
    runFirstGatheringCouncilEntrance();
  }
})();
