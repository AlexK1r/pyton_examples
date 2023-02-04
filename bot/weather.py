import requests
import datetime

def getweather():
    from config import APIKEY, CITY_ID
    # словарь с эмоджи
    code_to_smile = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': 'Дождь \U00002614',
        'Drizzle': 'Дождь \U00002614',
        'Thunderstorm': 'Гроза \U000026A1',
        'Swor': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F32B'
    }

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'id': CITY_ID, 'units': 'metric', 'lang': 'ru', 'APPID': APIKEY})
        
        data = res.json() 
        #pprint(data) 

        city = data['name']
        cur_weather = data['main']['temp']         
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Я не знаю;) Иди сам помотри!'
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        # время в time Unix это кол-во секунд с 1.1.1970 нужно вызвать библиотеку datetime
        # текущая дата datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        if data['wind']['deg'] >= 0 and data['wind']['deg'] < 22.5 or data['wind']['deg'] >= 337.5 and data['wind']['deg'] <= 360:
            wind_direction = 'Северный'
        elif data['wind']['deg'] >= 22.5 and data['wind']['deg'] < 67.5:
            wind_direction = 'Северо-Восточный'
        elif data['wind']['deg'] >= 67.5 and data['wind']['deg'] < 112.5:
            wind_direction = 'Восточный'
        elif data['wind']['deg'] >= 112.5 and data['wind']['deg'] < 157.5:
            wind_direction = 'Юго-Восточный'
        elif data['wind']['deg'] >= 157.5 and data['wind']['deg'] < 202.5:
            wind_direction = 'Южный'
        elif data['wind']['deg'] >= 202.5 and data['wind']['deg'] < 247.5:
            wind_direction = 'Юго-Западный'
        elif data['wind']['deg'] >= 247.5 and data['wind']['deg'] < 292.5:
            wind_direction = 'Западный'
        elif data['wind']['deg'] >= 292.5 and data['wind']['deg'] < 337.5:
            wind_direction = 'Северо-Западный'

        weather = f'Сейчас: {datetime.datetime.now().strftime("%H:%M %d-%m-%Y")}\n'
        weather += f'Погода в {city}\n Температура: {cur_weather} °С\n {wd}\n Ветер {wind_direction} {wind_speed} м/с\n Влажность: {humidity} %\n Давление: {pressure} мм рт.ст.\n Восход {sunrise_timestamp}\n Закат {sunset_timestamp}'

        # print(weather)
        return (weather)
    except Exception as ex:
        print("Exception (weather):", ex)