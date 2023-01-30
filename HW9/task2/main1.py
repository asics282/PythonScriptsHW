from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import *

app = ApplicationBuilder().token("5667596692:AAG_682gNenAoZIYfevLmiSpgewNhvzIqYs").build()

app.add_handler(CommandHandler("hi", hello))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calc_command))

app.run_polling()