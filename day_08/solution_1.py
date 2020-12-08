with open("data", "r") as f:
    data = f.read().splitlines()

addr = 0
ops = []
count = 0

while addr not in ops:
    ops.append(addr)
    cmd = data[addr].split(" ")
    action = cmd[0]
    steps = cmd[1]
    print(action, steps)
    if action == "nop":
        addr += 1
        continue
    if action == "acc":
        addr += 1
        count += int(steps)
        continue
    if action == "jmp":
        addr += int(steps)
        continue

print(count)