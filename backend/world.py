class WorldState:
    def __init__(self, name, description, locations):
        self.name = name
        self.description = description
        self.locations = locations
        self.tension = 1
        self.events = []

    def increase_tension(self):
        self.tension += 1

    def log_event(self, event):
        self.events.append(event)