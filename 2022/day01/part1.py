import os

INPUT = os.path.join(os.path.dirname(__file__), 'data.in')


def day01_1(filename=INPUT) -> int:
    elves = open(filename).read().strip().split('\n\n')

    calories = []

    for elf in elves:
        calories.append(sum([int(c) for c in elf.splitlines()]))

    return max(calories)


if __name__ == '__main__':
    print(day01_1())
