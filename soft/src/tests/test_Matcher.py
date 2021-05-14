from Dish import Dish
from data.Cpfc import Cpfc, Pfc
from data.Matcher import Matcher
from data.ingredients import ingredients, _

_target = Cpfc(10, Pfc(0.2, 0.3, 0.5, is_perc=True))
_dish = Dish([_(title="apple", serv=50, cals=10, prot=2, fats=3, carb=5)] * 2)
_matcher = Matcher(ingredients, _target)


def test__score():
    assert _matcher._score(_dish) == 0


def test__random_dish():
    _matcher._random_dish()


def test_find():
    _matcher.find()
