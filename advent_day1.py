with open("calibrationdoc_day1.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list
lines = [line.rstrip() for line in lines]

def getCalibrationSum(inputArr):
    sum = 0
    for line in inputArr:
        digits = [char for char in line if char.isdigit()]

        first_digit = digits[0]
        last_digit = digits[-1] if len(digits) > 1 else first_digit

        extracted_digits = first_digit + last_digit
        parsed_integer = int(extracted_digits)
        sum = sum + parsed_integer
    return sum

print(getCalibrationSum(lines))