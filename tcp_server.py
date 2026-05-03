import socket


serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Разрешение повторного использования адреса (избежать "Address already in use")
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_sock.bind(('localhost', 55000))  # или ('', 55000) для всех интерфейсов
serv_sock.listen(5)  # backlog=5, размер очереди ожидающих соединений
print("Сервер ожидает соединения...")
conn, addr = serv_sock.accept()  # Блокировка до подключения клиента
# conn — новый сокет для общения с клиентом, addr — кортеж (IP, port)
with conn:
    print(f"Подключен {addr}")
    while True:
        data = conn.recv(1024)  # Чтение до 1024 байт
        if not data:
            break  # Клиент отключился
        conn.sendall(data.upper())  # Отправка ответа
serv_sock.close()

