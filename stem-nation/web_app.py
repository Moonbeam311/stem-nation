 
from flask import Flask, render_template, request

app = Flask(__name__)

# STEM_NATION_DECISION_BRIDGE_ROUTE_ALIAS_V1
@app.route("/decision_bridge")
@app.route("/decision_bridge.html")
def decision_bridge():
    return render_template("decision_bridge.html")



@app.route("/council_stage")
def council_stage():
    return render_template("council_stage.html")


# =========================
# ZIP ENTRY (UNCHANGED)
# =========================
@app.route("/")
def landing():
    return render_template("landing.html")


# =========================
# CINEMATIC (ZIP FILES)
# =========================
@app.route("/intro1")
def intro1():
    return render_template("intro1.html")

@app.route("/intro2")
def intro2():
    return render_template("intro2.html")

@app.route("/intro3")
def intro3():
    return render_template("intro3.html")

@app.route("/intro4")
def intro4():
    return render_template("intro4.html")

@app.route("/intro5")
def intro5():
    return render_template("intro5.html")


# =========================
# WORLD SELECT (ZIP)
# =========================
@app.route("/world_select.html")
def world_select():
    return render_template("world_select.html")



@app.route("/environment_entry")
def environment_entry():
    world = request.args.get("world", "river")
    return render_template("environment_entry.html", world=world)


# =========================
# ACADEMY (ZIP)
# =========================
@app.route("/academy_individual")
def academy_individual():
    return render_template("academy_individual.html")


@app.route("/academy_memory_preview")
def academy_memory_preview():
    return render_template("academy_memory_preview.html")

@app.route("/academy_role")
def academy_role():
    return render_template("academy_role.html")

@app.route("/academy_thinking")
def academy_thinking():
    return render_template("academy_thinking.html")

@app.route("/academy_decision")
def academy_decision():
    return render_template("academy_decision.html")



# =========================
# SAFE PLACEHOLDERS
# =========================






@app.route("/teacher_dashboard")
def teacher_dashboard():
    return render_template("teacher_dashboard.html")

@app.route("/teacher_lesson_builder")
def teacher_lesson_builder():
    return render_template("teacher_lesson_builder.html")

@app.route("/teacher_packet_builder")
def teacher_packet_builder():
    return render_template("teacher_packet_builder.html")

@app.route("/teacher_facilitation_engine")
def teacher_facilitation_engine():
    return render_template("teacher_facilitation_engine.html")

@app.route("/teacher_resource_attach")
def teacher_resource_attach():
    return render_template("teacher_resource_attach.html")

@app.route("/teacher_resource_library")
def teacher_resource_library():
    return render_template("teacher_resource_library.html")

@app.route("/teacher")
def teacher():
    return render_template("teacher.html")


# =========================================================
# PHASE 7 STEP 1 — STEM NATION TEACHER DEMO ROUTES V1
# =========================================================
# STEM_NATION_TEACHER_DEMO_ROUTES_V1
@app.route("/teacher_demo")
def teacher_demo():
    return render_template("teacher_demo.html")

@app.route("/classroom_launch")
def classroom_launch():
    return render_template("classroom_launch.html")



# =========================================================
# PHASE 8 STEP 1 — STEM NATION CLASS SESSION ROUTES V1
# =========================================================
# STEM_NATION_CLASS_SESSION_ROUTES_V1
@app.route("/class_session")
def class_session():
    return render_template("class_session.html")

@app.route("/session_control")
def session_control():
    return render_template("session_control.html")


@app.route("/world_mission_1")
def world_mission_1():
    return render_template("world_mission_1.html")

@app.route("/map")
def map_mode():
    return render_template("map_mode.html")
@app.route("/partners")
def partners():
    return render_template("partners.html")

@app.route("/region_river")
def region_river():
    return render_template("region_river.html")










@app.route("/week2_survival_complete")
def week2_survival_complete():
    return render_template("week2_survival_complete.html")

@app.route("/week2_survival_print")
def week2_survival_print():
    return render_template("week2_survival_print.html")

