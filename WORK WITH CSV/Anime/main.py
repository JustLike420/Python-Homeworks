import csv

file = open('anime.csv', encoding='utf-8')
csv_file = csv.reader(file)
rows = []

all_geners = {'genre': []}
film_ratings = {}
film_members = {}
i = 0
for row in csv_file:
    if i != 0:
        name = row[1]
        genre = row[2]
        genres = genre.split(', ')
        rating = row[5]
        if rating != '':
            film_ratings[name] = float(rating)
        else:
            film_ratings[name] = 0
        film_members[name] = int(row[6])
        for one_genr in genres:
            if one_genr in all_geners.keys():
                all_geners[one_genr].append(name)
            else:
                all_geners[one_genr] = []

    else:
        i += 1
best_rating_dict = {}
best_members_dict = {}
best_film = ''
best_members = ''
for key in all_geners.keys():
    best_rating = -1
    film_list = all_geners[key]

    for film in film_list:
        if film_ratings[film] > best_rating:
            best_rating = film_ratings[film]
            best_film = film
    best_rating_dict[key] = best_film
    best_member = -1
    for film in film_list:
        if film_members[film] > best_member:
            best_member = film_members[film]
            best_members = film
    best_members_dict[key]=best_members

with open('new_anime.csv', "w", newline="", encoding="utf-8") as file:
    employee_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    list_head = ['Жанр', 'Кол-во фильмов', 'Фильм с максимальным rating', 'Фильм с максимальным members']
    employee_writer.writerow(list_head)
    i = 0
    for k, v in best_rating_dict.items():
        if i != 0:
            lis = [k,len(all_geners[k]), v, best_members_dict[k]]
            employee_writer.writerow(lis)
        else:
            i += 1

