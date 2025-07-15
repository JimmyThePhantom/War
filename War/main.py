import game, player
import matplotlib.pyplot as plt

gamesRun = 1000

player1 = player.Player()
player2 = player.Player()
Game = game.Game(player1, player2)

Game.shuffle()
Game.assignDeck()

rounds = []

winsPlayer1 = 0
winsPlayer1WithWars = 0

winsPlayer2 = 0
winsPlayer2WithWars = 0

sumRounds = 0
sumWars = 0
sumWars1 = 0
sumWars2 = 0

maxWars = 0
maxRounds = 0

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5, figsize=(20, 7), layout="constrained")

ax1.set_xlabel("Games")
ax1.set_ylabel("Rounds per Game")

for i in range(gamesRun):
    while Game.end == False:
        Game.makeTurn()
        Game.rounds += 1
        # player1.showDeck()
        # player2.showDeck()
        # print("\n")

    sumWars += Game.wars
    rounds.append(Game.rounds)
    sumRounds += Game.rounds

    if Game.rounds >= maxRounds:
        maxRounds = Game.rounds 
    
    if Game.wars >= maxWars:
        maxWars = Game.wars

    sumWars1 += Game.warsWonBy1
    sumWars2 += Game.warsWonBy2

    if Game.winner == "Player 1":
        winsPlayer1 += 1
        if Game.warsWonBy1 > Game.warsWonBy2:
            winsPlayer1WithWars += 1
    else:
        winsPlayer2 += 1
        if Game.warsWonBy2 > Game.warsWonBy1:
            winsPlayer2WithWars += 1

    Game.reset()

    # print(f"Rounds: {Game.rounds} \nWars: {Game.wars} \nWinner: {Game.winner} \nOverall Wars won by Player 1: {Game.warsWonBy1} \nOverall Wars won by Player 2: {Game.warsWonBy2}")

ax1.plot([i for i in range(1, gamesRun+1)], rounds)

aveWars = sumWars/gamesRun
aveRounds = sumRounds/gamesRun

aveWars1 = sumWars1/gamesRun
aveWars2 = sumWars2/gamesRun

ax2.bar(["Average Rounds\nper Game", "Average Wars\nper Game"], [aveRounds, aveWars], color='orange')

t1 = ax2.text(1, 70, f"Average Rounds\nper Game:\n{aveRounds}", ha="center", va="center", bbox=dict(boxstyle="square,pad=0.3",
                      fc="lightblue", ec="steelblue", lw=2))

t2 = ax2.text(1, 50, f"Average Wars\nper Game:\n{aveWars}", ha="center", va="center", bbox=dict(boxstyle="square,pad=0.3",
                      fc="lightblue", ec="steelblue", lw=2))

t3 = ax2.text(1, 90, f"Max Wars\nin one Game:\n{maxWars}", ha="center", va="center", bbox=dict(boxstyle="square,pad=0.3",
                      fc="lightblue", ec="steelblue", lw=2))

t3 = ax2.text(1, 110, f"Max Rounds\nin one Game:\n{maxRounds}", ha="center", va="center", bbox=dict(boxstyle="square,pad=0.3",
                      fc="lightblue", ec="steelblue", lw=2))


ax3.bar(["Average Wars\nwon by Player 1\nper Game", "Average Wars\nwon by Player 2\nper Game"], [aveWars1, aveWars2], color='green')

ax4.bar(["Games won\nby Player 1", "Games won\nby Player 1\nin which he won\nthe most Wars"], [winsPlayer1, winsPlayer1WithWars], color='purple')

ax5.bar(["Games won\nby Player 2", "Games won\nby Player 2\nin which he won\nthe most Wars"], [winsPlayer2, winsPlayer2WithWars], color='red')

plt.show()   