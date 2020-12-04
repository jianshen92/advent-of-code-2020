with open("data", "r") as f:
    data = f.read()

# replace new line with space
data = data.replace("\n", " ")

# split by double space
data = data.split("  ")

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

first_stage = data.copy()
for item in data:
    for field in fields:
        if field not in item:
            first_stage.remove(item)
            break

second_stage = []
for item in first_stage:
    infos = item.split(" ")
    info_dict = {}
    for info in infos:
        key, value = info.split(":")
        info_dict[key] = value
    second_stage.append(info_dict)


count = len(second_stage)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
for item in second_stage:
    if not 1920 <= int(item["byr"]) <= 2002:
        count -= 1
        continue
    if not 2010 <= int(item["iyr"]) <= 2020:
        count -= 1
        continue
    if not 2020 <= int(item["eyr"]) <= 2030:
        count -= 1
        continue

    height_value, height_unit = int(item["hgt"][:-2]), item["hgt"][-2:]

    if height_unit not in ["cm", "in"]:
        count -= 1
        continue

    if height_unit == "cm":
        if not 150 <= height_value <= 193:
            count -= 1
            continue

    if height_unit == "in":
        if not 59 <= height_value <= 76:
            count -= 1
            continue

    hcl = item["hcl"]

    if hcl[0] != "#":
        count -= 1
        continue

    if len(hcl) != 7:
        count -= 1
        continue

    for char in hcl[1:]:
        if char not in [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
        ]:
            count -= 1
            continue

    if item["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        count -= 1
        continue

    pid = item["pid"]

    if len(pid) != 9:
        count -= 1
        continue

    try:
        int(pid)
    except:
        count -= 1
        continue


print(count)
