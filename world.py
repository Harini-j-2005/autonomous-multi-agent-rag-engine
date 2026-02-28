class WorldState:
    def __init__(self):
        self.locations = {
            "Temple": {
                "treasure": True,
                "security_level": 1
            }
        }

        self.tension = 0

        # NEW: Player State
        self.player = {
            "reputation": 0,
            "inventory": [],
            "status": "free"
        }

        self.events = []

    def log_event(self, event):
        self.events.append(event)

    def increase_tension(self, amount=1):
        self.tension += amount

    def increase_security(self):
        self.locations["Temple"]["security_level"] += 1

    def update_reputation(self, amount):
        self.player["reputation"] += amount