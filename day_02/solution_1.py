from collections import Counter

with open("data", "r") as f:
    data = f.read().splitlines()

data = [item.split() for item in data]
proc = []
for item in data:
    nums = item[0]
    boundary = nums.split("-")
    lower_bound = int(boundary[0])
    upper_bound = int(boundary[1])
    key = item[1][0]
    password = item[2]
    entry = {
        "lower": lower_bound,
        "upper": upper_bound,
        "key": key,
        "password": password,
    }
    proc.append(entry)

valid_count = 0
for entry in proc:
    counter = Counter(entry["password"])
    key_count = counter[entry["key"]]
    if key_count >= entry["lower"] and key_count <= entry["upper"]:
        valid_count += 1

print(valid_count)
