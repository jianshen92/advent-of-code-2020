with open("data", "r") as f:
    data = f.read().splitlines()

LENGTH_PREAMBLE = 25

preamble = []
# try:
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

print(number)