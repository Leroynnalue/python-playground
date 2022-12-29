text = "Hello World"

# Slicing Strings
def subscripts():
    sliceOne = text[:6]
    sliceTwo = text[6:]
    print(sliceOne)
    print(sliceTwo)

# Looping Through String
def loopingStrings():
    count = 0
    for letter in text:
        count += 1
        print(letter,count)

# String Methods
def stringMethods():
    # Len Method (returns the number of characters in a string)
    lengthOfString = len(text)
    print("Length:" , lengthOfString)

    # Lower Method (returns the lowercase form of the string)
    lowerForm = text.lower()
    print("Lowercase of(", text , "):", lowerForm)

    # Upper Method (returns the uppercase form of the string)
    upperForm = text.upper()
    print("Lowercase of(", text , "):", upperForm)

    # Find Method (returns the subscript of the character in the string)
    character = 'W'
    position = text.find(character)
    print("Position of(", character , ") :" , position)

    # Replace Method (searches for characters(s) in a string and replaces them with  specified characters(s))
    byeWorld = text.replace('Hello','Bye')
    print(byeWorld)

    # lstrip(), rstrip(), strip() // Strips Whitespaces from strings (could be from the right or left or both sides)

    # startswith() // returns a boolean value

# Simple String Work
def parseExt():
    details = "From: somtochukukwu@aptech.ng.wa (Thr 29 13:33:30 2022)"
    at_pos = details.find("@")
    space_pos = details.find(" ",at_pos)
    host = details[at_pos+1:space_pos]
    print(host)



# Order Of Method Execution

# loopingStrings()
# subscripts()
# stringMethods()
# parseExt()
