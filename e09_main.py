# No ned to modify this function
def print_dictionary(dry):
  pairs = dry.items()
  print("Dictionary Contents:")
  print(16*"-")
  print("{")
  for name, score in pairs:
    print(f"\tPlayer {name:10s} : has {score:3s} points")
  print("}")


# Just add your code inside the while
def main():
  high_scores = {}

  #TODO:
  # Create your code here. A While loop should do this:
    # 1. Asks the user for a name
    # 2. Asks the user for a number of points
    # 3. Adds the points value to a dictionary using the name as key
    # 4. Prints the contents of the dictionary (using the normal print)
    # 5. Asks the user if they want to add more inputs
    #    If Yes… go to 1 (go to next iteration),
    #    Else exit the loop

  # AFTER the loop, prints the whole dictionary
  print_dictionary(high_scores)

if __name__ == "__main__":
  main()