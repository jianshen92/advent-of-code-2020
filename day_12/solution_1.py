with open("data", "r") as f:
    data = f.read().splitlines()

coor_x, coor_y = (0, 0)
theta = 0

displacement = {
    "E": lambda k, x, y: (x + k, y),
    "W": lambda k, x, y: (x - k, y),
    "N": lambda k, x, y: (x, y + k),
    "S": lambda k, x, y: (x, y - k),
}

rotation = {"L": lambda d, t: (t + d) % 360, "R": lambda d, t: (t - d) % 360}

forward = {
    0: lambda k, x, y: (x + k, y),
    180: lambda k, x, y: (x - k, y),
    90: lambda k, x, y: (x, y + k),
    270: lambda k, x, y: (x, y - k),
}

for item in data:
    instruction = item[0]
    value = int(item[1:])

    if instruction in displacement:
        action = displacement[instruction]
        coor_x, coor_y = action(value, coor_x, coor_y)

    if instruction == "F":
        action = forward[theta]
        coor_x, coor_y = action(value, coor_x, coor_y)

    if instruction in rotation:
        action = rotation[instruction]
        theta = action(value, theta)


print(abs(coor_x) + abs(coor_y))