import http.client
import json


def translate(text):
    conn = http.client.HTTPSConnection("microsoft-translator-text.p.rapidapi.com")
    payload = '[{"Text": "' + text.replace('"', "'") + '"}]'

    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com",
        'x-rapidapi-key': "db7d93cf34msh069dc19c117f9fcp112835jsnc95109e20ab8"
    }

    conn.request("POST", "/translate?to=ru&api-version=3.0&profanityAction=NoAction&textType=plain", payload, headers)

    res = conn.getresponse()
    if res.status == 200:

        data = res.read().decode("utf-8")
        fin_data = eval(data)
        trans_text = fin_data[0]['translations'][0]['text']
        return trans_text
    else:
        return text


if __name__ == '__main__':

    f = open('text.json', 'w')
    with open('nyt2.json', 'r', encoding='latin-1') as f:
        i = 0
        for line in f.readlines():
            file_text = ''
            js = json.loads(line)
            text = js['description']

            translated_text = translate(text)
            js['description'] = translated_text
            file_text += f'{js}\n'
            print(js['description'])
            f = open('text.json', 'a', encoding='utf-8')
            f.write(file_text)
