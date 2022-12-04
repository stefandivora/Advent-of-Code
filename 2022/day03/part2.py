import os

INPUT = os.path.join(os.path.dirname(__file__), 'data.in')


def day03_2(filename=INPUT) -> int:
    sum = 0
    backpacks = list(zip(*[iter(open(filename).read().splitlines())] * 3))

    for group in backpacks:
        duplicate = set(group[0]) & set(group[1]) & set(group[2])
        prio = ord(next(iter(duplicate)))
        sum += prio - 96 if prio >= 97 else prio - 38

    return sum


if __name__ == '__main__':
    print(day03_2())
