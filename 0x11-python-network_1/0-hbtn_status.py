#!/usr/bin/python3
"""
 a Python script that fetches https://intranet.hbtn.io/status
"""


import urllib.request as httpreq

if __name__ == "__main__":
    with httpreq.urlopen(" https://intranet.hbtn.io/status") as spot:
        spot_read = spot.read()
        print("Body Response:\n\t- type: {}\n\t- content: {}\n\t\
- utf8 content: {}".
              format(type(spot_read), spot_read, spot_read.decode("utf-8")))
