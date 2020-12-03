with open("data", "r") as f:
    data = f.read().splitlines()

pattern_length = len(data[0])
counts = 1

# Right 1, down 1.
start = 0
count = 0
for row in data:
    if row[start % pattern_length] == "#":
        count += 1
    start += 1

counts *= count

# Right 3, down 1.
start = 0
count = 0
for row in data:
    if row[start % pattern_length] == "#":
        count += 1
    start += 3

counts *= count

# Right 5, down 1.
start = 0
count = 0
for row in data:
    if row[start % pattern_length] == "#":
        count += 1
    start += 5

counts *= count

# Right 7, down 1.
start = 0
count = 0
for row in data:
    if row[start % pattern_length] == "#":
        count += 1
    start += 7

counts *= count

# Right 1, down 2.
start = 0
count = 0
for idx, row in enumerate(data):
    if idx % 2 != 0:  # odd number
        continue
    if row[start % pattern_length] == "#":
        count += 1
    start += 1

counts *= count

print(counts)
