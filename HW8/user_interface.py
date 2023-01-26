from input_data import *
from output_data import *

# меню программы
def choose():
    print('ПРОГРАММА ДЛЯ СОЗДАНИЯ БАЗЫ ДАННЫХ IT-КОМПАНИИ')
    help = ('''
    help - получить справку о программе
    show - посмотреть данные о сотрудниках
    show1 - посмотреть об отделах
    add - добавить сотрудника
    del - удалить сотрудника
    save - сохранить данные о сотрудниках в файл
    save1 - сохранить данные об отделах в файл
    exit - выход из программы
    ''')
    print(help)
    run = True
    while run:
        click = input('Введите команду: ')
        if click == 'help':
            print(help) # вызов справки
        elif click == 'show':
            console_staff() # печать в консоль данных о сотрудниках
        elif click == 'show1':
            console_dep() # печать в консоль данных об отделах
        elif click == 'add':
            create_employee() # создание сотрудника и добавление к отделу
        elif click == 'del':
            delete_employee() # удаление сотрудника из списка сотрудников и отдела
        elif click == 'save':
            save_staff_data(staff)
        elif click == 'save1':
            save_dep_data(departments)
        elif click == 'exit':
            break
        else:
            print('Некорректный ввод команды', 'Введите команду из справки', sep='\n')
    print('Для завершения работы программы нажмите "Enter"'); input()