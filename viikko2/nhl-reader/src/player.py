import requests
from rich.console import Console
from rich.table import Table

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.nationality = dict['nationality']
        self.goals = dict['goals']
        self.assists = dict['assists']

    def __str__(self):
        return f'[{self.team}] {self.name:26} {self.goals:3} + {self.assists:3} = {self.goals + self.assists:3}'


class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        self.players = players


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers(self, nationality, season):
        return sorted([x for x in self.players if x.nationality == nationality], reverse=True, key=lambda x: x.goals + x.assists)
    
    def format_table(self, players, nationality, season):
        table = Table(title=f'Top scorers of {nationality}, season {season}')

        table.add_column('name', style='cyan', no_wrap=True)
        table.add_column('team', style='magenta', no_wrap=True)
        table.add_column('goals', no_wrap=True)
        table.add_column('assists', no_wrap=True)
        table.add_column('points', no_wrap=True)

        for player in players:
            table.add_row(str(player.name), str(player.team), str(player.goals), str(player.assists), str(player.goals + player.assists))

        console = Console()
        console.print(table)
