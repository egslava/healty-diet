from data.Cpfc import Cpfc, Pfc
from data.Ingredient import Ingredient


def test_serv():
    assert Ingredient("a", _serv=None, _cpfc=Cpfc(100, Pfc(0, 0, 0, is_perc=False)), _price=100).serv() == 100
    assert Ingredient("a", _serv=100, _cpfc=Cpfc(100, Pfc(0, 0, 0, is_perc=False)), _price=100).serv() == 100
    assert Ingredient("a", _serv=50, _cpfc=Cpfc(100, Pfc(0, 0, 0, is_perc=False)), _price=100).serv() == 50
