#  Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

filename = input('Filename: ')

if len(filename) < 1: filename = 'mbox.txt'

filehandler = open(filename)

emails = list()
email_dictionary = dict()

for line in filehandler:
    if line.startswith('From ') and not line.startswith('From:'):
        words = line.split()
        emails.append(words[1])

        for email in emails:
            email_dictionary[email] = email_dictionary.get(email,0) + 1

    continue

Occurrence = 0
Email = None

for key , value in email_dictionary.items():
    if email_dictionary[key] > Occurrence:
        Email = key
        Occurrence = email_dictionary[key]

# print(Email,Occurrence)