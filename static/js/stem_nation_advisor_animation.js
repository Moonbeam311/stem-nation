/* ============================================================
   VIS-3C — STEM Nation Animated Advisor Shared JS
   ============================================================ */

window.STEMNationAdvisorAnimation = {
  setState(actor, state) {
    if (!actor) return;

    actor.classList.remove("idle", "speaking", "warning", "success");
    actor.classList.add(state || "idle");

    const badge = actor.querySelector("[data-sn-advisor-badge]");
    if (badge) {
      const symbols = {
        idle: "•",
        speaking: "💬",
        warning: "!",
        success: "✓"
      };
      badge.textContent = symbols[state] || "•";
    }
  },

  cyclePreview(actor) {
    if (!actor) return null;

    const states = ["idle", "speaking", "warning", "success"];
    let index = 0;

    this.setState(actor, states[index]);

    return setInterval(() => {
      index = (index + 1) % states.length;
      this.setState(actor, states[index]);
    }, 1700);
  }
};
