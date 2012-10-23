# -*- coding: utf-8 -*-
# A permutation of length n is some ordering of the positive integers
# {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.
#
# Given: A positive integer n≤7.
#
# Return: The total number of permutations of length n, followed by a
# list of all such permutations (in any order).

import itertools

def perm(n):
    perms = list(itertools.permutations(range(1,n+1)))
    return str(len(perms)) + '\n' + \
           '\n'.join([' '.join(map(str, p)) for p in perms])

if __name__ == '__main__':
    with open(r'./data/PERM.out', 'w') as f:
        f.write(perm(7))
