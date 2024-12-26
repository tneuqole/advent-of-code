from datetime import datetime

start = datetime.now()


def recurse(s):
    count = 0
    if "\\\\" in s:
        count += sum(recurse(ss) for ss in s.split("\\\\")) + s.count("\\\\")
    elif "\\x" in s:
        count += sum(recurse(ss) for ss in s.split("\\x")) - s.count("\\x")
    elif "\\" in s:
        count += sum(recurse(ss) for ss in s.split("\\"))
    else:
        count = len(s)

    return count


s_len, ch_len, e_len = 0, 0, 0
for s in open(0).read().splitlines():
    s_len += len(s)
    ch_len += recurse(s[1:-1])

    e_len += len(s) + s.count("\\") + s.count('"') + 2

print(s_len - ch_len)
print(e_len - s_len)

print(f"took={datetime.now() - start}")
