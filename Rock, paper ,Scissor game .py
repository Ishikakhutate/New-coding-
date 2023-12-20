#!/usr/bin/env python
# coding: utf-8

#  Projects 

# In[4]:


#reverse a string 
def reverse(string):
    string = string[::-1]
    return string 
    
a = "ishika"
print("reverse string")
print(reverse(a))


# In[ ]:


import random

choices = ['Rock', 'Paper', 'Scissor']
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0

while True:
    player = input('Rock, Paper, or Scissor? ').capitalize()

    if player == computer:
        print('Tie!')
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!")
            cpu_score += 1
        else:
            print("You won!")
            player_score += 1
    elif player == "Paper":
        if computer == "Scissor":
            print("You lose!")
            cpu_score += 1
        else:
            print("You won!")
            player_score += 1
    elif player == "Scissor":
        if computer == "Rock":
            print("You lose!")
            cpu_score += 1
        else:
            print("You won!")
            player_score += 1
    elif player == 'End':
        print('Final Score:')
        print(f"CPU: {cpu_score}")
        print(f"Player: {player_score}")
        break
    else:
        print("Invalid input. Please choose Rock, Paper, Scissor, or End.")

