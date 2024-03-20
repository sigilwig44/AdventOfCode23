with open("cube_input.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list
lines = [line.rstrip() for line in lines]

def solve_puzzle(game_data):
  """Solves the cube game puzzle for the given game data.

  Args:
    game_data: An array of strings, each containing information about a game.

  Returns:
    The sum of the IDs of games that could have been played with the given cube limits.
  """

  total = 0

  for game_string in game_data:
    parts = game_string.split(":")
    game_id = int(parts[0].split()[1])

    max_red = 0
    max_green = 0
    max_blue = 0

    for subset in parts[1].split("; "):
      cubes = subset.split(", ")
      for cube in cubes:
        num, color = cube.split()
        num = int(num)
        if color == "red":
          max_red = max(max_red, num)
        elif color == "green":
          max_green = max(max_green, num)
        elif color == "blue":
          max_blue = max(max_blue, num)

    #if max_red <= 12 and max_green <= 13 and max_blue <= 14:
     # total += game_id
    # Solution for part b:
    total += max_red * max_green * max_blue

  return total

print(solve_puzzle(lines))