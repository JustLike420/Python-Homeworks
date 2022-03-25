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
    """1"""
    if len(item['name']['enUS'].split()) == 2:
        try:
            if '+' in item['text']['enUS'] or '-' in item['text']['enUS']:
                task_1.append(item['id'])
        except:
            pass

    """2"""
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
    """3"""
    if 'artist' in item.keys():
        if len(item['artist'].split()) == 2:
            first_ = item['artist'].split()[0][0]
            second_ = item['artist'].split()[1][0]
            if first_ == second_ and item['name']['enUS'][0] == first_:
                task_3 += 1
        # print(item['artist'])
    """4"""
    if 'cost' in item.keys() and 'artist' in item.keys():
        if item['cost'] == 10:
            if 't' in item['artist'] and 'e' in item['artist'] and 'n' in item['artist']:
                task_4.append(item['name']['enUS'])
    """5"""
    if (sqrt(item['dbfId']) % 1) == 0.0:
        task_5 += 1
result = {
    'task_1': task_1,
    'task_2': task_2,
    'task_3': task_3,
    'task_4': task_4,
    'task_5': task_5
}
with open('result.json', 'w', encoding='utf-8') as write_file:
    json.dump(result, write_file)

