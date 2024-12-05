import pytest
from day2 import day2p1, day2p2
from day5 import day5p1, day5p2
from day9 import day9p1, day9p2


def test_run():
    assert day2p1() == 8017076
    assert day2p2() == 3146

    assert day5p1()[-1] == 13210611
    assert day5p2()[-1] == 584126

    assert day9p1()[0] == 3280416268
    assert day9p2()[0] == 80210
