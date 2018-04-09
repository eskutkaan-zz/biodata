import os
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "examle@example.com"
filename = input("Enter ID:")
if not os.path.isfile(filename):
    net_handle = Entrez.efetch(db="nucleotide", id="EU490707", rettype="gb", retmode="text")
    out_handle = open(filename, "w")
    out_handle.write(net_handle.read())
    out_handle.close()
    net_handle.close()
    print("Saved")
print("Parsing...")
record = SeqIO.read(filename, "genbank")
print(record)
print(record[0]["GBSeq_definition"])
print(record[0]["GBSeq_source"])
input("press <enter> to exit")
