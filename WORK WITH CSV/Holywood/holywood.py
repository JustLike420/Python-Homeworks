import csv

file = open('Highest Holywood Grossing Movies.csv', encoding='utf-8')
csv_file = csv.reader(file)
i = 0
compony_year = {}
film_price = {}
genres_films = {}
for row in csv_file:
    if i != 0:
        compony = row[3]
        if row[4] != 'NA':

            year = row[4].split(', ')[1]
            if compony in compony_year.keys():
                if year in compony_year[compony].keys():
                    compony_year[compony][year] += 1
                else:
                    compony_year[compony][year] = 1
            else:
                compony_year[compony] = {year: 1}
        title = row[1]
        domestic = int(row[5])
        international = int(row[6])
        world = int(row[7])
        film_price[title] = [domestic, international, world]
        genres = row[8].replace('[', '').replace(']', '').replace("'", '').split(', ')

        for genre in genres:
            if genre in genres_films.keys():

                if film_price[genres_films[genre][0]][0] < domestic:
                    genres_films[genre][0] = title
                if film_price[genres_films[genre][1]][1] < international:
                    genres_films[genre][2] = title
                if film_price[genres_films[genre][2]][2] < world:
                    genres_films[genre][2] = title
            else:
                genres_films[genre] = [title, title, title]
    else:
        i += 1
# print(compony_year)
with open('new_holywood.csv', "w", newline="", encoding="utf-8") as file:
    v_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    list_head = ['Company', 'Year - count']
    v_writer.writerow(list_head)
    for k, v in compony_year.items():
        lis = [k]
        for x, y in v.items():
            lis.append(f'{x} - {y}')
        v_writer.writerow(lis)
    list_head = ['Genre', 'Domestic Sales', 'International Sales', 'World Sales']
    v_writer.writerow(list_head)
    for k, v in genres_films.items():
        lis = [k]
        for film in v:
            lis.append(film)
        v_writer.writerow(lis)
