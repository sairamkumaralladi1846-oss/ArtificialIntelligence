# Problem Statement:
# Write a program to check whether the second word is the ending part (suffix)
# of the first word. If the first word ends with the second word, print True,
# otherwise print False.

# Taking inputs from user
first_word = input("Enter First Word: ")
second_word = input("Enter Second Word: ")

# Checking if first_word ends with second_word
print(first_word.endswith(second_word))


# ---------- Sample Inputs & Outputs ----------

'''
Sample 1:
Input:
Enter First Word: Blackhole
Enter Second Word: hole

Output:
True
'''

'''
Sample 2:
Input:
Enter First Word: boomerang
Enter Second Word: boom

Output:
False
'''
