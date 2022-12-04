import os

INPUT = os.path.join(os.path.dirname(__file__), 'data.in')


def day04_1(filename=INPUT) -> int:
    cnt = 0
    for group in open(filename).read().splitlines():
        limits = list(map(lambda elf: elf.split('-'), group.split(',')))

        range1 = range(int(limits[0][0]), int(limits[0][1]) + 1)
        range2 = range(int(limits[1][0]), int(limits[1][1]) + 1)

        if all(e in range1 for e in range2) or all(e in range2 for e in range1):
            cnt += 1

    return cnt


if __name__ == '__main__':
    print(day04_1())
