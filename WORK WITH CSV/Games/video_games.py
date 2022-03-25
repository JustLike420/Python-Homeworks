import csv

file = open('Video_Games_Sales_as_at_22_Dec_2016.csv', encoding='utf-8')
csv_file = csv.reader(file)
rows = []
i = 0
all_geners = {}
all_platforms = {}
all_platforms_y = {}
all_developers = {'dev': {}}
all_games = {}
for row in csv_file:
    if i != 0:
        genre = row[3]
        NA_Sales = float(row[5])
        EU_Sales = float(row[6])
        JP_Sales = float(row[7])
        Other_Sales = float(row[8])

        if genre in all_geners.keys():
            all_geners[genre]['NA_Sales'] += NA_Sales
            all_geners[genre]['EU_Sales'] += EU_Sales
            all_geners[genre]['JP_Sales'] += JP_Sales
            all_geners[genre]['Other_Sales'] += Other_Sales

        else:
            all_geners[genre] = {'NA_Sales': NA_Sales, 'EU_Sales': EU_Sales, 'JP_Sales': JP_Sales,
                                 'Other_Sales': Other_Sales}

        platform = row[1]
        if platform in all_platforms.keys():
            all_platforms[platform] += 1
        else:
            all_platforms[platform] = 1
        year = row[2]
        all_sales = float(row[9])

        if platform in all_platforms_y.keys():
            if year in all_platforms_y[platform].keys():
                all_platforms_y[platform][year] += all_sales

            else:
                all_platforms_y[platform][year] = all_sales
        else:
            all_platforms_y[platform] = {year: all_sales}

        developer = row[14]
        if developer in all_developers.keys():
            if genre in all_developers[developer].keys():

                all_developers[developer][genre] += all_sales
            else:
                all_developers[developer][genre] = all_sales
        else:
            all_developers[developer] = {genre: all_sales}
    else:
        i += 1

max_dev_gen = {}
sum_gen = {}
for k, v in all_developers.items():
    max_sale = -1
    max_genr = ''
    sum_sale = 0
    for t, x in all_developers[k].items():
        if x > max_sale:
            max_sale = x
            max_genr = t
        sum_sale += x
    sum_gen[k] = sum_sale
    max_dev_gen[k] = max_genr
print(sum_gen)
with open('new_video_games.csv', "w", newline="", encoding="utf-8") as file:
    v_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    list_head = ['Жанр', 'NA', 'EU', 'JP', 'Other']
    v_writer.writerow(list_head)
    i = 0
    for k, v in all_geners.items():
        if i != 0 and k != '':
            na = round(all_geners[k]['NA_Sales'], 3)
            eu = round(all_geners[k]['EU_Sales'], 3)
            jp = round(all_geners[k]['JP_Sales'], 3)
            other = round(all_geners[k]['Other_Sales'], 3)
            lis = [k, na, eu, jp, other]
            v_writer.writerow(lis)
        else:
            i += 1
    v_writer.writerow(['Жанр', 'Кол-во игр', 'Год - прибыль'])
    i = 0
    for k, v in all_platforms.items():
        if i != 0:
            years = []
            for s, x in all_platforms_y[k].items():
                years.append(f'{s} - {round(x, 3)}')
            lis = [k, v] + years
            v_writer.writerow(lis)
        else:
            i += 1
    v_writer.writerow(['Компания', 'Прибыльный жанр', 'Сумма'])
    i = 0
    for k, v in max_dev_gen.items():
        if i != 0 and k!='':
            lis = [k, v, round(sum_gen[k], 3)]
            v_writer.writerow(lis)
        else:
            i += 1