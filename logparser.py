import argparse
import re
import sys

# Создаём парсер аргументов
parser = argparse.ArgumentParser(description="Log analyzer CLI utility")
parser.add_argument('--file', required=True, help='Path to log file')
parser.add_argument('--verbose', action='store_true', help='Enable detailed output')

args = parser.parse_args()

# Чтение логов
try:
    with open(args.file, 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"[!] File {args.file} not found.")
    sys.exit(1)

# Обработка
for line in lines:
    if re.search(r'ERROR|WARNING', line):
        print(f"[!] Important: {line.strip()}")
        if args.verbose:
            # Покажем IP, если есть
            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            if ip_match:
                print(f"    → IP found: {ip_match.group()}")


'''
вызов команды из командной строки:
python logparser.py --file sample.log
python logparser.py --file sample.log --verbose
'''