class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, name, position, number, age, nationality):
        player = {
            "name" : name,
            "position": position,
            "number": number,
            "age": age,
            "nationality": nationality
        }
        self.players.append(player)

    def remove_player(self, player_number):
        for player in self.players:
            if player["number"] == player_number:
                self.players.remove(player)
                return
        print(f"There is no player with this {player_number}.Please enter valid player's number")

    def update_player_info(self, player_number, **kwargs):
        for player in self.players:
            if player["number"] == player_number:
                player.update(kwargs)
                return
        print(f"There is no player with this {player_number}.Please enter valid player's number")

    def display_team(self):
        print(f"Team: {self.team_name}")
        print(f"Coach: {self.coach}")

        for player in self.players:
            print(f"Player: {player['name']}, position: {player['position']}, number: {player['number']}, age: {player['age']}, nationality: {player['nationality']}")


    def display_player_info(self, player_number):
        for player in self.players:
            if player['number'] == player_number:
                print(f"Player info: {player}")
                return
        print(f"There is no player with this {player_number}.Please enter valid player's number")


team = FootballTeam("Barcelona", "Xavi Hernandez")
team.add_player("Lionel Messi", "Forward", 10, 36, "Argentina")
team.add_player("Pedri", "Midfielder", 8, 21, "Spain")
team.display_team()
team.update_player_info(10, goals=5, assists=3)
team.display_team()
team.remove_player(8)
team.display_team()
team.display_player_info(10)