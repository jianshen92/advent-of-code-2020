import math

with open("data", "r") as f:
    data = f.read().splitlines()

coor_x, coor_y = (0, 0)
way_x, way_y = (10, 1)

displacement = {
    "E": lambda k, x, y: (x + k, y),
    "W": lambda k, x, y: (x - k, y),
    "N": lambda k, x, y: (x, y + k),
    "S": lambda k, x, y: (x, y - k),
}

# x, y = x cos theta - y sin theta, x sin theta + y cos theta

rotation_matrix = lambda wx, wy, rad: (
    round(wx * math.cos(rad) - wy * math.sin(rad)),
    round(wx * math.sin(rad) + wy * math.cos(rad)),
)
rotation = {
    ("L", 90): lambda wx, wy: rotation_matrix(wx, wy, math.pi / 2),
    ("L", 180): lambda wx, wy: rotation_matrix(wx, wy, math.pi),
    ("L", 270): lambda wx, wy: rotation_matrix(wx, wy, -math.pi / 2),
    ("R", 90): lambda wx, wy: rotation_matrix(wx, wy, -math.pi / 2),
    ("R", 180): lambda wx, wy: rotation_matrix(wx, wy, math.pi),
    ("R", 270): lambda wx, wy: rotation_matrix(wx, wy, math.pi / 2),
}

forward = lambda k, wx, wy, cx, cy: (cx + wx * k, cy + wy * k)

for item in data:
    instruction = item[0]
    value = int(item[1:])

    if instruction in displacement:
        action = displacement[instruction]
        way_x, way_y = action(value, way_x, way_y)

    if instruction == "F":
        coor_x, coor_y = forward(value, way_x, way_y, coor_x, coor_y)

    if (instruction, value) in rotation:
        action = rotation[(instruction, value)]
        way_x, way_y = action(way_x, way_y)


print(abs(coor_x) + abs(coor_y))