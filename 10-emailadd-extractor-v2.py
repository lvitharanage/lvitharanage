# this scripy read through the mail box data and when it find line that starts
# with "From", it will split the line into words using the split function.
# we are interested in who sent the message, which is the second word on
# the "From" line.

fileHandle = open("mbox-short.txt")

emailcounter = 0
for line in fileHandle:
    line = line.rstrip()
    wds = line.split()
    # if statments have been used to filter out empty lists (guardian line) and
    # lists that does not contain the word 'From' at the begining.
    # this line could be written "if len(wds) < 1 or wds != 'From':"
    # (guardian in compund statement).
    # it is important to not that len < 1 condition must be first #
    # as error is created when checking for != 'From' condition in empty list
    if len(wds) < 1:
        continue
    if wds[0] != 'From':
        continue
    print(wds[1])
    emailcounter = emailcounter + 1

print(emailcounter, "Record/s Found")
