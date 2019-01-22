#!/usr/bin/python2
from itertools import product
for combo in product('abcdefghijklmnopqrstuvwxyz234567', repeat=16):
    onion = ''.join(combo)
    onion = onion + ".onion"
    print "%s" % (onion)
