position = 0
depth = 0

with open("02/input-02.txt", "r") as f:
    data = f.read().splitlines()

for value in data:
    values = value.split()
    command, value = values[0], int(values[1])
    if command == "forward":
        position += value
    elif command == "down":
        depth += value
    elif command == "up":
        depth -= value

print(position * depth)
