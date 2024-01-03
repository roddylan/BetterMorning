from mood import Mood

class DefaultRoutine:
    def __init__(self):
        pass


class Routine(DefaultRoutine):
    def __init__(self, mood: Mood):
        self.mood = mood

    def __str__(self):
        return f"< Routine: {self.mood.label} >"