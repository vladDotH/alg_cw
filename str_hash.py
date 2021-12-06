from hash_maps import nextPrime

K = 37
P = nextPrime(2 ** 32)


def str_hash(s: str, k: int = K, p: int = P) -> int:
    h = 0
    for i in s:
        h = (h * k + ord(i)) % p
    return h
