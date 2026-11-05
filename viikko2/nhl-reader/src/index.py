import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []
        self.get_players()

    def get_players(self):
        response = requests.get(self.url).json()

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        n_players = []

        for player in self.reader.players:
            if player.nationality == nationality:
                n_players.append(player)

        top_playas = sorted(n_players, key=lambda player: player.goals+player.assists, reverse=True)

        return top_playas

    def top_goal_scorers(self, how_many):
        sorted_players = sorted(self.reader.players, key=lambda player: player.goals, reverse=True)
        return sorted_players[:how_many]

    def top_scorers_by_team(self, team):
        team_players = [
            player for player in self.reader.players
            if player.team == team
        ]

        return sorted(
            team_players,
            key=lambda player: player.goals + player.assists,
            reverse=True
        )

if __name__ == "__main__":
    main()
