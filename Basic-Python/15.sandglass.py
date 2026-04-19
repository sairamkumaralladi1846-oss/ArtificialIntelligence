# Problem Statement:
# Write a program to print a diamond-like mirrored pattern of stars using a given number n.
# The pattern should first print decreasing star rows and then increasing rows again.

# Taking user input
n = int(input("n: "))

# Upper part including the middle line
for i in range(n):
    out = " " * i + "* " * (n - i)
    print(out)

# Lower part (excluding the already printed middle row)
i = n - 2
for j in range(n - 1):
    out = " " * i + "* " * (n - i)
    print(out)
    i -= 1


# -------- Sample Input & Output --------

'''
Sample Input:
n: 4

Output:
* * * * 
 * * * 
  * * 
   * 
  * * 
 * * * 
* * * * 
'''

'''
Sample Input:
n: 3

Output:
* * * 
 * * 
  * 
 * * 
* * * 
'''
