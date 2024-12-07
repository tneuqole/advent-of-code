from day2 import day2p1, day2p2
from day5 import day5p1, day5p2
from day7 import day7p1, day7p2
from day9 import day9p1, day9p2
from day11 import day11p1, day11p2


def test_run():
    assert day2p1() == 8017076
    assert day2p2() == 3146

    assert day5p1()[-1] == 13210611
    assert day5p2() == 584126

    assert day7p1() == 277328
    assert day7p2() == 11304734

    assert day9p1() == 3280416268
    assert day9p2() == 80210

    assert day11p1() == 2418
    assert (
        day11p2()
        == """..##..###..####...##..##..#....###..###....
.#..#.#..#.#.......#.#..#.#....#..#.#..#...
.#....#..#.###.....#.#..#.#....#..#.#..#...
.#.##.###..#.......#.####.#....###..###....
.#..#.#.#..#....#..#.#..#.#....#....#.#....
..###.#..#.####..##..#..#.####.#....#..#..."""
    )
