with open("data", "r") as f:
    data = f.read().splitlines()

pattern_length = len(data[0])
start = 0
count = 0
for row in data:
    if row[start % pattern_length] == "#":
        count += 1
    start += 3

print(count)