@app.route("/week2_survival_archive")
def week2_survival_archive():
    return render_template("week2_survival_archive.html")

@app.route("/week2_survival_workspace")
def week2_survival_workspace():
    return render_template("week2_survival_workspace.html")

@app.route("/week2_survival_intro")
def week2_survival_intro():
    return render_template("week2_survival_intro.html")

@app.route("/founding_complete")
def founding_complete():
    return render_template("founding_complete.html")

@app.route("/founding_archive_print")
def founding_archive_print():
    return render_template("founding_archive_print.html")


@app.route("/project_hub")
def project_hub():
    return render_template("project_hub.html")

@app.route("/hub")
def hub():
    return render_template("student_hub.html")


# STEM_NATION_GAMEBOARD_GALLERY_ROUTE_V1
@app.route("/gameboard")
def gameboard():
    return render_template("gameboard.html")


# STEM_NATION_WORLD_BOARD_ROUTE_V1
@app.route("/world-board")
def world_board():
    return render_template("world_board.html")


# STEM_NATION_SCOUT_REGION_ROUTE_V1
@app.route("/scout/<region>")
def scout_region(region):
    return render_template("scout_region.html", region=region)


# STEM_NATION_BASELINE_INQUIRY_ROUTE_V1
@app.route("/academy_observation")
def academy_observation():
    return render_template("academy_observation.html")

@app.route("/mystery_deepens")
def mystery_deepens():
    return render_template("mystery_deepens.html")

@app.route("/question_justification")
def question_justification():
    return render_template("question_justification.html")

@app.route("/advisor_reactions")
def advisor_reactions():
    return render_template("advisor_reactions.html")

@app.route("/mission_debrief")
def mission_debrief():
    return render_template("mission_debrief.html")

@app.route("/baseline_inquiry")
def baseline_inquiry():
    return render_template("baseline_inquiry.html")


# STEM_NATION_ACADEMY_TRANSITION_ROUTE_V1
@app.route("/academy_transition")
def academy_transition():
    return render_template("academy_transition.html")

# STEM_NATION_AVATAR_MISSION_FIRST_QUESTION_ROUTES_V1
@app.route("/avatar_select")
def avatar_select():
    return render_template("avatar_select.html")

# STEM_NATION_AVATAR_CONFIRM_ROUTE_V1
@app.route("/avatar_confirm")
def avatar_confirm():
    return render_template("avatar_confirm.html")

@app.route("/mission_intro")
def mission_intro():
    return render_template("mission_intro.html")

@app.route("/first-question")
def first_question():
    return render_template("first_question.html")

# STEM_NATION_STEP6J_ROUTE_V1
@app.route("/washed_out_crossing_intro")
def washed_out_crossing_intro():
    return render_template("washed_out_crossing_intro.html")




# STEM_NATION_STUDENT_LANDING_ROUTE_V1
@app.route("/dev_reset")
def dev_reset():
    return render_template("dev_reset.html")

@app.route("/student")
def student_landing():
    return render_template("student_landing.html")


# STEM_NATION_BASELINE_INQUIRY_ORIGINAL_ARCHIVE_ROUTE_V1
@app.route("/baseline_inquiry_original")
def baseline_inquiry_original():
    return render_template("baseline_inquiry_original_archive.html")



@app.route("/teach-robot")
def teach_robot():
    return render_template("teach_robot.html")



@app.route("/literal-listener")
def literal_listener():
    return render_template("literal_listener.html")



@app.route("/backpack-lab")
def backpack_lab():
    return render_template("backpack_lab.html")

# STEM_NATION_BACKPACK_ADVANCED_ROUTE_V1
@app.route("/backpack-lab-advanced")
def backpack_lab_advanced():
    return render_template("backpack_lab_advanced.html")



@app.route("/river-crossing-lab")
def river_crossing_lab():
    return render_template("river_crossing_lab.html")
@app.route("/academy_opening")
def academy_opening():
    return render_template("academy_opening.html")

@app.route("/academy_identity")
@app.route("/student_identity")
def academy_identity():
    return render_template("academy_identity.html")


