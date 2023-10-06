# A simple game of ROCK PAPER SCISSORS displaying the imported 'random' module

import random
print("Lets play ROCK, PAPER, SCISSORS!")

# Defining the variables with ASCII
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
PAPER'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSORS!'''


# The code mechanics of the game
hand = [rock, paper, scissors]

num_items = len(hand)

result = random.randint(0, 2)
result = hand[result]

your_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper, '2' for Scissors:\n "))

if your_choice == 0 and str(result) == rock:
    print(rock)
    print("")
    print(f"Computer chose: ROCK\n{result}\nDRAW! Let's play again!")
elif your_choice == 0 and str(result) == paper:
    print(rock)
    print("")
    print(f"Computer chose: PAPER\n{result}\nYOU LOSE! Wanna play again?")
elif your_choice == 0 and str(result) == scissors:
    print(rock)
    print("")
    print(f"Computer chose: SCISSORS\n{result}\nYOU WIN! Wanna play again?")

if your_choice == 1 and str(result) == rock:
    print(paper)
    print("")
    print(f"Computer chose: ROCK\n{result}\nYOU WIN! Wanna play again?")
elif your_choice == 1 and str(result) == paper:
    print(paper)
    print("")
    print(f"Computer chose: PAPER\n{result}\nDRAW! Let's play again!")
elif your_choice == 1 and str(result) == scissors:
    print(paper)
    print("")
    print(f"Computer chose: SCISSORS\n{result}\nYOU LOSE! Wanna play again?")

if your_choice == 2 and str(result) == rock:
    print(scissors)
    print("")
    print(f"Computer chose: ROCK\n{result}\nYOU LOSE! Wanna play again?")
elif your_choice == 2 and str(result) == paper:
    print(scissors)
    print("")
    print(f"Computer chose: PAPER\n{result}\nYOU WIN! Wanna play again?")
elif your_choice == 2 and str(result) == scissors:
    print(scissors)
    print("")
    print(f"Computer chose: SCISSORS\n{result}\nDRAW! Let's play again")
else:
    print("Please restart and type in valid entry such as '0', '1', or '2'.")