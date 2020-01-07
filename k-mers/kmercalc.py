from Bio import SeqIO
# from collections import Counter
import os
kmers = {}
def main():
    records = list(SeqIO.parse('inputfile', "fasta"))
    recordseq = records[0].seq
    genome = str(recordseq)
    k = int(input("K size?:"))
    for i in range(len(genome) - k + 1):
       kmer = genome[i:i+k]
       if kmer in kmers:
          kmers[kmer] += 1
       else:
          kmers[kmer] = 1
    f = open('k-mers.kaan','w')
    for kmer, count in kmers.items():
        f.writelines(kmer + "\t" + str(count) + '\n')
        print(kmer + "\t" + str(count))
    f.close()
    return(kmers)
        #a=sorted(kmers.values())
        #print([x-y for (x,y) in zip(a[1:],a[:-1])])
        #freq = Counter()
        #for i in range(len(genome) - k + 1):
         #  kmer = genome[i:i+k]
          # freq.update([kmer])
        #return(kmers)
