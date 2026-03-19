class Civilization:
    def __init__(self, name):
        self.name = name
        self.population = 100
        self.food = 80
        self.wealth = 60
        self.technology = 40
        self.stability = 70

    def display_stats(self):
        print(f"\nCivilization: {self.name}")
        print(f"Population: {self.population}")
        print(f"Food: {self.food}")
        print(f"Wealth: {self.wealth}")
        print(f"Technology: {self.technology}")
        print(f"Stability: {self.stability}")

    def apply_event(self, event):

        if event == "River Flood":
            self.population -= 5
            self.food -= 10

        elif event == "Trade Caravan":
            self.wealth += 15

        elif event == "Harvest Festival":
            self.food += 10
            self.stability += 5

        elif event == "Border Dispute":
            self.stability -= 10

        elif event == "Mine Discovery":
            self.wealth += 10
            self.technology += 5

    def calculate_score(self):

        score = (
            self.population
            + self.food
            + self.wealth
            + self.technology
            + self.stability
        )

        return score