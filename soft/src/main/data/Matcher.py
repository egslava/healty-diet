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

    def _score(self, dish: Dish) -> float:
        cpfc = dish.cpfc()
        dish_pfc = cpfc.pfc.perc()
        target_pfc = self.target.pfc  # .perc()

        return abs(self.target.cals - cpfc.cals) + abs(target_pfc - dish_pfc).sum() * 10000

    def _random_dish(self) -> Dish:
        day = Dish(ingredients=[])
        while day.cpfc().cals < self.target.cals:
            day.ingredients.append(choice(self.ingredients))
        return day

    def find(self, iters: int = 1000) -> Dish:
        return min((self._random_dish() for _ in range(iters)), key=self._score)
