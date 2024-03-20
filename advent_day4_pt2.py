with open("scratchcards.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list
lines = [line.rstrip() for line in lines]

def parse_card_numbers(input_array):
   """Parses card numbers from the input array into winning numbers and card numbers arrays.

   Args:
       input_array: An array of strings containing card data in the format specified.

   Returns:
       A tuple containing two arrays:
       - winning_numbers: An array of arrays, where each inner array contains the winning numbers for a card.
       - card_numbers: An array of arrays, where each inner array contains the numbers on a card.
   """

   winning_numbers = []
   card_numbers = []

   for card_string in input_array:
       parts = card_string.split(" | ")  # Split by the separator " | "
       winning_part = parts[0].split()[2:]  # Get winning numbers after removing "Card ##"
       card_part = parts[1].split()  # Get card numbers

       winning_numbers.append(list(map(int, winning_part)))  # Convert strings to integers
       card_numbers.append(list(map(int, card_part)))

   return winning_numbers, card_numbers

def tally_card_copies(winning_numbers, card_numbers):
    """Calculates the total score based on the game rules described.

    Args:
        winning_numbers: An array of arrays, where each inner array contains the winning numbers for a card.
        card_numbers: An array of arrays, where each inner array contains the numbers on a card.

    Returns:
        The total score of all cards, considering copies won.
    """

    card_copies = [1] * len(winning_numbers)  # Initially, one copy of each card

    for i in range(len(winning_numbers)):
        common_numbers = len(set(winning_numbers[i]) & set(card_numbers[i]))

        # Apply the card copying logic for the next cards:
        if i < len(winning_numbers) - 1:
            for j in range(common_numbers):
                if i + j + 1 < len(winning_numbers):
                    card_copies[i + j + 1] += card_copies[i]

    return sum(card_copies)

winning_numbers, card_numbers = parse_card_numbers(lines)
print(tally_card_copies(winning_numbers, card_numbers))

# Correct Answer: 5833065