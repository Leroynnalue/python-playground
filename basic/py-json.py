# Using python and json
import json

# using a json file in parent directory
data = '''
{
  "name": "John Doe",
  "phone": {
    "type": "intl",
    "number": "+234 000 0000 000"
  },
  "email": {
    "hide": "yes"
  }
}
'''

# creating an object of our json file
information = json.loads(data)

# scanning through our data
print('Name:', information['name'])
print('Hide:', information['email']['hide'])
