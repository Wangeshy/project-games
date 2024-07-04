class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def play(self):
        raise NotImplementedError("Subclasses should implement this method.")
