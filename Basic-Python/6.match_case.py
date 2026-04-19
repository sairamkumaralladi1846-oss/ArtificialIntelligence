# Problem Statement:
# Write a function that takes a grade letter as input and prints the performance
# based on the given grading scale:
# O → Outstanding
# A → Excellent
# B → Good
# C → Average
# Any other input → Unknown

# Function to determine performance using match-case (Python 3.10+)
def find_performance(grade):
    match grade:
        case 'O':
            print("Outstanding")
        case 'A':
            print("Excellent")
        case 'B':
            print("Good")
        case 'C':
            print("Average")
        case _:
            print("Unknown")

# Calling the function
find_performance("A")


# -------- Sample Inputs & Outputs --------

'''
Sample 1:
Input:
A

Output:
Excellent
'''

'''
Sample 2:
Input:
Z

Output:
Unknown
'''
