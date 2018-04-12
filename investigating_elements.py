from Bio import SeqIO
inputrc = input("Enter your .gb location:")
records = list(SeqIO.parse(inputrc, "gb"))
record = records[0]
record.seq
from collections import Counter
print(Counter([x.type for x in record.features]))
inputft = input("Which elements do you want?:")
aa= [x for x in record.features if x.type == inputft]
answw = input("Do you want to see locations? y/n ")
if answw == "y":
	for x in aa:
		print(x.location)
else:
	print("process completed")
i = int(input("Line number of what you want to look for?:"))
print(aa[i].location.extract(record))
print(aa[i].location.extract(record.seq))
input("enter")
