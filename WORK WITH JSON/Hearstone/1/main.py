import json
from math import sqrt

with open('cards-hearthstone.json', 'r', encoding='utf-8') as file:
    src = json.load(file)

task_1 = []
task_2 = []
task_3 = 0
task_4 = []
task_5 = 0
for item in src:
    if len(item['name']['enUS'].split()) == 2:
        try:
            if '+' in item['text']['enUS'] or '-' in item['text']['enUS']:
                task_1.append(item['id'])
        except:
            pass
    if 'attack' in item.keys():
        if 'health' not in item.keys():
            health = 0
        else:
            health = item['health']
        sum_ = item['attack'] + health
        try:
            if item['dbfId'] % sum_ == 0:
                task_2.append(item['name']['enUS'])
        except:
            pass
    if 'artist' in item.keys():
        if len(item['artist'].split()) == 2:
            first_ = item['artist'].split()[0][0]
            second_ = item['artist'].split()[1][0]
            if first_ == second_ and item['name']['enUS'][0] == first_:
                task_3 += 1
    if 'cost' in item.keys() and 'artist' in item.keys():
        if item['cost'] == 10:
            if 't' in item['artist'] and 'e' in item['artist'] and 'n' in item['artist']:
                task_4.append(item['name']['enUS'])
    if (sqrt(item['dbfId']) % 1) == 0.0:
        task_5 += 1
result = {
    'task_1': task_1,
    'task_2': task_2,
    'task_3': task_3,
    'task_4': task_4,
    'task_5': task_5
}
with open('output.json', 'w', encoding='utf-8') as write_file:
    json.dump(result, write_file)

