import string

import bs4
from io import BytesIO
import random
import requests

def random_game():

    url = "https://store.steampowered.com/explore/random/"
    req_game = requests.get(url)
    soup = bs4.BeautifulSoup(req_game.text, "html.parser")

    '''prise = ''
    name = soup.find('div', id="appHubAppName").getText()
    prise = soup.find('div', class_="game_purchase_price price")
    if prise == None:
        prise = ' '
    else:
        prise = soup.find('div', class_="game_purchase_price price").getText().strip()
    developer = soup.find('div', id="developers_list").getText().strip()'''

    info_list = []
    info = soup.find('div', class_="share share_dialog").getText()
    a = str(info)
    a = info[29:]
    print(a)

    '''picture_list = []
    video = soup.find('textarea', id="textarea").find("href")
    images = soup.find_all('webm')
    for image in images:
        src = image.get("src")
        picture_list.append(src)
        print(src)
    print(video)'''


    '''info_list = info.split()
    i = info_list.index("Title:")
    info_list[i] = "\nНазвание:"
    i = info_list.index("Genre:")
    info_list[i] = "\nЖанр:"
    i = info_list.index("Developer:")
    info_list[i] = "\nРазработчик:"
    i = info_list.index("Publisher:")
    info_list[i] = "\nИздатель:"
    i = info_list.index("Release")
    info_list[i] = "\nДата"
    i = info_list.index("Date:")
    info_list[i] = "выхода:"
    info_list.append("\nЦена:")
    info_list.append(prise)'''


random_game()


