import re

with open("data", "r") as f:
    data = f.read().splitlines()

family = {}
for item in data:
    item = item.replace("bags", "")
    item = item.replace("bag", "")
    item = item.replace(".", "")
    item = item.replace("no other", "")
    item = item.replace(r"no other", "")
    colors = item.split(" contain ")

    parent = colors[0].strip()
    children = colors[1].strip().split(",")

    family[parent] = {}
    for child in children:
        child = child.strip()
        amount = child[:1]
        color = child[2:]
        if amount == "":
            continue
        family[parent].update({color: amount})

count = 0


def get_children(member, multiplier=1):
    for color, amount in family[member].items():
        global count
        bags = int(amount) * multiplier
        count += bags
        get_children(member=color, multiplier=bags)


get_children(member="shiny gold")
print(count)
