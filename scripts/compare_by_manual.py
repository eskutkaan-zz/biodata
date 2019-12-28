from Bio import pairwise2
from Bio.pairwise2 import format_alignment
seq = input("Sequence 1:")
seq2 = input("Sequence 2:")
alignments = pairwise2.align.globalxx(seq, seq2)
print(format_alignment(*alignments[0]))
input("enter")
