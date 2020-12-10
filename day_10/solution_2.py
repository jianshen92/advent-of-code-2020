import collections
from typing import List

with open("data", "r") as f:
    data = f.read().splitlines()


l1 = [int(item) for item in data]
l1.sort()
l0 = [0]
l0.extend(l1.copy())
l0.pop()

difference = [post - pre for pre, post in zip(l0, l1)]

multiplier = 1
ones = 0

paths = 0


def perm(inputs: List[int]) -> int:

    tree = collections.defaultdict(list)
    for num in inputs:
        for i in range(1, 4):
            if (num + i) in inputs:
                tree[num].append(num + i)

    def travel_next(current):
        global paths

        if current not in tree:
            paths += 1
            return paths

        for next_item in tree[current]:
            travel_next(next_item)

    travel_next(inputs[0])
    return paths


for item in difference:
    if item == 1:
        ones += 1
        continue

    if item == 3 and ones != 0:
        multiplier *= perm([i for i in range(ones + 1)])
        paths = 0
        ones = 0

multiplier *= perm([i for i in range(ones + 1)])
print(multiplier)
