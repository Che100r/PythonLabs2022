import os
import re
import time
from threading import Thread


def search():
    # cur_dir = os.getcwd() + "\src\Lab6"   # Windows
    cur_dir = os.getcwd()   # MacOS
    r = re.compile(r"\w*key\w*\.txt\b")
    new_list = []

    for root, dirs, files in os.walk(cur_dir):
        for file in files:
            if r.match(file):
                new_list.append(root + "/" + file)

    return new_list


time_start = time.time()
result = search()
time_end = time.time()
print("Time: " + str(time_end - time_start))

th = Thread(target=search)
time_start = time.time()
result2 = th.start()
time_end = time.time()
print("Time: " + str(time_end - time_start))
