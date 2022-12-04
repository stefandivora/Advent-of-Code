from day04.part1 import day04_1
from day04.part2 import day04_2

import os


def test_part1():
    expected = 2

    assert day04_1(os.path.join(os.path.dirname(__file__), 'test.in')) == expected


def test_part2():
    expected = 4

    assert day04_2(os.path.join(os.path.dirname(__file__), 'test.in')) == expected
