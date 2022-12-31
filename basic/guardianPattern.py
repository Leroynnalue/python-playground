handle = open('../py4e-exercises\mbox.txt')

for line in handle:
    line = line.rstrip()
    words = line.split()
    # guardian in a compound statement
    if len(words) < 3 or words[0] != 'From' : continue
    print(words[2])