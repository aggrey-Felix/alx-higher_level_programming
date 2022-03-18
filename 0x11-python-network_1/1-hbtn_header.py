#!/usr/bin/python3
"""Takes in Url,send req to URl, displays value of x_request variable in heade
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
