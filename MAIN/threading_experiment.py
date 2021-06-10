import concurrent.futures
import threading
import time
import random
import requests
from typing import Optional, Callable, Any, Iterable, Mapping

start = time.perf_counter()


class ImageDownloadCTA(threading.Thread):


    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.image_url = "https://unsplash.com/photos/qjrjJnFypa0"

    def run(self):
        img_byte = requests.get(self.image_url).content
        img_name = self.image_url.split("/")[4]
        img_name = f"{img_name}.jpg"
        img_path = "C:\\Users\\User\\PycharmProjects\\firstOne\\CustomDownloads\\"
        with open(img_path + img_name, "wb") as fh:
            fh.write(img_byte)
            print(f"{img_name} was downloaded")

class CustomThreadClassAttempt(threading.Thread):

    def __init__(self, name, min, max):
        threading.Thread.__init__(self)
        self.name = name
        self.min = min
        self.max = max

    def run(self):
        print("Start: ", time.time())
        self.functionOfCTA(self.min, self.max)
        print("End: ", time.time())

    def functionOfCTA(self, min, max):
        a = [x for x in range(min, max)]
        print(random.choice(a))
        print(int(random.random() * 10))


def checkSec(v):  # just for fun and to consume more system resources
    if v == 1:
        return "Second"
    elif v < 0:
        raise ValueError
    else:
        return "Seconds"


def CustomThread(name, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(name, "-->", time.time())


def SquareAndCube(number):
    print(" Square = {}".format(number * number), "\n", "Cube = {}".format(number ** 3))


def PrintSquaresGen(minn, maxx):
    for i in range(minn, maxx + 1):
        output_sqr = i ** 2
        yield output_sqr


def PrintSquares(minn, maxx):
    a = PrintSquaresGen(minn, maxx)
    for i in a:
        print(i)
    print("_____COMPLETED_____")


if __name__ == "__main__":
    # t1 = threading.Thread(target=CustomThread, args=["Thread 1", 1])
    # t2 = threading.Thread(target=CustomThread, args=("Thread 2", 3))
    # squareAndCube =  threading.Thread(target=SquareAndCube, args=[int(input("Number: "))])
    # sqrs = threading.Thread(target=PrintSquares, args=[1,20])

    # t1.start()
    # t1.join()

    # squareAndCube.start()
    # squareAndCube.join()

    # sqrs.start()
    # sqrs.join()

    cta = CustomThreadClassAttempt("CTA", 1, 999)
    img_cta = ImageDownloadCTA("Download")

    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     rangee = [5,2,3,8]
    #     results = [executor.submit(PrintSquares, 1, ran) for ran in rangee]
    #
    #     for f in concurrent.futures.as_completed(results):
    #         print(f.result())

    # Link drive: https://drive.google.com/file/d/1ZeWzgWmKM8qTba0bBNJlFJKEhhW4spBg/view?usp=sharing

    cta.start()
    cta.join()

    img_cta.start()
    img_cta.join()

    finish = time.perf_counter()
    TT = round(finish - start, 2)

    print(f"Done in..... {TT} {checkSec(TT)}")
