from typing import List

from HashMap import Pair, HashMap


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
        return '[' + ' '.join(list(map(str, self.spread()))) + ']'


class ChainMap(HashMap):
    def __init__(self, size: int):
        super().__init__(size)
        for i in range(self.mapSize()):
            self.arr[i] = LinkedList()

    def __find(self, key) -> Node:
        i = hash(key) % self.mapSize()
        node = self.arr[i].head
        while node.nxt is not None:
            if node.nxt.item.key == key:
                return node
            node = node.nxt
        return node

    def insert(self, obj: Pair) -> bool:
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
            return node.nxt.item
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

    def expand(self, add: int):
        super().expand(add)
        self.refresh()

    def refresh(self):
        newMap = ChainMap(self.mapSize())
        for i in self.arr:
            for j in i.spread():
                newMap.insert(j)
        self.arr = newMap.arr

    def getListsFill(self) -> List[int]:
        return [len(i.spread()) for i in self.arr]

    def __str__(self) -> str:
        return '{\n' + '\n'.join([str(i) for i in self.arr if i.head.nxt is not None]) + '\n}'
