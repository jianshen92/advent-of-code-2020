with open("data", "r") as f:
    data = f.read().splitlines()

data = [int(d) for d in data]
second_data = data.copy()

for first in data:
    second_data.remove(first)
    for second in second_data:
        summ = first + second
        if summ == 2020:
            print(first * second)
