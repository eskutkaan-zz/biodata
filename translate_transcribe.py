from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import generic_dna
fasta_sample = str(input("enter fasta file location:"))
for record in SeqIO.parse(fasta_sample, "fasta"):
    print(record.id)
sequence_sample = record.seq
print("you can see dna.complement and dna.reverse_complement")
giveans1 = str(input("Do you want to transcribe y/n?:"))
if giveans1 == "y":
    rna_sample = sequence_sample.transcribe()
    print(rna_sample)
else:
    print("continuing..")
print("you can .back_transcribe")
giveans2 = str(input("Do you want to translate y/n?:"))
if giveans2 == "y":
    translated = sequence_sample.translate()
    print(translated)
input("enter")
