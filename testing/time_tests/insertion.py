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
added 10 items in Chained Map with starting length = 10 with average time 25.0 mсs for 100 tests, all time = 0.002595562 s
added 10 items in Double Hashed Map with starting length = 10 with average time 61.0 mсs for 100 tests, all time = 0.006155014 s
__________________________________________________
added 10 items in Chained Map with starting length = 100 with average time 66.0 mсs for 100 tests, all time = 0.006683478 s
added 10 items in Double Hashed Map with starting length = 100 with average time 30.0 mсs for 100 tests, all time = 0.003067882 s
__________________________________________________
added 10 items in Chained Map with starting length = 1000 with average time 705.0 mсs for 100 tests, all time = 0.070528902 s
added 10 items in Double Hashed Map with starting length = 1000 with average time 27.0 mсs for 100 tests, all time = 0.002782739 s
__________________________________________________
added 10 items in Chained Map with starting length = 10000 with average time 10307.0 mсs for 100 tests, all time = 1.030774281 s
added 10 items in Double Hashed Map with starting length = 10000 with average time 49.0 mсs for 100 tests, all time = 0.004901711 s
__________________________________________________
added 10 items in python dict with average time 1.0 mсs  for 100 tests, all time = 0.000116225 s
##################################################
added 100 items in Chained Map with starting length = 10 with average time 671.0 mсs for 100 tests, all time = 0.067151178 s
added 100 items in Double Hashed Map with starting length = 10 with average time 769.0 mсs for 100 tests, all time = 0.076974521 s
__________________________________________________
added 100 items in Chained Map with starting length = 100 with average time 221.0 mсs for 100 tests, all time = 0.022177607 s
added 100 items in Double Hashed Map with starting length = 100 with average time 497.0 mсs for 100 tests, all time = 0.049719556 s
__________________________________________________
added 100 items in Chained Map with starting length = 1000 with average time 915.0 mсs for 100 tests, all time = 0.091599608 s
added 100 items in Double Hashed Map with starting length = 1000 with average time 223.0 mсs for 100 tests, all time = 0.022364347 s
__________________________________________________
added 100 items in Chained Map with starting length = 10000 with average time 9875.0 mсs for 100 tests, all time = 0.987598174 s
added 100 items in Double Hashed Map with starting length = 10000 with average time 236.0 mсs for 100 tests, all time = 0.023667353 s
__________________________________________________
added 100 items in python dict with average time 10.0 mсs  for 100 tests, all time = 0.001032323 s
##################################################
added 1000 items in Chained Map with starting length = 10 with average time 8696.0 mсs for 100 tests, all time = 0.869638385 s
added 1000 items in Double Hashed Map with starting length = 10 with average time 10286.0 mсs for 100 tests, all time = 1.02866069 s
__________________________________________________
added 1000 items in Chained Map with starting length = 100 with average time 7359.0 mсs for 100 tests, all time = 0.735906682 s
added 1000 items in Double Hashed Map with starting length = 100 with average time 9599.0 mсs for 100 tests, all time = 0.959916934 s
__________________________________________________
added 1000 items in Chained Map with starting length = 1000 with average time 2487.0 mсs for 100 tests, all time = 0.248732051 s
added 1000 items in Double Hashed Map with starting length = 1000 with average time 4654.0 mсs for 100 tests, all time = 0.465447036 s
__________________________________________________
added 1000 items in Chained Map with starting length = 10000 with average time 12147.0 mсs for 100 tests, all time = 1.214703074 s
added 1000 items in Double Hashed Map with starting length = 10000 with average time 2377.0 mсs for 100 tests, all time = 0.237765544 s
__________________________________________________
added 1000 items in python dict with average time 102.0 mсs  for 100 tests, all time = 0.010208181 s
##################################################
added 10000 items in Chained Map with starting length = 10 with average time 141073.0 mсs for 100 tests, all time = 14.107388877 s
added 10000 items in Double Hashed Map with starting length = 10 with average time 99792.0 mсs for 100 tests, all time = 9.979245429 s
__________________________________________________
added 10000 items in Chained Map with starting length = 100 with average time 148729.0 mсs for 100 tests, all time = 14.872941767 s
added 10000 items in Double Hashed Map with starting length = 100 with average time 104894.0 mсs for 100 tests, all time = 10.489439955 s
__________________________________________________
added 10000 items in Chained Map with starting length = 1000 with average time 109002.0 mсs for 100 tests, all time = 10.900242488 s
added 10000 items in Double Hashed Map with starting length = 1000 with average time 120074.0 mсs for 100 tests, all time = 12.007419704 s
__________________________________________________
added 10000 items in Chained Map with starting length = 10000 with average time 43515.0 mсs for 100 tests, all time = 4.351513121 s
added 10000 items in Double Hashed Map with starting length = 10000 with average time 56383.0 mсs for 100 tests, all time = 5.638385737 s
__________________________________________________
added 10000 items in python dict with average time 1335.0 mсs  for 100 tests, all time = 0.133519041 s
##################################################
'''
