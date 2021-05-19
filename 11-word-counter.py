""" This script reads through a mail log and built a histogram
using  a dictionary to count how many messages have come from
each email address. It also prints email address and number of
messages for the email address with highest number of messages"""

email_counter = dict()
file_name = open(input('Please enter file name:'))

""" this code block reads the file line by line and then build a
dictionary where a key is created for each new email and update
the value field if a email already exist"""
for line in file_name:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1 or wds[0] != 'From':
        continue
    email = wds[1]
    email_counter[email] = email_counter.get(email, 0) + 1
    """ print(email, email_counter[email]) can be used to
    print key and value pair as it loops through"""
print(email_counter)

""" First method of finding and printing email with
highest number of messages"""
value_before = 0
maximum_value = ('string', 0)
for key, value in email_counter.items():
    value_before = key, value
    if value_before[1] > maximum_value[1]:
        maximum_value = value_before
print(maximum_value[0], maximum_value[1])

""" Second method of finding and printing email with
highest number of messages, this is better method as it uses
None value"""
big_email = None
big_email_value = None
for key, value in email_counter.items():
    if big_email_value is None or value > big_email_value:
        big_email = key
        big_email_value = value

print(big_email, big_email_value)
