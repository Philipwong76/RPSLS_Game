class Player:
    def __init__(self, name, gestures):
        self.name = name
        self.points = 0
        self.gestures = gestures
        self.gesture = ""

    def chooseGesture(self):
        while self.gesture not in self.gestures:
            self.gesture = input("What gesture do you choose?")