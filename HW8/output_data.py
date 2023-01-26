from input_data import staff, departments # импорт словарей


# сохранение данных отделам в txt файл
def save_dep_data(departments):
    with open("departments.txt", "w", encoding='utf-8') as file:
        for key, value in departments.items():
            file.write(f'{key}, {value}\n')

# сохранение данных по сотрудникам в txt файл
def save_staff_data(staff):
    with open("staff.txt", "w", encoding='utf-8') as file:
        for key, value in staff.items():
            file.write(f'{key}, {value}\n')

def console_dep():
    for i in departments:
        print(i, departments[i])

def console_staff():
    for i in staff:
        print(i, staff[i])