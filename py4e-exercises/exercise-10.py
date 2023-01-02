# Sorting a dictionary using tuples

filename = input('Filename: ')

if len(filename) < 1:
    filename = 'clown.txt'

filehandler = open(filename)

dictionary = dict()


for line in filehandler:
    line = line.rstrip()
    words = line.split()

    for word in words:
        # retrieve / create/ update word counter
        dictionary[word] = dictionary.get(word,0) + 1


# Flipping Value For Key
reversedDict = dict()
for key , value in  dictionary.items():
    reversedDict[value] = reversedDict.get(value,key)

# print(reversedDict)

sortedTuple = sorted(reversedDict.items(),reverse=True)
# print(sortedTuple[:5])

# Flipping Back
for value , key in sortedTuple[:5]:
    print(key,value)