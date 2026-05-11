import socket
import threading

def handle_client(client_socket, client_address):
    try:
        print(f"Обработка клиента {client_address}")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            print(f"Получено от {client_address}: {data.decode('utf-8')}")
            client_socket.sendall(f"Эхо: {data.decode('utf-8').upper()}".encode('utf-8'))
    except Exception as e:
        print(f"Ошибка при обработке клиента {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"Соединение с {client_address} закрыто")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8888)
    server_socket.bind(server_address)
    server_socket.listen(10)
    print(f"Сервер запущен на {server_address[0]}:{server_address[1]}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_address)
            )
            client_thread.daemon = True
            client_thread.start()
            print(f"Активные соединения: {threading.active_count() - 1}")
    except KeyboardInterrupt:
        print("Завершение работы сервера")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()

