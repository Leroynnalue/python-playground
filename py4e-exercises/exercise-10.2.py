#  Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


filename = input('Filename: ')

if len(filename) < 1:
    filename = 'mbox.txt'

filehandler = open(filename)


timeCount = dict()

for line in filehandler:
    if line.startswith('From ') and not line.startswith('From:'):
        line = line.rstrip()
        words = line.split()

        time = words[5]
        # print(time)

        time_section = time.split(':')
        hour = time_section[0]
        #print(hour)

        # Check for hour and increase count if found
        timeCount[hour] = timeCount.get(hour, 0) + 1

    else:
        continue

print(timeCount)

# Sorting Time Count
sortedTable = sorted(timeCount.items())

# Iterating Through Timecount
for key , value in sortedTable:
    print(key,value)