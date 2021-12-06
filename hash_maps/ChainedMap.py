from typing import List, Callable

from .HashMap import Pair, HashMap, defautlHash


class Node:
    def __init__(self, item, nxt=None):
        self.item = item
        self.nxt = nxt


class LinkedList:
    def __init__(self):
        self.head = Node(None, None)

    def spread(self) -> List[Pair]:
        node = self.head.nxt
        lst = []
        while node is not None:
            lst.append(node.item)
            node = node.nxt
        return lst

    def __str__(self):
        return '[' + ', '.join(list(map(str, self.spread()))) + ']'

    def __repr__(self):
        return str(self)


class ChainedMap(HashMap):
    EXPAND_COEF = 0.5
    MAX_FILL_COEFF = 1.5

    def __init__(self, size: int, hashFunc: Callable[[HashMap, object], int] = defautlHash):
        super().__init__(size, hashFunc)
        for i in range(self.mapSize()):
            self.arr[i] = LinkedList()

    def calcHash(self, key) -> int:
        return self.hashFunc(self, key) % self.mapSize()

    def __find(self, key) -> Node:
        i = self.calcHash(key)
        node = self.arr[i].head
        while node.nxt is not None:
            if node.nxt.item.key == key:
                return node
            node = node.nxt
        return node

    def insert(self, obj: Pair) -> bool:
        if self.fillCoef() > ChainedMap.MAX_FILL_COEFF:
            self.expand(int(self.mapSize() * ChainedMap.EXPAND_COEF))

        node = self.__find(obj.key)
        if node.nxt is None:
            node.nxt = Node(obj, None)
            self._itemsSize += 1
            return True
        else:
            return False

    def get(self, key):
        node = self.__find(key)
        if node.nxt is not None:
            return node.nxt.item.value
        else:
            return None

    def remove(self, key) -> bool:
        node = self.__find(key)
        if node.nxt is not None:
            node.nxt = node.nxt.nxt
            self._itemsSize -= 1
            return True
        else:
            return False

    def keyset(self) -> list:
        return [item.key for items in self.arr for item in items.spread()]

    def expand(self, add: int):
        self.arr.extend([LinkedList() for i in range(add)])
        self.refresh()

    def refresh(self):
        newMap = ChainedMap(self.mapSize())
        for i in self.arr:
            for j in i.spread():
                newMap.insert(j)
        self.arr = newMap.arr

    def getListsFill(self) -> List[int]:
        return [len(i.spread()) for i in self.arr]
