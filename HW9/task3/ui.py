from operations import *

# меню программы
help = ('''
/help - получить список команд
/show - посмотреть кто есть в справочнике
/add - добавить номер телефона (/add Фамилия Имя Телефон Описание)
/find - поиск телефона (/find Фамилия)
/del - удалить запись (/del Фамилия)
''')
# run = True
# while run:
#     click = input('Введите команду: ')
#     if click == 'help':
#         print(help) # вызов справки
#     elif click == 'show':
#         phones_print() # печать в консоль всех телефонов
#     elif click == 'add':
#         create_note() # создание создание записи и добавление
#     elif click == 'del':
#         delete_note() # удаление записи
#     elif click == 'find':
#         find_note() # поиск записи
#     elif click == 'exit':
#         print('Спасибо за использование! До свидания!')
#         break
#     else:
#         print('Некорректный ввод команды', 'Введите команду из справки', sep='\n')