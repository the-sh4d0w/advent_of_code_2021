with open("03/input-03.txt", "r") as f:
    data = f.read().splitlines()

oxygen_generator_rating = data
co2_scrubber_rating = data

for index in range(len(oxygen_generator_rating[0])):
    oxygen_values = [value[index] for value in oxygen_generator_rating]
    most_common = max(set(oxygen_values), key=oxygen_values.count)
    least_common = min(set(oxygen_values), key=oxygen_values.count)
    if len(oxygen_generator_rating) > 1:
        if most_common == least_common:
            oxygen_generator_rating = [value for value in oxygen_generator_rating
                                       if value[index] == "1"]
        else:
            oxygen_generator_rating = [value for value in oxygen_generator_rating
                                       if value[index] == most_common]

for index in range(len(co2_scrubber_rating[0])):
    co2_values = [value[index] for value in co2_scrubber_rating]
    most_common = max(set(co2_values), key=co2_values.count)
    least_common = min(set(co2_values), key=co2_values.count)
    if len(co2_scrubber_rating) > 1:
        if most_common == least_common:
            co2_scrubber_rating = [value for value in co2_scrubber_rating
                                   if value[index] == "0"]
        else:
            co2_scrubber_rating = [value for value in co2_scrubber_rating
                                   if value[index] == least_common]

print(int(oxygen_generator_rating[0], base=2)
      * int(co2_scrubber_rating[0], base=2))
