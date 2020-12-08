with open("data", "r") as f:
    data = f.read()

data = data.split("\n\n")

count = 0
for item in data:
    l_set = [set(answer) for answer in item.split("\n")]
    count += len(set.intersection(*l_set))

print(count)