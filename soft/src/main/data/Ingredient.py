from dataclasses import dataclass
from typing import Optional

from data.Cpfc import Cpfc


@dataclass(frozen=True)
class Ingredient:
    title: str
    serv: Optional[float]  # in grams, one carrot = 120g

    # per 100g. I.e. 1 carrot = 120g, cals = 100. Means cals/carrot = 120cals
    _cpfc: Cpfc

    def cpfc(self): return self._cpfc * 0.01 * (self.serv or 100)
