from dataclasses import dataclass
from typing import Optional

from data.Cpfc import Cpfc


@dataclass(frozen=True)
class Ingredient:
    title: str
    _serv: Optional[float]  # in grams, one carrot = 120g

    # per 100g. I.e. 1 carrot = 120g, cals = 100. Means cals/carrot = 120cals
    _cpfc: Cpfc
    _price: float

    def serv(self) -> float:
        return self._serv or 100

    def cpfc(self) -> Cpfc:
        return self._cpfc * (self.serv() / 100)

    def price(self) -> float:
        return self._price * (self.serv() / 100)
