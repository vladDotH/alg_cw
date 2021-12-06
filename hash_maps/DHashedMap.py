from typing import Callable, Hashable, Tuple

from .HashMap import Pair, HashMap, defautlHash


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


def defaultHash2(hm: HashMap, key) -> int:
    return 1 + hm.hashFunc(hm, key) % (hm.mapSize() - 1)


class Node:
    def __init__(self, item):
        self.item = item
        self.deleted = False

    def delete(self):
        self.deleted = True

    def __str__(self):
        return str(self.item) if not self.deleted else 'deleted'

    def __repr__(self):
        return str(self)


class DHashedMap(HashMap):
    EXPAND_COEF = 0.5
    MAX_FILL_COEFF = 0.7

    def __init__(self, size: int, hashFunc: Callable[[HashMap, object], int] = defautlHash,
                 hashFunc2: Callable[[HashMap, object], int] = defaultHash2):
        super().__init__(nextPrime(size), hashFunc)
        self.hashFunc2 = hashFunc2

    def expand(self, add: int):
        super().expand(nextPrime(add))
        self.refresh()

    def __probe(self, h1: int, h2: int, i: int) -> int:
        return (h1 + i * h2) % self.mapSize()

    def calcHash(self, key) -> Tuple[int, int]:
        h2 = self.hashFunc2(self, key)
        if h2 == 0:
            raise ArithmeticError('incorrect second hash function')
        return self.hashFunc(self, key), h2,

    def __find(self, key) -> Tuple[int, bool]:
        h1, h2 = self.calcHash(key)
        j = 0
        i = self.__probe(h1, h2, j)
        free = None
        while j < self.mapSize() and self.arr[i] is not None:
            if self.arr[i].item.key == key:
                return i, True
            elif self.arr[i].deleted:
                free = i
            j += 1
            i = self.__probe(h1, h2, j)

        if free is not None:
            return free, False
        else:
            return i, False

    def insert(self, obj: Pair) -> bool:
        if self.fillCoef() >= DHashedMap.MAX_FILL_COEFF:
            self.expand(int(self.mapSize() * DHashedMap.EXPAND_COEF))
        i, res = self.__find(obj.key)
        if res:
            return False
        else:
            self.arr[i] = Node(obj)
            self._itemsSize += 1
            return True

    def get(self, key):
        i, res = self.__find(key)
        if res:
            return self.arr[i].item.value
        else:
            return None

    def keyset(self) -> list:
        return [i.item.key for i in self.arr if i is not None and not i.deleted]

    def remove(self, key) -> bool:
        i, res = self.__find(key)
        if res:
            self.arr[i].delete()
            self._itemsSize -= 1
            return True
        else:
            return False

    def refresh(self):
        newMap = DHashedMap(self.mapSize())
        for i in self.arr:
            if i is not None and not i.deleted:
                newMap.insert(i.item)
        self.arr = newMap.arr
