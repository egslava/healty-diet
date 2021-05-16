#
# p * 4 + f * 8 + c * 4 == kCal
# 4(p + c) + 8*f == kCal
# 4(2f + p + c) == kCal
#
# 2f + p + c == kCal / 4
#
# Вот тут желательно бы найти правильные БЖУ-балансы, чтобы понять, точно ли я не наебался в расчётах
# f + fpc == kCal / 4
# fpc == kCal / 4 - f

# kCal = 1800
# 0.35 = p/fpc
# 0.16 = f/fpc
# 0.49 = c/fpc
from dataclasses import dataclass
from random import choice
from typing import Sequence

from Dish import Dish
from data.Cpfc import Cpfc
from data.Ingredient import Ingredient


@dataclass
class Matcher:
    ingredients: Sequence[Ingredient]
    target: Cpfc

    def _score_price(self, dish: Dish):
        return dish.price()

    def _score_ingredients(self, dish: Dish):
        return len(set(dish.ingredients))

    def _score_kpfc(self, dish: Dish) -> float:
        cpfc = dish.cpfc()
        dish_pfc = cpfc.pfc.perc()

        if self.target.pfc.is_perc:
            target_pfc = self.target.pfc
        else:
            target_pfc = self.target.pfc.perc()

        return abs(self.target.cals - cpfc.cals) + abs(target_pfc - dish_pfc).sum() * 1000

    def _score(self, dish: Dish):
        return self._score_kpfc(dish) + self._score_ingredients(dish) + self._score_price(dish) / 2

    def _random_dish(self) -> Dish:
        day = Dish(ingredients=[])
        while day.cpfc().cals < self.target.cals:
            day.ingredients.append(choice(self.ingredients))
        return day

    def find(self, iters: int = 100) -> Dish:
        return min((self._random_dish() for _ in range(iters)), key=self._score)
