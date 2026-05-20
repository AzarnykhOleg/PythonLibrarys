'''
Создайте CLI-утилиту portscanner.py, которая принимает IP-адрес
и порт как параметры и проверяет, открыт ли порт.
📌 Параметры:
    -ip (обязательный): IP-адрес хоста.
    -port (обязательный): порт или диапазон (-port 22, -port 20-80).
✅ Условия успешного выполнения:
    Работает с одним портом и диапазоном.
    Показывает, какие порты открыты.
    Использует argparse.
💬Подсказка
    Используйте socket.
    Разберите порт (один или диапазон).
    Попробуйте сделать -verbose для подробного вывода.
'''
import argparse
import socket
import sys
import threading


def scanner(ip_addr, port, verbose=False):
    with socket.socket() as sock:
        sock.settimeout(1)
        sock_answer = sock.connect_ex((ip_addr, port))
        if sock_answer == 0:
            print(f'[+] порт {port} открыт')
        elif verbose:
            print(f'[-] порт {port} закрыт - {sock_answer}')

def parse_ports(port_arg):
    port_arg = port_arg.split('-')
    start_port = int(port_arg[0])
    end_port = int(int(port_arg[-1]) + 1)
    return start_port, end_port

def main():
    parser = argparse.ArgumentParser(description="Скрипт для сканирования портов")
    parser.add_argument(
        '--ip',
        help="IP-адрес",
        required=True,
        type=str,
        action='store'
    )
    parser.add_argument(
        '--port',
        help="Порт или диапазон портов (например, 22 или 22-80)",
        required=True,
        type=str,
        action='store'
    )
    parser.add_argument(
        '--verbose',
        help="Подробный вывод результата выполнения скрипта",
        required=False,
        default=False,
        action='store_true'
    )
    args = parser.parse_args()
    start_port, end_port = parse_ports(args.port)
    ip_addr = args.ip
    threads = []
    for port in range(start_port, end_port):
        t = threading.Thread(target=scanner, args=(ip_addr, port, args.verbose))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print('Сканирование завершено')



if __name__ == '__main__':
    main()
    sys.exit(0)
