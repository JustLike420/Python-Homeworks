import json


with open('iso-container-codes_json.json', 'r', encoding='utf-8') as file:
    src = json.load(file)

# 1. Программа должна вывести среднюю высоту и длину каждого объекта принадлежащее классу «Tank» и «Standard Dry»
# 2. Составить список используемых описаний контейнеров ("description"), которые входят в группу "22GP".
# 3. Вывести элементы высота которых выше 4 и длина больше 13
# 4. Вывести все существующие дескрипшны существующие в файле без повторений и вывести их количество
# 5. Вывести количество элементов с символом «T» в коде элемента в каждой группе.
task_1 = {}
task_2 = []
task_3 = []
task_4 = {}
task_5 = {}
all_height = []
all_length = []

for item in src:
    if item['description'] == 'Tank' or item['description'] == 'Standard Dry':
        all_height.append(item['height'])
        all_length.append(item['height'])

    if item['group'] == '22GP':
        task_2.append(item['description'])

    if item['height'] > 4 and item['length'] > 13:
        task_3.append(item)
    if item['description'] in task_4.keys():
        task_4[item['description']] += 1
    else:
        task_4[item['description']] = 1

    if item['group'] in task_5.keys():
        if 'T' in item['code']:
            task_5[item['group']] += 1
    else:
        if 'T' in item['code']:
            task_5[item['group']] = 1
avg_h = sum(all_height) / len(all_height)
avg_l = sum(all_length) / len(all_length)
task_1 = {
    'avg_height': avg_h,
    'avg_length': avg_l,
}
result = {
    'task_1': task_1,
    'task_2': task_2,
    'task_3': task_3,
    'task_4': task_4,
    'task_5': task_5
}
with open('res.json', 'w', encoding='utf-8') as write_file:
    json.dump(result, write_file)

