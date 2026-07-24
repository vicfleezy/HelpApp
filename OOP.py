class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

    def __str__(self):
        return f"{self.playerName} ({self.playerPosition})"


class NFLTeam:
    def __init__(self, team_name, player_list=None):
        self.team_name = team_name
        self.player_list = player_list if player_list is not None else []

    def display_roster(self):
        print(f"Team: {self.team_name}")
        print("Roster:")
        for player in self.player_list:
            print(f"- {player.playerName}: {player.playerPosition}")


player1 = Player("Lamar Jackson", "QB")
player2 = Player("Eric Dickerson", "RB")
player3 = Player("Randy Moss", "WR")
player4 = Player("Morten Andersen", "K")

playerList = [player1, player2, player3, player4]

Freedom_Patriots = NFLTeam("Freedom Patrioits", playerList)
#My high school teams name, LOL

Freedom_Patriots.display_roster()