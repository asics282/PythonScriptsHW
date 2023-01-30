from data_base import phones

# поиск человека в списке контактов
def find_note(surName):
    if surName in phones: # если человек есть среди контактов, то печатаем информацию о нем
        text = str(surName)
        for value in phones[surName]:
            text = text + " " + (value)
        return text
    else:
        return 'Такого человека нет'

# печать всего словаря (ключ)
def phones_print():
    if len(phones) == 0: # если словарь пустой, то говорим об этом
        return 'Справочник пуст'
    else:
        text = ''
        for key in phones: # если непустой, то печатаем
                text = text + key + '\n'
    return text
            

# создание новой записи
def create_note(surName, description):
    phones[surName] = [] # добавление фамилии как ключа в словаре
    phones[surName].append(description) # добавление описания в список как значения по указанному ключу

# удалиение записи
def delete_note(surName):
    if surName in phones:
        try:
            del phones[surName]
            return 'Запись ' + surName + ' удалена'
        except KeyError:
            pass
    else:
        return 'Вы пытаетесь удалить запись, которой нет'