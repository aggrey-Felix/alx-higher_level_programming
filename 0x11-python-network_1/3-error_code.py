#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the body
the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import urllib.error
    import urllib.request
    import sys
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
