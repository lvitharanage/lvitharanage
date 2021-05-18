# this scripy read through the mail box data and when it find line that starts
# with "From", it will split the line into words using the split function.
# we are interested in who sent the message, which is the second word on
# the "From" line.

fileHandle = open("mbox-short.txt")

emailcounter = 0
for line in fileHandle:
    line = line.rstrip()
    wds = line.split()
    # the try and except deals with issues caused by empty lists, which is
    # caused by running 'split' method on empty line.
    # An alternative/better way to handle this is using if fucntion which
    # has been used in version 2 ofthis script
    try:
        if wds[0] != 'From':
            continue
        else:
            print(wds[1])
            emailcounter = emailcounter + 1
    except Exception:
        pass
print(emailcounter, "Record/s Found")
