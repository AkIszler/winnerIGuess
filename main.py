
import random

contestPlayers = ["boredsolocat", "dev-siri", "ducky",
"travy", "ThePrimeagen Twitch prime", "reroll", "dev-siri", "boredsolocat", "ducky"]

def pickPlayer(player):
    players = len(player)
    return random.randint(0, players - 1)
    
def main():
    luckyPick = pickPlayer(contestPlayers)

    print(contestPlayers[luckyPick])

if __name__ == "__main__":
    main()
