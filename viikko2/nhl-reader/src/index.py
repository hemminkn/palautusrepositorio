import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == "FIN":
            players.append(player)

    print("Players from FIN:")
    print()
    print()

    players = sorted(players, key=lambda player: player.goals+player.assists, reverse=True)

    for player in players:
        points = f"{player.goals} + {player.assists} = {player.goals+player.assists}"
        print(f"{player.name:20} {player.team:16} {points}")

if __name__ == "__main__":
    main()
