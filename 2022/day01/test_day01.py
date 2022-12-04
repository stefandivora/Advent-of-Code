from day01.part1 import day01_1
from day01.part2 import day01_2

import os


def test_part1():
    expected = 24000

    assert day01_1(os.path.join(os.path.dirname(__file__), 'test.in')) == expected


def test_part2():
    expected = 45000

    assert day01_2(os.path.join(os.path.dirname(__file__), 'test.in')) == expected
