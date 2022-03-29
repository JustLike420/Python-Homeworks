import requests
import json
import pyttsx3


def speek(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    req = requests.get(url)
    cur_data = json.loads(req.text)
    speek(f"{cur_data['Valute']['USD']['Name']}: {str(cur_data['Valute']['USD']['Value']).replace('.', ',')} рубля")
    speek(f"{cur_data['Valute']['EUR']['Name']}: {str(cur_data['Valute']['EUR']['Value']).replace('.', ',')} рубля")
    speek(f"{cur_data['Valute']['CNY']['Name']}: {str(cur_data['Valute']['CNY']['Value']).replace('.', ',')} рубля")
    speek(f"{cur_data['Valute']['CAD']['Name']}: {str(cur_data['Valute']['CAD']['Value']).replace('.', ',')} рубля")
    speek(f"{cur_data['Valute']['GBP']['Name']}: {str(cur_data['Valute']['GBP']['Value']).replace('.', ',')} рубля")


if __name__ == '__main__':
    main()
