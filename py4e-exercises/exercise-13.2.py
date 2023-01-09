import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>John</name>
        </user>
        <user x="9">
            <id>007</id>
            <name>Doe</name>
        </user>
    </users>
</stuff>
'''


stuff = ET.fromstring(data)

users = stuff.findall('users/user')
print('User Count:', len(users))
print('-----------------------')

for user in users:
    print('Id:', user.find('name').text)
    print('Name:', user.find('name').text)
    print('Attribute:', user.get('x'))
    print('-----------------------')
