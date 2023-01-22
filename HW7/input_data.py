# введение данных пользователем
def input_data(): # хранит список введенных пользователем данных
    print('Введите Фамилию:'); lastName = input()
    print('Введите Имя:'); firstName = input()
    print('Введите Телефон:'); phone = input()
    print('Введите Описание:'); other = input()
    return [lastName, firstName, phone, other]