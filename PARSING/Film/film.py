from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json
import os

session = HTMLSession()
r = session.get('https://www.ivi.ru/watch/146387/person').text

soup = BeautifulSoup(r, 'lxml')
end_json = {}
end_json['title'] = soup.find(class_='movie-extras__title').text
end_json['rating'] = soup.find(class_='ratingBlock__value').text
side = soup.find(class_='aside-poster-block__text').text
end_json['year'] = side.split(', ')[0]
end_json['country'] = side.split(', ')[1]
end_json['ganre'] = side.split(', ')[2]
end_json['time'] = soup.find(class_='iconedText__title').text

end_json['img_url'] = soup.find(class_='aside-poster-block__poster').find('img').get('src')
photo = session.get(url=end_json['img_url']).content

os.mkdir('img')
with open(f'img/img.jpg', 'wb') as file:
    file.write(photo)

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
end_json['actors'] = actors
with open('final_data.json', 'w', encoding='utf-8') as file:
    json.dump(end_json, file, indent=4, ensure_ascii=False)
print('Done!')
