/* STEP_2C_ACADEMY_MISSION_RECORD_V1 */
(() => {
  "use strict";

  const RECORD_KEY = "stemNationMissionRecord";
  const IDENTITY_KEY = "stemNationStudentIdentity";
  const SIGNAL_KEY = "stemNationFirstSignal";
  const ADVISOR_KEY = "stemNationFirstAdvisor";
  const RANKING_KEY = "stemNationQuestionPriorityRankingV1";
  const REACTION_KEY = "stemNationAdvisorReactionV1";
  const DEBRIEF_KEY = "stemNationMissionDebriefV1";

  const STAGE_BY_PATH = {
    "/academy_identity": "Identity Chamber",
    "/academy_cinematic": "Journey Passage",
    "/academy_arrival": "Arrival Hall",
    "/first_gathering": "First Gathering",
    "/council_stage": "Council Hall",
    "/advisor_reactions": "Advisor Reflection Chamber",
    "/mission_debrief": "Mission Debrief"
  };

  function readJson(key, fallback = null) {
    try {
      const raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (error) {
      console.warn(`Could not read ${key}.`, error);
      return fallback;
    }
  }

  function writeJson(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.warn(`Could not save ${key}.`, error);
    }
  }

  function cleanName(value) {
    return String(value || "")
      .replace(/^New Arrival\s*/i, "")
      .replace(/^Academy Learner\s*/i, "")
      .trim();
  }

  function uniqueList(values) {
    return Array.from(new Set(values.filter(Boolean)));
  }

  function resolveCompletedStages(pathname, existingStages, data) {
    const stages = [...existingStages];

    if (data.identity) stages.push("Identity Chamber");
    if (data.signal) stages.push("Arrival Hall");
    if (data.firstAdvisor) stages.push("First Gathering");
    if (data.ranking.length) stages.push("Council Hall");
    if (data.reaction) stages.push("Advisor Reflection Chamber");
    if (data.debrief) stages.push("Mission Debrief");

    const currentStage = STAGE_BY_PATH[pathname];
    if (currentStage) stages.push(currentStage);

    return uniqueList(stages);
  }

  function deriveRecord() {
    const existing = readJson(RECORD_KEY, {});
    const identity = readJson(IDENTITY_KEY, null);
    const signal = readJson(SIGNAL_KEY, null);
    const rankingRecord = readJson(RANKING_KEY, null);
    const reaction = readJson(REACTION_KEY, null);
    const debrief = readJson(DEBRIEF_KEY, null);
    const storedAdvisor = localStorage.getItem(ADVISOR_KEY) || "";

    const learnerName = cleanName(
      identity?.teacherApprovedName ||
      identity?.approvedName ||
      identity?.name ||
      existing.learnerName
    ) || "Academy Learner";

    const firstAdvisor =
      storedAdvisor ||
      signal?.advisor ||
      existing.firstAdvisor ||
      "";

    const ranking = Array.isArray(rankingRecord?.ranking)
      ? rankingRecord.ranking
      : [];

    const currentPath = window.location.pathname;
    const data = {
      identity,
      signal,
      firstAdvisor,
      ranking,
      reaction,
      debrief
    };

    const completedStages = resolveCompletedStages(
      currentPath,
      Array.isArray(existing.completedStages) ? existing.completedStages : [],
      data
    );

    const councilLensesActivated = uniqueList([
      ...(Array.isArray(existing.councilLensesActivated)
        ? existing.councilLensesActivated
        : []),
      firstAdvisor
    ]);

    const chamberUnlocks = uniqueList([
      ...(Array.isArray(existing.chamberUnlocks)
        ? existing.chamberUnlocks
        : []),
      ...completedStages
    ]);

    const evidenceMarks = uniqueList([
      ...(Array.isArray(existing.evidenceMarks) ? existing.evidenceMarks : []),
      ranking.length ? "Useful Question" : "",
      reaction ? "Evidence Before Claim" : "",
      debrief ? "Plan Revised" : ""
    ]);

    const currentMissionStep =
      STAGE_BY_PATH[currentPath] ||
      existing.currentMissionStep ||
      "Academy Journey";

    return {
      version: 1,
      learnerName,
      portrait: identity?.portrait || identity?.fallback || existing.portrait || "",
      academyRank: existing.academyRank || "Chief Investigator in Training",
      currentSignal: signal || existing.currentSignal || null,
      firstAdvisor,
      completedStages,
      evidenceMarks,
      councilLensesActivated,
      chamberUnlocks,
      currentMissionStep,
      updatedAt: new Date().toISOString()
    };
  }

  function updateMissionRecord() {
    const record = deriveRecord();
    writeJson(RECORD_KEY, record);
    window.stemNationMissionRecord = record;
    window.dispatchEvent(
      new CustomEvent("stemNationMissionRecordUpdated", { detail: record })
    );
    return record;
  }

  window.STEMNationMissionRecord = {
    key: RECORD_KEY,
    update: updateMissionRecord,
    read: () => readJson(RECORD_KEY, null)
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", updateMissionRecord, {
      once: true
    });
  } else {
    updateMissionRecord();
  }
})();
