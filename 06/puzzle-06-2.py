amount = 0

with open("06/input-06.txt", "r") as f:
    data = f.read().strip().split(",")

data = [int(fish) for fish in data]
fishes = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for fish in data:
    fishes[fish] += 1

for day in range(256):
    temp = fishes[0]
    fishes[0] = fishes[1]
    fishes[1] = fishes[2]
    fishes[2] = fishes[3]
    fishes[3] = fishes[4]
    fishes[4] = fishes[5]
    fishes[5] = fishes[6]
    fishes[6] = fishes[7] + temp
    fishes[7] = fishes[8]
    fishes[8] = temp

for fish in fishes:
    amount += fishes[fish]

print(amount)
