import os

# loops
# indefinite loop (while)
condition = True
iterationNumber = 0

while(condition):
    iterationNumber += 1
    print(iterationNumber)
    if(iterationNumber == 5):
        print("Existing")
        condition = False

os.system('cls')

# definite loop
friends = ["Somtochukwu", "Samuel", "Olamide", "Kingsley"]

for friend in friends:
    print("Season Greeting:",friend)

print("Much Love")