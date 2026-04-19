# Problem Statement:
# Write a program to check:
# 1) Whether the second word exists anywhere inside the first word.
# 2) Whether the character at the given index of the first word
#    matches the first character of the second word.
# If both conditions are satisfied, print True; otherwise print False.

# Taking inputs
info = input("Enter first word: ")
check = input("Enter second word: ")
i = int(input("Enter index to check: "))

# Condition check
print((check in info) and (info[i] == check[0]))


# ----------- Sample Inputs & Outputs -----------

'''
Sample 1:
Input:
Repeat
pea
2

Output:
True
'''

'''
Sample 2:
Input:
Banana
Ball
0

Output:
False
'''
