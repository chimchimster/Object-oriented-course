import requests
from bs4 import BeautifulSoup
import csv
from http import HTTPStatus

CSV = 'Cards.csv'
HOST = 'https://stopgame.ru/'
URL = 'https://stopgame.ru/news'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'accept': '*/*'
}

def get_html(URL, params=''):
    r = requests.get(URL, headers=HEADERS, params=params).text
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='items')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('div', class_= 'caption caption-bold').find('a').get_text(strip=True),
                'link_product': HOST + item.find('div', class_='caption caption-bold').find('a').get('href'),
                'brand': item.find('div', class_='info').find('span').get_text(strip=True),
                'card_img': HOST + item.find('div', class_='item article-summary').find('img').get('src')
                        }
                    )
    return cards

def save_doc(items, path):

    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название статьи', 'Сссылка на статью', 'Дата публикации', 'Изображение статьи'])

        for item in items:
            writer.writerow([item['title'], item['link_product'], item['brand'], item['card_img']])

def parser():
    PAGENATION = input('Укажите, число страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if HTTPStatus.OK == 200:
        cards = []
        for page in range(1, PAGENATION):

            html = get_html(URL, params={'page': {page}})
            cards.extend(get_content(html))
            save_doc(cards, CSV)
        print('Парсинг окончен')
        pass
    else:
        print('Error')

parser()