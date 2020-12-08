with open("data", "r") as f:
    data = f.read()

data = data.split("\n\n")

count = 0
for item in data:
    removed_nl = item.replace("\n", "")
    count += len(set(removed_nl))

print(count)