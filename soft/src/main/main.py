from Dish import Dish
# kCal, fats, prot, carb = 1800, 0.83, 0.1, 0.07
from Reporter import print_report_cpfc, report_meal
from data.Cpfc import Cpfc, Pfc
# https://nestarenie.ru/ol-diet.html/comment-page-3#comment-459426
from data.Matcher import Matcher
from data.ingredients import ingredients
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

_target = Cpfc(cals=1800, pfc=Pfc(prot=0.35, fats=0.16, carb=0.49, is_perc=True))
_matcher = Matcher(ingredients, _target)
_meal: Dish = _matcher.find()

_meal.ingredients.sort(key=lambda i: i.title)
print_report_cpfc(_target, _meal.cpfc())
rep = report_meal(_meal)
print(rep)
print(rep[set(rep.columns) - {'title'}].sum())
