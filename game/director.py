from dealer import Dealer

class Director:
    def __init__(self):
        self.playerScore = 400
        self.dealer = Dealer()

    def startGame(self):
        pass

    def getInput(self):
        pass

    def doUpdates(self, guess):
        if self.current_card < self.next_card and guess == "h":
            self.points += 100
        elif self.current_card < self.next_card and guess == "l":
            self.points -= 75
        elif self.current_card > self.next_card and guess == "l":
            self.points += 100
        elif self.current_card > self.next_card and guess == "h":
            self.points -= 75