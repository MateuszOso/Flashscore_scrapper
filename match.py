import scraper

class Match():

    def teams(self):
        teams_list = []
        for match in scraper.matches:
            home_team = match.find('div', class_ = "event__participant--home").text.strip()
            away_team = match.find('div', class_ = "event__participant--away").text.strip()
            teams_list.append(f"{home_team} - {away_team}")
        return teams_list


    def scores(self):
        scores_list = []
        for match in scraper.matches:
            home_team_score = match.find('div', class_ = "event__score--home").text.strip()
            away_team_score = match.find('div', class_ = "event__score--away").text.strip()
            scores_list.append(f"{home_team_score} - {away_team_score}")
        return scores_list

    def dates(self):
        match_date_list = []
        for match in scraper.matches:
            match_date = match.find('div', class_ = "event__time").text.strip()
            match_date_list.append(match_date)
        return match_date_list


matches = Match()
matches.teams()
matches.scores()
matches.dates()
