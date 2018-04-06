import os
print("Hello There!")
patient_id = input("Enter patient id:")
name = input("Name of gene:")
number = input("chromosome location:")
mapofv = input("map of variant:")
def generate_id(name_gene = name, number_chr = number, map_v = mapofv):
    ans = name_gene[0] + name_gene[1] + number_chr[0] + number_chr[1] + map_v
    print(ans)
    return(ans)
def descript(name_gene = name, number_chr = number, map_v = mapofv):
    ans = name_gene + "." + number_chr + "." + map_v
    print(ans)
    return(ans)
print("gene id;")
the_id = generate_id()
the_descript = descript()
input("Press <enter> to exit")
with open('genestorage.txt', 'a') as the_file:
    the_file.write("Pt.ID:" + patient_id + os.linesep)
    the_file.write("ID:" + the_id + os.linesep)
    the_file.write(the_descript + os.linesep)





