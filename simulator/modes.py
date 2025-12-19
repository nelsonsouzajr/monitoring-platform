import random
import time


def normal():
    time.sleep(random.uniform(0.05, 0.15))
    return 200


def slow():
    time.sleep(random.uniform(1.0, 2.5))
    return 200


def error():
    time.sleep(random.uniform(0.1, 0.3))
    return 500


def intermittent():
    if random.random() < 0.3:
        return error()
    if random.random() < 0.3:
        return slow()
    return normal()
