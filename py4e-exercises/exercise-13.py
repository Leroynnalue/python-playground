# XML Worked Exercise

import xml.etree.ElementTree as ET

data = '''
<Person>
    <name>Somtochukwu</name>
    <phone type="intl">
        +234 000 0000 000 
    </phone>
    <email hide="yes"/>
</Person>
'''

tree = ET.fromstring(data)

print('Name:', tree.find('name').text)
print('Phone:', tree.find('phone').text.strip())
print('Attr:', tree.find('email').get('hide'))
