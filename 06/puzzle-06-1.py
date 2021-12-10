with open("06/input-06.txt", "r") as f:
    data = f.read().strip().split(",")

fishes = [int(fish) for fish in data]

for day in range(80):
    for index, fish in enumerate(fishes):
        fishes[index] -= 1
        if fish == 0:
            fishes[index] = 6
            fishes.append(9)

print(len(fishes))
