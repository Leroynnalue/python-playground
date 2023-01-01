occurrence = {'james':1,'stephen':2,'jacob':3}

# Iterating through a dictionary
for key in occurrence:
    print(key , ":", occurrence[key])

# Two Iteration Variables
for key,value in occurrence.items():
    print(key,value)

# dict().items() is a method that gives the key and value pair