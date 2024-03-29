# Given two strings s and t of equal length, the Hamming distance between
# s and t, denoted dH(s,t), is the number of corresponding symbols that differ
# in s and t. See Figure 2.
# 
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#
# Return: The Hamming distance dH(s,t).
#
# Sample Dataset
#
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
#
# Sample Output
#
# 7

def dH(s, t):
    return sum(i != j for (i,j) in zip(s,t))

def hamm(data):
    with open(data) as f:
        lines = f.read().strip().split('\n')
        return dH(*lines)

if __name__ == '__main__':
    data = r'./data/HAMM.data'
    print hamm(data)
