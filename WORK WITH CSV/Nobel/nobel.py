import csv
from datetime import datetime

file = open('nobel_prize_by_winner.csv', encoding='utf-8')
csv_file = csv.reader(file)
rows = []
all_counrty_cat = {}
all_cat_years = {}
all_cat_age = {}
i = 0
for row in csv_file:
    if i != 0:
        counrty = row[6]
        category = row[14]
        # print(counrty, category)
        if counrty in all_counrty_cat.keys():
            all_counrty_cat[counrty].append(category)
        else:
            all_counrty_cat[counrty] = [category]

        born = row[4]
        died = row[5]
        if died != '0000-00-00' and died != '0000/00/00' and born != 'born':
            try:
                b = datetime.strptime(born, '%M/%d/%Y')
                d = datetime.strptime(died, '%M/%d/%Y')
                delta = (d - b).days

                if category in all_cat_years.keys():
                    all_cat_years[category].append(delta)
                else:
                    all_cat_years[category] = [delta]
            except:
                pass
        if row[13] != '' and born != '' and born != '0000/00/00':
            year = float(row[13])
            b_year = float(born.split('/')[2])
            if category in all_cat_age.keys():
                all_cat_age[category].append(year-b_year)
            else:
                all_cat_age[category] = [year-b_year]
    else:
        i +=1
print(all_cat_age)
with open('new_nobel.csv', "w", newline="", encoding="utf-8") as file:
    v_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    list_head = ['Страна', 'Кол-во лауреатов', 'Катеории', ]
    v_writer.writerow(list_head)
    i = 0
    for k, v in all_counrty_cat.items():
        if i != 0 and k != '':
            lis = []
            lis.append(k)
            lis.append(len(v))
            for cat in v:
                lis.append(cat)
            v_writer.writerow(lis)
        else:
            i = 1
    list_head = ['Категория', 'Средня продолжительность жизни в днях', 'Средний возраст получения премии']
    v_writer.writerow(list_head)
    for k, v in all_cat_years.items():
        lis = []
        lis.append(k)
        sum_list = sum(v)
        avg = sum_list/len(v)
        lis.append(round(avg, 0))

        sum_list_y = sum(all_cat_age[k])
        avg_y = sum_list_y / len(all_cat_age[k])
        lis.append(round(avg_y, 0))
        v_writer.writerow(lis)