from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

HELP = '''
/hi - приветствие
/help - получить список команд
/calc - произвести действие +,-,*,/ (/calc 4 + 5 или /act 4+j / 5-2j)
'''

# приветствие
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# вызов справки
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{HELP}')

# калькулятор для рациональных и комплексных чисел
async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    
    items = msg.split() # /calc 123 + 534
    # определяем комплесные числа в строке или нет
    if 'j' not in msg:
        x = int(items[1])
        y = int(items[3])
    else:
        x = complex(items[1])
        y = complex(items[3])

    if items[2] == '+':
        await update.message.reply_text(f'{x} + {y} = {x+y}')

    elif items[2] == '-':
        await update.message.reply_text(f'{x} - {y} = {x-y}')

    elif items[2] == '*':
        await update.message.reply_text(f'{x} * {y} = {x*y}')

    elif items[2] == '/':
        await update.message.reply_text(f'{x} / {y} = {x/y}')

    else:
        print('Неизвестное действие')
        await update.message.reply_text('Неизвестное действие')