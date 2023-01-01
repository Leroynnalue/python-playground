filename = input('Filename: ')

if len(filename) < 1 : filename = 'clown.txt'

handle = open(filename)

dictionary = dict()

# Word Occurrence To Dictionary

for line in handle:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)

    for word in words:
        dictionary[word] = dictionary.get(word,0) + 1


print(dictionary)

# Find Most Common Word And It's Count

largest = -1
theword = None

for key,value in dictionary.items():
    # print(key,value)
    if value > largest :
        largest = value
        theword = key
    
print('Done(Word):',theword)
print('Done(Count):',largest)