@app.route("/academy_threshold")
def academy_threshold():
    return render_template("academy_threshold.html")


@app.route("/academy_cinematic")
def academy_cinematic():
    return render_template("academy_cinematic.html")

@app.route("/academy_arrival")
def academy_arrival():
    return render_template("academy_arrival.html")

@app.route("/first_gathering")
def first_gathering():
    return render_template("first_gathering.html")













@app.route("/investigation_replay")
def investigation_replay():
    return render_template("investigation_replay.html")

@app.route("/mission_resolution")
def mission_resolution():
    return render_template("mission_resolution.html")

@app.route("/revise_or_act")
def revise_or_act():
    return render_template("revise_or_act.html")

@app.route("/test_the_claim")
def test_the_claim():
    return render_template("test_the_claim.html")

@app.route("/name_the_cause")
def name_the_cause():
    return render_template("name_the_cause.html")

@app.route("/evidence_comparison")
def evidence_comparison():
    return render_template("evidence_comparison.html")

@app.route("/evidence_review")
def evidence_review():
    return render_template("evidence_review.html")

@app.route("/council_reports")
def council_reports():
    return render_template("council_reports.html")

@app.route("/active_investigation")
def active_investigation():
    return render_template("active_investigation.html")

@app.route("/council_command_table")
def council_command_table():
    return render_template("council_command_table.html")

@app.route("/student_command_entry")
def student_command_entry():
    return render_template("student_command_entry.html")




@app.route("/student_hub")
def student_hub():
    return render_template("student_hub.html")



@app.route("/council_stage_clean")
def council_stage_clean():
    return render_template("council_stage_clean.html")

# VIS-1 — STEM Nation Visual Experience Layer Preview
@app.route("/visual_layer_preview")
def visual_layer_preview():
    return render_template("visual_layer_preview.html")

# VIS-2 — Washed-Out Crossing Illustrated Mission Prototype
@app.route("/washed_out_crossing_visual")
def washed_out_crossing_visual():
    import json
    from pathlib import Path

    mission_path = Path("data/washed_out_crossing_visual_mission.json")
    if mission_path.exists():
        mission = json.loads(mission_path.read_text(encoding="utf-8"))
    else:
        mission = {
            "title": "The Washed-Out Crossing",
            "subtitle": "Academy Readiness Evaluation",
            "advisor": {
                "name": "Guardian",
                "verb": "Protect",
                "question": "What should we protect first?"
            },
            "materials": []
        }

    asset_hooks = mission.get("asset_hooks", {})
    resolved_assets = {}
    for key, rel_path in asset_hooks.items():
        full_path = Path("static") / rel_path
        resolved_assets[key] = {
            "exists": full_path.exists(),
            "url": rel_path
        }

    return render_template(
        "washed_out_crossing_visual.html",
        mission=mission,
        resolved_assets=resolved_assets,
        visual_css_exists=Path("static/css/stem_nation_visual_layer.css").exists(),
        visual_js_exists=Path("static/js/stem_nation_visual_layer.js").exists()
    )

# VIS-3D — Advisor Animation Preview
@app.route("/advisor_animation_preview")
def advisor_animation_preview():
    import json
    from pathlib import Path

    registry_path = Path("data/stem_nation_animated_advisor_registry.json")
    registry = json.loads(registry_path.read_text(encoding="utf-8"))

    advisors = registry.get("advisors", {})
    for key, advisor in advisors.items():
        locked_face = advisor.get("locked_face_asset", "")
        fallback = advisor.get("fallback_asset", "")

        display_asset = locked_face or fallback

        advisor["display_asset"] = display_asset
        advisor["display_asset_exists"] = (Path("static") / display_asset).exists()
        advisor["fallback_exists"] = (Path("static") / fallback).exists()
        advisor["locked_face_exists"] = (Path("static") / locked_face).exists() if locked_face else False

    return render_template(
        "advisor_animation_pipeline_preview.html",
        advisors=advisors
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
# STEM_NATION_ACADEMY_ARRIVAL_ROUTE_V1
# STEM_NATION_OPENING_FLOW_ROUTES_V1
