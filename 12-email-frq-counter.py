""" This script reads through a mail log and built a histogram
using  a dictionary to count how many messages have come from
each email address.

After all the data has been read, script prints the person
with the most emails by creating a list of (count, email)
tuples from the dictionary."""

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
# print(email_counter)

''' This section iterrate throuh the dictionary key and the value
and append them to a email_list_tup (tupple) in reverse order.
This is then appended to the email_list (list) and sorted in reverse
order to get the highest number of emails.
'''
email_list = list()
for key, val in email_counter.items():
    email_list_tup = (val, key)
    email_list.append(email_list_tup)
    email_list = sorted(email_list, reverse=True)

top_email = list(email_list[0])
print("Top emailer raw output:", email_list[0])
print("Email address for top emailer:", top_email[1], "¦",
      "Number of emails sent:", top_email[0])

''' This is a list comprehnsion code that does the same as above
with single line of code'''
print(sorted([(v, k) for k, v in email_counter.items()], reverse=True)[0])
