# Problem Statement:
# Two players (Abhinav and Anjali) choose Rock, Paper, or Scissors.
# Write a program to decide who wins based on classic rules:
#   - Rock beats Scissors
#   - Scissors beats Paper
#   - Paper beats Rock
# If both choose the same, the result should be "Tie".

# Taking choices from players
a = input("Abhinav: ")
b = input("Anjali: ")

# Rules stored in a dictionary: key beats value
play = { "Rock":"Scissors", "Paper":"Rock", "Scissors":"Paper" }

# Decision making
if a == b:
    print("Tie")
elif play.get(a) == b:   # play.get() avoids errors if invalid input
    print("Abhinav Wins")
else:
    print("Anjali Wins")


# -------- Sample Inputs & Outputs --------

'''
Sample 1:
Input:
Abhinav: Rock
Anjali: Scissors

Output:
Abhinav Wins
'''

'''
Sample 2:
Input:
Abhinav: Paper
Anjali: Paper

Output:
Tie
'''

'''
Sample 3:
Input:
Abhinav: Scissors
Anjali: Rock

Output:
Anjali Wins
'''
