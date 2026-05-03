import subprocess


result = subprocess.run(['dir'], capture_output=True, text=True, shell=True) # обязательно для встроенных команд Windows
print(result.stdout)
'''
# С перехватом вывода как текста
result = subprocess.run(['echo', 'Hello'],
                       capture_output=True,
                       text=True)
print(result.stdout)  # Hello
# С проверкой ошибок и таймаутом
try:
    result = subprocess.run(['sleep', '10'],
                           timeout=5,
                           check=True)
except subprocess.TimeoutExpired:
    print('Процесс завис')
except subprocess.CalledProcessError as e:
    print(f'Ошибка: код {e.returncode}')
'''