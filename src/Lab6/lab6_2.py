import threading
import time
import urllib.request


def sync():
    tStart = time.time()
    for u in urls:
        r = urllib.request.urlopen(u)
        text = r.read().decode()
        r.close()

    tStop = time.time()
    print("Time sync: " + str(tStop - tStart) + " seconds\n")


def asyncc(s):
    r = urllib.request.urlopen(s)
    text = r.read().decode()
    r.close()


urls = ["https://www.google.com", "https://ya.ru", "https://stackoverflow.com", "https://www.miet.ru",
        "https://www.python.org", "https://www.apple.com", "https://www.youtube.com", "https://vk.com",
        "https://www.w3schools.com", "https://developer.mozilla.org"]

sync()

tStart = time.time()

threads = []

for u in urls:
    thread = threading.Thread(target=asyncc, args=(u,))
    print(u)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

tStop = time.time()
print("Time sync: " + str(tStop - tStart) + " seconds")
