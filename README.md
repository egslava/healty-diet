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

1. Price minimization.
1. Diversity balance.
1. Weekly plans: some products should be eaten several times a week only.
1. Improve readability of the output.
1. Add 'dishes' that consist of ingredients.

### Input example

```_target = Cpfc(cals=1800, pfc=Pfc(prot=0.35, fats=0.16, carb=0.49, is_perc=True))```

```
# name                      serving     kCal    prot    fats    carb    price, ₽
_("carrot",                 110,        41,     0.93,   0.24,   9.58),
_("broccoli (1 middle flower)", 20,     28,     3,      0.4,    5.2),
# _("White early cabbage",    None,       27,     1.8,    0.1,    4.7),
# _("Bean seed sprouts Mash Dou-ya", None, 30,    3.1,    0.2,    6),
_("Chicory Elza",           7,          305,    3.8,    0.1,    56),
_("Kefir cup 1%",           206,        37,     3,      1,      4),
_("traditional oat flakes ( table spoon)",
                            6,          352,    12.3,   6.2,    61.8),  # 6g = 1 soup/table spoon
# _("Avocado",                170,        212,    2,      20,     6),
# _("0.5 Avocado",            170/2,      212,    2,      20,     6),
_("0.25 Avocado",           170/4,      212,    2,      20,     6),
_("Cashew tablespoon",      15,         571,    19,     44,     27),
_("Peanut tablespoon",      10,         610,    29,     50,     11),
_("Olive oil tablespoon",   13.5,       898,    0,      99.8,   0),
_("Casein (32g)",           32,         375,    75,     3,      12.5),
```

### Example output

```
          Aim Real % Aim % Real
Calories 1800 1800             
 Protein  128  136   35%    36%
    Fats   58   61   16%    16%
    Carb  179  179   49%    48%
                                    title   serv    kCal    prot   fats    carb
0                            0.25 Avocado   42.5   90.10   0.850  8.500   2.550
1                            Casein (32g)   32.0  120.00  24.000  0.960   4.000
2                            Casein (32g)   32.0  120.00  24.000  0.960   4.000
3                            Casein (32g)   32.0  120.00  24.000  0.960   4.000
4                            Casein (32g)   32.0  120.00  24.000  0.960   4.000
5                       Cashew tablespoon   15.0   85.65   2.850  6.600   4.050
6                       Cashew tablespoon   15.0   85.65   2.850  6.600   4.050
7                       Cashew tablespoon   15.0   85.65   2.850  6.600   4.050
8                            Chicory Elza    7.0   21.35   0.266  0.007   3.920
9                            Chicory Elza    7.0   21.35   0.266  0.007   3.920
10                           Chicory Elza    7.0   21.35   0.266  0.007   3.920
11                           Chicory Elza    7.0   21.35   0.266  0.007   3.920
12                           Chicory Elza    7.0   21.35   0.266  0.007   3.920
13                           Chicory Elza    7.0   21.35   0.266  0.007   3.920
14                           Chicory Elza    7.0   21.35   0.266  0.007   3.920
15                           Chicory Elza    7.0   21.35   0.266  0.007   3.920
16                      Peanut tablespoon   10.0   61.00   2.900  5.000   1.100
17                      Peanut tablespoon   10.0   61.00   2.900  5.000   1.100
18                      Peanut tablespoon   10.0   61.00   2.900  5.000   1.100
19                      Peanut tablespoon   10.0   61.00   2.900  5.000   1.100
20                      Peanut tablespoon   10.0   61.00   2.900  5.000   1.100
21             broccoli (1 middle flower)   20.0    5.60   0.600  0.080   1.040
22             broccoli (1 middle flower)   20.0    5.60   0.600  0.080   1.040
23             broccoli (1 middle flower)   20.0    5.60   0.600  0.080   1.040
24             broccoli (1 middle flower)   20.0    5.60   0.600  0.080   1.040
25             broccoli (1 middle flower)   20.0    5.60   0.600  0.080   1.040
26                                 carrot  110.0   45.10   1.023  0.264  10.538
27                                 carrot  110.0   45.10   1.023  0.264  10.538
28                                 carrot  110.0   45.10   1.023  0.264  10.538
29                                 carrot  110.0   45.10   1.023  0.264  10.538
30                                 carrot  110.0   45.10   1.023  0.264  10.538
31                                 carrot  110.0   45.10   1.023  0.264  10.538
32                                 carrot  110.0   45.10   1.023  0.264  10.538
33                                 carrot  110.0   45.10   1.023  0.264  10.538
34                                 carrot  110.0   45.10   1.023  0.264  10.538
35  traditional oat flakes ( table spoon)    6.0   21.12   0.738  0.372   3.708
36  traditional oat flakes ( table spoon)    6.0   21.12   0.738  0.372   3.708
37  traditional oat flakes ( table spoon)    6.0   21.12   0.738  0.372   3.708
title    0.25 AvocadoCasein (32g)Casein (32g)Casein (32...
serv                                                1429.5
kCal                                               1800.11
prot                                               136.449
fats                                                61.088
carb                                               178.726
dtype: object
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
