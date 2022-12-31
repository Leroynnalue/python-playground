# Open the file mbox.txt and read it line by line. When you find a line that starts with 'From ' like the following line:

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.

# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.


filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"

filehandler = open(filename)
count = 0

for line in filehandler:
    line.rstrip()
    if line.startswith('From') and not line.startswith('From:') :
        wordList = line.split()
        print(wordList[1])
        count += 1
    else:
        continue

print("There were", count, "lines in the file with From as the first word")