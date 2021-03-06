from game.dealer import Dealer

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
            print("The card is: " + str(self.current_card))
            guess = self.getInput()
            self.next_card = self.dealer.drawCard()
            print("Next card was: " + str(self.next_card))
            self.doUpdates(guess)
            print("Your score is: " + str(self.playerScore))
            self.keepPlaying = self.getKeepPlaying()
            print("")

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

    def getKeepPlaying(self):
      #Samson
        valid = False
        while not valid:
            text = input("Keep playing? [y/n]: ")
            if isinstance(text, str):
                prompt = text.lower()
                if prompt == "n":
                    valid = True
                    return False
                
                elif prompt == "y":
                    valid = True
                    return True
                else:
                    valid = False
                    print("Error: Please enter y/n to keep playing or stop playing.")
