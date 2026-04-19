# Problem Statement:
# Write a program to print a slanted pattern (like a side view of a tent or slope)
# based on a given integer n.
# The last line should have underscores (_) before the closing bar to form a base.

# Taking input
n = int(input("Enter number of lines: "))

# Loop to print pattern
for i in range(1, n + 1):
    
    # If it's the last line → print slanted line with underline base
    if i == n:
        print(" " * (n - i) + "/" + "_" * (i - 1) + "|")
    
    # Otherwise → print slanted growing line
    else:
        print(" " * (n - i) + "/" + " " * (i - 1) + "|")


# -------- Sample Input & Output --------

'''
Sample Input:
Enter number of lines: 5

Output:
    /|
   / |
  /  |
 /   |
/____|
'''

'''
Sample Input:
Enter number of lines: 3

Output:
  /|
 / |
/__|
'''
