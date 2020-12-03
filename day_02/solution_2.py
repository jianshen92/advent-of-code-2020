from collections import Counter

with open("data", "r") as f:
    data = f.read().splitlines()

data = [item.split() for item in data]
proc = []
for item in data:
    nums = item[0]
    boundary = nums.split("-")
    pos_1 = int(boundary[0])
    pos_2 = int(boundary[1])
    key = item[1][0]
    password = item[2]
    entry = {
        "pos_1": pos_1 - 1,
        "pos_2": pos_2 - 1,
        "key": key,
        "password": password,
    }
    proc.append(entry)

# print(proc)
valid_count = 0
for entry in proc:
    try:
        pass_1 = entry["password"][entry["pos_1"]]
        pass_2 = entry["password"][entry["pos_2"]]
    except IndexError:
        continue
    if pass_1 == entry["key"] or pass_2 == entry["key"]:
        if pass_1 != pass_2:
            valid_count += 1

print(valid_count)