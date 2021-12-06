from hash_maps import Pair, DHashedMap, ChainedMap
from testing.maps_comparator import compare_insertion, compare_deleting
from testing.str_hash import str_hash
import string
import random


def strTest1(printing=True):
    N = 6
    data = [
        Pair('hello', 0),
        Pair('world', None),
        Pair('string', 9),
        Pair('hash', 'str'),
        Pair('code', 16),
        Pair('oaoa', [1, 2, 3])
    ]
    cm = ChainedMap(N, lambda hm, s: str_hash(s))
    dm = DHashedMap(N, lambda hm, s: str_hash(s))
    pm = dict()
    compare_insertion(cm, dm, pm, data, printing)
    compare_deleting(cm, dm, pm, ['world', 'hash', 'hello'], printing)


def strTest2(printing=True):
    WORD_LEN = 10
    START = 10
    N = 100
    data = [
        Pair(''.join(random.choices(string.ascii_letters, k=WORD_LEN)), i) for i in range(N)
    ]
    cm = ChainedMap(START, lambda hm, s: str_hash(s))
    dm = DHashedMap(START, lambda hm, s: str_hash(s))
    pm = dict()
    compare_insertion(cm, dm, pm, data, printing)
    DELETE = 30
    compare_deleting(cm, dm, pm, list(set(random.choices(list(pm.keys()), k=DELETE))), printing)


if __name__ == "__main__":
    print('Strings as keys test 1:')
    strTest1()

    print('Strings as keys (random test):')
    strTest2()
