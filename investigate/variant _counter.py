from collections import Counter
file_object  = open("genestorage.txt", "r")
temp_fileobj = file_object.readlines()
cnt = Counter()
for i in temp_fileobj:
    cnt[i] += 1
print(cnt)
input("press <enter> to exit")

