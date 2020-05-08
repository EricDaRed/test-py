import math
import os
import sys

import requests

# print(sys.version)
print(sys.executable)


def greet(person):
    greeting = 'Hello, {}'.format(person)
    return greeting


r = requests.get('https://google.com')
print(r.status_code)
