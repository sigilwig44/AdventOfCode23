import re

with open("calibrationdoc_day1.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list
lines = [line.rstrip() for line in lines]

def extract_numbers(text):
    pattern = r"(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))"
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    return matches

def get_calibration_sum(input_arr):
    total = 0
    for line in input_arr:
        numbers = extract_numbers(line)

        if numbers:
            first_number = numbers[0]
            last_number = numbers[-1]

            # Convert spelled-out numbers to digits
            try:
                first_digit = int(first_number)
            except ValueError:
                first_digit = {
                    "zero": 0,
                    "one": 1,
                    "two": 2,
                    "three": 3,
                    "four": 4,
                    "five": 5,
                    "six": 6,
                    "seven": 7,
                    "eight": 8,
                    "nine": 9
                }[first_number.lower()]

            try:
                last_digit = int(last_number)
            except ValueError:
                last_digit = {
                    "zero": 0,
                    "one": 1,
                    "two": 2,
                    "three": 3,
                    "four": 4,
                    "five": 5,
                    "six": 6,
                    "seven": 7,
                    "eight": 8,
                    "nine": 9
                }[last_number.lower()]

            extracted_digits = str(first_digit) + str(last_digit)
            total += int(extracted_digits)

    return total

print(get_calibration_sum(lines))