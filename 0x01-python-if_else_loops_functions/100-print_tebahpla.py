#!/usr/bin/python3
for c in reversed(range(97, 123)):
    if (c % 2 == 0):
        print('{:c}'.format(i), end='')
    else:
        print('{:c}'.format(i - 32), end='')
