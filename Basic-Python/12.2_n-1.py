# Problem Statement:
# Write a program to print a diamond number pattern based on a given integer `n`.
# The pattern increases numbers from 1 to n (center row), then decreases back to 1.

# Example for n = 4:
#       1
#      2 2
#     3 3 3
#    4 4 4 4   ← Middle
#     3 3 3
#      2 2
#       1

# Taking input
n = int(input("num: "))

k = 1  # Helper variable for lower part of pattern

for i in range(1, 2*n):  # Loop runs for top + bottom (diamond shape)
    
    # Upper pyramid including the middle row
    if i < n + 1:
        print(" " * (n - i) + (str(i) + " ") * i)
    
    # Lower inverted pyramid
    else:
        print(" " * k + (str(n - k) + " ") * (n - k))
        k += 1


# -------- Sample Input & Output --------

'''
Sample Input:
num: 4

Output:
   1 
  2 2 
 3 3 3 
4 4 4 4 
 3 3 3 
  2 2 
   1 
'''

'''
Sample Input:
num: 3

Output:
  1 
 2 2 
3 3 3 
 2 2 
  1 
'''
