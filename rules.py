class RuleEngine:
    def validate(self, action, world):
        if action["type"] == "steal":
            if not world.locations["Temple"]["treasure"]:
                return False, "Treasure already gone."
        return True, "Valid"