from telegram import Update
from telegram.ext import ContextTypes
import datetime
import requests

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n'
                                    '/help\n'
                                    '/time\n'                                    
                                    'вводить только так /sum 12 15\n'
                                    '/game\n'
                                    '/NY\n'
                                    '/weath')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
   await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')


async def daysBeforeNewYear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{daysNY()}')

def daysNY():
    now = datetime.datetime.today()
    NY = datetime.datetime(now.year + 1, 1, 1)
    d = NY-now    
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    return ('До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))


async def getweath(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{getweather()}')

def getweather():
    from config import APIKEY, CITY_ID

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'id': CITY_ID, 'units': 'metric', 'lang': 'ru', 'APPID': APIKEY})
        
        data = res.json()
        # print(data)
        weather = 'Температура: {} °С'.format(data['main']['temp']), 'Погода в вашем городе\nОблачность: {}\n'.format(data['weather'][0]['description'])
        
        # print(weather)
        return (weather)
    except Exception as e:
        print("Exception (weather):", e)