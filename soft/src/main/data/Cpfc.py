from __future__ import annotations

import dataclasses
from dataclasses import dataclass

from data.PfcAlreadyPercentException import PfcAlreadyPercentException
from data.PfcNotPercentException import PfcNotPercentException

PC_CAL, F_CAL = 4.1, 9.29


@dataclass(frozen=True)
class Pfc:
    prot: float
    fats: float
    carb: float
    is_perc: bool = False

    def __mul__(self, o: float) -> Pfc:
        return dataclasses.replace(self, prot=self.prot * o, fats=self.fats * o, carb=self.carb * o)

    def __add__(self, o: Pfc) -> Pfc:
        if self.is_perc != o.is_perc:
            raise PfcNotPercentException()
        return dataclasses.replace(self, prot=self.prot + o.prot, fats=self.fats + o.fats, carb=self.carb + o.carb)

    def __neg__(self) -> Pfc:
        return dataclasses.replace(self, prot=-self.prot, fats=-self.fats, carb=-self.carb)

    def __sub__(self, other: Pfc):
        if self.is_perc != other.is_perc:
            raise PfcNotPercentException()
        return self + (-other)

    def __abs__(self):
        return dataclasses.replace(self, prot=abs(self.prot), fats=abs(self.fats), carb=abs(self.carb))

    def sum(self) -> float:
        return self.prot + self.fats + self.carb

    def perc(self) -> Pfc:
        if self.is_perc:
            raise PfcAlreadyPercentException()
        _sum = self.sum()
        return Pfc(
            prot=self.prot / _sum,
            fats=self.fats / _sum,
            carb=self.carb / _sum,
            is_perc=True
        )


@dataclass(frozen=True)
class Cpfc:
    cals: float
    pfc: Pfc

    def unperc(self) -> Cpfc:
        if not self.pfc.is_perc:
            raise PfcNotPercentException()

        f = (self.pfc.fats * self.cals) / (PC_CAL + (F_CAL - PC_CAL) * self.pfc.fats)
        ppfpc = (self.cals - (F_CAL - PC_CAL) * f) / PC_CAL  # ppfpc means 'p + f + c'
        p = ppfpc * self.pfc.prot
        c = ppfpc * self.pfc.carb

        return dataclasses.replace(self, pfc=dataclasses.replace(self.pfc, prot=p, fats=f, carb=c, is_perc=False))

    def __add__(self, other: Cpfc) -> Cpfc: return Cpfc(self.cals + other.cals, self.pfc + other.pfc)

    def __neg__(self) -> Cpfc: return Cpfc(-self.cals, -self.pfc)

    def __sub__(self, other: Cpfc) -> Cpfc: return self + (-other)

    def __mul__(self, o: float) -> Cpfc: return dataclasses.replace(self, cals=self.cals * o, pfc=self.pfc * o)
