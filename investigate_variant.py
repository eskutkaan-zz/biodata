file_object  = open("genestorage.txt", "r")
temp_fileobj = file_object.readlines()
for i in temp_fileobj:
	if i == '\n':
		temp_fileobj.remove(i)
indexofvrnt = input("investigating variant:") + "\n"
aavrnt= [i -2 for i,x in enumerate(temp_fileobj) if x == indexofvrnt]
print(aavrnt)
print("look at this positions for the IDs of patient that you are looking for")
print("related list <temp_fileobj>")
for i in aavrnt:
    print(temp_fileobj[i])
input("press <enter> to exit")
