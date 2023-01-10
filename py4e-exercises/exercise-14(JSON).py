import urllib.request as fetch
import json


def exerciseJSON():
    api_url = input('Enter Location: ')

    print('Retrieving', api_url)
    end_point = fetch.urlopen(api_url)
    data = end_point.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        json_data = json.loads(data)
    except:
        json_data = None

    comments_dict = json_data['comments']

    number_of_counts = 0
    total_counts = 0

    for index in comments_dict:
        if 'count' in index:
            number_of_counts += 1
            total_counts += index['count']

    print('Count:', number_of_counts)
    print('Sum:', total_counts)


exerciseJSON()
