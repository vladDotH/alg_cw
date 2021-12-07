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
Found all items in Chained Map with size = 100 with average time 1189 ns for 100 tests, all time = 0.011890376 s
Found all items in Double Hashed Map with size = 149 with average time 2448 ns for 100 tests, all time = 0.024483182 s
Found all items in python dict with size = 100 with average time 149 ns for 100 tests, all time = 0.001490118 s
##################################################
Found all items in Chained Map with size = 1000 with average time 1028 ns for 100 tests, all time = 0.102807026 s
Found all items in Double Hashed Map with size = 1429 with average time 3348 ns for 100 tests, all time = 0.334850222 s
Found all items in python dict with size = 1000 with average time 128 ns for 100 tests, all time = 0.012818644 s
##################################################
Found all items in Chained Map with size = 10000 with average time 1521 ns for 100 tests, all time = 1.52185614 s
Found all items in Double Hashed Map with size = 14293 with average time 3169 ns for 100 tests, all time = 3.169557833 s
Found all items in python dict with size = 10000 with average time 138 ns for 100 tests, all time = 0.138550454 s
##################################################
Found all items in Chained Map with size = 100000 with average time 1533 ns for 100 tests, all time = 15.331074181 s
Found all items in Double Hashed Map with size = 142867 with average time 3177 ns for 100 tests, all time = 31.773628002 s
Found all items in python dict with size = 100000 with average time 214 ns for 100 tests, all time = 2.148154342 s
##################################################
'''