import csv

file = open('summer.csv', encoding='utf-8')
csv_file = csv.reader(file)
rows = []
i = 0
olymp_yaer = {}
discipline_country = {}
country_medals = {}
country_medals1 = {}
for row in csv_file:
    if i != 0:
        year = row[0]
        medal = row[-1]
        discipline = row[3]
        country = row[5]
        if year in olymp_yaer.keys():
            if medal in olymp_yaer[year]:
                olymp_yaer[year][medal] += 1
            else:
                olymp_yaer[year][medal] = 1
        else:
            olymp_yaer[year] = {medal: 1}
        if discipline in discipline_country.keys():
            if country in discipline_country[discipline].keys():
                discipline_country[discipline][country] += 1
            else:
                discipline_country[discipline][country] = 1
        else:
            discipline_country[discipline] = {country: 1}

        gender = row[6]
        if country in country_medals.keys():
            if gender in country_medals[country]:
                country_medals[country][gender] += 1
            else:
                country_medals[country][gender] = 1
        else:
            country_medals[country] = {gender: 1}
        if country in country_medals1.keys():
            if medal in country_medals1[country]:
                country_medals1[country][medal] += 1
            else:
                country_medals1[country][medal] = 1
        else:
            country_medals1[country] = {medal: 1}
    else:
        i += 1
# print(country_medals1)
with open('new_olymp.csv', "w", newline="", encoding="utf-8") as file:
    v_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    list_head = ['Год', 'Золото', 'Серебро', 'Бронза']
    v_writer.writerow(list_head)
    for k, v in olymp_yaer.items():
        lis = [k, v['Gold'], v['Silver'], v['Bronze']]
        v_writer.writerow(lis)
    list_head = ['Страна', 'Мужчины', 'Женщины', 'Золото', 'Серебро', 'Бронза']
    v_writer.writerow(list_head)
    for k, v in country_medals.items():
        lis = [k]
        for x, s in country_medals[k].items():
            lis.append(s)
        if 'Gold' in country_medals1[k].keys():
            lis.append(country_medals1[k]['Gold'])
        else:
            lis.append('')
        if 'Silver' in country_medals1[k].keys():
            lis.append(country_medals1[k]['Silver'])
        else:
            lis.append('')
        if 'Bronze' in country_medals1[k].keys():
            lis.append(country_medals1[k]['Bronze'])
        else:
            lis.append('')
        v_writer.writerow(lis)

    for k, v in discipline_country.items():
        lis = [k]
        best_c = ''
        best_med = -1
        for s, x in discipline_country[k].items():
            if x > best_med:
                best_c = s
                best_med = x
        lis.append(best_c)
        v_writer.writerow(lis)
