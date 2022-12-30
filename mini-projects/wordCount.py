print("Word Counter")
print("-------------------")
print("Choose From Menu:")
print("-------------------")
print("1.\100Write And Count")
print("2.\100Read And Count")
print("3.\100Exit")
print("-------------------")

def Menu(choice):
    if choice == 1:
        print('Writing And Counting')
    else:
        print('Reading And Counting')

while True:
    try:
        choice = int(input("Enter: "))
        if choice == 3:
            break
        elif choice == 1 or choice == 2:
            Menu(choice)
        else :
            print('Invalid Choice')

        useAgain = input('Try Again(Y/N): ')

        if useAgain == 'Y':
            continue
        else:
            break
        
    except:
        print('Numbers Only')