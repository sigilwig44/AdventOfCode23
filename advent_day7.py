import collections

hands = []
with open("card_hands.txt", "r") as file:
   for line in file:
       card, score = line.strip().split()  # Remove potential extra spaces and split
       hands.append((card, int(score)))

def card_rank(hand):
 """Returns the rank of a card from highest to lowest: A, K, Q, J, T, ..."""
 ranks = []
 for card in hand:
   ranks.append("23456789TJQKA".find(card))
 return ranks

def sort_hands(hands):
 
 def hand_rank(hand):
   cards, _ = hand  # Extract cards and discard the secondary value
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

   return (hand_type, *card_rank(cards))  # Use card_rank for tie-breaking

 return sorted(hands, key=hand_rank, reverse=True)

def add_rank(hands):
 # Create a new list to store the modified hands
 modified_hands = []

 # Iterate through the hands list
 for i, hand in enumerate(hands):
   # Calculate the third number based on position
   rank = len(hands) - i

   # Create a new tuple with the added third number
   new_hand = (hand[0], hand[1], rank)

   # Append the new hand to the modified hands list
   modified_hands.append(new_hand)

 # Return the modified hands list
 return modified_hands

hands = sort_hands(hands)
hands = add_rank(hands)

total_winnings = 0
for hand, bid, rank in hands:
  total_winnings += bid * rank

print(total_winnings)