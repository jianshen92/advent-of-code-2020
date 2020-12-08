with open("data", "r") as f:
    data = f.read().splitlines()

fail = True

for idx, item in enumerate(data):
    command = item.split(" ")
    if command[0] == "nop":
        new_command = f"jmp {command[1]}"
    if command[0] == "jmp":
        new_command = f"nop {command[1]}"
    test_data = data.copy()
    test_data[idx] = new_command

    try:
        addr = 0
        ops = []
        count = 0

        while addr not in ops:
            ops.append(addr)
            cmd = test_data[addr].split(" ")
            action = cmd[0]
            steps = cmd[1]
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
    except IndexError as e:
        print(e)
        print(count)
        break
