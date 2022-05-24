import bs4
from io import BytesIO
import random
import requests


def random_game():
    page = 1
    # req_game = requests.get("https://stopgame.ru/games?p=" + str(page))
    # html = bs4.BeautifulSoup(r.content, "html.parser")
    #url = "https://randomgeeks.ru/generator-games/random/"
    #result_find = soup.find('section', class_="generator").find('div', class_="generator-box")

    url = "https://store.steampowered.com/explore/random/"
    req_game = requests.get(url)
    soup = bs4.BeautifulSoup(req_game.text, "html.parser")

    name = soup.find('div', id="appHubAppName").getText()
    prise = soup.find('div', class_="game_purchase_price price").getText()
    print(name)
    print(prise)

random_game()
