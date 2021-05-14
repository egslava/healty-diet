from data.Cpfc import Pfc, Cpfc


def test___mul__():
    assert Pfc(1, 2, 3) * 2 == Pfc(2, 4, 6)


def test___add__():
    assert Pfc(1, 2, 3) + Pfc(2, 3, 4) == Pfc(3, 5, 7)


def test___neg__():
    assert -Pfc(1, 2, 3) == Pfc(-1, -2, -3)
    assert -Pfc(-1, -2, -3) == Pfc(1, 2, 3)
    assert Pfc(0, 0, 0) == -Pfc(0, 0, 0)


def test___sub__():
    assert Pfc(1, 2, 3) - Pfc(2, 3, 4) == Pfc(-1, -1, -1)


def test___abs__():
    assert abs(Pfc(-1, -2, -3)) == Pfc(1, 2, 3)
    assert abs(Pfc(-1, 0, 1)) == Pfc(1, 0, 1)


def test_sum():
    assert Pfc(0.93, 0.24, 9.58).sum() == 10.75


def test_perc():
    assert Pfc(100, 200, 300, is_perc=False).perc() == Pfc(1 / 6, 2 / 6, 3 / 6, is_perc=True)


def test_scale():
    assert Pfc(1, 1, 1) * 2 == Pfc(2, 2, 2)


def test_unperc():
    p, f, c = 3, 4, 5
    cals = 4.1 * p + 9.29 * f + 4.1 * c
    pfc_perc = Cpfc(cals, Pfc(p, f, c)).pfc.perc()
    assert Cpfc(cals, pfc_perc).unperc() == Cpfc(cals, Pfc(p, f, c))
