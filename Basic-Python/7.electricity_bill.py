# Problem Statement:
# Write a program to calculate the electricity bill based on the number of units consumed.
# Billing Slabs:
#  - First 50 units: ₹2 per unit
#  - Next 50 units (51–100): ₹3 per unit
#  - Next 100 units (101–200): ₹5 per unit
#  - Above 250 units: ₹8 per unit
# After calculating the cost, add 20% tax to the final bill and print it.

# Input: Number of electricity units consumed
units = int(input("Enter units used: "))

# Calculating bill based on slabs
if units > 250:
    total = (units - 250) * 8 + 100 * 5 + 100 * 3 + 50 * 2
elif units > 150:
    total = (units - 150) * 5 + 100 * 3 + 50 * 2
elif units > 100:
    total = (units - 100) * 3 + 50 * 2
else:
    total = units * 2  # For <= 50 units (missing case added)

# Adding 20% tax on total amount
final_amount = total * 1.2

print("Final Bill Amount: ₹", final_amount)


# -------- Sample Inputs & Outputs --------

'''
Sample 1:
Input:
Enter units used: 120

Calculation:
50*2 + 50*3 + 20*3 = 100 + 150 + 60 = 310
Plus 20% tax: 310 * 1.2 = 372.0

Output:
Final Bill Amount: ₹ 372.0
'''

'''
Sample 2:
Input:
Enter units used: 270

Calculation:
50*2 + 50*3 + 100*5 + 20*8 = 100 + 150 + 500 + 160 = 910
Plus 20% tax: 910 * 1.2 = 1092.0

Output:
Final Bill Amount: ₹ 1092.0
'''
