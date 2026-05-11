import socket
import threading
import queue

# МНОГОПОТОЧНЫЙ СКАНЕР ПОРТОВ С ОЧЕРЕДЬЮ

THREADS = 25
ip_addr = ['127.0.0.1', '8.8.8.8', 'petr-winner.ru']
start_port = 20
end_port = 200

# Создание очереди задач (хранит (ip_addr, port))
task_queue = queue.Queue()
for ip in ip_addr:
    for port in range(start_port, end_port + 1):
        task_queue.put((ip, port))

# Блокировка для безопасного вывода из нескольких потоков
print_lock = threading.Lock()

# Функция для проверки портов
def scan_port ():
    while not task_queue.empty():
        ip_addr, port  = task_queue.get()

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
                soc.settimeout(2)
                result = soc.connect_ex((ip_addr, port))

            with print_lock:
                if result == 0:
                    print(f'[+] {ip_addr}:{port} открыт')
                else:
                    pass
        except Exception as e:
            with print_lock:
                print(f'[!] {ip_addr}:{port} ошибка: {e}')
        finally:
            task_queue.task_done()

# Создаём и запускаем потоки
threads = []
for i in range(THREADS):
    t = threading.Thread(target=scan_port, name=f'Scanner-{i+1}')
    t.start()
    threads.append(t)

# Ждём завершения обработки всех задач
task_queue.join()

# Дожидаемся завершения всех потоков
for t in threads:
    t.join()
print('Сканирование завершено')




