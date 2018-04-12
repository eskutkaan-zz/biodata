from Bio import SeqIO
inputrc = input("Enter your .gb location:")
records = list(SeqIO.parse(inputrc, "gb"))
recordseq = records[0].seq
genome = str(recordseq)
kmers = {}
k = int(input("K size?:"))
for i in range(len(genome) - k + 1):
   kmer = genome[i:i+k]
   if kmer in kmers:
      kmers[kmer] += 1
   else:
      kmers[kmer] = 1
for kmer, count in kmers.items():
   print(kmer + "\t" + str(count))
a=sorted(kmers.values())
print([x-y for (x,y) in zip(a[1:],a[:-1])])
from collections import Counter
freq = Counter()
for i in range(len(genome) - k + 1):
   kmer = genome[i:i+k]
   freq.update([kmer])
input("enter")