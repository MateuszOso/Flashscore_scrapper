from config import config


class Match:

    def __init__(self, scraper_instance):
        self.scraper = scraper_instance
        self.main_soup = self.scraper.get_soup(config["score_page"]["base_url"]+config["score_page"]["matches_endpoint"])

    def teams(self):
        teams_list = []
        for match in self.scraper.get_newest_round(self.main_soup):
            home_team = match.find('div', class_ = config["score_page"]["dynamic_class_names"]["home_players"]).text.strip()
            away_team = match.find('div', class_ = config["score_page"]["dynamic_class_names"]["away_players"]).text.strip()
            teams_list.append(f"{home_team} - {away_team}")
        return teams_list


    def scores(self):
        scores_list = []
        for match in self.scraper.get_newest_round(self.main_soup):
            home_team_score = match.find('div', class_ = config["score_page"]["dynamic_class_names"]["score_home"]).text.strip()
            away_team_score = match.find('div', class_ = config["score_page"]["dynamic_class_names"]["score_away"]).text.strip()
            scores_list.append(f"{home_team_score} - {away_team_score}")
        return scores_list

    def dates(self):
        match_date_list = []
        for match in self.scraper.get_newest_round(self.main_soup):
            match_date = match.find('div', class_ = config["score_page"]["dynamic_class_names"]["time"]).text.strip()
            match_date_list.append(match_date)
        return match_date_list



