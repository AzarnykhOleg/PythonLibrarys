import schedule
import time
import logging
from datetime import datetime

# Настройка логгера
logging.basicConfig(
    filename="task_log.log",
    level=logging.INFO,
    format="%(asctime)s — %(message)s",
    encoding='utf-8'
)

def cleanup_temp():
    logging.info("Очистка временных файлов выполнена.")

def backup_data():
    logging.info("Создан бэкап данных.")

schedule.every(0.1).minutes.do(cleanup_temp)  # для демонстрации, вместо 10
# schedule.every().day.at("23:00").do(backup_data)
schedule.every(0.1).minutes.do(backup_data)

# Основной цикл
while True:
    schedule.run_pending()
    time.sleep(1)