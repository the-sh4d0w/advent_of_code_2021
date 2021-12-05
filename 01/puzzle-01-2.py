last_value = 1e6
count = 0

with open("01/input-01.txt", "r") as f:
    data = f.read().splitlines()

for index, value in enumerate(data[:-2]):
    value = int(value) + int(data[index + 1]) + int(data[index + 2])
    if value > last_value:
        count += 1
    last_value = value

print(count)
