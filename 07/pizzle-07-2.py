minimum_fuel_cost = 1e22

with open("07/input-07.txt", "r") as f:
    data = f.read().strip().split(",")

data = [int(value) for value in data]

for position in range(min(data), max(data) + 1):
    fuel_cost = 0
    for value in data:
        cost = abs(position - value)
        fuel_cost += int((cost * (cost + 1)) / 2)
    if fuel_cost < minimum_fuel_cost:
        minimum_fuel_cost = fuel_cost

print(minimum_fuel_cost)
