# -*- coding: utf-8 -*-
# GC-content gives us a natural way to form a realistic random DNA string for a
# given species. If the GC-content is x, then we make the symbol frequencies of
# C and G equal to x/2 and set the symbol frequencies of A and T equal to 1−x/2.
# In other words, if the GC-content is 40%, then as we construct the string, we
# have a 20% chance of the next added symbol being 'C', a 20% chance that it is
# 'G', a 30% chance that it is 'A', and a 30% chance that it is 'T'.
#
# Given: An array A containing at most 20 real numbers between 0 and 1,
# inclusively.
#
# Return: An array B in which B[i] represents the probability (to an accuracy
# of three decimal places) that for the GC-content in A[i], two randomly chosen
# symbols will be the same.
#
# Sample Dataset
# 0.23 0.31 0.75
#
# Sample Output
# 0.322900 0.286100 0.312500

def prob(gc):
    g = c = gc / 2
    a = t = (1 - gc) / 2
    return g**2 + c**2 + a**2 + t**2

if __name__ == '__main__':
    data = [0.0, 0.067, 0.176, 0.207, 0.265, 0.338, 0.403, 0.465, 0.513, 0.534, 0.596, 0.657, 0.716, 0.802, 0.871, 0.884, 1.0]
    print ' '.join(str(prob(gc)) for gc in data)
