from hash_maps import Pair, DHashedMap, ChainedMap
from maps_comparator import compare
import random

N1 = 100
data1 = [Pair(random.randint(0, 1_000), i) for i in range(N1)]

N2 = 100_000
data2 = [Pair(random.randint(0, 1_000_000), i) for i in range(N2)]

if __name__ == "__main__":
    print("Random test 1:")
    compare(data1, N1)

    print("Random test 2:")
    compare(data2, N2, printing=False)
