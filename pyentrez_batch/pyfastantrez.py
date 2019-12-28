from Bio import Entrez
from Bio import SeqIO

Entrez.email = "example@example.com"
ids = ["6273291","6273290"]
def batch_entrez():
    for i in range(0,len(ids)):
        with Entrez.efetch(
            db="nucleotide", rettype="fasta", retmode="text", id=ids[i]
            ) as handle:
            seq_record = SeqIO.read(handle, "fasta")
            print("%s with %i features" % (seq_record.id, len(seq_record.features)))
            SeqIO.write(seq_record, (str(ids[i]) + '.fasta'), "fasta")
