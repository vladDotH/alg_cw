class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f'( {self.key} : {self.value} )'

    def __repr__(self):
        return str(self)


def defautlHash(hm, key):
    return hash(key)


class HashMap:
    def __init__(self, size: int, hashFunc=defautlHash):
        self.hashFunc = hashFunc
        self.arr = [None] * size
        self._itemsSize: int = 0

    def mapSize(self) -> int:
        return len(self.arr)

    def itemsSize(self) -> int:
        return self._itemsSize

    def fillCoef(self) -> float:
        return self.itemsSize() / self.mapSize()

    def calcHash(self, key) -> int:
        pass

    def insert(self, obj: Pair) -> bool:
        pass

    def get(self, key):
        pass

    def remove(self, key) -> bool:
        pass

    def refresh(self):
        pass

    def keyset(self) -> list:
        pass

    def expand(self, add: int):
        self.arr.extend([None] * add)

    def __str__(self) -> str:
        return '{\n' + '\n'.join([str(i) for i in self.arr]) + '\n}'

    def __repr__(self):
        return str(self)
