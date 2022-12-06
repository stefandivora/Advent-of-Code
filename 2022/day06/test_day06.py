from day06.part1 import day06_1
from day06.part2 import day06_2

import os


def test_part1():
    assert day06_1(os.path.join(os.path.dirname(__file__), 'test1.in')) == 7
    assert day06_1(os.path.join(os.path.dirname(__file__), 'test2.in')) == 5
    assert day06_1(os.path.join(os.path.dirname(__file__), 'test3.in')) == 6
    assert day06_1(os.path.join(os.path.dirname(__file__), 'test4.in')) == 10
    assert day06_1(os.path.join(os.path.dirname(__file__), 'test5.in')) == 11


def test_part2():
    assert day06_2(os.path.join(os.path.dirname(__file__), 'test1.in')) == 19
    assert day06_2(os.path.join(os.path.dirname(__file__), 'test2.in')) == 23
    assert day06_2(os.path.join(os.path.dirname(__file__), 'test3.in')) == 23
    assert day06_2(os.path.join(os.path.dirname(__file__), 'test4.in')) == 29
    assert day06_2(os.path.join(os.path.dirname(__file__), 'test5.in')) == 26
