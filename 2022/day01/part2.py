import os

INPUT = os.path.join(os.path.dirname(__file__), 'data.in')


def day01_2(filename=INPUT) -> int:
    elves = open(filename).read().strip().split('\n\n')

    calories = []

    for elf in elves:
        calories.append(sum([int(c) for c in elf.splitlines()]))

    calories.sort()
    return sum(calories[-3:])


if __name__ == '__main__':
    print(day01_2())
