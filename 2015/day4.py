import hashlib
from datetime import datetime
from pprint import pprint

start = datetime.now()


data = open(0).read().strip()
pprint(data)


def calc(prefix):
    i = 1
    while True:
        if hashlib.md5(f"{data}{i}".encode()).hexdigest().startswith(prefix):
            print(i)
            break
        i += 1


calc("00000")
calc("000000")

print(f"took={datetime.now() - start}")
