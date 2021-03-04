from dealer import Dealer

class Director:
    def __init__(self):
        self.playerScore = 400
        self.current_card = 0
        self.next_card = 0
        self.dealer = Dealer()
        self.keepPlaying = True

    def startGame(self):
        
        while (self.keepPlaying):
            self.current_card = self.dealer.drawCard()
            print("The card is: " + self.currentCard)
            guess = self.getInput()
            self.next_card = self.dealer.drawCard()
            self.doUpdates(guess)
            self.keepPlaying = getKeepPlaying()


    def getInput(self):
        pass

    def doUpdates(self):
        pass