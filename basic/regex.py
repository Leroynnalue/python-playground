# importing regular expression
import re
import enum


# Regular Expression Method

# Findall
words = 'My 2 favorite numbers are 6 and 10'
test = '[0-9]+'
wordMod = re.findall(test, words)

print(wordMod)