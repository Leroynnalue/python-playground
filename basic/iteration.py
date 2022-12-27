target = 3
for index in range(5):
    if(index < target):
        print(index, "lesser than", target)
    elif index == target:
        print(index, "equal to", target)
    else:
        print(index, "greater than",target)