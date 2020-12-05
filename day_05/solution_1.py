def bin_to_dec(binary: str, ones: str, zeros: str) -> int:
    length = len(binary)

    dec = 0
    for idx, char in enumerate(binary):
        dec += 2 ** (length - idx - 1) if char == ones else 0
    return dec


# Test cases
string = "FBFBBFF"
assert bin_to_dec(string, "B", "F") == 44

string = "RLR"
assert bin_to_dec(string, "R", "L") == 5

with open("data", "r") as f:
    data = f.read().splitlines()

biggest = 0
for item in data:
    row = bin_to_dec(item[:7], "B", "F")
    col = bin_to_dec(item[7:], "R", "L")
    sid = row * 8 + col
    if sid > biggest:
        biggest = sid

print(biggest)
