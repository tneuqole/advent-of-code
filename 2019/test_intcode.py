import pytest
from day2 import day2p1, day2p2
from day5 import day5p1, day5p2
from day9 import day9p1, day9p2


def test_run(capsys):
    assert day2p1() == 8017076
    assert day2p2() == 3146

    day5p1()
    assert "13210611" in capsys.readouterr().out

    day5p2()
    assert "584126" in capsys.readouterr().out

    day9p1()
    assert "3280416268" in capsys.readouterr().out

    day9p2()
    assert "80210" in capsys.readouterr().out
