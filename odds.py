from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraper import scraper

class Odds:
    def __init__(self, driver, scraper_instance):
        self.driver = driver
        self.scraper = scraper_instance
        odds_urls, _ = self.scraper.get_odds_and_players_urls(self.scraper.match_ids)
        self.get_all_odds(odds_urls)

    def get_odds(self, url):
        self.driver.get(url)
        odds_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'oddsCell__odd'))
        )
        return [element.get_attribute('title') for element in odds_elements]

    def get_all_odds(self, urls):
        home_win_odds = []
        draw_odds = []
        away_win_odds = []
        for url in urls:
            odds_values = self.get_odds(url)
            home_win_odds.append(self.get_valid_odds(odds_values, 0))
            draw_odds.append(self.get_valid_odds(odds_values, 1))
            away_win_odds.append(self.get_valid_odds(odds_values, 2))
        return home_win_odds, draw_odds, away_win_odds

    def get_valid_odds(self, odds_values, starting_index):
        for i in range(starting_index, len(odds_values), 3):
            odds = odds_values[i][-4:]
            if odds.replace('.', '', 1).isdigit():
                return odds
        return ''

odds = Odds(scraper.driver, scraper)

