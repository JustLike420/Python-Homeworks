# Погода
from datetime import datetime, timezone
from PIL import Image, ImageDraw, ImageFont
import requests
import json


def get_weather(location):
    url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

    querystring = {"aggregateHours": "24", "location": f"{location}", "contentType": "json", "unitGroup": "us",
                   "shortColumnNames": "0"}

    headers = {
        "X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com",
        "X-RapidAPI-Key": "136e3b2ec2msh3ffcdf1cae7ee7dp1ae7e8jsnfa5735b6a15d"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


if __name__ == '__main__':

    # https://github.com/visualcrossing/WeatherIcons/tree/main/PNG/3rd%20Set%20-%20Color
    icon_data = {
        'Clear': 'https://raw.githubusercontent.com/visualcrossing/WeatherIcons/main/PNG/3rd%20Set%20-%20Color/clear-day.png',
        'Partially cloudy': 'https://raw.githubusercontent.com/visualcrossing/WeatherIcons/main/PNG/3rd%20Set%20'
                            '-%20Color/partly-cloudy-day.png',
        'Snow': 'https://raw.githubusercontent.com/visualcrossing/WeatherIcons/main/PNG/3rd%20Set%20-%20Color/snow.png',
        'Overcast': 'https://raw.githubusercontent.com/visualcrossing/WeatherIcons/main/PNG/3rd%20Set%20-%20Color/showers-day.png',
        'Rain': 'https://raw.githubusercontent.com/visualcrossing/WeatherIcons/main/PNG/3rd%20Set%20-%20Color/rain.png'
    }
    city = 'Moscow'
    weather = json.loads(get_weather(city))
    weather_list = weather['locations'][city]['values']
    Date = []
    Wind_Direction = []
    Minimum_Temperature = []
    Maximum_Temperature = []
    Temperature = []
    Wind_Speed = []
    Cloud_Cover = []
    Heat_Index = []
    Chance_Precipitation = []
    Precipitation = []
    Sea_Level_Pressure = []
    Snow_Depth = []
    Snow = []
    Relative_Humidity = []
    Wind_Gust = []
    Wind_Chill = []
    Conditions = []
    for i in range(0, 9):
        # перепроверить позже
        # Date.append(str(weather_list[i]['datetimeStr']))
        date_time_obj = datetime.fromisoformat(weather_list[i]['datetimeStr']).astimezone(timezone.utc)
        Date.append(date_time_obj.strftime('%d.%m'))
        Wind_Direction.append(str(weather_list[i]['wdir']))
        Minimum_Temperature.append(str(weather_list[i]['mint']))
        Maximum_Temperature.append(str(weather_list[i]['maxt']))
        Temperature.append(str(weather_list[i]['temp']))
        Wind_Speed.append(str(weather_list[i]['wspd']))
        Cloud_Cover.append(str(weather_list[i]['cloudcover']))
        Heat_Index.append(str(weather_list[i]['heatindex']))
        Chance_Precipitation.append(str(weather_list[i]['pop']))
        Precipitation.append(str(weather_list[i]['precip']))
        Sea_Level_Pressure.append(str(weather_list[i]['sealevelpressure']))
        Snow_Depth.append(str(weather_list[i]['snowdepth']))
        Snow.append(str(weather_list[i]['snow']))
        Relative_Humidity.append(str(weather_list[i]['humidity']))
        Wind_Gust.append(str(weather_list[i]['wgust']))
        Wind_Chill.append(str(weather_list[i]['windchill']))
        Conditions.append(str(weather_list[i]['conditions'].split(', ')[0]))

    image = Image.open('5f6874eb0f1820506f4bd9f7-700x.jpeg')
    image = image.resize((1920, 1080))
    draw = ImageDraw.Draw(image)
    image_w, image_h = image.size

    font = ImageFont.truetype("ofont.ru_Times New Roman.ttf", size=60)
    char_w, char_h = font.getsize('2')
    j = 0

    for i in range(0, 1920, 192):
        if i == 0:

            draw.text((i, 10), 'date', font=font, fill='red')
            draw.text((i, char_h + 10), 'mint', font=font, fill='red')
            draw.text((i, 2 * char_h + 10), 'maxt', font=font, fill='red')
            draw.text((i, 3 * char_h + 10), 'temp', font=font, fill='red')
            draw.text((i, 4 * char_h + 10), 'wspd', font=font, fill='red')
            draw.text((i, 5 * char_h + 10), 'cloudc', font=font, fill='red')
            draw.text((i, 6 * char_h + 10), 'wdir', font=font, fill='red')
            draw.text((i, 7 * char_h + 10), 'pop', font=font, fill='red')
            draw.text((i, 8 * char_h + 10), 'precip', font=font, fill='red')
            draw.text((i, 9 * char_h + 10), 'sealeve', font=font, fill='red')
            draw.text((i, 10 * char_h + 10), 'snowd', font=font, fill='red')
            draw.text((i, 11 * char_h + 10), 'snow', font=font, fill='red')
            draw.text((i, 12 * char_h + 10), 'humid', font=font, fill='red')
            draw.text((i, 13 * char_h + 10), 'wgust', font=font, fill='red')
            draw.text((i, 14 * char_h + 10), 'windc', font=font, fill='red')
            draw.text((i, 17 * char_h + 10), city, font=font, fill='blue')

        else:

            draw.text((i, 10), Date[j], font=font, fill='black')
            draw.text((i, char_h + 10), Minimum_Temperature[j], font=font, fill='black')
            draw.text((i, 2 * char_h + 10), Maximum_Temperature[j], font=font, fill='black')
            draw.text((i, 3 * char_h + 10), Temperature[j], font=font, fill='black')
            draw.text((i, 4 * char_h + 10), Wind_Speed[j], font=font, fill='black')
            draw.text((i, 5 * char_h + 10), Cloud_Cover[j], font=font, fill='black')
            draw.text((i, 6 * char_h + 10), Wind_Direction[j], font=font, fill='black')
            draw.text((i, 7 * char_h + 10), Chance_Precipitation[j], font=font, fill='black')
            draw.text((i, 8 * char_h + 10), Precipitation[j], font=font, fill='black')
            draw.text((i, 9 * char_h + 10), Sea_Level_Pressure[j], font=font, fill='black')
            draw.text((i, 10 * char_h + 10), Snow_Depth[j], font=font, fill='black')
            draw.text((i, 11 * char_h + 10), Snow[j], font=font, fill='black')
            draw.text((i, 12 * char_h + 10), Relative_Humidity[j], font=font, fill='black')
            draw.text((i, 13 * char_h + 10), Wind_Gust[j], font=font, fill='black')
            draw.text((i, 14 * char_h + 10), Wind_Chill[j], font=font, fill='black')

            url1 = icon_data[Conditions[j]]
            resp = requests.get(url1, stream=True).raw
            img1 = Image.open(resp, formats=['png'])
            image.paste(img1, (i, 15 * char_h + 10), img1)

            j += 1
    image.save('new.png')
    image.show()
