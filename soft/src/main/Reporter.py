import pandas as pd
from pandas import DataFrame

from Dish import Dish
from data.Cpfc import Cpfc


def print_report_cpfc(aim: Cpfc, real: Cpfc):
    report = report_cpfc(aim, real)
    df = DataFrame(columns=report[0], data=report[1:])
    print(df.to_string(index=False))


def report_cpfc(aim: Cpfc, real: Cpfc):
    """ ["",        "Aim",  "Real",     "% Aim",    "% Real"],
        ["kCal",    "1000", "100",       "",         ""],
        ["Protein", "200",  "20",        "0.20",     "0.20"],
        ["Fats",    "300",  "30",        "0.30",     "0.30"],
        ["Carb",    "500",  "50",        "0.50",     "0.50"] """

    if aim.pfc.is_perc:
        aim = aim.unperc()
    if real.pfc.is_perc:
        real = real.unperc()

    return [
        ["", "Aim", "Real", "% Aim", "% Real"],
        ["Calories", "%.0f" % aim.cals, "%.0f" % real.cals, "", ""],
        ["Protein", "%.0f" % aim.pfc.prot, "%.0f" % real.pfc.prot, "%.0f%%" % (aim.pfc.perc().prot * 100),
         "%.0f%%" % (real.pfc.perc().prot * 100)],
        ["Fats", "%.0f" % aim.pfc.fats, "%.0f" % real.pfc.fats, "%.0f%%" % (aim.pfc.perc().fats * 100),
         "%.0f%%" % (real.pfc.perc().fats * 100)],
        ["Carb", "%.0f" % aim.pfc.carb, "%.0f" % real.pfc.carb, "%.0f%%" % (aim.pfc.perc().carb * 100),
         "%.0f%%" % (real.pfc.perc().carb * 100)],
    ]
    # @formatter:off


def report_meal(meal: Dish) -> DataFrame:
    _rows = []
    for _i in meal.ingredients:
        _cpfc = _i.cpfc()
        _pfc = _cpfc.pfc
        _rows.append([_i.title, _i.serv(), _cpfc.cals, _pfc.prot, _pfc.fats, _pfc.carb, _i.price()])

    df = pd.DataFrame(columns=["title", "a serv weight", "kCal", "prot", "fats", "carb", "price"], data=_rows)
    df['servs'] = 1
    df['weight'] = df['a serv weight']
    df = df['title, servs, a serv weight, weight, price, kCal, prot, fats, carb'.split(', ')]
    df = df.groupby(by=["title", "a serv weight"]).sum().reset_index()
    return df

# print(meal.cpfc().kCal, "/", target.kCal)
# print("Prot: ", meal.cpfc().pfc.prot, "/", target.pfc.prot, f'({meal.cpfc().pfc.perc().prot}/{target.pfc.prot})')
# print("Fats: ", meal.cpfc().pfc.fats, "/", target.pfc.fats, f'({meal.cpfc().pfc.perc().fats}/{target.pfc.fats})')
# print("Carb: ", meal.cpfc().pfc.carb, "/", target.pfc.carb, f'({meal.cpfc().pfc.perc().carb}/{target.pfc.carb})')
