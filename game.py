from player import Player
from ai import AI

class gameplay:

    def playGame(self):
        gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        numPlayers = input("How many players are there? (1 or 2)")
        winnerFound = False
        if numPlayers == '1':
            player1 = Player("Player 1", gestures)
            AIPlayer = AI(gestures)
            while not winnerFound:
                print("Possible gestures: ", gestures)
                playerGesture = player1.chooseGesture()
                player1.gesture = playerGesture
                AIPlayer.chooseGesture()

                result = self.checkGestures(player1.gesture, AIPlayer.gesture)
                if result == 1:
                    player1.points += 1
                elif result == 2:
                    AIPlayer.points += 1
                
                if player1.points == 3:
                    winnerFound = True
                    print("Player 1 wins")

                if AIPlayer.points == 3:
                    winnerFound = True
                    print("AI wins")

        elif numPlayers == '2':
            player1 = Player("Player 1",gestures)
            player2 = Player("Player 2",gestures)
            while not winnerFound:
                print("Possible gestures: ", gestures)
                playerGesture = player1.chooseGesture()
                player1.gesture = playerGesture
                playerGesture = player2.chooseGesture()
                player2.gesture = playerGesture

                result = self.checkGestures(player1.gesture, player2.gesture)
                if result == 1:
                    player1.points += 1
                elif result == 2:
                    player2.points += 1
                
                if player1.points == 3:
                    winnerFound = True
                    print("Player 1 wins")

                if player2.points == 3:
                    winnerFound = True
                    print("Player 2 wins")

    def checkGestures(self, gesture1, gesture2):
        if gesture1 == gesture2:
            return 0
        if gesture1 == "rock":
            if gesture2 == "scissors" or "lizard":
                return 1
        elif gesture1 == "paper":
            if gesture2 == "rock" or "spock":
                return 1
        elif gesture1 == "scissors":
            if gesture2 == "paper" or "lizard":
                return 1
        elif gesture1 == "lizard":
            if gesture2 == "paper" or "spock":
                return 1
        elif gesture1 == "spock":
            if gesture2 == "rock" or "scissors":
                return 1
        else:
            return 2
        