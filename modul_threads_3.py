import threading
import socket

# Для проверки работы запустить сервер на одном из портов из диапазона 20...100 (например, nc -lv 127.0.0.1 -p 25)
def check_port(host, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"[+] Порт {port} открыт")
        s.close()
    except Exception as e:
        print(f"[!] Ошибка на порту {port}: {e}")

host = "127.0.0.1"
start_port = 20
end_port = 100

threads = []

for port in range(start_port, end_port + 1):
    thr = threading.Thread(target=check_port, args=(host, port))
    thr.start()
    threads.append(thr)

for thr in threads:
    thr.join()