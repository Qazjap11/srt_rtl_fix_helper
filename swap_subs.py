#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

subs = open(sys.argv[1], 'rb').read().decode('utf-8')

def map_subs(subs):
    is_new = True
    m = []
    for l in subs.split("\n"):
        if is_new:
            m += [[l]]
            is_new = False
        else:
            if l == '':
                is_new = True
            else:
                m[-1] += [l]
    return m

def replace_map(m, w):
    is_new = True
    wm = []
    for l in w.split("\n"):
        if is_new:
            wm += [[l]]
            is_new = False
        else:
            if l == '':
                is_new = True
            else:
                wm[-1] += [l]

    for i in xrange(len(m)):
        m[i][2:] = wm[i]
    print_map(m, True)

def print_map(m, all=False):
    for l in m:
        print '\n'.join(l[2 if not all else 0:]).encode('utf-8')
        print

def main():
    m = map_subs(subs)
    if sys.argv[2] == 'map':
        print_map(m)
    elif sys.argv[2] == 'replace':
        w = open(sys.argv[3], 'rb').read().decode('utf-8')
        replace_map(m, w)

if __name__ == '__main__':
    main()
