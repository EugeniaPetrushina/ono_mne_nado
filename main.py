import bs4
from io import BytesIO
import random
import requests

def random_game():

    url = "https://store.steampowered.com/explore/random/"
    req_game = requests.get(url)
    soup = bs4.BeautifulSoup(req_game.text, "html.parser")
    prise = ''
    name = soup.find('div', id="appHubAppName").getText()
    prise = soup.find('div', class_="game_purchase_price price")
    if prise == None:
        prise = ' '
    else:
        prise = soup.find('div', class_="game_purchase_price price").getText().strip()
    developer = soup.find('div', id="developers_list").getText().strip()
    #genre = soup.find('div', id="genresAndManufacturer").find('href')
    #tags = soup.find('div', class_="glance_tags popular_tags").getText().split(' ')
    info = soup.find('div', id="genresAndManufacturer").getText()
    picture=soup.find('img', class_="game_header_image_full")

    print(info)
    print(prise)
    print(info)
    print(picture)
random_game()
