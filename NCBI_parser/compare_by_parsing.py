from Bio import Entrez
from Bio import SeqIO
Entrez.email = "example@example.com"
idn = input("Enter ID:")
handle = Entrez.efetch(db="nucleotide", id = idn, rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
idnT = input("Enter ID:")
handlet = Entrez.efetch(db="nucleotide", id = idnT, rettype="gb", retmode="text")
record2 = SeqIO.read(handlet, "genbank")
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
seq = record.seq.tostring()
seq2 = record2.seq.tostring()
alignments = pairwise2.align.globalxx(seq, seq2)
print(format_alignment(*alignments[0]))
input("enter")
