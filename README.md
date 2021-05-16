# Diet combinator

<b>Collaboration is welcome — feel free to reach me out!</b>

Sport/longevity diet combinator. Takes into account calories, fats, proteins and carbs proportion.

## Project vision

### Aims

1. Should automatically form list of groceries.
1. Shopping should be done weekly.
1. Maximum easy, no complicated recipes

### Roadmap

#### No go

1. For developers: no time for front-end/nice UX right now.

#### In the near future:

1. ✅ Price minimization.
2. ✅ Diversity balance.
3. Super simple recipes. For instance: kefir + oat flakes. Cause it's almost impossible to eat oat flakes without kefir
4. min/max daily and weekly values (i.e. avoid much nuts a day, but consume some minimal amount of olive oil)
5. Weekly plans: some products should be eaten several times a week only.
6. Improve readability of the output.
8. Sbermarket API? (https://avdeevdenis.github.io/tools-parser-api/)

### Input example

```_target = Cpfc(cals=1800, pfc=Pfc(prot=0.35, fats=0.16, carb=0.49, is_perc=True))```

```
ingredients: List[Ingredient] = [
    # name                      serving     kCal    prot    fats    carb    price, ₽
    _("carrot",                 110,        41,     0.93,   0.24,   9.58,   5.8),
    _("broccoli (1 middle flower)", 20,     28,     3,      0.4,    5.2,    25.16),
  # _("White early cabbage",    None,       27,     1.8,    0.1,    4.7),
  # _("Bean seed sprouts Mash Dou-ya", None, 30,    3.1,    0.2,    6),
    _("Chicory Elza",           7,          305,    3.8,    0.1,    56,     100),
    _("Kefir cup 1%",           206,        37,     3,      1,      4,      5),
    _("traditional oat flakes "
      "( table spoon)",         6,          352,    12.3,   6.2,    61.8,   5),  # 6g = 1 soup/table spoon
  # _("Avocado",                170,        212,    2,      20,     6),
  # _("0.5 Avocado",            170/2,      212,    2,      20,     6),
    _("0.25 Avocado",           170/4,      212,    2,      20,     6,      25),
    _("Cashew tablespoon",      15,         571,    19,     44,     27,     30),
    _("Peanut tablespoon",      10,         610,    29,     50,     11,     30),
    _("Olive oil tablespoon",   13.5,       898,    0,      99.8,   0,      140),
    _("Casein (32g)",           32,         375,    75,     3,      12.5,   166),
]
```

### Example output

```
          Aim Real % Aim % Real
Calories 1800 1809             
 Protein  128  160   35%    42%
    Fats   58   57   16%    15%
    Carb  179  168   49%    44%
                                   title    serv    kCal    prot    fats    carb    price  servs
0                           0.25 Avocado    42.5   90.10   0.850   8.500   2.550   10.625      1
1                           Casein (32g)   128.0  480.00  96.000   3.840  16.000  212.480      4
2                      Cashew tablespoon    30.0  171.30   5.700  13.200   8.100    9.000      2
3                           Chicory Elza    21.0   64.05   0.798   0.021  11.760   21.000      3
4                           Kefir cup 1%  1236.0  457.32  37.080  12.360  49.440   61.800      6
5                      Peanut tablespoon    30.0  183.00   8.700  15.000   3.300    9.000      3
6             broccoli (1 middle flower)    40.0   11.20   1.200   0.160   2.080   10.064      2
7                                 carrot   550.0  225.50   5.115   1.320  52.690   31.900      5
8  traditional oat flakes ( table spoon)    36.0  126.72   4.428   2.232  22.248    1.800      6
serv     2113.500
kCal     1809.190
prot      159.871
carb      168.168
fats       56.633
price     367.669
servs      32.000
dtype: float64

Process finished with exit code 0

```

# Theory

### Slang

- fpc = Fats, Protein, Carbs
- cfpc = calories, fats, protein, carbs
- gi = glycemic index

### links

1. The Largest Glycemic index search ([link](https://glycemicindex.com/gi-search/)).

### Info

Fats slow down digesting of carbs, so when you are eating them decreases glycemic index. It works also in case of frying
with lots of oil. That's why smashed potato has a higher GI than potato chips [1], and fat-free milk has a higher GI
than jut a normal milk [2]

1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3205609/
2. https://style.rbc.ru/health/602cbb679a79477540129e9f
