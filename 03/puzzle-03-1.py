gamma_rate = ""
epsilon_rate = ""

with open("03/input-03.txt", "r") as f:
    data = f.read().splitlines()

for index in range(len(data[0])):
    values = [value[index] for value in data]
    gamma_rate += max(set(values), key=values.count)
    epsilon_rate += min(set(values), key=values.count)

print(int(gamma_rate, base=2) * int(epsilon_rate, base=2))
