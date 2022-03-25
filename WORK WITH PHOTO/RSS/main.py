from PIL import Image, ImageFont, ImageDraw
from bs4 import BeautifulSoup
import requests
import json


def searsh_photo(text):
    url = "https://bing-image-search1.p.rapidapi.com/images/search"
    querystring = {"q": f"{text}"}

    headers = {
        "X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com",
        "X-RapidAPI-Key": "136e3b2ec2msh3ffcdf1cae7ee7dp1ae7e8jsnfa5735b6a15d"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text


def main():
    req = requests.get('https://3dnews.ru/games/rss/')

    bs = BeautifulSoup(req.text, 'lxml')
    text = ''
    first_10 = []
    for title in bs.find_all('title'):
        if len(first_10) != 10:
            first_10.append(title.text)
        text += title.text + ' '
    counter = {}
    line = text.split()
    for word in line:
        if len(word) >= 4:
            counter[word] = counter.get(word, 0) + 1

    max_count = max(counter.values())
    most_frequent = [k for k, v in counter.items() if v == max_count]
    s = json.loads(searsh_photo(min(most_frequent)))
    bg_url = s['value'][0]['thumbnailUrl']

    resp = requests.get(bg_url, stream=True).raw
    image = Image.open(resp, formats=None)

    image = image.resize((1920, 1080))
    font = ImageFont.truetype("arialmt.ttf", size=30)
    draw = ImageDraw.Draw(image)
    y = 100
    for t in first_10:
        draw.text((100, y), t, font=font, fill='black')
        y += 100
    image.save('new.png')
    image.show()


if __name__ == '__main__':
    main()
