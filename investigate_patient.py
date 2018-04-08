file_object  = open("genestorage.txt", "r")
temp_fileobj = file_object.readlines()
indexofptt = "Pt.ID:" + input("investigating patient:") + "\n"
aavv= [i + 3 for i,x in enumerate(temp_fileobj) if x == indexofptt]
for i in range(1, len(aavv)):
    aavv[i] = aavv[i] + 1
print(aavv)
print("look at this positions for the variants of patient that you are looking for")
print("related list <temp_fileobj>")
for i in aavv:
    print(temp_fileobj[i])
input("press <enter> to exit")

