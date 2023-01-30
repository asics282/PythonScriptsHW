import telebot
from ui import help as HELP
from data_base import phones
from operations import create_note, phones_print, find_note, delete_note


THOKEN = '6167563919:AAGJQHugVj1Y_pulVBDnFLYphKgkuJJKB40'

bot = telebot.TeleBot(THOKEN)

@bot.message_handler(commands=['help']) # вызов справки
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['add']) # добавление записи
def add(message):
    command = message.text.split(maxsplit=2)
    surName = command[1]
    description = command[2]
    create_note(surName, description)
    text = (f'Добавлена запись {surName} {description}')
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['show']) # вывод тех, кто есть в справочнике
def show(message):
    bot.send_message(message.chat.id, phones_print())

@bot.message_handler(commands=['find']) # поиск по справочнику
def show(message):
    command = message.text.split(maxsplit=2)
    surName = command[1]
    bot.send_message(message.chat.id, find_note(surName))

@bot.message_handler(commands=['del']) # поиск по справочнику
def show(message):
    command = message.text.split(maxsplit=2)
    surName = command[1]
    bot.send_message(message.chat.id, delete_note(surName))

bot.polling(non_stop=True)