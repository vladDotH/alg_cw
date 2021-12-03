from typing import Callable, Hashable

from HashMap import Pair, HashMap


def isPrime(n: int) -> bool:
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** (1 / 2)) + 1, 2):
        if n % i == 0:
            return False
    return True


def nextPrime(n: int) -> int:
    while not isPrime(n):
        n += 1
    return n


def defaultHash2(hm: HashMap, key):
    return 1 + hash(key) % (hm.mapSize() - 1)


class DHashedMap(HashMap):
    def __init__(self, size: int, hashfunc: Callable[[HashMap, object], int] = defaultHash2):
        super().__init__(size)
        self.hash2 = hashfunc

    def expand(self, add: int):
        super().expand(nextPrime(add))
        self.refresh()

    def __probe(self, h1: int, h2: int, i: int):
        return (h1 + i * h2) % self.mapSize()

    def insert(self, obj: Pair) -> bool:
        h1 = hash(obj.key)
        h2 = self.hash2(self, obj.key)
        j = 0
        i = self.__probe(h1, h2, j)
        while self.arr[i] is not None:
            j += 1
            i = self.__probe(h1, h2, j)
        self.arr[i] = obj

    def get(self, key):
        h1 = hash(obj.key)
        h2 = self.hash2(self, obj.key)
        j = 0
        i = self.__probe(h1, h2, j)
        while self.arr[i] is not None:
            j += 1
            i = self.__probe(h1, h2, j)
        self.arr[i] = obj

    def remove(self, key) -> bool:

    def refresh(self):
        newMap = DHashedMap(self.mapSize())
        for i in self.arr:
            if i is not None:
                newMap.insert(i)
        self.arr = newMap.arr
