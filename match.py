class Match:

    def __init__(self, scraper_instance):
        self.scraper = scraper_instance
#         Statyczne zmienne, takie jak URL'e raczej zapisujemy w osobnym pliku z którego je pobieramy, a nie w kodzie
        self.main_soup = self.scraper.get_soup("https://www.flashscore.pl/pilka-nozna/polska/pko-bp-ekstraklasa/wyniki/")

    def teams(self):
        teams_list = []
        for match in self.scraper.get_newest_round(self.main_soup):
            home_team = match.find('div', class_ = "event__participant--home").text.strip()
            away_team = match.find('div', class_ = "event__participant--away").text.strip()
            teams_list.append(f"{home_team} - {away_team}")
        return teams_list


    def scores(self):
        scores_list = []
        for match in self.scraper.get_newest_round(self.main_soup):
            home_team_score = match.find('div', class_ = "event__score--home").text.strip()
            away_team_score = match.find('div', class_ = "event__score--away").text.strip()
            scores_list.append(f"{home_team_score} - {away_team_score}")
        return scores_list

    def dates(self):
        match_date_list = []
        for match in self.scraper.get_newest_round(self.main_soup):
            match_date = match.find('div', class_ = "event__time").text.strip()
            match_date_list.append(match_date)
        return match_date_list



