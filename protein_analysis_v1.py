from Bio.SeqUtils.ProtParam import ProteinAnalysis
my_seq = str(input("manual sequence from translate.py :"))
analysed_seq = ProteinAnalysis(my_seq)
answer1 = str(input("detect molecular weight y/n? :"))
if answer1 == "y":
    mweight = analysed_seq.molecular_weight()
    print(mweight)
answer2 = str(input("detect gravy y/n? :"))
if answer2 == "y":
    gravy_protein = analysed_seq.gravy()
    print(gravy_protein)
print(analysed_seq.count_amino_acids())
input("enter")
