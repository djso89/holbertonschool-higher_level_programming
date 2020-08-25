#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    email = argv[2]
    values ={'email': email}
    r = requests.post(url, data=values)
    print(r.text)
