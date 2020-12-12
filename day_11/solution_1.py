from typing import List, Tuple
import collections

with open("data", "r") as f:
    data = f.read().splitlines()

data_2d = [item for item in data]

state_dict = {
    "L": lambda x: "#" if x == 0 else "L",
    "#": lambda x: "L" if x >= 4 else "#",
    ".": lambda x: ".",
}


def adjecency(data_2d: List[str], position: Tuple[int, int], seat_state: str):
    num_rows = len(data_2d)
    num_cols = len(data_2d[0])

    r, c = position

    seats_to_check = []

    # left
    c_target = c - 1
    if c_target >= 0:
        seats_to_check.append(data_2d[r][c_target])

    # right
    c_target = c + 1
    if c_target < num_cols:
        seats_to_check.append(data_2d[r][c_target])

    # up
    r_target = r - 1
    if r_target >= 0:
        seats_to_check.append(data_2d[r_target][c])

    # down
    r_target = r + 1
    if r_target < num_rows:
        seats_to_check.append(data_2d[r_target][c])

    # UL
    c_target = c - 1
    r_target = r - 1
    if c_target >= 0 and r_target >= 0:
        seats_to_check.append(data_2d[r_target][c_target])

    # UR
    c_target = c + 1
    r_target = r - 1
    if c_target < num_cols and r_target >= 0:
        seats_to_check.append(data_2d[r_target][c_target])

    # DL
    c_target = c - 1
    r_target = r + 1
    if c_target >= 0 and r_target < num_rows:
        seats_to_check.append(data_2d[r_target][c_target])

    # DR
    c_target = c + 1
    r_target = r + 1
    if c_target < num_cols and r_target < num_rows:
        seats_to_check.append(data_2d[r_target][c_target])

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