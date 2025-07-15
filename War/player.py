class Player:
    def __init__(self):
        self.deck = []
    
    def showDeck(self):
        print(self.deck, len(self.deck))