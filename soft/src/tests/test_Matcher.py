from Dish import Dish
from data.Cpfc import Cpfc, Pfc
from data.Matcher import Matcher
from data.ingredients import ingredients, _

_target = Cpfc(10, Pfc(0.2, 0.3, 0.5, is_perc=True))
_dish = Dish([_(title="apple", serv=50, cals=10, prot=2, fats=3, carb=5)] * 2)
_matcher = Matcher(ingredients, _target)


def test__score_kpfc():
    assert _matcher._score_kpfc(_dish) == 0


def test__score_kpfc_non_perc():
    assert Matcher(ingredients, Cpfc(10, Pfc(20, 30, 50)))._score_kpfc(_dish) == 0


def test__random_dish():
    _matcher._random_dish()


def test_find():
    _matcher.find()
