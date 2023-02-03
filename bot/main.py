# # команду выполнить в PowerShell Set-ExecutionPolicy Unrestricted -Scope CurrentUser

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from config import TOKIEN

app = ApplicationBuilder().token(TOKIEN).build()


app.add_handler(CommandHandler('hi', hi_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('time', time_command))
app.add_handler(CommandHandler('sum', sum_command))
app.add_handler(CommandHandler('NY', daysBeforeNewYear))
app.add_handler(CommandHandler('weath', getweath))

print("start")
app.run_polling()