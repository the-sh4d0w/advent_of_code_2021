vertical_lines = []
horizontal_lines = []
diagonal_lines = []
points = []

with open("05/input-05.txt", "r") as f:
    data = f.read().splitlines()

for line in data:
    coordinates = line.split(" -> ")
    x1, y1 = coordinates[0].split(",")
    x2, y2 = coordinates[1].split(",")
    if x1 == x2:
        if int(y2) > int(y1):
            vertical_lines.append(((int(x1), int(y1)), (int(x2), int(y2))))
        else:
            vertical_lines.append(((int(x1), int(y2)), (int(x2), int(y1))))
    elif y1 == y2:
        if int(x2) > int(x1):
            horizontal_lines.append(((int(x1), int(y1)), (int(x2), int(y2))))
        else:
            horizontal_lines.append(((int(x2), int(y1)), (int(x1), int(y2))))
    else:
        if int(x2) > int(x1):
            diagonal_lines.append(((int(x1), int(y1)), (int(x2), int(y2))))
        else:
            diagonal_lines.append(((int(x2), int(y2)), (int(x1), int(y1))))

for line in vertical_lines:
    for y in range(line[0][1], line[1][1] + 1):
        points.append((line[0][0], y))

for line in horizontal_lines:
    for x in range(line[0][0], line[1][0] + 1):
        points.append((x, line[0][1]))

for line in diagonal_lines:
    x_range = range(line[0][0], line[1][0] + 1)
    if line[1][1] > line[0][1]:
        for x in x_range:
            points.append((x, line[0][1] + (x - line[0][0])))
    else:
        for x in x_range:
            points.append((x, line[0][1] - (x - line[0][0])))

print(len([point for point in set(points) if points.count(point) > 1]))
