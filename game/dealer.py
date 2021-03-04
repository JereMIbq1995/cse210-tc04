import random
#Samson do this one
class Dealer:
    def __init__(self):
        self.card = []

    def drawCard(self):
        return random.randrange(range(1,14))
