import bs4
from io import BytesIO
import random
import requests


def random_game():

    url = "https://store.steampowered.com/explore/random/"
    req_game = requests.get(url)
    soup = bs4.BeautifulSoup(req_game.text, "html.parser")

    name = soup.find('div', id="appHubAppName").getText()
    prise = soup.find('div', class_="game_purchase_price price").getText().strip()
    genre = soup.find('div', id="developers_list").getText().strip()
    print(name)
    print(prise)
    print(genre)

random_game()
