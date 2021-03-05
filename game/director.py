from dealer import Dealer

class Director:
    def __init__(self):
        self.playerScore = 300
        self.current_card = 0
        self.next_card = 0
        self.dealer = Dealer()
        self.keepPlaying = True

    def startGame(self):
        # Jeremy does this one       
        while (self.keepPlaying):
            self.current_card = self.dealer.drawCard()
            print("The card is: " + self.current_card)
            guess = self.getInput()
            self.next_card = self.dealer.drawCard()
            self.doUpdates(guess)
            self.keepPlaying = getKeepPlaying()

    def getInput(self):
        #mikaela does this
        guess_1 = input("Higher or Lower? [h/l]: ")
        return guess_1

    def doUpdates(self, guess):
      #Abram
        if self.current_card < self.next_card and guess == "h":
            self.playerScore += 100
        elif self.current_card < self.next_card and guess == "l":
            self.playerScore -= 75
        elif self.current_card > self.next_card and guess == "l":
            self.playerScore += 100
        elif self.current_card > self.next_card and guess == "h":
            self.playerScore -= 75
