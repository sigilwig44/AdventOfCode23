with open("scratchcards.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list
lines = [line.rstrip() for line in lines]

def calculate_point_values(card_data_strings):
    point_values = []
    for card_data in card_data_strings:
        # Remove prefix and split card data
        card_data_without_prefix = card_data.split(":")[1].strip()
        parts = card_data_without_prefix.split(" | ")
        winning_numbers = [int(num) for num in parts[0].split()]
        card_numbers = [int(num) for num in parts[1].split()]

        # Calculate points for the card
        matches = len(set(winning_numbers) & set(card_numbers))  # Find common numbers using set intersection
        if matches > 0:
            points = 2 ** (matches - 1)  # Calculate points based on matches
        else:
            points = 0
        point_values.append(points)

    return point_values

point_values = calculate_point_values(lines)
print(sum(point_values))