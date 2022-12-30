# A program that reads a file and capitalize all characters to uppercase

filepath = input('Filepath: ')

try:
    filehandler = open(filepath)
    for line in filehandler:
        print(line.upper())
except:
    print('Invalid Filepath:',filepath)
