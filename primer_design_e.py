import primer3
import os
import sys
id_of_seq = int(input("enter sequence id"))
descriptseq = str(input("description:"))
sequencecalc = str(input("enter your sequence to calculate Tm"))
print("Tm:")
Tmseq = primer3.calcTm(sequencecalc) 
print(Tmseq)
answ1 = str(input("design primers? y/n?"))
if answ1 == "n":
	sys.exit(0)
seq_inc_region = [int(x) for x in input("Included region:").split()]
primeroptsizerr = int(input("primer opt size:"))
primerpickintoligo = int(input("PRIMER_PICK_INTERNAL_OLIGO:"))
primerintmax = int(input("internal max self end:"))
primerminsize = int(input("primer minimum size:"))
primermaxsize = int(input("primer maximum size:"))
primeroptimaltm = float(input("primer optimal tm:"))
primermintm = float(input("primer minimum tm:"))
primermaxtm = float(input("primer maximum tm:"))
primermingc = float(input("primer min gc:"))
primermaxgc = float(input("primer max gc:"))
primermaxpoly = int(input("primer max polyx:"))
primerinternalmaxpoly = int(input("primer internal max polyx:"))
primersaltmonovalent = float(input("primer salt monovalent:"))
DNAconc = float(input("dna conc:"))
maxnsacc = int(input("max ns accepted:"))
maxsefany = int(input("max self any:"))
maxsefend = int(input("max self end:"))
primerpairmaxcomplany = int(input("PRIMER_PAIR_MAX_COMPL_ANY")) 
primerpairmaxcomplend = int(input("PRIMER_PAIR_MAX_COMPL_END")) 
the_sizes = []
howmanyrange = int(input("range sizes num:"))
for i in range(1,howmanyrange):
	listof = [int(x) for x in input("Size range:").split()]
	the_sizes.append(listof)
seqdict =  {
        'SEQUENCE_ID': str(id_of_seq),
        'SEQUENCE_TEMPLATE': str(sequencecalc),
        'SEQUENCE_INCLUDED_REGION': seq_inc_region
    },{
        'PRIMER_OPT_SIZE': primeroptsizerr,
        'PRIMER_PICK_INTERNAL_OLIGO': primerpickintoligo,
        'PRIMER_INTERNAL_MAX_SELF_END': primerintmax,
        'PRIMER_MIN_SIZE': primerminsize,
        'PRIMER_MAX_SIZE': primermaxsize,
        'PRIMER_OPT_TM': primeroptimaltm,
        'PRIMER_MIN_TM': primermintm,
        'PRIMER_MAX_TM': primermaxtm,
        'PRIMER_MIN_GC': primermingc,
        'PRIMER_MAX_GC': primermaxgc,
        'PRIMER_MAX_POLY_X': primermaxpoly,
        'PRIMER_INTERNAL_MAX_POLY_X': primerinternalmaxpoly,
        'PRIMER_SALT_MONOVALENT': primersaltmonovalent,
        'PRIMER_DNA_CONC': DNAconc,
        'PRIMER_MAX_NS_ACCEPTED': maxnsacc,
        'PRIMER_MAX_SELF_ANY': maxsefany,
        'PRIMER_MAX_SELF_END': maxsefend,
        'PRIMER_PAIR_MAX_COMPL_ANY': primerpairmaxcomplany,
        'PRIMER_PAIR_MAX_COMPL_END': primerpairmaxcomplend,
        'PRIMER_PRODUCT_SIZE_RANGE': the_sizes,
    }
with open('primer_design.txt', 'a') as the_file:
    the_file.write("Seq.ID:" + str(id_of_seq) + os.linesep)
    the_file.write("Desc:" + str(descriptseq) + os.linesep)
    the_file.write("Tm:" + str(Tmseq) + os.linesep)
    the_file.write("Primer3:" + str(seqdict) + os.linesep)

