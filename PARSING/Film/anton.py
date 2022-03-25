import json
import os

import requests
from bs4 import BeautifulSoup

url = 'https://www.ivi.ru/watch/146387/person'
req = requests.get(url).text
soup = BeautifulSoup(req, 'lxml')
title = soup.find(class_='movie-extras__title').text
rating = soup.find(class_='ratingBlock__value').text
side = soup.find(class_='aside-poster-block__text').text
year = side.split(', ')[0]
country = side.split(', ')[1]
ganre = side.split(', ')[2]
time = soup.find(class_='iconedText__title').text

img_url = soup.find(class_='aside-poster-block__poster').find('img').get('src')
photo = requests.get(url=img_url)
response = photo.content

if os.path.exists('img'):
    pass
else:
    os.mkdir('img')
with open(f'img/img.jpg', 'wb') as file:
    file.write(response)

actors = {
}
actor_block = soup.find(class_='movie-extras__content').find_all(class_='movieDetails__gallery')
for block in actor_block:
    actor_header = block.find(class_='gallery__headerLink').text
    actors[actor_header] = {}
    for person in block.find_all(class_='gallery__item'):
        first_name = person.find(class_='slimPosterBlock__title').text
        try:
            second_name = person.find(class_='slimPosterBlock__secondTitle').text
        except:
            second_name = ''
        film_count = person.find(class_='slimPosterBlock__extra').text
        profile = person.find('a').get('href')
        img = person.find(class_='poster__image').get('src')
        actors[actor_header][first_name] = {
            'first_name': first_name,
            'second_name': second_name,
            'film_count': film_count,
            'profile': profile,
            'img': img
        }


final_data = {
    'title': title,
    'rating': rating,
    'side': side,
    'year': year,
    'country': country,
    'ganre': ganre,
    'time': time,
    'img_url': img_url,
    'actors': actors
}
with open('final_data.json', 'w', encoding='utf-8') as file:
    json.dump(final_data, file, indent=4, ensure_ascii=False)
print('Done!')