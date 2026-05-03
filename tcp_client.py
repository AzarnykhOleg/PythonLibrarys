import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))  # Подключение к серверу
try:
    sock.sendall('Hello, world'.encode('utf-8'))
    data = sock.recv(1024)  # Может потребоваться цикл для больших данных
    print(data.decode('utf-8'))
finally:
    sock.close()