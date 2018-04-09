file_object  = open("genestorage.txt", "r")
temp_fileobj = file_object.readlines()
for i in temp_fileobj:
	if i == '\n':
		temp_fileobj.remove(i)
indexofptt = "Pt.ID:" + input("investigating patient:") + "\n"
aavv= [i + 2 for i,x in enumerate(temp_fileobj) if x == indexofptt]
print(aavv)
print("look at this positions for the variants of patient that you are looking for")
print("related list <temp_fileobj>")
for i in aavv:
    print(temp_fileobj[i])
print(temp_fileobj)
input("press <enter> to exit")

