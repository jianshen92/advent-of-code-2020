from typing import List, Tuple
import collections

with open("data", "r") as f:
    data = f.read().splitlines()

data_2d = [item for item in data]

state_dict = {
    "L": lambda x: "#" if x == 0 else "L",
    "#": lambda x: "L" if x >= 5 else "#",
    ".": lambda x: ".",
}


def adjecency(data_2d: List[str], position: Tuple[int, int], seat_state: str):
    num_rows = len(data_2d)
    num_cols = len(data_2d[0])

    r, c = position

    seats_to_check = []

    # left
    c_target = c
    while c_target > 0:
        c_target -= 1
        if not data_2d[r][c_target] == ".":
            seats_to_check.append(data_2d[r][c_target])
            break

    # right
    c_target = c
    while c_target < num_cols - 1:
        c_target += 1
        if not data_2d[r][c_target] == ".":
            seats_to_check.append(data_2d[r][c_target])
            break

    # up
    r_target = r
    while r_target > 0:
        r_target -= 1
        if not data_2d[r_target][c] == ".":
            seats_to_check.append(data_2d[r_target][c])
            break

    # down
    r_target = r
    while r_target < num_rows - 1:
        r_target += 1
        if not data_2d[r_target][c] == ".":
            seats_to_check.append(data_2d[r_target][c])
            break

    # UL
    c_target = c
    r_target = r
    while c_target > 0 and r_target > 0:
        c_target -= 1
        r_target -= 1
        if not data_2d[r_target][c_target] == ".":
            seats_to_check.append(data_2d[r_target][c_target])
            break

    # UR
    c_target = c
    r_target = r
    while c_target < num_cols - 1 and r_target > 0:
        c_target += 1
        r_target -= 1
        if not data_2d[r_target][c_target] == ".":
            seats_to_check.append(data_2d[r_target][c_target])
            break

    # DL
    c_target = c
    r_target = r
    while c_target > 0 and r_target < num_rows - 1:
        c_target -= 1
        r_target += 1
        if not data_2d[r_target][c_target] == ".":
            seats_to_check.append(data_2d[r_target][c_target])
            break

    # DR
    c_target = c
    r_target = r
    while c_target < num_cols - 1 and r_target < num_rows - 1:
        c_target += 1
        r_target += 1
        if not data_2d[r_target][c_target] == ".":
            seats_to_check.append(data_2d[r_target][c_target])
            break

    counter = collections.Counter(seats_to_check)
    return counter[seat_state]


current_seats = data_2d.copy()
while 1:
    new_seats = []
    for row, row_item in enumerate(current_seats):
        new_row = ""
        for col, col_item in enumerate(row_item):
            position = (row, col)
            occupied_seat = adjecency(current_seats, position, "#")
            action = state_dict[current_seats[row][col]]
            new_state = action(occupied_seat)
            new_row += new_state
        new_seats.append(new_row)

    if new_seats == current_seats:
        break

    current_seats = new_seats.copy()

seat_counter = collections.Counter()

for rows in new_seats:
    seat_counter.update(rows)

print(seat_counter["#"])