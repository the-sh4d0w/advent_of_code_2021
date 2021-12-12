amount = 0

with open("08/input-08.txt", "r") as f:
    data = f.read().splitlines()

data = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
data = [line.split(" | ")[1] for line in data]

for line in data:
    for value in line.split():
        if len(value) in (2, 3, 4, 7):
            amount += 1

print(amount)
