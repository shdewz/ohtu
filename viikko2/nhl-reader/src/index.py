import requests
from player import Player, PlayerReader, PlayerStats
from rich.prompt import Prompt

seasons = ['2018-19', '2019-20', '2020-21',
           '2021-22', '2022-23', '2023-24', '2024-25']
nationalities = ['AUT', 'CZE', 'AUS', 'SWE', 'GER', 'DEN', 'SUI',
                 'SVK', 'NOR', 'RUS', 'CAN', 'LAT', 'BLR', 'SLO', 'USA', 'FIN', 'GBR']


def main():
    while True:
        season = Prompt.ask('Select season: ', choices=seasons+[''])
        if season == '': return
        while True:
            nationality = Prompt.ask(
                'Select nationality: ', choices=sorted(nationalities)+[''])
            if nationality == '': break
            url = f'https://studies.cs.helsinki.fi/nhlstats/{season}/players'
            reader = PlayerReader(url)
            stats = PlayerStats(reader)
            players = stats.top_scorers(nationality, season)
            print('')
            stats.format_table(players, nationality, season)
            print('')


if __name__ == '__main__':
    main()
