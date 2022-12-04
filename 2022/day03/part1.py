import os

INPUT = os.path.join(os.path.dirname(__file__), 'data.in')


def day03_1(filename=INPUT) -> int:
    sum = 0
    for backpack in open(filename).read().splitlines():
        duplicate = set(backpack[:len(backpack) // 2]) & set(backpack[len(backpack) // 2:])

        prio = ord(next(iter(duplicate)))
        sum += prio - 96 if prio >= 97 else prio - 38

    return sum


if __name__ == '__main__':
    print(day03_1())
