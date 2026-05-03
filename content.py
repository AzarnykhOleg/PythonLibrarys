import requests
import os

url = ("https://img.freepik.com/free-photo/cute-kitten-sitting-looking-camera-"
       "surrounded-by-flowers-generated-by-artificial-intelligence_25030-66192.jpg"
       "?semt=ais_hybrid")
filename = "cat_2.jpg"
path = os.path.join('C:\\', 'Users', 'User', 'Pictures', filename)

response = requests.get(url)

if response.status_code == 200:
    with open(path, 'wb') as file:
        file.write(response.content)
    print(f"Файл загружен: {path}")
else:
    print(f"Не удалось скачать изображение. Статус код: {response.status_code}")



