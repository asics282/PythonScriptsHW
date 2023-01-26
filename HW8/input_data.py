departments = {'Директора':[], 'Back-end':[], 'Front-end':[], 'Бухгалтерия':[], 'HR':[]}
staff = {}

# создание отдела
# def create_dep():
#     dep = input('Введите название отдела: ')
#     departments[dep] = {} # создание пустого словоря для отделов
#     print(f'Создан отдел {dep}')

def print_dict(d): # печать словаря ключ - значение
    for item in d.items():
        print(item)

# создание сотрудника
def create_employee():
    employee = input('Введите должность сотрудника: ')
    staff[employee] = [] # создание пустого списка для данных сотрудника
    surName = input('Введите фамилию сотрудника: '); staff[employee].append(surName)
    firstName = input('Введите имя сотрудника: '); staff[employee].append(firstName)
    patronymic = input('Введите отчество сотрудника: '); staff[employee].append(patronymic)
    phone = input('Введите телефон сотрудника: '); staff[employee].append(phone)
    print(f'Создан сотрудник {employee}') # показываем, что создан такой-то сотрудник
    print(f'На данный момент существуют следующие отделы:')
    print_dict(departments) # показываем какие отделы сейчас существуют
    department = input('Введите название отдела, куда прикрепить сотрудника: ')
    departments[department].append(employee) # добавление должности в словарь отделов

# def edit_employee():

# удаление сотрудника
def delete_employee():
    employee = input('Введите должность сотрудника: ')
    staff.pop(employee) # удаляем ключ (и соотв. значение) из списка сотрудников
    for key in departments: # удаление сотрудника из отдела
        if employee in departments[key]:
            departments[key].remove(employee)
    print(f'Сотрудник {employee} удален!') # показываем, что сотрудник удален