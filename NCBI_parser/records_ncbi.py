from Bio import Entrez
from Bio import SeqIO
Entrez.email = "example@example.com"
idn = input("Enter ID:")
handle = Entrez.efetch(db="nucleotide", id = idn, rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
print("Record ID:")
print(record.id)
print("Record name:")
print(record.name)
print("Record description:")
print(record.description)
print("Length of record:")
print(len(record.features))
print(repr(record.seq))
print("Sequence:")
print(record.seq)
input("press <enter> to exit")