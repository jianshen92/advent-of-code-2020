with open("data", "r") as f:
    data = f.read().splitlines()

LENGTH_PREAMBLE = 25

preamble = []

for item in data:
    qualify = False
    number = int(item)

    if len(preamble) < LENGTH_PREAMBLE:
        preamble.append(number)
        continue

    for num in preamble:
        temp_preamble = preamble.copy()
        temp_preamble.remove(num)

        if (number - num) in temp_preamble:
            qualify = True
            break

    if not qualify:
        break

    preamble.pop(0)
    preamble.append(number)

invalid = number

weakness = []
for item in data:
    number = int(item)

    if len(weakness) < 2:
        weakness.append(number)
        continue

    if sum(weakness) < invalid:
        weakness.append(number)
        continue

    while sum(weakness) > invalid:
        weakness.pop(0)

    if sum(weakness) == invalid:
        break

    weakness.append(number)

print(min(weakness) + max(weakness))
