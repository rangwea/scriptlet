import time

loop = True


def run():
    while loop:
        print("sleep begin")
        time.sleep(5)
        print("sleep end")


import threading


th = threading.Thread(target=run)
th.start()

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    loop = False

print("sleep finished")
th.join()