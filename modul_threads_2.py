import threading
import time

def worker(num):
    print(f"Поток {num} запущен")
    time.sleep(2)
    print(f"Поток {num} завершён")

threads = []

for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Все потоки завершены")
