import collections

with open("data", "r") as f:
    data = f.read().splitlines()


l1 = [int(item) for item in data]
l1.sort()
l0 = [0]
l0.extend(l1.copy())
l0.pop()

difference = [post - pre for pre, post in zip(l0, l1)]
count = collections.Counter(difference)
print(difference)
print(count)
print(count[1] * (count[3] + 1))
