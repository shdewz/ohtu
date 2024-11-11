import requests
from player import Player, PlayerReader, PlayerStats
from rich.prompt import Prompt

seasons = ['2018-19', '2019-20', '2020-21',
           '2021-22', '2022-23', '2023-24', '2024-25']
nationalities = ['AUT', 'CZE', 'AUS', 'SWE', 'GER', 'DEN', 'SUI',
                 'SVK', 'NOR', 'RUS', 'CAN', 'LAT', 'BLR', 'SLO', 'USA', 'FIN', 'GBR']


def main():
    players = PlayerReader(
        'https://studies.cs.helsinki.fi/nhlstats/2023-24/players').players

    print(players[0])

    # for player in sorted(players, reverse=True, key=lambda x: x.goals + x.assists):
    #     if (player.nationality == 'FIN'):
    #         print(player)


def main():
    season = Prompt.ask('Select season: ', choices=seasons)
    while True:
        nationality = Prompt.ask('Select nationality: ', choices=sorted(nationalities))
        url = f'https://studies.cs.helsinki.fi/nhlstats/{season}/players'
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers(nationality, season)
        print('')
        stats.format_table(players, nationality, season)
        print('')


if __name__ == '__main__':
    main()
