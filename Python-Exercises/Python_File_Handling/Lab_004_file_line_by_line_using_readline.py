# print line by line using readline method
file = open("file1.txt")
line = file.readline()

while line !=  "":
    print(line)
    line = file.readline()

file.close()