import pyttsx3
import json
import random


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    with open('pokedex.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    pockemon = random.choice(data)
    text = f"Имя: {pockemon['name']['english']}, " \
           f"Тип: {pockemon['type']}, " \
           f"Здоровья: {pockemon['base']['HP']}, " \
           f"Атака: {pockemon['base']['Attack']}, " \
           f"Защита: {pockemon['base']['Defense']}, " \
           f"Супер атака: {pockemon['base']['Sp. Attack']}, " \
           f"Супер защита: {pockemon['base']['Sp. Defense']}, " \
           f"Скорость: {pockemon['base']['Speed']}."
    say(text)
