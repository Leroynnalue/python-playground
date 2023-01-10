# URL does't return address details, due to the fact you need an AUTH KEY to access API_RESOURCE.

import json
import urllib.request as fetch
import urllib.parse

service_url = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input('Enter Location: ')
    if len(address) < 1:
        break

    api_url = service_url + urllib.parse({
        'address': address
    })

    print('Retrieving', api_url)
    end_point_handler = fetch.urlopen(api_url)
    data = end_point_handler.read().decode()

    # decode() - converts UTF-8 to Unicode

    print('Retrieved', len(data), 'characters')

    try:
        json_data = json.loads(data)
    except:
        json_data = None

    if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
        print('=== Failure ===')
        print(data)
        continue
