import time
import os
import socket

def run_scanner(host, port):
    # Код сканера
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((host, port))
    if result == 0:
        print(f"[+] Порт {port} открыт")
    elif result == 111 or result == 10061:
        print(f"[-] Порт {port} закрыт")
    else:
        print(f"[?] Порт {port} фильтруется или неизвестный ответ ({result})")
    s.close()
    time.sleep(2)

while True:
    for port in range(80, 90):
        run_scanner("127.0.0.1", port)
    time.sleep(7)