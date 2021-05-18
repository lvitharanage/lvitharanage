# The script open the file romeo.txt and read it line by line.
# Each line is added into a list of words using the split function.
# each word is checked against the list and if the word is not in the list,
# it is add to the list.  At the tend list is sorted and printed
# in alphabetical order.

romeoText = open("romeo.txt")
# creatng a list to append words to
outputList = []
# iterating through each line in romeoText to read the lines
for line in romeoText:
    line = line.rstrip()
    words = line.split()
    # iterating trhough each word within the lines and checking to see if
    # the word is already on the outputList before appending.
    for word in words:
        if word not in outputList:
            outputList.append(word)
# sorting the output list before printng on screen
outputList.sort()
print(outputList)
