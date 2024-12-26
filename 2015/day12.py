import json
import re
from datetime import datetime

start = datetime.now()

data = open(0).read()

print(sum(list(map(int, re.findall(r"-?\d+", data)))))


def recurse(obj):
    count = 0
    if type(obj) is list:
        for o in obj:
            count += recurse(o)
    elif type(obj) is dict:
        if "red" in obj.values():
            return count

        for _, v in obj.items():
            count += recurse(v)
    else:
        try:
            count += int(obj)
        except ValueError:
            pass

    return count


print(recurse(json.loads(data)))

print(f"took={datetime.now() - start}")
