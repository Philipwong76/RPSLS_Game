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

                result = (player1.gesture, AIPlayer.gesture)
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