minimum_fuel_cost = 1e6

with open("07/input-07.txt", "r") as f:
    data = f.read().strip().split(",")

data = [int(value) for value in data]

for position in range(min(data), max(data) + 1):
    fuel_cost = 0
    for value in data:
        fuel_cost += abs(position - value)
    if fuel_cost < minimum_fuel_cost:
        minimum_fuel_cost = fuel_cost

print(minimum_fuel_cost)
