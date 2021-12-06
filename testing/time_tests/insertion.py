from hash_maps import Pair, DHashedMap, ChainedMap
import time
import random

MAX_KEY = 2 ** 32
PROBES = 1000


def insertionCM(n, start, probes):
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
          f'with average time {avg // 1000} mсs for {probes} tests, all time = {sum(dT) / 1e9} s')
    return avg


def insertionDM(n, start, probes):
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
        f'with average time {avg // 1000} mсs for {probes} tests, all time = {sum(dT) / 1e9} s')
    return avg


def insertionPD(n, probes):
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
    print(f'added {n} items in python dict with average time {avg // 1000} mсs  for {probes} tests, all time = {sum(dT) / 1e9} s')
    return avg


if __name__ == "__main__":
    for n in range(1, 4 + 1):
        N = 10 ** n
        for sz in range(1, n + 1):
            START = 10 ** sz
            insertionCM(N, START, PROBES)
            insertionDM(N, START, PROBES)
            print('_' * 50)
        insertionPD(N, PROBES)
        print('#' * 50)
