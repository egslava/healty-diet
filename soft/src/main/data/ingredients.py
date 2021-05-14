import dataclasses
from typing import List

from data.Cpfc import Cpfc, Pfc
from data.Ingredient import Ingredient


def _(title, serv, cals, prot, fats, carb):
    return Ingredient(title, serv, Cpfc(cals, Pfc(prot, fats, carb)))


# @formatter:off
ingredients: List[Ingredient] = [dataclasses.replace(i, serv=i.serv or 100) for i in [
    # name                      serving     kCal    prot    fats    carb    price, ₽
    _("carrot",                 110,        41,     0.93,   0.24,   9.58),
    _("broccoli (1 middle flower)", 20,     28,     3,      0.4,    5.2),
    # _("White early cabbage",    None,       27,     1.8,    0.1,    4.7),
    # _("Bean seed sprouts Mash Dou-ya", None, 30,    3.1,    0.2,    6),
    _("Chicory Elza",           7,          305,    3.8,    0.1,    56),
    _("Kefir cup 1%",           206,        37,     3,      1,      4),
    _("traditional oat flakes "
      "( table spoon)",         6,          352,    12.3,   6.2,    61.8),  # 6g = 1 soup/table spoon
    # _("Avocado",                170,        212,    2,      20,     6),
    # _("0.5 Avocado",            170/2,      212,    2,      20,     6),
    _("0.25 Avocado",           170/4,      212,    2,      20,     6),
    _("Cashew tablespoon",      15,         571,    19,     44,     27),
    _("Peanut tablespoon",      10,         610,    29,     50,     11),
    _("Olive oil tablespoon",   13.5,       898,    0,      99.8,   0),
    _("Casein (32g)",           32,         375,    75,     3,      12.5),
]]
# @formatter:on
