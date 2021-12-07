from hash_maps import Pair, DHashedMap, ChainedMap
import time
import random

MAX_KEY = 2 ** 32
PROBES = 100
TESTS = [100, 1_000, 10_000, 100_000]


def searchCM(cm: ChainedMap, probes: int):
    keys = cm.keyset()
    dT = []
    for i in range(probes):
        for k in keys:
            t = time.time_ns()
            cm.get(k)
            dt = time.time_ns() - t
            dT.append(dt)
    avg = sum(dT) / len(dT)
    print(f'Found all items in Chained Map with size = {cm.mapSize()} '
          f'with average time {int(avg)} ns for {probes} tests, all time = {sum(dT) / 1e9} s')


def searchDM(dm: DHashedMap, probes: int):
    keys = dm.keyset()
    dT = []
    for i in range(probes):
        for k in keys:
            t = time.time_ns()
            dm.get(k)
            dt = time.time_ns() - t
            dT.append(dt)
    avg = sum(dT) / len(dT)
    print(f'Found all items in Double Hashed Map with size = {dm.mapSize()} '
          f'with average time {int(avg)} ns for {probes} tests, all time = {sum(dT) / 1e9} s')


def searchPD(pm: dict, probes: int):
    keys = pm.keys()
    dT = []
    for i in range(probes):
        for k in keys:
            t = time.time_ns()
            _ = pm[k]
            dt = time.time_ns() - t
            dT.append(dt)
    avg = sum(dT) / len(dT)
    print(f'Found all items in python dict with size = {len(pm)} '
          f'with average time {int(avg)} ns for {probes} tests, all time = {sum(dT) / 1e9} s')


if __name__ == "__main__":
    for n in TESTS:
        cm = ChainedMap(n)
        dm = DHashedMap(int(n / DHashedMap.MAX_FILL_COEFF) + 1)
        pm = dict()
        data = [Pair(random.randint(0, MAX_KEY), i) for i in range(n)]
        for i in data:
            cm.insert(i)
            dm.insert(i)
            pm[i.key] = i.value
        searchCM(cm, PROBES)
        searchDM(dm, PROBES)
        searchPD(pm, PROBES)
        print('#' * 50)


''' TEST OUTPUT
Found all items in Chained Map with size = 100 with average time 1085 ns for 100 tests, all time = 0.010858023 s
Found all items in Double Hashed Map with size = 149 with average time 2569 ns for 100 tests, all time = 0.025699018 s
Found all items in python dict with size = 100 with average time 115 ns for 100 tests, all time = 0.001158311 s
##################################################
Found all items in Chained Map with size = 1000 with average time 1059 ns for 100 tests, all time = 0.105911365 s
Found all items in Double Hashed Map with size = 1429 with average time 2819 ns for 100 tests, all time = 0.281961068 s
Found all items in python dict with size = 1000 with average time 170 ns for 100 tests, all time = 0.017064445 s
##################################################
Found all items in Chained Map with size = 10000 with average time 1551 ns for 100 tests, all time = 1.551005037 s
Found all items in Double Hashed Map with size = 14293 with average time 2982 ns for 100 tests, all time = 2.982108829 s
Found all items in python dict with size = 10000 with average time 130 ns for 100 tests, all time = 0.130166659 s
##################################################
Found all items in Chained Map with size = 100000 with average time 1691 ns for 100 tests, all time = 16.911993505 s
Found all items in Double Hashed Map with size = 142867 with average time 2978 ns for 100 tests, all time = 29.787553976 s
Found all items in python dict with size = 99997 with average time 216 ns for 100 tests, all time = 2.16109659 s
##################################################
'''