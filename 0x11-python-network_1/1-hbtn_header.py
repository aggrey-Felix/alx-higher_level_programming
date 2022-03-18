#!/usr/bin/python3
"""Takes in Url,send req to URl, displays value of x_request variable in heade
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv
    request = request.Request(argv[1])
    with request.urlopen(request)as response:
        print(response.headers.get('X-Request-Id'))
