import csv

file = open('Car_Prices_Poland_Kaggle.csv', encoding='utf-8')
csv_file = csv.reader(file)
rows = []
i = 0
province_year = {}
province_mark = {}
proivnce_model = {}
for row in csv_file:
    if i != 0:
        province = row[9]
        year = row[4]
        if province in province_year.keys():
            if year in province_year[province].keys():
                province_year[province][year] += 1
            else:
                province_year[province][year] = 1
        else:
            province_year[province] = {year: 1}
        mark = row[1]
        price = int(row[10])
        if province in province_mark.keys():
            if mark in province_mark[province].keys():
                province_mark[province][mark]['count'] += 1
                province_mark[province][mark]['price'].append(price)
            else:
                province_mark[province][mark] = {'count': 1, 'price': [price]}

        else:
            province_mark[province] = {mark: {'count': 1, 'price': [price]}}
        model = row[2]
        if province in proivnce_model.keys():
            if model in proivnce_model[province].keys():
                proivnce_model[province][model]['price'].append(price)
            else:
                proivnce_model[province][model] = {'price': [price]}
        else:
            proivnce_model[province] = {model: {'price': [price]}}
    else:
        i += 1

print(proivnce_model)
with open('new_cars.csv', "w", newline="", encoding="utf-8") as file:
    v_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    list_head = ['Провинция', 'Модель', 'Сред Мин Макс']
    v_writer.writerow(list_head)
    for k, v in proivnce_model.items():
        lis = []
        lis.append(k)
        for s, x in v.items():
            lis.append(s)
            sum_ = sum(x['price'])
            avg = sum_ / len(x['price'])
            lis.append(f'{round(avg, 0)} - {min(x["price"])} - {max(x["price"])}')
        v_writer.writerow(lis)
    list_head = ['Провинция', 'Марка', 'Кол-во', 'Средняя стоимость']
    v_writer.writerow(list_head)
    for k, v in province_mark.items():
        lis = []
        lis.append(k)
        for s, x in v.items():
            lis.append(s)
            lis.append(x['count'])
            sum_ = sum(x['price'])
            avg = sum_ / len(x['price'])
            lis.append(round(avg, 0))
        v_writer.writerow(lis)


    list_head = ['Провинция', 'Год - кол-во']
    v_writer.writerow(list_head)
    for k, v in province_year.items():
        lis = []
        lis.append(k)
        for s, x in province_year[k].items():
            lis.append(f'{s} - {x}')
        v_writer.writerow(lis)
