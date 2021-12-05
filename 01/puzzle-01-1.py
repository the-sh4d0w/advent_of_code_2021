last_value = 1e6
count = 0

with open("01/input-01.txt", "r") as f:
    data = f.read().splitlines()

for value in data:
    value = int(value)
    if value > last_value:
        count += 1
    last_value = value

print(count)
