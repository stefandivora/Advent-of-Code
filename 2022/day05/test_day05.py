from day05.part1 import day05_1
from day05.part2 import day05_2

import os


def test_part1():
    expected = 'CMZ'

    assert day05_1(os.path.join(os.path.dirname(__file__), 'test.in')) == expected


def test_part2():
    expected = 'MCD'

    assert day05_2(os.path.join(os.path.dirname(__file__), 'test.in')) == expected
