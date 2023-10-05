# A Treasure Island game designed by Melvin Raymond
# Designed to display concepts of 'If / Else / Elif' inputs and statements

# Low budget ASCII Art splash screen

print("Welcome to Treasure Island - Where your greatest fantasies and fears may come true!")
print("")
print("Your mission is to find the treasure!")
print("")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# follow the logic of the code below
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left", "right" or "forward" \n').lower()
if choice1 == "left" or choice1 == "forward":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over. Please Try Again" )
    if choice3 == "yellow":
        choice4 = input('You found the treasure! But a monster shows up right behind you.  Type "fight" to stay and fight. Or type "run" to drop the treasure and "run". \n').lower()
        if choice4 == "fight":
            print("You were not strong enough. The monster killed you AND took your treasure. Game Over. Please Try Again.")
        elif choice4 == "run":
          print("You didn't keep the treasure, you escaped with your life! Thanks for playing!")
        else:
          print("You were not fast enough. The monster killed you AND took your treasure. Game Over. Please Try Again.")    
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over. Please Try Again.")
    else:
      print("You chose a door that doesn't exist. Game Over. Please try again.")
  else:
    print("You got attacked by an angry trout. Game Over. Please try again.")
else:
  print("You fell into a hole. Game Over. Please try again.")