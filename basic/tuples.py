# numbers = (1,2,3,4,5)
# or
numbers = tuple((1,2,3,4,5))

# Iterating a tuple
# for number in numbers:
    # print(number)


# Tuples Method
# print("Count()",numbers.count(1))
# print("index()",numbers.index(1))

# Tuples and assignment
(numberone, numberTwo) = (200, 400)
(stringOne, stringTwo) = ('Bat', 'Cat')
# print(numberone)
# print(numberTwo)
# print(stringOne)
# print(stringTwo)


# Tuples and dictionaries
sendersMessageCount = {
    'abc@yah.com': 100,
    'gji@def.com': 21,
    'xyz@fer.com': 43,
}

sendersTuple = sendersMessageCount.items() # returns a dictionary value into a list of tuple(s).
# print(sendersTuple)


# Sorted Method
unsortedNumbers = {
    "b": 2,
    "c": 3,
    "a": 1,
    "d": 4,
    "e": 5,
}

sortedNumbers = sorted(unsortedNumbers.items())
reversedSortedNumbers = sorted(unsortedNumbers.items(), reverse=True)

print("Unsorted:",unsortedNumbers)
print("Sorted:",sortedNumbers)
print("Reversed Sorted:",reversedSortedNumbers)


for key, value in sortedNumbers:
    print(key,value)