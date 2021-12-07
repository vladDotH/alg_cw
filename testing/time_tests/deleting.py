from hash_maps import Pair, DHashedMap, ChainedMap
import time
import random

MAX_KEY = 2 ** 32
PROBES = 100
TESTS = [10, 100, 1_000, 10_000]


def deleteCM(cm: ChainedMap):
    keys = cm.keyset()
    t = time.time_ns()
    for k in keys:
        cm.remove(k)
    return time.time_ns() - t


def deleteDM(dm: DHashedMap):
    keys = dm.keyset()
    t = time.time_ns()
    for k in keys:
        dm.remove(k)
    return time.time_ns() - t


def deletePD(pm: dict):
    keys = list(pm.keys())
    t = time.time_ns()
    for k in keys:
        del pm[k]
    return time.time_ns() - t


if __name__ == "__main__":
    for n in TESTS:
        cT, dT, pT = [], [], []
        for i in range(PROBES):
            cm = ChainedMap(n)
            dm = DHashedMap(int(n / DHashedMap.MAX_FILL_COEFF) + 1)
            pm = dict()
            data = [Pair(random.randint(0, MAX_KEY), i) for i in range(n)]
            for j in data:
                cm.insert(j)
                dm.insert(j)
                pm[j.key] = j.value
            cT.append(deleteCM(cm))
            dT.append(deleteDM(dm))
            pT.append(deletePD(pm))

        print(f'Deleted all {n} items in Chained Map '
              f'with average time {(sum(cT) / PROBES) // 1e3} mcs for {PROBES} tests, all time = {sum(cT) / 1e9} s')
        print(f'Deleted all {n} items in Double Hashed Map '
              f'with average time {(sum(dT) / PROBES) // 1e3} mcs for {PROBES} tests, all time = {sum(dT) / 1e9} s')
        print(f'Deleted all {n} items in python dict '
              f'with average time {(sum(pT) / PROBES) // 1e3} mcs for {PROBES} tests, all time = {sum(pT) / 1e9} s')
        print('#' * 50)

''' TEST OUTPUT
Deleted all 10 items in Chained Map with average time 10.0 mcs for 100 tests, all time = 0.001025149 s
Deleted all 10 items in Double Hashed Map with average time 22.0 mcs for 100 tests, all time = 0.002228118 s
Deleted all 10 items in python dict with average time 0.0 mcs for 100 tests, all time = 8.1671e-05 s
##################################################
Deleted all 100 items in Chained Map with average time 104.0 mcs for 100 tests, all time = 0.010463553 s
Deleted all 100 items in Double Hashed Map with average time 261.0 mcs for 100 tests, all time = 0.026182143 s
Deleted all 100 items in python dict with average time 5.0 mcs for 100 tests, all time = 0.000541691 s
##################################################
Deleted all 1000 items in Chained Map with average time 1007.0 mcs for 100 tests, all time = 0.100732934 s
Deleted all 1000 items in Double Hashed Map with average time 2445.0 mcs for 100 tests, all time = 0.244504677 s
Deleted all 1000 items in python dict with average time 47.0 mcs for 100 tests, all time = 0.004737376 s
##################################################
Deleted all 10000 items in Chained Map with average time 16323.0 mcs for 100 tests, all time = 1.63236785 s
Deleted all 10000 items in Double Hashed Map with average time 31773.0 mcs for 100 tests, all time = 3.177328269 s
Deleted all 10000 items in python dict with average time 656.0 mcs for 100 tests, all time = 0.065617894 s
##################################################
'''
