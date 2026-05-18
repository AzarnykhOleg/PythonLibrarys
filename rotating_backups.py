'''
скрипт, который раз в минуту делает бэкап папки data/,
и сохраняет не более 5 последних копий (старые удаляет)
'''
import os
import time
import shutil
from datetime import datetime

SOURCE_FOLDER = 'data'
BACKUP_FOLDER = 'backups'
MAX_BACKUPS = 5

os.makedirs(BACKUP_FOLDER, exist_ok=True)

# Функция для сортировки по дате
def get_mtime(item):
    return item[1]

while True:
    # Создание имени бэкапа
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_name = 'backup_' + now
    backup_path = os.path.join(BACKUP_FOLDER, backup_name)

    # Копируем папку
    shutil.copytree(SOURCE_FOLDER, backup_path)
    print("Создан бэкап:", backup_path)

    # Получаем список всех бэкапов с датой изменения
    backups = []
    for folder in os.listdir(BACKUP_FOLDER):
        full_path = os.path.join(BACKUP_FOLDER, folder)
        if os.path.isdir(full_path):
            backups.append((full_path, os.path.getmtime(full_path)))

    # Сортируем по дате изменения
    backups.sort(key=get_mtime)

    # Удаляем старые, если их больше 5
    while len(backups) > MAX_BACKUPS:
        to_delete = backups.pop(0)[0]
        shutil.rmtree(to_delete)
        print("Удалён старый бэкап:", to_delete)

    time.sleep(5)
