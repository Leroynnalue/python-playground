# Creating a web browser using url library (urllib)
import urllib.request

url = 'http://data.pr4e.org/romeo.txt'
datahandler = urllib.request.urlopen(url)

for line in datahandler:
    print(line.decode().strip())