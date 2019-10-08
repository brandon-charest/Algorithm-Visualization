import random
import time

numbers = 100
A = [i + 1 for i in range(numbers)]
random.seed(time.time())
random.shuffle(A)


def get_data():
    return A
