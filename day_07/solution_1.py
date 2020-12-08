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
    item = re.sub(r"\d", "", item)
    colors = item.split(" contain ")

    parent = colors[0].strip()
    children = colors[1].strip().split(",")
    for color in children:
        color = color.strip()
        if color in family:
            family[color].append(parent)
            continue

        family[color] = [parent]

parents = set()


def get_parent(member):
    if member in family:
        for parent in family[member]:
            parents.add(parent)
            get_parent(parent)


get_parent("shiny gold")
print(len(parents))
