'''
Периодический бэкап папки
Создает резервные копии с временными метками
Использует модули: shutil, time, os, datetime
Автоматически создает директорию для бэкапов, если она отсутствует
Каждый бэкап получает уникальное имя с временной меткой
'''
import shutil
import time
from datetime import datetime
import os


def backup_folder(target_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    backup_date = datetime.now()
    formatted_backup_date = backup_date.strftime("%d.%m.%Y_%H-%M-%S")
    full_destination_folder = os.path.join(destination_folder, f'backup_{formatted_backup_date}')
    os.makedirs(full_destination_folder, exist_ok=True)
    shutil.copytree(target_folder, full_destination_folder, dirs_exist_ok=True)
    print(f'Backup folder created at {formatted_backup_date}')
    dirs = 0
    files = 0
    for path in os.walk(full_destination_folder):
        dirs += len(path[1])
        files += len(path[2])
    print(f'{dirs} directories and {files} files created')
    return None

if __name__ == "__main__":
    while True:
        backup_folder("C:/target_folder", "C:/destination_folder")
        time.sleep(10)
