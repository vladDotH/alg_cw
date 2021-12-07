from hash_maps import Pair, DHashedMap, ChainedMap
from testing.maps_comparator import assertion
import time
import random

MAX_KEY = 100
PROBES = 100
TESTS = [10, 100, 1_000, 10_000]
START_LEN = 10


def solveCM(cm: ChainedMap, data):
    t = time.time_ns()
    for k in data:
        if k not in cm.keyset():
            cm.insert(Pair(k, 1))
        else:
            cm.insert(Pair(k, 1 + cm.get(k)))
    return time.time_ns() - t


def solveDM(dm: DHashedMap, data):
    t = time.time_ns()
    for k in data:
        if k not in dm.keyset():
            dm.insert(Pair(k, 1))
        else:
            dm.insert(Pair(k, 1 + dm.get(k)))
    return time.time_ns() - t


def solvePD(pm: dict, data):
    t = time.time_ns()
    for k in data:
        if k not in pm.keys():
            pm[k] = 1
        else:
            pm[k] = 1 + pm[k]
    return time.time_ns() - t


if __name__ == "__main__":
    for n in TESTS:
        cT, dT, pT = [], [], []
        for i in range(PROBES):
            cm = ChainedMap(START_LEN)
            dm = DHashedMap(START_LEN)
            pm = dict()
            data = [random.randint(0, MAX_KEY) for _ in range(n)]

            cT.append(solveCM(cm, data))
            dT.append(solveDM(dm, data))
            pT.append(solvePD(pm, data))
            assertion(cm, dm, pm)

        print(f'Start length = {START_LEN}, N = {n}:')
        print(f'Task solved by Chained Map '
              f'with average time {(sum(cT) / PROBES) // 1e3} mcs for {PROBES} tests, all time = {sum(cT) / 1e9} s')
        print(f'Task solved by Double Hashed Map '
              f'with average time {(sum(dT) / PROBES) // 1e3} mcs for {PROBES} tests, all time = {sum(dT) / 1e9} s')
        print(f'Task solved by python dict '
              f'with average time {(sum(pT) / PROBES) // 1e3} mcs for {PROBES} tests, all time = {sum(pT) / 1e9} s')
        print('#' * 50)


''' TEST OUTPUT
Start length = 10, N = 10:
Task solved by Chained Map with average time 38.0 mcs for 100 tests, all time = 0.00383661 s
Task solved by Double Hashed Map with average time 56.0 mcs for 100 tests, all time = 0.005634003 s
Task solved by python dict with average time 1.0 mcs for 100 tests, all time = 0.000174735 s
##################################################
Start length = 10, N = 100:
Task solved by Chained Map with average time 1687.0 mcs for 100 tests, all time = 0.168750701 s
Task solved by Double Hashed Map with average time 1194.0 mcs for 100 tests, all time = 0.119491606 s
Task solved by python dict with average time 16.0 mcs for 100 tests, all time = 0.001612102 s
##################################################
Start length = 10, N = 1000:
Task solved by Chained Map with average time 29091.0 mcs for 100 tests, all time = 2.909157416 s
Task solved by Double Hashed Map with average time 15016.0 mcs for 100 tests, all time = 1.501651232 s
Task solved by python dict with average time 138.0 mcs for 100 tests, all time = 0.013826631 s
##################################################
Start length = 10, N = 10000:
Task solved by Chained Map with average time 299401.0 mcs for 100 tests, all time = 29.940142077 s
Task solved by Double Hashed Map with average time 152750.0 mcs for 100 tests, all time = 15.275052389 s
Task solved by python dict with average time 1276.0 mcs for 100 tests, all time = 0.127690082 s
##################################################
'''
