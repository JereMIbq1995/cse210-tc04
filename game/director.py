from dealer import Dealer

class Director:
    def __init__(self):
        self.playerScore = 300
        self.dealer = Dealer()

    def startGame(self):
        # Jeremy does this one
        pass

    def getInput(self):
        #mikaela does this
        guess_1 = input("Higher or Lower? [h/l]: ")
        return guess_1

    def doUpdates(self):
        #Abram
        pass