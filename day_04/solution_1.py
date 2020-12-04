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

count = len(data)
for item in data:
    for field in fields:
        if field not in item:
            count -= 1
            break

print(count)
