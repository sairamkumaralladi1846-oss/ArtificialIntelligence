# Problem Statement:
# Write a program to generate all prime numbers below a given number `n`.
# A number is prime if it has no divisors other than 1 and itself.

# Function to count factors (excluding 1 and the number itself)
def fact_num(num):
    fact = 0
    for i in range(2, num):
        if num % i == 0:
            fact += 1
    return fact

# List to store prime numbers
prime_list = []

# Taking user input
n = int(input("Enter a number: "))

# Checking each number from 2 to n-1
for i in range(2, n):
    if fact_num(i) == 0:   # If no extra factors → it's prime
        prime_list.append(i)

# Printing the list of prime numbers
print("Prime numbers below", n, ":", prime_list)


# -------- Sample Inputs & Outputs --------

'''
Sample Input:
Enter a number: 20

Output:
Prime numbers below 20: [2, 3, 5, 7, 11, 13, 17, 19]
'''

'''
Sample Input:
Enter a number: 10

Output:
Prime numbers below 10: [2, 3, 5, 7]
'''
