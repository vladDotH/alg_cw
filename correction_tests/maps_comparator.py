from typing import List

from hash_maps import ChainedMap, DHashedMap, Pair


def compare(data: List[Pair], size: int, printing: bool = True):
    cm = ChainedMap(size)
    dm = DHashedMap(size)
    pm = dict()

    for i in data:
        cm.insert(i)
        dm.insert(i)
        pm[i.key] = i.value

    if printing:
        print("Input list:", data)
        print('-' * 50)
        print("Chained Map:", cm, "fill coefficient = {}".format(cm.fillCoef()))
        print('-' * 50)
        print("Double Hashed Map:", dm, "fill coefficient = {}".format(dm.fillCoef()))
        print('-' * 50)
        print("Python standard Map:", pm)

        print('-' * 50)
        print('Comparison:')
    for i in data:
        assert cm.get(i.key) == dm.get(i.key) == pm[i.key]
        if printing:
            print("key: {}, values: {} | {} | {}".format(i, cm.get(i.key), dm.get(i.key), pm[i.key]))
    print("test finished successfully")
