# An Empty List
names = ['John','Doe','Foo']

# Length of a list
Length = len(names)
print('Length:',Length)

# Using The Range Function
Range = range(Length)
print(Range)

# Iterating a list
for name in names:
    print("Name:",name)


# Iterating with the range function
for index in Range:
    name = names[index]
    print("Range(Name):",name)


# Concatenating Lists
friends = ['Samuel','John','James']
friend_names = names + friends
print("Concatenated:",friend_names)


# Slicing Lists
firstThree = friend_names[0:3]
print("First Three:",firstThree)


# List Methods
# Empty List
first_names = list()
# append method
first_names.append('Jackson')
first_names.append('Simpson')
first_names.append('Traversy')
print(first_names)

# in keyword in list
cond_one = 'Jackson' in first_names
cond_two = 'James' not in first_names
print('Condition One:',cond_one,'\nCondition Two:',cond_two,)


# sort method
names.sort()
print("Sorted:",names)

# split method
string = 'My name is somtochukwu'
usernames = 'somtodev;johndoe;admin'
wordList = string.split()
userList = usernames.split(';')
print("Splitted List:",wordList)
print("Splitted List:",userList)