from hash_maps import Pair, DHashedMap, ChainedMap
from testing.maps_comparator import assertion
import time
import random

MAX_KEY = 100
PROBES = 100
TESTS = [10, 100, 1_000, 10_000]
START_LEN = 10


def insertCM(cm: ChainedMap, data):
    t = time.time_ns()
    for k in data:
        if k not in cm.keyset():
            cm.insert(Pair(k, 1))
        else:
            cm.insert(Pair(k, 1 + cm.get(k)))
    return time.time_ns() - t


def insertDM(dm: DHashedMap, data):
    t = time.time_ns()
    for k in data:
        if k not in dm.keyset():
            dm.insert(Pair(k, 1))
        else:
            dm.insert(Pair(k, 1 + dm.get(k)))
    return time.time_ns() - t


def insertPD(pm: dict, data):
    t = time.time_ns()
    for k in data:
        if k not in pm.keys():
            pm[k] = 1
        else:
            pm[k] = 1 + pm[k]
    return time.time_ns() - t


def deleteCM(cm: ChainedMap, data):
    t = time.time_ns()
    for k in data:
        cm.remove(k)
    return time.time_ns() - t


def deleteDM(dm: DHashedMap, data):
    t = time.time_ns()
    for k in data:
        dm.remove(k)
    return time.time_ns() - t


def deletePD(pm: dict, data):
    t = time.time_ns()
    for k in data:
        del pm[k]
    return time.time_ns() - t


if __name__ == "__main__":
    for n in TESTS:
        cT, dT, pT = [], [], []
        for i in range(PROBES):
            cm = ChainedMap(START_LEN)
            dm = DHashedMap(START_LEN)
            pm = dict()

            data = [random.randint(0, MAX_KEY) for _ in range(n)]
            ct = insertCM(cm, data)
            dt = insertDM(dm, data)
            pt = insertPD(pm, data)

            assertion(cm, dm, pm)

            DEL = n // 2
            toDelete = list(set(random.choices(list(pm.keys()), k=DEL)))

            ct += deleteCM(cm, toDelete)
            dt += deleteDM(dm, toDelete)
            pt += deletePD(pm, toDelete)

            assertion(cm, dm, pm)

            newData = [random.randint(0, MAX_KEY) for _ in range(n)]
            ct += insertCM(cm, newData)
            dt += insertDM(dm, newData)
            pt += insertPD(pm, newData)

            assertion(cm, dm, pm)

            cT.append(ct)
            dT.append(dt)
            pT.append(pt)

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
Task solved by Chained Map with average time 141.0 mcs for 100 tests, all time = 0.014118986 s
Task solved by Double Hashed Map with average time 213.0 mcs for 100 tests, all time = 0.021348581 s
Task solved by python dict with average time 6.0 mcs for 100 tests, all time = 0.000649831 s
##################################################
Start length = 10, N = 100:
Task solved by Chained Map with average time 4710.0 mcs for 100 tests, all time = 0.471094879 s
Task solved by Double Hashed Map with average time 3148.0 mcs for 100 tests, all time = 0.314838996 s
Task solved by python dict with average time 42.0 mcs for 100 tests, all time = 0.004249368 s
##################################################
Start length = 10, N = 1000:
Task solved by Chained Map with average time 56611.0 mcs for 100 tests, all time = 5.661117013 s
Task solved by Double Hashed Map with average time 30265.0 mcs for 100 tests, all time = 3.026554371 s
Task solved by python dict with average time 269.0 mcs for 100 tests, all time = 0.026978653 s
##################################################
Start length = 10, N = 10000:
Task solved by Chained Map with average time 592642.0 mcs for 100 tests, all time = 59.264219204 s
Task solved by Double Hashed Map with average time 311453.0 mcs for 100 tests, all time = 31.145343531 s
Task solved by python dict with average time 2553.0 mcs for 100 tests, all time = 0.255348443 s
##################################################
'''
