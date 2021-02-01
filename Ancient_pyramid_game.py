#ancient throne room
def ancient_throne_room():
    # promts
    print("\nYou have now entered what looks like an ancient throne room of some kind.\nLooks like it must have been for some Pharo long ago.")
    print("You can't see an obviouse exit to be found.")
    print("There does look to be a handle of some kind on the wall. It looks like maybe it could be pulled down on, to make something happen.")
    print("There also looks to be a week looking section in a wall that is sort of in the shape of a door possibly.")
    print("What would you choose?(1 or 2)")
    print("1). Pull the handle?")
    print("2). Try and push through the weak looking wall?")

    # take input
    answer = input('>')

    if answer == '1':
      # they win
      print('\nNice work, you chose the correct exit. You win!')
      # activate play_again
      play_again()
    elif answer == '2':
      # the player loses
      print('Sorry that wall crumbles, you fall into a spiked pit and die.')
      play_again()
    else:
      # call game_over with reason
      game_over('You need to learn how to pick a number!')


#demon room
def demon_room():
    #give some prompts
    print('\nThere is a demon here.')
    print('Behind the demon is the only other door.')
    print('The demon is eating someone he killed!')
    print('What would you do?(1 or 2)')
    print('1). Try to kill the demon?')
    print('2). Sneek past the demon?')

    #take input()
    answer = input('>')

    if answer == '1':
        # the player is dead!
        game_over('The demon killed you!')
    elif answer == '2':
        #lead them to the diamond_room()
        print('\nYour lucky, you got around the demon. Now you can go through the next door.')
        diamond_room()
    else:
        # else call game_over() function with the 'reason' argument
        game_over("Don't you know how to type a number?")

# monster room
def monster_room():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nNow you entered the room of a monster!")
  print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2)")
  print("1). Go through the door silently.")
  print("2). Kill the monster and show your courage!")

  # take input()
  answer = input(">")

  if answer == "1":
    # lead him to the diamond_room()
    diamond_room()
  elif answer == "2":
    # the player is dead, call game_over() with "reason"
    game_over("The monster was hungry, it ate you.")
  else:
    # game_over() with "reason"
    game_over("Go and learn how to type a number.")

# diamond room
def diamond_room():
  # some prompts
  print("\nYou are now in a room filled with diamonds!")
  print("And there is a door too!")
  print("What would you do? (1 or 2)")
  print("1). Take some diamonds and go through the door.")
  print("2). Just go through the door.")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead, call game_over() function with the "reason"
    game_over("They were cursed diamonds! The moment you touched it, the building collapsed, and you die!")
  elif answer == "2":
    # the player continues the game
    print("\nNice, you're are an honest person! You succesfully go through the next door!")
    # activate ancient_throne_room() function
    ancient_throne_room()
  else:
    # call game_over() with "reason"
    game_over("Go and learn how to type a number.")

# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()

# function to ask play again or not
def play_again():
  print("\nDo you want to play again? (y or n)")
  
  # convert the player's input to lower_case
  answer = input(">").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()



def start():
  # give some prompts
  print("\nYou are standing in a dimmly lit ancient pyramid.\nYou can't see very well.\nYou know you need to get out, but don't how. ")
  print('There is a door to your left and right, which one do you take?(L or R)')


  #convert the players input to lower_case
  answer = input('>').lower()

  if 'l' in answer:
    #if player typed 'left' or 'l' lead them to the demon_room()
    demon_room()
  elif 'r' in answer:
    #else if player typed 'right or 'r' lead them to the monster_room()
    monster_room()
  else:
    #else call game_over() function with 'reason" argument
    game_over("Don't you know how to type something properly?")

# start game
start()