from day02.part1 import day02_1
from day02.part2 import day02_2

import os


def test_part1():
    expected = 15

    assert day02_1(os.path.join(os.path.dirname(__file__), 'test.in')) == expected


def test_part2():
    expected = 12

    assert day02_2(os.path.join(os.path.dirname(__file__), 'test.in')) == expected
