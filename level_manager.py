class LevelManager:
    def __init__(self):
        self.current_level = 1
        self.level_objectives = {
            1: "Introduce the temple and treasure.",
            2: "NPC attempts first theft.",
            3: "Guardian reacts.",
            4: "Conflict escalates.",
            5: "Final outcome decided."
        }

    def get_objective(self):
        return self.level_objectives[self.current_level]

    def next_level(self):
        self.current_level += 1