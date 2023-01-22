# добавление новой записи в словарь (справочник)
from input_data import input_data
from database import d


new_array = (input_data()) # ввод новой записи
def add_new_note():
    d[new_array[0]] = (" ".join(new_array[1:]))