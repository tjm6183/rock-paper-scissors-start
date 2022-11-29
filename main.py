rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
  
computer_choice = random.randint(0,2)

int(computer_choice)
print("The computer's choice is:")
if computer_choice == 0:
  print(f"Rock.\n" + rock)
elif computer_choice == 1:
  print(f"Paper.\n" + paper)
elif computer_choice == 2:
  print(f"Scissors.\n" + scissors)

if(computer_choice == choice):
  print("Tie.")
elif(computer_choice == 0 and choice == 1):
  print("Win.")
elif(computer_choice == 0 and choice == 2):
  print("Lose.")
elif(computer_choice == 1 and choice == 0):
  print("Lose.")
elif(computer_choice == 1 and choice == 2):
  print("Win.")
elif(computer_choice == 2 and choice == 0):
  print("Win.")
elif(computer_choice == 2 and choice == 1):
  print("Lose.")