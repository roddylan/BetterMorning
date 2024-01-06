class Mood:
    def __init__(self, label):
        self._label = label
        self._awake, self._emotion = label.split('-')
    
    def is_awake(self):
        return self._awake == "awake"

    def get_awake(self):
        return self._awake

    def get_emotion(self):
        return self._emotion

    def get_label(self):
        return self._label

    def __str__(self):
        return f"< Mood: {self.label} >"
    
    def __repr__(self):
        return f"< Mood: {self.label} >"
    