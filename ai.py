from player import Player
import random

class AI(Player):
    def __init__(self, gestures):
        Player.__init__(self, 'AI', gestures)

    def chooseGesture(self):
        gestureVal =  random.randint(0,4)
        self.gesture = self.gestures[gestureVal]