from typing import List

from hash_maps import ChainedMap, DHashedMap, Pair


def compare(data: List[Pair], size: int):
    cm = ChainedMap(size)
    dm = DHashedMap(size)
    pm = dict()

    for i in data:
        cm.insert(i)
        dm.insert(i)
        pm[i.key] = i.value

    print("Input list:", data)
    print('-' * 50)
    print("Chained Map:", cm)
    print('-' * 50)
    print("Double Hashed Map:", dm)
    print('-' * 50)
    print("Python standard Map:", pm)

    print('-' * 50)
    print('Comparison:')
    for i in data:
        assert cm.get(i.key) == dm.get(i.key) == pm[i.key]
        print(cm.get(i.key) == dm.get(i.key) == pm[i.key])
