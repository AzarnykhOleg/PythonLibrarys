import socket


HOST = "127.0.0.1"
PORT = 88

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Сервер ожидает подключения...")
    conn, addr = s.accept()
    with conn:
        print(f"Подключен IP - {addr[0]} порт - {addr[1]}")
        while True:
            data = conn.recv(1024)
            if not data:
                print("Сервер остановлен.")
                break
            print(f'Получено сообщение от клиента: {data.decode('utf-8')}')
            conn.sendall(data.upper())
s.close()
