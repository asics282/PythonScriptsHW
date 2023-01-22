from get_data import get_data
# from input_data import input_data
from database import print_dict

print('Программа "ТЕЛЕФОННЫЙ СПРАВОЧНИК"')
print('Желаете посмотерь справочник? (Да/Нет):'); button = input()
if button == "Да":
    print_dict()
print('Ввести данные в ручную?'); button1 = input()
if button1 == "Да":
    print('Введите данные в ручную? (Да/Нет):')
    from add_note import add_new_note
    add_new_note() # ввод новой записи
    from database import print_dict
    print()
    print('ТЕЛЕФОННЫЙ СПРАВОЧНИК')
    print_dict()
    print()
    print("Сохранить справочник? (Да/Нет): "); button2 = input()
    if button2 == "Да":
        from save_data import save_data
        save_data()
        print('Данные сохранены в файл save_data.txt')
    else:
        print('Для завершения работы программы нажмите Enter')
        input()
        exit()
print('Для завершения работы программы нажмите Enter')
input()