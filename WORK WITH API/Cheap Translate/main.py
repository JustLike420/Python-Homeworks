import json
import time

import requests


def trans_func(text):
    url = "https://cheap-translate.p.rapidapi.com/translate"

    payload = {
        "fromLang": "auto-detect",
        "text": f"{text}",
        "to": "ru"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Host": "cheap-translate.p.rapidapi.com",
        "X-RapidAPI-Key": "f583881c90mshcac603b9de35fc4p13b9d2jsnb343805b2953"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    if response.status_code == 200:
        s = json.loads(response.text)
        return s['translatedText']
    else:
        s = json.loads(response.text)
        print(s['message'])
        time.sleep(60)
        return trans_func(text)


if __name__ == '__main__':
    # s = trans_func('test')
    f = open('text.json', 'w')
    with open('recipes.json', 'r', encoding='utf-8') as file:
        file_lines = file.readlines()
        for line in file_lines:
            file_text = ''
            js = json.loads(line)
            text = js['Description']
            trans_text = trans_func(text)
            js['Description'] = trans_text
            file_text += f'{js}\n'
            f = open('text.json', 'a', encoding='utf-8')
            f.write(file_text)
