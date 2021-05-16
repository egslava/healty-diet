from Dish import Dish
from data.Cpfc import Cpfc, Pfc
from data.ingredients import _


def test_cpfc_zero():
    dish = Dish(ingredients=[])
    assert dish.cpfc() == Cpfc(cals=0, pfc=Pfc(prot=0, fats=0, carb=0))


def test_cpfc_one():
    dish = Dish([_("carrot", serv=50, cals=2, prot=4, fats=8, carb=16, price=1)])
    expected = Cpfc(cals=1, pfc=Pfc(prot=2, fats=4, carb=8))
    assert dish.cpfc() == expected


def test_price():
    dish = Dish([_("carrot", serv=50, cals=2, prot=4, fats=8, carb=16, price=1000)] * 3)
    assert dish.price() == 1000 / 2 * 3
