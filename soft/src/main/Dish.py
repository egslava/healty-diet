from __future__ import annotations

import dataclasses
from dataclasses import dataclass
from typing import List

from data.Cpfc import Cpfc, Pfc
from data.Ingredient import Ingredient


@dataclass
class Dish:
    ingredients: List[Ingredient]

    def cpfc(self) -> Cpfc:
        return sum((_.cpfc() for _ in self.ingredients), start=Cpfc(0, Pfc(0, 0, 0))) or Cpfc(0, Pfc(0, 0, 0))

    def __add__(self, new_ingredient: Ingredient) -> Dish:
        return dataclasses.replace(self, ingredients=self.ingredients + [new_ingredient])


@dataclass
class Day:
    meals: List[Dish]

    def cpfc(self) -> Cpfc:
        return sum(_.cpfc() for _ in self.meals)
