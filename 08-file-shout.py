# this script through a file and print the contents of
# the file (line by line) all in upper case.

fHandle = open("mbox-short.txt")

for line in fHandle:
    line = line.rstrip()
    print(line.upper())
