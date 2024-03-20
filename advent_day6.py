def count_wins(max_time, min_distance):
 """
 This function counts the number of winning times in a range.

 Args:
   max_time: The upper limit of the time range (inclusive).
   min_distance: The minimum distance required to count as a win.

 Returns:
   The number of winning times in the range.
 """

 # Initialize the counter for winning times.
 win_count = 0

 # Loop through each time in the range.
 for time in range(max_time + 1):
   # Calculate the distance based on the formula.
   distance = time * (max_time - time)

   # Check if the distance is greater than the minimum distance.
   if distance > min_distance:
     # Increment the counter if it is a winning time.
     win_count += 1

 return win_count

times = [62, 64, 91, 90]
distances = [553, 1010, 1473, 1074]

product = 1
for time, distance in zip(times, distances):
  product *= count_wins(time, distance)
print(product)
print(count_wins(62649190, 553101014731074))