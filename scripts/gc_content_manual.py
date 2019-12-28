from Bio.SeqUtils import GC
from Bio.SeqUtils import GC123
seq = input(str("DNA manual:"))
print("Total GC content:")
print(GC(seq))
print("GC by parts:")
print(GC123(seq))
input("enter")
