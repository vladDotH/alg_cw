from hash_maps import Pair, DHashedMap, ChainedMap
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

            assert sorted(cm.keyset()) == sorted(dm.keyset()) == sorted(pm.keys())
            for j in pm.keys():
                assert cm.get(j) == dm.get(j) == pm[j]

            DEL = n // 2
            toDelete = list(set(random.choices(list(pm.keys()), k=DEL)))

            ct += deleteCM(cm, toDelete)
            dt += deleteDM(dm, toDelete)
            pt += deletePD(pm, toDelete)

            assert sorted(cm.keyset()) == sorted(dm.keyset()) == sorted(pm.keys())
            for j in pm.keys():
                assert cm.get(j) == dm.get(j) == pm[j]

            newData = [random.randint(0, MAX_KEY) for _ in range(n)]
            ct += insertCM(cm, newData)
            dt += insertDM(dm, newData)
            pt += insertPD(pm, newData)

            assert sorted(cm.keyset()) == sorted(dm.keyset()) == sorted(pm.keys())
            for j in pm.keys():
                assert cm.get(j) == dm.get(j) == pm[j]

            cT.append(ct)
            dT.append(dt)
            pT.append(pt)

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
Task solved by Chained Map with average time 121.0 mcs for 100 tests, all time = 0.012145603 s
Task solved by Double Hashed Map with average time 174.0 mcs for 100 tests, all time = 0.017428668 s
Task solved by python dict with average time 5.0 mcs for 100 tests, all time = 0.000542584 s
##################################################
N = 100:
Task solved by Chained Map with average time 3683.0 mcs for 100 tests, all time = 0.368397977 s
Task solved by Double Hashed Map with average time 2310.0 mcs for 100 tests, all time = 0.231098895 s
Task solved by python dict with average time 32.0 mcs for 100 tests, all time = 0.003280555 s
##################################################
N = 1000:
Task solved by Chained Map with average time 52945.0 mcs for 100 tests, all time = 5.294576304 s
Task solved by Double Hashed Map with average time 28035.0 mcs for 100 tests, all time = 2.803580611 s
Task solved by python dict with average time 256.0 mcs for 100 tests, all time = 0.025638557 s
##################################################
N = 10000:
Task solved by Chained Map with average time 562107.0 mcs for 100 tests, all time = 56.210758877 s
Task solved by Double Hashed Map with average time 292236.0 mcs for 100 tests, all time = 29.223615809 s
Task solved by python dict with average time 2498.0 mcs for 100 tests, all time = 0.249829485 s
##################################################
'''
