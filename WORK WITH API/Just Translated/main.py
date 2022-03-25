import json
import requests


def translate_text(text):
    url = "https://just-translated.p.rapidapi.com/"

    querystring = {"lang": "ru", "text": f"{text}"}

    headers = {
        'x-rapidapi-host': "just-translated.p.rapidapi.com",
        'x-rapidapi-key': "8aee7aefdamsh1d4ff8ddb4ccd6dp1b0641jsn905444034ef5"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    if response.status_code == 200:
        if '<!DOCTYPE html>' in response.text:
            print('ERROR')
            return ''
        else:

            response = eval(response.text)
            return response['text'][0]
    else:
        return ''


if __name__ == '__main__':

    with open('quotes-100-en.json', 'r', encoding='utf-8') as file:
        json_file = json.load(file)
        out_json = {}
        for key, value in json_file.items():
            ls = []
            for text in value:
                translated_text = translate_text(text)
                ls.append(translated_text)
            out_json[key] = ls
            with open('json_data.json', 'w', encoding='utf-8') as outfile:
                json.dump(out_json, outfile, indent=4, ensure_ascii=False)