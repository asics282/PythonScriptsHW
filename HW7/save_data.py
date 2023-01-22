# запись словоря в txt файл
from database import d

def save_data():
    with open("save.txt", "w", encoding='utf-8') as file:
        for key, value in d.items():
            file.write(f'{key}, {value}\n')