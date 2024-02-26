from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


class Scrapper:

    def get_soup(self, url_address):

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get(url_address)

        html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html, "html.parser")
        return soup

    def get_newest_round(self, soup):

        rounds = soup.find_all(class_= "event__round--static")
        newest_round = rounds[0] if rounds else None

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


scraper = Scrapper()

soup = scraper.get_soup("https://www.flashscore.pl/pilka-nozna/polska/pko-bp-ekstraklasa/wyniki/")

scraper.get_newest_round(soup)
