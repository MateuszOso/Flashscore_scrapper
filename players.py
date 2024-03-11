from bs4 import BeautifulSoup
import time

class Players:

    def __init__(self, driver, scraper_instance):
        self.driver = driver
        self.scraper = scraper_instance
        self.all_players = []
        _, players_urls = self.scraper.get_odds_and_players_urls(self.scraper.match_ids)
        self.process_players_urls(players_urls)

    def process_players_urls(self, urls):
        for url in urls:
            self.get_players_data(url)

    def get_players_data(self, url):
        self.driver.get(url)
        time.sleep(1)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        home_players, away_players = self.find_participants(soup)
        match_players = {
            "home_players": [participant.text for participant in home_players],
            "away_players": [player.text for player in away_players]
        }
        self.all_players.append(match_players)

    def find_participants(self, soup):
        section_title = soup.find_all(class_="section__title--center")
        participants, away_players = [], []
        for title in section_title:
#         To też jest zmienna, która dosyc czesto jest zalezna od serwisu z ktorego korzystamy, warto byloby ja przeniesc do pliku konfiguracyjnego
#        Plik konfiguracyjny moze byc zwyklym obiektem, w ktorym bedzie lista serwisow a kazdy serwis bedzie mial swoje stale takie jak URL, nazwa zmiennej dla skladu, nazwa zmiennej dla wyniku itp.
            if "Składy wyjściowe" in title.text:
                container = title.find_next_sibling()
                if container:
                    participants.extend(container.select(".lf__participant"))
                    away_players.extend(container.select(".lf__isReversed"))
        home_players = [player for player in participants if player not in away_players]
        return home_players, away_players

    def get_all_players(self):
        return self.all_players




