import csv
from scraper import Scrapper
from match import Match
from odds import Odds
from players import Players

class CsvSaver:


    def starter(self, filename='combined_data.csv'):
        scraper = Scrapper()
        scraper.update_match_ids()

        matches = Match(scraper)
        odd = Odds(scraper.driver, scraper)
        player = Players(scraper.driver, scraper)

        teams_list = matches.teams()
        scores_list = matches.scores()
        dates_list = matches.dates()
        home_win_odds, draw_odds, away_win_odds = odd.get_all_odds(scraper.get_odds_and_players_urls(scraper.match_ids)[0])
        players_list = player.all_players

        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Teams', 'Scores', 'Date', 'Home Win Odds', 'Draw Odds', 'Away Win Odds', 'Home Players', 'Away Players'])
            for i in range(len(teams_list)):
                writer.writerow([
                    teams_list[i],
                    scores_list[i],
                    dates_list[i],
                    home_win_odds[i],
                    draw_odds[i],
                    away_win_odds[i],
                    "; ".join(players_list[i]['home_players']),
                    "; ".join(players_list[i]['away_players'])
                ])


