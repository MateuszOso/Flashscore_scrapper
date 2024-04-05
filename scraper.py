import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from config import config


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
            rounds = soup.find_all(class_=config["score_page"]["dynamic_class_names"]["rounds"])
            if not rounds:
                print("No rounds found.")
                return []

            newest_round = None
            highest_round_number = 0

            for round in rounds:
                round_number_text = round.text
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
                        if config["score_page"]["dynamic_class_names"]["matches"] in current_match['class']:
                            matches.append(current_match)

                        elif config["score_page"]["dynamic_class_names"]["basic_round"] in current_match['class'] and config["score_page"]["dynamic_class_names"]["rounds"] in current_match['class']:
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
#TODO Bierz cały ID
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
        #  TODO, Otypowanie configu
        odds_url_list = [config["score_page"]["base_url"] + config["score_page"]["odds_endpoint"].format(match_id=mid) for mid in match_ids]
        players_url_list = [config["score_page"]["base_url"] + config["score_page"]["players_endpoint"].format(match_id=mid) for mid in match_ids]

        return odds_url_list, players_url_list

    def update_match_ids(self):
        main_soup = self.get_soup(config["score_page"]["base_url"]+config["score_page"]["matches_endpoint"])
        matches = self.get_newest_round(main_soup)
        self.match_ids = self.get_match_ids(matches)




