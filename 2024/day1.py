from datetime import datetime

start = datetime.now()

input = open(0).read().splitlines()

list1, list2 = [], []
for line in input:
    ints = line.split("   ")
    list1.append(int(ints[0]))
    list2.append(int(ints[1]))

list1 = sorted(list1)
list2 = sorted(list2)

print(sum(abs(list1[i] - list2[i]) for i in range(len(list1))))

print(sum(list1[i] * list2.count(list1[i]) for i in range(len(list1))))

print(f"took={datetime.now() - start}")
