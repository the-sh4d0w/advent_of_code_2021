digit_sum = 0

with open("08/input-08.txt", "r") as f:
    data = f.read().splitlines()

data = [line.split(" | ") for line in data]

for line in data:
    patterns = ["".join(sorted(pattern)) for pattern in line[0].split()]
    patterns_digits = {pattern: None for pattern in patterns}
    pattern_length = dict()
    for pattern in patterns:
        if not pattern_length.get(len(pattern)):
            pattern_length[len(pattern)] = pattern
        else:
            if isinstance(pattern_length[len(pattern)], list):
                pattern_length[len(pattern)] = pattern_length[len(
                    pattern)] + [pattern, ]
            else:
                pattern_length[len(pattern)] = [
                    pattern_length[len(pattern)], ] + [pattern, ]
    all_letters = "".join(line[0].split())
    letter_frequency = dict()
    for letter in set(all_letters):
        if not letter_frequency.get(all_letters.count(letter)):
            letter_frequency[all_letters.count(letter)] = letter
        else:
            if isinstance(letter_frequency[all_letters.count(letter)], list):
                letter_frequency[all_letters.count(
                    letter)] = letter_frequency[all_letters.count(letter)] + [letter, ]
            else:
                letter_frequency[all_letters.count(letter)] = [
                    letter_frequency[all_letters.count(letter)], ] + [letter, ]
    patterns_digits[pattern_length[2]] = 1
    patterns_digits[pattern_length[3]] = 7
    patterns_digits[pattern_length[4]] = 4
    patterns_digits[pattern_length[7]] = 8
    patterns_digits[[pattern for pattern in pattern_length[5]
                     if letter_frequency[4] in pattern][0]] = 2
    patterns_digits[[pattern for pattern in pattern_length[5]
                     if letter_frequency[6] in pattern][0]] = 5
    patterns_digits[[pattern for pattern in pattern_length[6]
                     if letter_frequency[4] not in pattern][0]] = 9
    patterns_digits[[pattern for pattern in pattern_length[6] if not (
        letter_frequency[7][0] in pattern and letter_frequency[7][1] in pattern)][0]] = 0
    patterns_digits[[pattern for pattern in pattern_length[5]
                     if patterns_digits[pattern] == None][0]] = 3
    patterns_digits[[pattern for pattern in pattern_length[6]
                     if patterns_digits[pattern] == None][0]] = 6
    number = ""
    for digit in line[1].split():
        digit = "".join(sorted(digit))
        number += str(patterns_digits[digit])
    digit_sum += int(number)

print(digit_sum)
