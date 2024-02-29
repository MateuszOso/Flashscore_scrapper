import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
from bs4 import BeautifulSoup


class Scrapper:


    def __init__(self):
        self.driver = self.get_driver()

    def __del__(self):
        self.driver.quit()

    def get_driver(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        return driver

    def get_soup(self, url_address):
        self.driver.get(url_address)
        html = self.driver.page_source

        soup = BeautifulSoup(html, "html.parser")

        return soup

    def get_newest_round(self, soup):
        rounds = soup.find_all(class_="event__round--static")
        newest_round = None
        highest_round_number = -1  # Start with a default that's lower than any expected round number

        for round in rounds:
            round_number_text = round.text
            # Use regular expression to find numbers in the round text
            match = re.search(r'\d+', round_number_text)
            if match:
                round_number = int(match.group())
                if round_number > highest_round_number:
                    highest_round_number = round_number
                    newest_round = round

        if newest_round:
            matches = []
            current_match = newest_round.find_next_sibling()

            while current_match:
                if 'class' in current_match.attrs:
                    if 'event__match' in current_match['class']:
                        matches.append(current_match)

                    # It checks if the next round has been reached
                    elif 'event__round' in current_match['class'] and 'event__round--static' in current_match['class']:
                        break

                current_match = current_match.find_next_sibling()

            return matches

    def get_match_ids(self, matches):

        if matches:
            match_ids = [match['id'][4:] for match in matches if 'id' in match.attrs]
            return match_ids
    def get_odds_soup(self, match_ids):

            if match_ids:
                url = f"https://www.flashscore.pl/mecz/{match_ids[0]}/#/zestawienie-kursow/kursy-1x2/koniec-meczu"
                print(url)
                return self.get_soup(url)

    def get_players_soup(self, match_ids):

        if match_ids:
            url = f"https://www.flashscore.pl/mecz/{match_ids[0]}/#/szczegoly-meczu/sklady"
            print(url)
            return self.get_soup(url)



scraper = Scrapper()

main_soup = scraper.get_soup("https://www.flashscore.pl/pilka-nozna/polska/pko-bp-ekstraklasa/wyniki/")
matches = scraper.get_newest_round(main_soup)

match_ids = scraper.get_match_ids(matches)
time.sleep(10)
odds_soup = scraper.get_odds_soup(match_ids)
time.sleep(10)
players_soup = scraper.get_players_soup(match_ids)


