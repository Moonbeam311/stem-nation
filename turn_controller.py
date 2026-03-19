"""
TURN CONTROLLER
Authoritative turn coordination layer for Nation Builder
"""

from simulation_engine import run_turn
from leaderboard_engine import generate_leaderboard
from victory_engine import check_victory
import contact_engine


def execute_turn(civilizations, decisions):
    """
    Centralized turn resolution
    """

    result = run_turn(civilizations, decisions)
    generate_leaderboard(civilizations)
    contact_engine.detect_contacts(civilizations)

    victory = check_victory(civilizations)

    return {
        "civilizations": civilizations,
        "result": result,
        "victory": victory
    }
