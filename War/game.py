import random

class Game:
    def __init__(self, player1, player2): 
        self.gameDeck=[]

        self.wars = 0
        self.warsWonBy1 = 0
        self.warsWonBy2 = 0

        self.player1 = player1
        self.player2 = player2

        self.winner = ""
        self.end = False

        self.rounds = 0
    
    def shuffle(self):
        for i in range (1,14):
            for j in range(4):
                self.gameDeck.append(i)

            random.shuffle(self.gameDeck)
        for i in range(4): 
            random.shuffle(self.gameDeck)

    def assignDeck(self):
        self.player1.deck = self.gameDeck[1:27]
        self.player2.deck = self.gameDeck[26:]

    def check(self, i):
        if self.player2.deck[i] == 13 and self.player1.deck[i] == 1:
            return 1

        elif self.player1.deck[i] == 13 and self.player2.deck[i] == 1:
            return 2

        elif self.player1.deck[i] > self.player2.deck[i]:
            return 1
        
        elif self.player1.deck[i] < self.player2.deck[i]:
            return 2
        
        else:
            return 3

    def checkEnd(self, war, j):
        if war == True:
            if len(self.player1.deck) < 5+j:
                self.winner = "Player 2"
                return True
            if len(self.player2.deck) < 5+j:
                self.winner = "Player 1"
                return True
        if len(self.player1.deck) == 0:
            self.winner = "Player 2"
            return True
        if len(self.player2.deck) == 0:
            self.winner = "Player 1"
            return True
        return False
        
    def makeTurn(self):
        # print(self.player1.deck[0])
        # print(self.player2.deck[0])

        if self.checkEnd(False, 0):
            self.end = True
            return

        result = self.check(0)

        if result == 3: 
            # print("WAR")
            
            j = 0

            while self.player1.deck[j] == self.player2.deck[j]:
                if self.checkEnd(True, j):
                    self.end = True
                    return
                self.wars += 1
                j += 4

            result = self.check(j)

            # print(self.player1.deck[j])
            # print(self.player2.deck[j])

            # print(f"result: Player {result}")

            if result == 1:
                self.warsWonBy1 += 1
                for i in range(0, j+1):
                    self.player1.deck.append(self.player2.deck[0])
                    del self.player1.deck[0]
                    self.player1.deck.append(self.player1.deck[0])
                    del self.player2.deck[0]

            elif result == 2:
                self.warsWonBy2 += 1
                for i in range(0, j+1):
                    self.player2.deck.append(self.player1.deck[0])
                    del self.player1.deck[0]
                    self.player2.deck.append(self.player2.deck[0])
                    del self.player2.deck[0]
            return
        
        if result == 1:
            self.player1.deck.append(self.player2.deck[0])
            self.player1.deck.append(self.player1.deck[0])
        elif result == 2:
            self.player2.deck.append(self.player1.deck[0])
            self.player2.deck.append(self.player2.deck[0])
        
        del self.player1.deck[0]
        del self.player2.deck[0]

        if self.checkEnd(False, 0):
            self.end = True
            return
        
    def reset(self):
        self.player1.deck = []
        self.player2.deck = []
        self.gameDeck = []
        self.end = False
        self.rounds = 0
        self.wars = 0
        self.warsWonBy1 = 0
        self.warsWonBy2 = 0

        self.shuffle()
        self.assignDeck()
