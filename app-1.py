import datetime
from typing import List, Union, TypeAlias

# =====> (1)
# W Python możesz stosować UNION TYPES, które pozwolą sugerować, jaki typ lub typy
# może posiadać rozpatrywany obiekt

# Sposób przed Python 3.10
# def sum_items(items: List[Union[float, int]]) -> float:
#     return sum(items)

# Od Python 3.10 możesz stosować unie z wykorzystaniem operatora |
# Zapis jest bardziej czytelny
# Nie musisz nic importować
# Możesz też łatwo zasugerować, że dany element może być None


def sum_items(items: list[float | int], message: str | None) -> float:
    return sum(items)

# sum_items(["a", "b"], 'Message')
sum_items([10, 12], 'Message')
sum_items([10.1, 12], 'Message')
sum_items([10.1, 12.2], 'Message')

# Możesz zastosować unie do pracy z funkcjami isinstance oraz issubclass
print(isinstance('Message', str | int))
print(issubclass(int, float | int | bytes))
print(issubclass(datetime.datetime, float | int | bytes))

# =====> (2)
# Możesz definiować TYPE ALIASES, które pozwolą wprowadzić do Twojej aplikacji
# przejrzyste nazwy dla zdefiniowanych typów.

# Poniższe przykłady typów są ok, ale type checker może miec problemy
# z interpretacją, czy Point lub Triangle są aliasami czy po prostu
# nazwami pewnych zdefiniowanych wcześniej zmiennych globalnych
Point = tuple[float, float]
Triangle = tuple[Point, Point, Point]

# Dlatego możemy zastosować specjalny typ TypeAlias, który jednoznacznie
# pozwoli interpretować taki zapis jako TYPE ALIAS
Point: TypeAlias = tuple[float, float]
Triangle: TypeAlias = tuple[Point, Point, Point]

def f(t: Triangle):
    print(t)

f(((1.1, 2.2), (3.3, 4.4), (5.5, 6.6)))
# fun((('1.1', 2.2), (3.3, 4.4), (5.5, 6.6)))
# fun(((1.1, 2.2), (3.3, 4.4)))