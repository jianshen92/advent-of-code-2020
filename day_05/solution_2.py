def bin_to_dec(binary: str, ones: str, zeros: str) -> int:
    length = len(binary)

    dec = 0
    for idx, char in enumerate(binary):
        dec += 2 ** (length - idx - 1) if char == ones else 0
    return dec


with open("data", "r") as f:
    data = f.read().splitlines()

seats_set = set()
for row in range(1, 127):
    for col in range(0, 8):
        seats_set.add(row * 8 + col)

occupied_set = set()
for item in data:
    row = bin_to_dec(item[:7], "B", "F")
    col = bin_to_dec(item[7:], "R", "L")
    occupied_set.add(row * 8 + col)

leftover_ids = seats_set - occupied_set
for ids in leftover_ids:
    if ids + 1 not in leftover_ids and ids - 1 not in leftover_ids:
        print(ids)