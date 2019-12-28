import os
from Bio.SeqUtils import GC
from Bio.SeqUtils import GC123
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
def mainloop():
	seq = input("Sequence 1:")
	seq2 = input("Sequence 2:")
	alignments = pairwise2.align.globalxx(seq, seq2)
	print(format_alignment(*alignments[0]))	
	print("No1.Total GC content:")
	print(GC(seq))
	print("No1.GC by parts:")
	print(GC123(seq))
	print("No2.Total GC content:")
	print(GC(seq2))
	print("No2.GC by parts:")
	print(GC123(seq2))
	input('next prot')
	cls = lambda: os.system('cls')
	cls()
	mainloop()
mainloop()
