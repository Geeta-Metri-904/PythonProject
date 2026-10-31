# print line by line using readline method
file = open("file1.txt")

for line in file.readlines():# each line stored in list
    print(line)

file.close()