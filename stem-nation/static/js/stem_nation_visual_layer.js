/* ============================================================
   VIS-1 — STEM Nation Visual Experience Layer JS
   Purpose: simple reusable animation + selection helpers
   ============================================================ */

window.STEMNationVisual = {
  selectObject(card) {
    if (!card) return;
    card.classList.toggle("selected");
    this.flash(card);
  },

  flash(element) {
    if (!element) return;
    element.classList.remove("sn-anim-glow");
    void element.offsetWidth;
    element.classList.add("sn-anim-glow");
    setTimeout(() => element.classList.remove("sn-anim-glow"), 900);
  },

  shake(element) {
    if (!element) return;
    element.classList.remove("sn-anim-shake");
    void element.offsetWidth;
    element.classList.add("sn-anim-shake");
  },

  reveal(selector) {
    const el = document.querySelector(selector);
    if (!el) return;
    el.classList.remove("sn-hidden");
    el.classList.add("sn-anim-rise");
  },

  checkpoint(message) {
    const box = document.querySelector("[data-sn-checkpoint]");
    if (!box) return;
    box.textContent = message;
    box.classList.remove("sn-hidden");
    box.classList.add("sn-anim-rise");
  }
};

document.addEventListener("click", (event) => {
  const card = event.target.closest("[data-sn-object]");
  if (card) {
    window.STEMNationVisual.selectObject(card);
  }
});
