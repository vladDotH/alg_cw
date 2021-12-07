from hash_maps import Pair, DHashedMap, ChainedMap
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
            assert sorted(cm.keyset()) == sorted(dm.keyset()) == sorted(pm.keys())
            for j in pm.keys():
                assert cm.get(j) == dm.get(j) == pm[j]

        print(f'N = {n}:')
        print(f'Task solved by Chained Map '
              f'with average time {(sum(cT) / PROBES) // 1e3} mcs for {PROBES} tests, all time = {sum(cT) / 1e9} s')
        print(f'Task solved by Double Hashed Map '
              f'with average time {(sum(dT) / PROBES) // 1e3} mcs for {PROBES} tests, all time = {sum(dT) / 1e9} s')
        print(f'Task solved by python dict '
              f'with average time {(sum(pT) / PROBES) // 1e3} mcs for {PROBES} tests, all time = {sum(pT) / 1e9} s')
        print('#' * 50)


''' TEST OUTPUT
N = 10:
Task solved by Chained Map with average time 53.0 mcs for 100 tests, all time = 0.005317759 s
Task solved by Double Hashed Map with average time 69.0 mcs for 100 tests, all time = 0.006941773 s
Task solved by python dict with average time 2.0 mcs for 100 tests, all time = 0.000217382 s
##################################################
N = 100:
Task solved by Chained Map with average time 1651.0 mcs for 100 tests, all time = 0.165188329 s
Task solved by Double Hashed Map with average time 1145.0 mcs for 100 tests, all time = 0.114501898 s
Task solved by python dict with average time 15.0 mcs for 100 tests, all time = 0.001597059 s
##################################################
N = 1000:
Task solved by Chained Map with average time 29485.0 mcs for 100 tests, all time = 2.948556988 s
Task solved by Double Hashed Map with average time 15740.0 mcs for 100 tests, all time = 1.574085629 s
Task solved by python dict with average time 143.0 mcs for 100 tests, all time = 0.014383495 s
##################################################
N = 10000:
Task solved by Chained Map with average time 281598.0 mcs for 100 tests, all time = 28.159805566 s
Task solved by Double Hashed Map with average time 149723.0 mcs for 100 tests, all time = 14.972315714 s
Task solved by python dict with average time 1225.0 mcs for 100 tests, all time = 0.12255279 s
##################################################
'''
