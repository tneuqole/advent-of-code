from collections import defaultdict
from datetime import datetime

start = datetime.now()

nums = list(map(int, open(0).read().splitlines()))

P = 16777216
N = 2000

ans1 = 0
prices = defaultdict(list)
for n in nums:
    prices[n].append(n % 10)
    num = n
    for _ in range(N):
        num = (num ^ (num * 64)) % P
        num = (num ^ (num // 32)) % P
        num = (num ^ (num * 2048)) % P
        prices[n].append(num % 10)

    ans1 += num

print(ans1)

seqs = {}
for n, p_list in prices.items():
    seqs[n] = defaultdict(list)
    seq = []
    for i in range(1, len(p_list)):
        seq.append(p_list[i] - p_list[i - 1])
        if len(seq) < 4:
            continue

        seqs[n][tuple(seq)].append(p_list[i])
        seq.pop(0)

final = defaultdict(int)
for n, s_list in seqs.items():
    for s, p_list in s_list.items():
        final[s] += p_list[0]

print(max(final.items(), key=lambda x: x[1])[1])

print(f"took={datetime.now() - start}")
