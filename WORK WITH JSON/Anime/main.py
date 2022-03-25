import json
import re

with open('anime-offline-database.json', 'r', encoding='utf-8') as file:
    src = json.load(file)
all_data = src['data']

first_task = []
second_task = 0
therd_task = 0
fourth_task = 0
fifth_task = {}
for anime in all_data:
    """task 1"""
    if 'based on a manga' in anime['tags'] and len(re.findall('(\d+)', anime['title'])) > 0:
        first_task.append(anime['title'])
    """task 2"""
    try:
        if 'OVA' not in anime['type'] and anime['animeSeason']['year'] < 2017:
            for synonym in anime['synonyms']:
                if 'OVA' in synonym:
                    second_task += 1
    except:
        pass
    """task 3"""
    if 'comedy' in anime['tags']:
        for source in anime['sources']:
            if 'anidb' in source:
                therd_task += 1
    """task 4"""
    if anime['animeSeason']['season'] == 'SPRING':
        try:
            ostatok = anime['animeSeason']['year'] % anime['episodes']
            if ostatok == 0:
                fourth_task += 1
        except:
            pass
    """task 5"""
    for tag in anime['tags']:
        if tag in fifth_task.keys():
            fifth_task[tag] += 1
        else:
            fifth_task[tag] = 1

json_finished = {
    'task1': first_task,
    'task2': second_task,
    'task3': therd_task,
    'task4': fourth_task,
    'task5': fifth_task
}

with open("json_finished.json", "w") as write_file:
    json.dump(json_finished, write_file)
print(json_finished)
