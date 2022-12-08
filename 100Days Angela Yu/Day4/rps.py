import random

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

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
player_hand = "default"

if player_choice == 0:
    player_hand = rock
elif player_choice == 1:
    player_hand = paper
elif player_choice == 2:
    player_hand = scissors
else:
    print(f"{player_choice} is an invalid player choice number, run again")

if player_choice == 0 or player_choice == 1 or player_choice == 2:
    print("player hand: " + player_hand)

agent_choice = random.randint(0,2)
agent_hand = "default"

if agent_choice == 0:
    agent_hand = rock
elif agent_choice == 1:
    agent_hand = paper
elif agent_choice == 2:
    agent_hand = scissors
else:
    print(agent_choice, type(agent_choice))
    print("Invalid number, run again")

if agent_choice == 0 or agent_choice == 1 or agent_choice == 2:
    print("agent hand: ", agent_hand)
  
if (agent_choice == 0 and player_choice == 0) or (agent_choice == 1 and player_choice == 1) or (agent_choice == 2 and player_choice == 2):
  print("it's a draw")
elif (agent_choice == 1 and player_choice == 0) or (agent_choice == 2 and player_choice == 1) or (agent_choice == 0 and player_choice == 2):
  print("you lose")
elif (agent_choice == 0 and player_choice == 1) or (agent_choice == 1 and player_choice == 2) or (agent_choice == 2 and player_choice == 0):
  print("you win")