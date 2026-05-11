import socket


HOST = "127.0.0.1"
PORT = 88


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        s.sendall("Hello, world".encode('utf-8'))
        data = s.recv(1024)
        print(f'Получено сообщение от сервера: "{data.decode('utf-8')}"')
    except ConnectionRefusedError:
        print("Сервер не доступен. Проверьте, запущен ли он.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Соединение закрыто")
