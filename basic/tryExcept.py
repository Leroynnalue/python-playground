prompt = "What is the air velocity of an unladen swallow?\n"
try:
    speed = input(prompt)
    speed = int(speed)
except:
    print("Please enter a number")

print("Your Guess:", speed)
