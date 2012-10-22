# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#
# Return: The ID of the string having the highest GC-content, followed by the
# GC-content of that string. The GC-content should have a precision of at least
# 2 decimal places.
# 
# Sample Dataset
# 
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT
# Sample Output
# 
# Rosalind_0808
# 60.919540%

from Bio import SeqIO
from Bio.SeqUtils import GC

def highest_GC_content(seq_records):
    record_id = ''
    gc_content = 0
    for seq_record in SeqIO.parse(seq_records, "fasta"):
        if GC(seq_record.seq) > gc_content:
            record_id = seq_record.id
            gc_content = GC(seq_record.seq)
    return '{0}\n{1}%'.format(record_id, gc_content)

if __name__ == '__main__':
    seq_records = r'.\data\GC.fa'
    print highest_GC_content(seq_records)
