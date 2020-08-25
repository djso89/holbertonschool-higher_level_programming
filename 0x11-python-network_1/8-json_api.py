#!/usr/bin/python3
"""
Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    if len(argv) < 2:
        tkn = ""
    else:
        tkn = argv[1]

    vals = {'q': tkn}

    r = requests.post('http://0.0.0.0:5000/search_user', data=vals)
    try:
        j_dict = r.json()
        if j_dict == {}:
            print('No result')
        else:
            print('[{}] {}'.format(j_dict['id'], j_dict['name']))
    except ValueError:
        print('Not a valid JSON')
