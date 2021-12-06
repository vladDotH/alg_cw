from hash_maps import Pair, DHashedMap, ChainedMap
from testing.maps_comparator import compare_insertion, compare_deleting
import random


def rand1(printing=True):
    START = 10
    N = 50
    data = [Pair(random.randint(0, 1_000), i) for i in range(N)]
    cm = ChainedMap(START)
    dm = DHashedMap(START)
    pm = dict()
    compare_insertion(cm, dm, pm, data, printing)
    DELETE = 25
    compare_deleting(cm, dm, pm, list(set(random.choices(list(pm.keys()), k=DELETE))), printing)


def rand2(printing=False):
    START = 100
    N = 100_000
    data = [Pair(random.randint(0, 1_000_000), i) for i in range(N)]
    cm = ChainedMap(START)
    dm = DHashedMap(START)
    pm = dict()
    compare_insertion(cm, dm, pm, data, printing)
    DELETE = 50_000
    compare_deleting(cm, dm, pm, list(set(random.choices(list(pm.keys()), k=DELETE))), printing)


if __name__ == "__main__":
    print('Random test 1:')
    rand1()

    print('Random test 2:')
    rand2()
