import datetime
import random
import os

STORAGE_PATH='/tmp'
FILENAME_PATTERN='unique_key-%s.list'

def to_base(num, base, numerals='0123456789abcdefghijklmnopqrstuvwxyz'):
    assert int(num)
    assert int(base)
    if len(numerals) < base < 1:
        raise ValueError("str_base: base must be between 1 and %i" % len(numerals))

    if num == 0:
        return '0'

    if num < 0:
        sign = '-'
        num = -num
    else:
        sign = ''

    if base == 1:
        return sign + ('1'*num)

    result = ''
    while num:
        result = numerals[num % (base)] + result
        num //= base

    return sign + result

def baseNgenerator(base=10, keylength=5, step=1):
    assert int(base) <= 36
    assert int(keylength) > 0
    while 1:
        yield to_base(random.randrange(base**(keylength-1), base**keylength), base)

def generate_keys(generator, amount=50):
    generator = baseNgenerator(base=36)
    keys = set(generator.next() for i in range(amount))
    return tuple(keys)

