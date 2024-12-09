import requests
from random import seed
from random import randint
from threading import Thread

def task(id):
    while True:
        print(requests.get(url, proxies=proxies))

url = input("url: ")
proxies = {}

threads = []
for n in range(1, 3001):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

