from day03.part1 import day03_1
from day03.part2 import day03_2

import os


def test_part1():
    expected = 157

    assert day03_1(os.path.join(os.path.dirname(__file__), 'test.in')) == expected


def test_part2():
    expected = 70

    assert day03_2(os.path.join(os.path.dirname(__file__), 'test.in')) == expected
