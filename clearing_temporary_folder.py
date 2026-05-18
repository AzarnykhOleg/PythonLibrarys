'''
Очистка временной папки
Автоматически удаляет файлы старше заданного времени
Использует функции: os.listdir(), os.path.join(), os.remove(), time.time()
Проверяет возраст файла и удаляет, если он превышает заданный порог
Выполняется по расписанию через time.sleep()
'''
import os
import time


def clearing_temporary_folder(folder_name, age_of_file):
    now = time.time()
    files = os.listdir(folder_name)
    for file in files:
        file_path = os.path.join(folder_name, file)
        if os.path.isfile(file_path) and now - os.path.getmtime(file_path) > age_of_file:
            os.remove(file_path)
            print(f'Удалён файл {file}')


if "__main__" == __name__:
    while True:
        clearing_temporary_folder("C:/Temp/", age_of_file=10)
        time.sleep(60)
