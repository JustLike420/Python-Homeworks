import calendar
from PIL import Image, ImageDraw, ImageFont

data = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Декабрь'
}
year = int(input("Введите год: "))
month = int(input("Введите номер месяца: "))
file_name = input("Введите название итогового файла: ")
# year = 2022
# month = 3
# file_name = 'new.png'
s = calendar.monthcalendar(year, month)
image = Image.open('photo_2022-03-23_06-18-28.jpg')
image = image.resize((1920, 1080))
draw = ImageDraw.Draw(image)
image_w, image_h = image.size
font = ImageFont.truetype("ofont.ru_Times New Roman.ttf", size=100)
char_w, char_h = font.getsize('2')


draw.text((500, 100), f'{year} {data[month]}', font=font, fill='red')


draw.text((500, 200), 'ПН', font=font, fill='black')
draw.text((650, 200), 'ВТ', font=font, fill='black')
draw.text((800, 200), 'СР', font=font, fill='black')
draw.text((950, 200), 'ЧТ', font=font, fill='black')
draw.text((1100, 200), 'ПТ', font=font, fill='black')
draw.text((1250, 200), 'СБ', font=font, fill='black')
draw.text((1400, 200), 'ВС', font=font, fill='black')
y = 300
for i in s:
    x = 500
    for j in i:
        if j == 0:
            j = ''
        draw.text((x, y), str(j), font=font, fill='white')
        x += 150
    y += 150

image.save(file_name)
image.show()
