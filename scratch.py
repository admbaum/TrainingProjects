import random
import time

one = random.randrange(-100, 1000)
two = random.randrange(-100, 1000)
timeout_start = time.time()
timeout = 4


def add(param1, param2):
    while True:
        test = 0
        print(param1 + param2)
        if test == 4 or time.time() > timeout:
            break


add(one, two)
