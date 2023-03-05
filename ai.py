from player import Player

class AI(Player):
    def __init__(self, gestures):
        Player.__init__(self, 'AI', gestures)