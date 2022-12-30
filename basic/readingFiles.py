# Open Method open(filename,mode) // mode(r) - read and mode(w) - write

# Read() // Reads the entire file
filename = input('Filename: ')
filehandler = open(filename)
fileContent = filehandler.read()
print(fileContent)