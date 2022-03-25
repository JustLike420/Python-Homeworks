import json

import requests
from bs4 import BeautifulSoup
import os
url = 'https://freesoft.ru/windows/cpython'

req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')
title = soup.find(class_='i-title').text.strip()
sub_title = soup.find(class_='i-subtitle').text.strip()

img_link = soup.find(class_='i-image').find('img').get('src')

if os.path.exists('img') is not True:
    os.mkdir('img')
with open(f'img/{title}.jpg', 'wb') as file:
    img = requests.get(img_link).content
    file.write(img)

specs = soup.find(class_='fs-app-specifications').find_all(class_='s-item')
char = {}
for spec in specs:

    block = spec.text.split('\n')

    spec_name = block[1]
    if block[2] != '':
        spec_desc = block[2]
    else:
        spec_desc = block[3]
    char[spec_name.strip()] = spec_desc.strip()

description = soup.find('span', itemprop='description').text

download_block = soup.find(class_='fs-app-versions').find_all(class_='v-item')
versions = []
for item in download_block:
    ver_name = item.find(class_='v-item__wrap').text.strip()
    versions.append(ver_name)
r_stars = soup.find(class_='fs-app-rating__value').text.strip()
r_count = soup.find(class_='fs-app-rating__text').text.strip()
rating = {
    'rating_stars': r_stars,
    'rating_count': r_count
}
print(rating)
json_file = {
    'title': title,
    'sub_title': sub_title,
    'img_link': img_link,
    'charactiristics': char,
    'description': description,
    'versions': versions,
    'rating': rating
}
with open('json_file.json', 'w', encoding='utf-8') as file:
    json.dump(json_file, file, indent=4, ensure_ascii=False)