# An RNA string is formed from the alphabet containing A, C, G, and U.
#
# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is
# formed by replacing all occurrences of T with U.
# 
# Given: A DNA string t of length at most 1000 nucleotides.
#
# Return: The transcribed RNA string of t.
# 
# Sample Dataset
# 
# GATGGAACTTGACTACGTAAATT
#
# Sample Output
# 
# GAUGGAACUUGACUACGUAAAUU

dna = "CCCCATGCCACTCCCACCGGTTGTAACATTTTCGGTTAACACTCCCTTGGCTCTATCATGGAGGCTTGTCCAGCTCGAGGAAATTCGCAGGTTTTCAGGATTCAGAAAGCTTCCCGGGTACTAACTGCTAATGCGCGATCTTGGCCCTGTGTAAGAAAATGTGAGGCTCCCCAGGGCCGTTAACCCCGCGTCGTCAGGCGTGCGCACTCTCAATACTCATCTTCTGTATTTGGACCTACTCGAATGAGGTTCACGAGTTTTTTGTTCGCGGCCGCAACCCGGTCCGCTCGTTGACCGAATACACGACCAGCTTGCCCCTGGGGCACTTTCGTCATCACAGCCTGGGGCCTTGGGAACCGTATCGCTGTCATAAAAGTAACGCTGGCTTGCAGACGGTCCACACAGGCCTCCAACAGCTATAAGCATTGTGATGGTGAAGTAATTTAGAAACCTCACGTTTTAGGCGACCTATTATCCGACGCCGATTCTACAGATCCGTCGACAGACCTTATGACTTAGCGTGCTGTCAGGCGTTCCAGACGGTATGGGGTAACAGCTGAAAGCACTTACATGCGGAGTCACTGGGGAACACAAATCTTGAGGGTGGAGCCGTATTGAGTGACGCGGGGCTGCAGGTGGACGCGCCTCAGATTTCAATCCACTATTCCGTTATATAGAGATTGGGGACCATGCAAAGTTTCGCATTTGAGGTCCTATCCCCCATAAATGGTATACAGCTAAATGCAGCGCCCACCGCGGGGTGATACCCTGGTATTGAAAGAACTACGGGGGAGTTAGCAGTATTAATCGTCACCTTCAAAGTGCGAAAAATCCTTACTACAAATGAGTCGCATCTTAATTTCGGTCGGAGCTCTGAATAACAGACTATGAGGTTTCAAACGCATTGCTACTCTTCTCGAAAGTTAATCAGGTGTGTCAGTGTGTTGCTCGTAGTCATGACGCACTGAGAAATC"

def transcribe(dna):
    return dna.replace('T', 'U')

print transcribe(dna)
