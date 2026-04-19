# Problem Statement:
# Write a Python program to generate all Pythagorean triplets where:
# i > j > k and i² = j² + k².
# The program should take an integer n and find all valid triplets up to that range.

# Taking input from the user
n = int(input("Enter a number: "))

# Using list comprehension to generate triplets
triplet_list = [(i, j, k) 
                for i in range(5, n + 1) 
                for j in range(4, i) 
                for k in range(3, j) 
                if i**2 == j**2 + k**2]

# Printing the result
print("Pythagorean Triplets:", triplet_list)


# -------- Sample Inputs & Outputs --------

'''
Sample Input:
Enter a number: 20

Output:
Pythagorean Triplets: [(5, 4, 3), (10, 8, 6), (13, 12, 5), (15, 12, 9), (17, 15, 8), (20, 16, 12)]
'''

'''
Sample Input:
Enter a number: 10

Output:
Pythagorean Triplets: [(5, 4, 3), (10, 8, 6)]
'''
