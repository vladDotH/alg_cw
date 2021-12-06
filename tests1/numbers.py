from hash_maps import Pair, DHashedMap, ChainedMap
from tests1.maps_comparator import compare

N1 = 6
dataNonCollision = [
    Pair(0, 0),
    Pair(8, None),
    Pair(9, 9),
    Pair(13, 'str'),
    Pair(16, 16),
    Pair(23, [1, 2, 3])
]

N2 = 5
dataCollision = [
    Pair(0, 0),
    Pair(8, None),
    Pair(6, 9),
    Pair(12, 'str'),
    Pair(1, 16),
    Pair(7, [1, 2, 3]),
    Pair(18, 18),
    Pair(14, None),
    Pair(20, 3.14)
]

if __name__ == "__main__":
    print("Test without collisions:")
    compare(dataNonCollision, N1)
    print('-' * 50)
    print("Test with collisions:")
    compare(dataCollision, N2)
