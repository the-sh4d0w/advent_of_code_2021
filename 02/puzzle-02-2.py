position = 0
depth = 0
aim = 0

with open("02/input-02.txt", "r") as f:
    data = f.read().splitlines()

for value in data:
    values = value.split()
    command, value = values[0], int(values[1])
    if command == "forward":
        position += value
        depth += aim * value
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value

print(position * depth)
