# Calculating a user's electricity bill
try:
    hours = int(input("Enter Hour(s): "))
    rate = float(input("Enter Rate: "))
    if(hours > 40):
        rate = rate * 1.5
    pay = float((hours * rate))
    print("Pay:",pay)
except:
    print("Please enter a number")

