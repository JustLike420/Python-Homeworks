import requests
import json
import random

from PIL import Image, ImageFont, ImageDraw
from bs4 import BeautifulSoup


def get_photo(word):
    api = f'https://pixabay.com/api/?key=26541811-2c8e763681749498153216c66&q={word}&image_type=photo&pretty=true'
    req = requests.get(api).text
    photo = json.loads(req)
    return random.choice(photo['hits'])['webformatURL']


def main():
    RSS_URL = 'https://3dnews.ru/games/rss/'
    r = requests.get(RSS_URL)
    bs = BeautifulSoup(r.text, 'lxml')
    text = ''
    first_10 = []
    for title in bs.find_all('title'):
        if len(first_10) != 12:
            first_10.append(title.text)
        text += title.text + ' '
    counter = {}
    line = text.split()
    for word in line:
        if len(word) >= 4:
            counter[word] = counter.get(word, 0) + 1

    max_count_word = max(counter.values())
    max_count_word1 = [k for k, v in counter.items() if v == max_count_word]
    photo_url = get_photo(max_count_word1[0].replace(':', ''))

    photo_resp = requests.get(photo_url, stream=True).raw
    photo = Image.open(photo_resp, formats=None)
    photo = photo.resize((1920, 1080))
    font = ImageFont.truetype("timesnewromanpsmt.ttf", size=30)
    draw = ImageDraw.Draw(photo)
    y = 100
    first_10.pop(0)
    first_10.pop(0)
    for t in first_10:
        draw.text((100, y), t, font=font, fill='red')
        y += 100
    photo.save('photo.jpeg')
    photo.show()
    print(max_count_word1[0])


if __name__ == '__main__':
    main()
