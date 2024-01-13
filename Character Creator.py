import random

# Define a function to generate a random class
def generate_class():
    classes = ["cleric", "bard", "barbarian", "fighter", "druid", "rogue", "wizard", "ranger", "warlock", "sorcerer", "monk", "paladin"]
    class_choice = random.choice(classes)
    return class_choice

def generate_race():
    races = ["human", "elf", "dwarf", "halfling", "dragonborn", "gnome", "half-elf", "half-orc", "tiefling", "githyanki", "drow"]
    race_choice = random.choice(races)
    return race_choice

#function for strength stats
def generate_stats_strength():
  numlist = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
  str_stats = random.choice(numlist)
  return str_stats

#function for dexterity stats
def generate_stats_dexterity():
  numlist = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
  dex_stats = random.choice(numlist)
  return dex_stats

#function for constitution stats
def generate_stats_constitution():
  numlist = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
  con_stats = random.choice(numlist)
  return con_stats

#function for intelligence stats
def generate_stats_intelligence():
  numlist = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
  int_stats = random.choice(numlist)
  return int_stats

#function for wisdom stats
def generate_stats_wisdom():
  numlist = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
  wis_stats = random.choice(numlist)
  return wis_stats

#function for charisma stats
def generate_stats_charisma():
  numlist = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
  cha_stats = random.choice(numlist)
  return cha_stats

# the main function
def main():
  print("Welcome to the Random Character Creator!")
  print()
  while True:
    character_create = input("Would you like you create a character? (Y/N): ")
    print()
    if character_create.lower() == "y":
      # Generate a random class
      class_choice = generate_class()
       # Generate a random race
      race_choice = generate_race()
      # Generate strength stats
      str_stats = generate_stats_strength()
      # Generate dexterity stats
      dex_stats = generate_stats_dexterity()
      # Generate constitution stats
      con_stats = generate_stats_constitution()
      # Generate intelleigence stats
      int_stats = generate_stats_intelligence()
      # Generate wisdom stats
      wis_stats = generate_stats_wisdom()
      # Generate charisma stats
      cha_stats = generate_stats_charisma()
      # prompts the user to enter a name for their character
      name = input("Enter a name for your character: ")
      print()
      # greets the user by their chose character name
      print(f"Welcome, {name}.")
      print()
      # prints the entir character sheet for the user
      print("Character Sheet:")
      print("=" * 20)
      print("Name:    " + name)
      print("Race:    " + race_choice.capitalize())
      print("Class:   " + class_choice.capitalize())
      print("STR:  \t", str_stats)
      print("DEX:  \t", dex_stats)
      print("CON:  \t", con_stats)
      print("INT:  \t", int_stats)
      print("WIS:  \t", wis_stats)
      print("CHA:  \t", cha_stats)
      print()
    # if the user choose not to create a(nother) character
    elif character_create.lower() == "n":
      print("Okay, have a good day!")
      return
    # if the user enters an invalid input, they are informed their choice is invalid and are allowed to restart the loop
    else:
      print("Invalid input. Please enter Y or N")
      continue
if __name__ == "__main__":
    main()