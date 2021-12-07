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
Deleted all 10 items in Chained Map with average time 9.0 mcs for 100 tests, all time = 0.000937549 s
Deleted all 10 items in Double Hashed Map with average time 20.0 mcs for 100 tests, all time = 0.002016884 s
Deleted all 10 items in python dict with average time 0.0 mcs for 100 tests, all time = 7.2243e-05 s
##################################################
Deleted all 100 items in Chained Map with average time 94.0 mcs for 100 tests, all time = 0.009436975 s
Deleted all 100 items in Double Hashed Map with average time 228.0 mcs for 100 tests, all time = 0.022852996 s
Deleted all 100 items in python dict with average time 4.0 mcs for 100 tests, all time = 0.000479309 s
##################################################
Deleted all 1000 items in Chained Map with average time 991.0 mcs for 100 tests, all time = 0.099167684 s
Deleted all 1000 items in Double Hashed Map with average time 2315.0 mcs for 100 tests, all time = 0.231515583 s
Deleted all 1000 items in python dict with average time 42.0 mcs for 100 tests, all time = 0.004271671 s
##################################################
Deleted all 10000 items in Chained Map with average time 16164.0 mcs for 100 tests, all time = 1.616496639 s
Deleted all 10000 items in Double Hashed Map with average time 29335.0 mcs for 100 tests, all time = 2.933574184 s
Deleted all 10000 items in python dict with average time 587.0 mcs for 100 tests, all time = 0.058792608 s
##################################################
'''
