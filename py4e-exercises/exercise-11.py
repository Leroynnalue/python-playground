import re

filename = input('Filename: ')

if len(filename) < 1:
    filename = 'regex_one.txt'

filehandler = open(filename)


numbers = list()

lineNumbers = re.findall('[0-9]+',filehandler.read())
numbers = numbers + lineNumbers

total = 0

for number in numbers:
    number = int(number)
    total += number


print(total)