lists = []
with open("day9_input.txt", 'r') as file:
    for line in file:
        numbers = [int(num) for num in line.split()]  # Split line and convert to numbers
        lists.append(numbers)

def extrapolate_next_value(list_of_numbers):
   """Extrapolates the next value for a list based on successive differences.

   Args:
       list_of_numbers: A list of numbers.

   Returns:
       The extrapolated next value in the list.
   """

   temp_list = [list_of_numbers]  # Initialize temporary list with the input list

   while True:
       difference_list = [b - a for a, b in zip(temp_list[-1], temp_list[-1][1:])]  # Calculate differences
       if all(diff == 0 for diff in difference_list):  # Check for all zeros
           break
       temp_list.append(difference_list)  # Append differences list

   # Extend lists back to original length
   for i in reversed(range(len(temp_list) - 1)):
       temp_list[i].append(temp_list[i + 1][-1] + temp_list[i][-1])  # Add extrapolated value

   return temp_list[0][-1]  # Return the extrapolated next value

#lists = [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45], [5, 1, -3, -11, -29, -65]]
total_sum = 0
for list in lists:
    total_sum += extrapolate_next_value(list)
print(total_sum)