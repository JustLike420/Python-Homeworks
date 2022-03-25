import json
import os

from requests_html import HTMLSession
from bs4 import BeautifulSoup
url = 'https://www.regard.ru/catalog/tovar244993'
session = HTMLSession()
r = session.get(url)
soup = BeautifulSoup(r.text, 'lxml')

name = soup.find(id='goods_head').text
aticle = soup.find(class_='goods_id').text
small_description = soup.find(class_='block-text').text.strip()
# available = soup.find_all(class_='action_block')[0].text
price = soup.find(class_='price lot').text.strip()
table_div = soup.find(id='tabs').find('table')
rows = table_div.find_all('tr')
data = []
characteristic = {}
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
head = ''
for el in data:
    if len(el) == 1:
        characteristic[el[0]] = []
        head = el[0]
    else:
        characteristic[head].append({el[0]: el[1]})
reviews = soup.find(id='reviewsCount').text.replace('(', '').replace(')', '')

photo_link = 'https://www.regard.ru' + soup.find(class_='big_preview').find('a').get('href')

if os.path.exists('img'):
    pass
else:
    os.mkdir('img')
req_photo = session.get(url=photo_link)
response = req_photo.content
with open(f'img/{name}.jpg', 'wb') as file:
    file.write(response)

final_data = {
    'name': name,
    'aticle': aticle,
    'small_description': small_description,
    'price': price,
    'characteristic': characteristic,
    'reviews': reviews
}
print(final_data)
with open('data_file.json', 'w', encoding='utf-8') as file:
    json.dump(final_data, file, indent=4, ensure_ascii=False)