# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.


filepath = input("Enter file name: ")
filehandler = open(filepath)
total = 0
count = 0
average = 0

for line in filehandler:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    first_number = line.find('0')
    numbers = float(line[first_number:])
    total += numbers
    count += 1

average = total / count
print("Average:",average)
