import os
from collections import Counter

INPUT = os.path.join(os.path.dirname(__file__), 'data.in')


def day06_1(filename=INPUT) -> int:
    inp = open(filename).read()

    counter = 4

    substr = inp[counter - 4 : counter]
    while not (len(Counter(substr)) == len(substr)):
        counter += 1
        substr = inp[counter - 4: counter]

    return counter


if __name__ == '__main__':
    print(day06_1())
