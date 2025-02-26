class Player:
    player_id_counter = 1

    def __init__(self, name: str, position: str, number: int, age: int, nationality: str):
        self.player_id = Player.player_id_counter
        Player.player_id_counter += 1
        self.name = name
        self.position = position
        self.__number = number
        self.__age = age
        self.nationality = nationality
        self.stats = {"matches": 0, "goals": 0, "assists": 0}

    def update_stats(self, matches=0, goals=0, assists=0):
        self.stats["matches"] += matches
        self.stats["goals"] += goals
        self.stats["assists"] += assists

    def display_info(self):
        return f"ID: {self.player_id}, Name: {self.name}, Position: {self.position}, Number: {self.__number}, Age: {self.__age}, Nationality: {self.nationality}, Stats: {self.stats}"

    def __str__(self):
        return self.display_info()


class Coach:
    def __init__(self, name: str, experience: int):
        self.name = name
        self.__experience = experience

    def display_info(self):
        return f"Coach: {self.name}, Experience: {self.__experience} years"

    def __str__(self):
        return self.display_info()


class Team:
    def __init__(self, team_name: str, coach: Coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, player: Player):
        if len(self.players) >= 25:
            print("Cannot add more players. Maximum limit reached.")
            return
        self.players.append(player)

    def find_player(self, player_id: int):
        for player in self.players:
            if player.player_id == player_id:
                return player
        print(f"Player with ID {player_id} not found.")
        return None

    def update_player_info(self, player_id: int, **kwargs):
        player = self.find_player(player_id)
        if player:
            for key, value in kwargs.items():
                if hasattr(player, key):
                    setattr(player, key, value)
                elif key in player.stats:
                    player.stats[key] = value
                else:
                    print(f"Invalid attribute: {key}")

    def remove_player(self, player_id: int):
        player = self.find_player(player_id)
        if player:
            self.players.remove(player)

    def display_team(self):
        print(f"Team: {self.team_name}\nCoach: {self.coach}")
        print("Players:")
        for player in self.players:
            print(player)

    def __str__(self):
        return self.display_team()


# Example Usage
coach = Coach("Xavi Hernandez", 10)
team = Team("Barcelona", coach)

player1 = Player("Lionel Messi", "Forward", 10, 36, "Argentina")
player2 = Player("Pedri", "Midfielder", 8, 21, "Spain")

team.add_player(player1)
team.add_player(player2)
team.display_team()

team.update_player_info(player1.player_id, goals=5, assists=3)
team.display_team()

team.remove_player(player2.player_id)
team.display_team()
