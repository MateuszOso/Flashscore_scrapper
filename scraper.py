import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


class Scrapper:


    def __init__(self):
        self.driver = self.get_driver()
        self.match_ids = []

    def __del__(self):
        self.driver.quit()

    def get_driver(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        return driver

    def get_soup(self, url_address):
        try:
            self.driver.get(url_address)
            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            return soup
        except Exception as e:
            print(f"Error fetching page content from {url_address}: {e}")
        return None

    def get_newest_round(self, soup):
        try:
            rounds = soup.find_all(class_="event__round--static")
            if not rounds:
                print("No rounds found.")
                return []

            newest_round = None
            highest_round_number = 0

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
        except Exception as e:
            print(f"Error finding newest round: {e}")
        return []

    def get_match_ids(self, matches):
        try:
            if not matches:
                print("No matches provided to extract IDs from.")
                return []

            match_ids = [match['id'][4:] for match in matches if 'id' in match.attrs]
            if not match_ids:
                print("No valid match IDs found.")
            return match_ids

        except Exception as e:
            print(f"Error extracting match IDs: {e}")
            return []

    def get_odds_and_players_urls(self, match_ids):
        if not match_ids:
            print("No match IDs provided for URL generation.")
            return [], []

        odds_url_list = []
        players_url_list =[]
        for match_id in match_ids:
            odds_url_list.append(f"https://www.flashscore.pl/mecz/{match_id}/#/zestawienie-kursow/kursy-1x2/koniec-meczu")
            players_url_list.append(f"https://www.flashscore.pl/mecz/{match_id}/#/szczegoly-meczu/sklady")

        return odds_url_list, players_url_list

    def get_players_soup(self, match_ids):

        if match_ids:
            url = f"https://www.flashscore.pl/mecz/{match_ids[0]}/#/szczegoly-meczu/sklady"
            print(url)
            return self.get_soup(url)

    def update_match_ids(self):
        main_soup = scraper.get_soup("https://www.flashscore.pl/pilka-nozna/polska/pko-bp-ekstraklasa/wyniki/")
        matches = scraper.get_newest_round(main_soup)
        self.match_ids = self.get_match_ids(matches)



scraper = Scrapper()
scraper.update_match_ids()
"""
main_soup = scraper.get_soup("https://www.flashscore.pl/pilka-nozna/polska/pko-bp-ekstraklasa/wyniki/")
matches = scraper.get_newest_round(main_soup)

match_ids = scraper.get_match_ids(matches)

time.sleep(10)
odds_soup = scraper.get_odds_and_players_urls(match_ids)
time.sleep(10)
players_soup = scraper.get_players_soup(match_ids)
print(odds_soup)
"""
