# Problem Statement:
# Write a program to check whether a given year is a leap year or not.
# A year is a leap year if:
#   - It is divisible by 400  OR
#   - It is divisible by 4 but NOT divisible by 100

# Taking user input
y = int(input("Enter a year: "))

# Checking leap year conditions
if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
    print(True)
else:
    print(False)


# -------- Sample Inputs & Outputs --------

'''
Sample 1:
Input:
Enter a year: 2024

Output:
True
(Reason: 2024 is divisible by 4 but not by 100)
'''

'''
Sample 2:
Input:
Enter a year: 1900

Output:
False
(Reason: 1900 is divisible by 100 but not by 400)
'''

'''
Sample 3:
Input:
Enter a year: 2000

Output:
True
(Reason: 2000 is divisible by 400)
'''
