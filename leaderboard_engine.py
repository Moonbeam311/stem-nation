def calculate_score(civilization):

    score = (
        civilization.population
        + civilization.wealth
        + civilization.technology
        + civilization.stability
    )

    return score


def generate_leaderboard(civilizations):

    board = []

    for civ in civilizations:
        board.append((civ.name, calculate_score(civ)))

    board.sort(key=lambda x: x[1], reverse=True)

    return board
