from bs4 import BeautifulSoup
import time
from config import config


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
        section_title = soup.find_all(class_= config["flashscore"]["dynamic_class_names"]["section_title"])
        participants, away_players = [], []
        for title in section_title:
            if config["flashscore"]["titles"]["starting_lineup"] in title.text:
                container = title.find_next_sibling()
                if container:
                    participants.extend(container.select(config["flashscore"]["dynamic_class_names"]["home_participants"]))
                    away_players.extend(container.select(config["flashscore"]["dynamic_class_names"]["away_participants"]))
        home_players = [player for player in participants if player not in away_players]
        return home_players, away_players

    def get_all_players(self):
        return self.all_players




