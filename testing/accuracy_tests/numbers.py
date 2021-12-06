from hash_maps import Pair, DHashedMap, ChainedMap
from testing.maps_comparator import compare_insertion, compare_deleting


def nonCollisionTest(printing=True):
    N = 6
    data = [
        Pair(0, 0),
        Pair(8, None),
        Pair(9, 9),
        Pair(13, 'str'),
        Pair(16, 16),
        Pair(23, [1, 2, 3])
    ]
    cm = ChainedMap(N)
    dm = DHashedMap(N)
    pm = dict()
    compare_insertion(cm, dm, pm, data, printing)


def collisionTest(printing=True):
    N = 5
    data = [
        Pair(0, 0),
        Pair(8, None),
        Pair(6, 9),
        Pair(12, 'str'),
        Pair(1, 16),
        Pair(7, [1, 2, 3]),
        Pair(18, 18),
        Pair(14, None),
        Pair(20, 3.14),
        Pair(12, 'new_str')
    ]
    cm = ChainedMap(N)
    dm = DHashedMap(N)
    pm = dict()
    compare_insertion(cm, dm, pm, data, printing)


def deletingTest1(printing=True):
    N = 6
    data = [
        Pair(0, 0),
        Pair(8, None),
        Pair(9, 9),
        Pair(13, 'str'),
        Pair(16, 16),
        Pair(23, [1, 2, 3])
    ]
    cm = ChainedMap(N)
    dm = DHashedMap(N)
    pm = dict()
    compare_insertion(cm, dm, pm, data, False)
    compare_deleting(cm, dm, pm, [8, 13, 23], printing)


def deletingTest2(printing=True):
    N = 5
    data = [
        Pair(0, 0),
        Pair(8, None),
        Pair(6, 9),
        Pair(12, 'str'),
        Pair(1, 16),
        Pair(7, [1, 2, 3]),
        Pair(18, 18),
        Pair(14, None),
        Pair(20, 3.14),
        Pair(12, 'new_str')
    ]
    cm = ChainedMap(N)
    dm = DHashedMap(N)
    pm = dict()
    compare_insertion(cm, dm, pm, data, printing=False)
    compare_deleting(cm, dm, pm, [8, 12, 0, 14, 20], printing)


if __name__ == "__main__":
    print('Test with collisions:')
    nonCollisionTest()

    print('Test without collisions:')
    collisionTest()

    print('Deleting test 1:')
    deletingTest1()

    print('Deleting test 2:')
    deletingTest2()
