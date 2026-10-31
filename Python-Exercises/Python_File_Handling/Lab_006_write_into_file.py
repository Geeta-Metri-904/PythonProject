# no need to close the file when we use with
# with open('file1.txt', "r") as file: read file
# with open('file1.txt', "w") as file: write to file

# read the file and store all the lines in list
# reverse the list
# write the list back to the file

with open('file1.txt', "r") as reader:
    content = reader.readlines() # list
    reversed(content) # this method reverses the content
    with open('file2.txt', "w") as writer:
        for line in reversed(content):
            writer.write(line)

