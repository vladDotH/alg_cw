from hash_maps import Pair, DHashedMap, ChainedMap
import time
import random

MAX_KEY = 2 ** 32
PROBES = 100
TESTS = [10, 100, 1_000, 10_000]
START_LEN = [10, 100, 1_000, 10_000]


def insertionCM(n: int, start: int, probes: int):
    dT = []
    for i in range(probes):
        data = [Pair(random.randint(0, MAX_KEY), i) for i in range(n)]
        t = time.time_ns()
        cm = ChainedMap(start)
        for i in data:
            cm.insert(i)
        dt = time.time_ns() - t
        dT.append(dt)
    avg = sum(dT) / len(dT)
    print(f'added {n} items in Chained Map with starting length = {start} '
          f'with average time {avg // 1e3} mсs for {probes} tests, all time = {sum(dT) / 1e9} s')


def insertionDM(n: int, start: int, probes: int):
    dT = []
    for i in range(probes):
        data = [Pair(random.randint(0, MAX_KEY), i) for i in range(n)]
        t = time.time_ns()
        cm = DHashedMap(start)
        for i in data:
            cm.insert(i)
        dt = time.time_ns() - t
        dT.append(dt)
    avg = sum(dT) / len(dT)
    print(
        f'added {n} items in Double Hashed Map with starting length = {start} '
        f'with average time {avg // 1e3} mсs for {probes} tests, all time = {sum(dT) / 1e9} s')


def insertionPD(n: int, probes: int):
    dT = []
    for i in range(probes):
        data = [Pair(random.randint(0, MAX_KEY), i) for i in range(n)]
        t = time.time_ns()
        cm = dict()
        for i in data:
            cm[i.key] = i.value
        dt = time.time_ns() - t
        dT.append(dt)
    avg = sum(dT) / len(dT)
    print(
        f'added {n} items in python dict with average time {avg // 1e3} mсs  for {probes} tests, all time = {sum(dT) / 1e9} s')


if __name__ == "__main__":
    for n in TESTS:
        for sz in START_LEN:
            insertionCM(n, sz, PROBES)
            insertionDM(n, sz, PROBES)
            print('_' * 50)
        insertionPD(n, PROBES)
        print('#' * 50)


''' TEST OUTPUT
added 10 items in Chained Map with starting length = 10 with average time 35.0 mсs for 100 tests, all time = 0.003515742 s
added 10 items in Double Hashed Map with starting length = 10 with average time 94.0 mсs for 100 tests, all time = 0.009431659 s
__________________________________________________
added 10 items in Chained Map with starting length = 100 with average time 36.0 mсs for 100 tests, all time = 0.00361337 s
added 10 items in Double Hashed Map with starting length = 100 with average time 44.0 mсs for 100 tests, all time = 0.004455676 s
__________________________________________________
added 10 items in Chained Map with starting length = 1000 with average time 39.0 mсs for 100 tests, all time = 0.003999679 s
added 10 items in Double Hashed Map with starting length = 1000 with average time 53.0 mсs for 100 tests, all time = 0.005361216 s
__________________________________________________
added 10 items in Chained Map with starting length = 10000 with average time 60.0 mсs for 100 tests, all time = 0.006020321 s
added 10 items in Double Hashed Map with starting length = 10000 with average time 55.0 mсs for 100 tests, all time = 0.005577796 s
__________________________________________________
added 10 items in python dict with average time 1.0 mсs  for 100 tests, all time = 0.000129994 s
##################################################
added 100 items in Chained Map with starting length = 10 with average time 813.0 mсs for 100 tests, all time = 0.08135296 s
added 100 items in Double Hashed Map with starting length = 10 with average time 956.0 mсs for 100 tests, all time = 0.095694441 s
__________________________________________________
added 100 items in Chained Map with starting length = 100 with average time 190.0 mсs for 100 tests, all time = 0.019090094 s
added 100 items in Double Hashed Map with starting length = 100 with average time 487.0 mсs for 100 tests, all time = 0.048796013 s
__________________________________________________
added 100 items in Chained Map with starting length = 1000 with average time 201.0 mсs for 100 tests, all time = 0.020179824 s
added 100 items in Double Hashed Map with starting length = 1000 with average time 236.0 mсs for 100 tests, all time = 0.02369964 s
__________________________________________________
added 100 items in Chained Map with starting length = 10000 with average time 230.0 mсs for 100 tests, all time = 0.023082137 s
added 100 items in Double Hashed Map with starting length = 10000 with average time 244.0 mсs for 100 tests, all time = 0.024453619 s
__________________________________________________
added 100 items in python dict with average time 10.0 mсs  for 100 tests, all time = 0.001027796 s
##################################################
added 1000 items in Chained Map with starting length = 10 with average time 8842.0 mсs for 100 tests, all time = 0.884248505 s
added 1000 items in Double Hashed Map with starting length = 10 with average time 10489.0 mсs for 100 tests, all time = 1.048990195 s
__________________________________________________
added 1000 items in Chained Map with starting length = 100 with average time 9456.0 mсs for 100 tests, all time = 0.945666486 s
added 1000 items in Double Hashed Map with starting length = 100 with average time 10797.0 mсs for 100 tests, all time = 1.07974645 s
__________________________________________________
added 1000 items in Chained Map with starting length = 1000 with average time 2303.0 mсs for 100 tests, all time = 0.230382512 s
added 1000 items in Double Hashed Map with starting length = 1000 with average time 5089.0 mсs for 100 tests, all time = 0.508995638 s
__________________________________________________
added 1000 items in Chained Map with starting length = 10000 with average time 2557.0 mсs for 100 tests, all time = 0.25571524 s
added 1000 items in Double Hashed Map with starting length = 10000 with average time 2657.0 mсs for 100 tests, all time = 0.265748179 s
__________________________________________________
added 1000 items in python dict with average time 109.0 mсs  for 100 tests, all time = 0.010992038 s
##################################################
added 10000 items in Chained Map with starting length = 10 with average time 136339.0 mсs for 100 tests, all time = 13.633976647 s
added 10000 items in Double Hashed Map with starting length = 10 with average time 111838.0 mсs for 100 tests, all time = 11.183888263 s
__________________________________________________
added 10000 items in Chained Map with starting length = 100 with average time 129522.0 mсs for 100 tests, all time = 12.952221614 s
added 10000 items in Double Hashed Map with starting length = 100 with average time 106055.0 mсs for 100 tests, all time = 10.605520348 s
__________________________________________________
added 10000 items in Chained Map with starting length = 1000 with average time 109494.0 mсs for 100 tests, all time = 10.949424868 s
added 10000 items in Double Hashed Map with starting length = 1000 with average time 116472.0 mсs for 100 tests, all time = 11.647218988 s
__________________________________________________
added 10000 items in Chained Map with starting length = 10000 with average time 31968.0 mсs for 100 tests, all time = 3.196841517 s
added 10000 items in Double Hashed Map with starting length = 10000 with average time 65042.0 mсs for 100 tests, all time = 6.504218164 s
__________________________________________________
added 10000 items in python dict with average time 1630.0 mсs  for 100 tests, all time = 0.163049332 s
##################################################
'''
