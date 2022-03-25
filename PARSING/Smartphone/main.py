import json
import os
import requests
from bs4 import BeautifulSoup
from lxml import etree
if os.path.exists('img'):
    pass
else:
    os.mkdir('img')

url = 'https://www.po.co/ru/poco-x4-pro-5g/specs'

req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')

name = soup.find(class_='xm-text header').text

img_url = 'https:' + soup.find(class_='specs-con').find('img').get('data-src')

photo = requests.get(url=img_url)
response = photo.content
with open(f'img/{name}.jpg', 'wb') as file:
    file.write(response)

dom = etree.HTML(str(soup))
charactiristic = {}
for i in range(1, 20):
    if len(dom.xpath(f'/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[{i}]/div[1]/span/text()')) != 0:
        char_name = dom.xpath(f'/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[{i}]/div[1]/span/text()')[0]
        char = ' '.join(dom.xpath(f'/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[{i}]/div[2]/span/text()'))
        charactiristic[char_name] = char

data = {
    'name': name,
    'charactiristic': charactiristic
}
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
