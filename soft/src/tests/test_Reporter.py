from Dish import Dish
from Reporter import report_cpfc, report_meal
from data.Cpfc import Cpfc, Pfc

_expected = Cpfc(1000, Pfc(200, 300, 500))
_actual = Cpfc(100, Pfc(20, 30, 50))


def test_report_cpfc():
    # @formatter:off
    assert report_cpfc(_expected, _actual) == [
        ["",         "Aim",  "Real",     "% Aim",    "% Real"],
        ["Calories", "1000", "100",       "",         ""],
        ["Protein",  "200",  "20",        "20%",     "20%"],
        ["Fats",     "300",  "30",        "30%",     "30%"],
        ["Carb",     "500",  "50",        "50%",     "50%"],
    ]
    # @formatter:on


def test_report():
    _target = Cpfc(1800, Pfc(0.35, 0.16, 0.49, is_perc=True))
    from data.ingredients import _
    _meal = Dish([_("carrot", serv=50, cals=2, prot=4, fats=8, carb=16, price=0)])
    report_meal(_meal)
