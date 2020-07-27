ALPHABET_MAP = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
DEFAULT_BLOCK_SIZE = 24
MIN_LENGTH = 5

block_size = DEFAULT_BLOCK_SIZE
mask = (1 << block_size) - 1
mapping = range(block_size)


def encode_id( n, min_length=MIN_LENGTH):
    # Convert int into base62
    base62_int = (n & ~mask) | base62_encode(n & mask)
    # Map to Alphabet
    return enbase(base62_int, min_length)


def base62_encode( n):
    result = 0
    for i, b in enumerate(reversed(mapping)):
        if n & (1 << i):
            result |= (1 << b)
    return result


def enbase( x, min_length=MIN_LENGTH):
    result = _enbase(x)
    padding = ALPHABET_MAP[0] * (min_length - len(result))
    return '%s%s' % (padding, result)


def _enbase( x):
    n = len(ALPHABET_MAP)
    if x < n:
        return ALPHABET_MAP[x]
    return _enbase(int(x // n)) + ALPHABET_MAP[int(x % n)]
