#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
-You must use the package requests
-You are not allow to import packages other than requests
-The body of the response must be display like the following example
(tabulation before -)
"""

if __name__ == "__main__":
    import requests
    r = requests.get('https://intranet.hbtn.io/status')
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
