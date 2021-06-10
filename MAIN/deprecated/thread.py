import _thread
import time

def CustomThread(name, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(name, "-->", time.time())


def CustomThreadTwo(name, delay):
    count = 0

    while count < 3:
        time.sleep(delay)
        count += 1
        print(name, "-->", time.time())


_thread.start_new_thread(CustomThread, ("Sleeper one", 1))
_thread.start_new_thread(CustomThreadTwo, ("Second Thread", 3))

input()