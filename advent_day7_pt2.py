import collections
import itertools

hands = []
with open("card_hands.txt", "r") as file:
   for line in file:
       card, score = line.strip().split()  # Remove potential extra spaces and split
       hands.append((card, int(score)))

def card_rank(hand):
 """Returns the rank of a card from highest to lowest: A, K, Q, J, T, ..."""
 ranks = []
 for card in hand:
   ranks.append("J23456789TQKA".find(card))
 return ranks

def find_joker_indices(hand):
  indicies = []
  for i, card in enumerate(hand):
    if card == "J":
      indicies.append(i)
  return indicies

def sort_hands(hands):

  def hand_rank(hand):
    cards, _ = hand  # Extract cards and discard the secondary value

    # Find optimal hand_type by considering all possible wild card replacements
    best_hand_type = 0
    if cards.count("J") > 0:
      for replacements in itertools.product("23456789TQKA", repeat=cards.count("J")):
        replaced_cards = replace_cards(cards, replacements)
        hand_type = determine_hand_type(replaced_cards)
        best_hand_type = max(best_hand_type, hand_type)
    else:
      best_hand_type = determine_hand_type(cards)

    return (best_hand_type, *card_rank(cards))  # Use card_rank for tie-breaking

  return sorted(hands, key=hand_rank, reverse=True)

def replace_cards(cards, replacements):
  j_indices = []
  replaced_cards = cards[:]
  for i, card in enumerate(cards):
    if card == "J":
      j_indices.append(i)
  for index, j in enumerate(j_indices):
    replaced_cards = replaced_cards.replace(replaced_cards[j], replacements[index], 1)
  return replaced_cards

def determine_hand_type(cards):
  """Determines the hand type without considering wild cards."""
  card_counts = collections.Counter(cards)
  most_common = card_counts.most_common()

  hand_type = (
    9 if len(most_common) == 1 else  # Five of a kind
    8 if most_common[0][1] == 4 else  # Four of a kind
    7 if most_common[0][1] == 3 and most_common[1][1] == 2 else  # Full house
    6 if most_common[0][1] == 3 else  # Three of a kind
    5 if len(most_common) == 3 else  # Two pair
    4 if len(most_common) == 4 else  # One pair
    3  # High card
  )

  return hand_type

def add_rank(hands):
 # Create a new list to store the modified hands
 modified_hands = []

 # Iterate through the hands list
 for i, hand in enumerate(hands):
   # Calculate the third number based on position
   cur_hand_rank = len(hands) - i

   # Create a new tuple with the added third number
   new_hand = (hand[0], hand[1], cur_hand_rank)

   # Append the new hand to the modified hands list
   modified_hands.append(new_hand)

 # Return the modified hands list
 return modified_hands

#hands = sort_hands([('32T3K', 765), ('T55J5', 684), ('KK677', 28), ('KTJJT', 220), ('QQQJA', 483)])
hands = sort_hands(hands)
hands = add_rank(hands)

total_winnings = 0
for hand, bid, cur_hand_rank in hands:
  total_winnings += bid * cur_hand_rank

print(total_winnings)