import socket
import time

def receive_all(sock, length):
# Функция для приема точного количества байт
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise ConnectionError("Соединение прервано")
        data += more
    return data

def send_message(sock, message):
# Отправка сообщения с префиксом длины
    encoded_message = message.encode('utf-8')
    length_prefix = len(encoded_message).to_bytes(4, byteorder='big')
    sock.sendall(length_prefix + encoded_message)

def receive_message(sock):
# Получение сообщения с префиксом длины
# Получаем 4 байта префикса длины
    length_prefix = receive_all(sock, 4)
    message_length = int.from_bytes(length_prefix, byteorder='big')

# Получаем сообщение указанной длины
    message_data = receive_all(sock, message_length)
    return message_data.decode('utf-8')

def create_robust_client():
# Максимальное количество попыток подключения
    max_attempts = 5
    attempt = 0

    while attempt < max_attempts:
        attempt += 1

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(1) # Тайм-аут 3 секунды

        server_address = ('127.0.0.1', 8888)

        try:
            print(f"Попытка подключения {attempt}/{max_attempts}")
            client_socket.connect(server_address)

            # Отправляем сообщение
            message = "Это тестовое сообщение от клиента!"
            send_message(client_socket, message)
            print(f"Отправлено: {message}")

            # Мой костыль в попытках разобраться в причинах отсутствия ответа от сервера
            data = client_socket.recv(1024)
            print(f'Получено сообщение от сервера: "{data.decode('utf-8')}"')

            # Получаем ответ
            #response = receive_message(client_socket)
            #print(f"Получено: {response}")

            # Успешное завершение, выходим из цикла
            break

        except ConnectionRefusedError:
            print("Сервер не доступен")
            if attempt < max_attempts:
                print(f"Повторная попытка через 2 секунды...")
                time.sleep(2)
        except socket.timeout:
            print("Тайм-аут операции")
            if attempt < max_attempts:
                print(f"Повторная попытка через 2 секунды...")
                time.sleep(2)
        except Exception as e:
            print(f"Ошибка: {e}")
            if attempt < max_attempts:
                print(f"Повторная попытка через 2 секунды...")
                time.sleep(2)
        finally:
            client_socket.close()

            if attempt == max_attempts:
                print("Все попытки подключения исчерпаны")

if __name__ == "__main__":
    create_robust_client()