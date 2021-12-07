from typing import List, Tuple

from hash_maps import ChainedMap, DHashedMap, Pair


def assertion(cm: ChainedMap, dm: DHashedMap, pm: dict, printing=False):
    assert cm.itemsSize() == dm.itemsSize() == len(pm)
    assert sorted(cm.keyset()) == sorted(dm.keyset()) == sorted(pm.keys())
    for i in list(pm.keys()):
        assert cm.get(i) == dm.get(i) == pm[i]
        if printing:
            print(f"key: {i}, values: {cm.get(i)} | {dm.get(i)} | {pm[i]}")


def compare_insertion(cm: ChainedMap, dm: DHashedMap, pm: dict, data: List[Pair], printing: bool = True):
    for i in data:
        cm.insert(i)
        dm.insert(i)
        pm[i.key] = i.value

    if printing:
        print('Input list: [', *data, ']', sep='\n')
        print('_' * 50)
        print('Chained Map:', cm, f'fill coefficient = {cm.fillCoef()}')
        print('_' * 50)
        print('Double Hashed Map:', dm, f'fill coefficient = {dm.fillCoef()}')
        print('_' * 50)
        print("Python standard dict: {", *pm.items(), '}', sep='\n')
        print('_' * 50)
        print('Comparison:')

    assertion(cm, dm, pm, printing)
    print('insertion finished successfully')
    print('#' * 50)


def compare_deleting(cm: ChainedMap, dm: DHashedMap, pm: dict, keys: list, printing: bool = True):
    for i in keys:
        cm.remove(i)
        dm.remove(i)
        del pm[i]

    if printing:
        print('Input keys for deleting:[', *keys, ']', sep='\n')
        print('_' * 50)
        print('Chained Map:', cm, f"fill coefficient = {cm.fillCoef()}")
        print('_' * 50)
        print("Double Hashed Map:", dm, f'fill coefficient = {dm.fillCoef()}')
        print('_' * 50)
        print('Python standard Dict: {', *pm.items(), '}', sep='\n')
        print('_' * 50)
        print('Comparison:')

    assertion(cm, dm, pm, printing)
    print('deleting finished successfully')
    print('#' * 50)
