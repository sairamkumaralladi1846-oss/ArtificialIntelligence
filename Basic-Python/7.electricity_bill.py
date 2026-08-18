# Problem Statement:
# Write a program to calculate the electricity bill based on the number of units consumed.
# Billing Slabs:
#  - First 50 units: ₹2 per unit
#  - Next 50 units (51–100): ₹3 per unit
#  - Next 150 units (101–250): ₹5 per unit
#  - Above 250 units: ₹8 per unit
# After calculating the cost, add 20% tax to the final bill and print it.

# Input: Number of electricity units consumed
units = int(input("Enter units used: "))

# Calculating bill based on slabs
if units > 250:
    total = (units - 250) * 8 + 150 * 5 + 50 * 3 + 50 * 2
elif units > 100:
    total = (units - 100) * 5 + 50 * 3 + 50 * 2
elif units > 50:
    total = (units - 50) * 3 + 50 * 2
else:
    total = units * 2

# Adding 20% tax on total amount
final_amount = total * 1.2

print("Final Bill Amount: ₹", final_amount)


# -------- Sample Inputs & Outputs --------

'''
Sample 1:
Input:
Enter units used: 120

Calculation:
50*2 + 50*3 + 20*5 = 100 + 150 + 100 = 350
Plus 20% tax: 350 * 1.2 = 420.0

Output:
Final Bill Amount: ₹ 420.0
'''

'''
Sample 2:
Input:
Enter units used: 270

Calculation:
50*2 + 50*3 + 150*5 + 20*8 = 100 + 150 + 750 + 160 = 1160
Plus 20% tax: 1160 * 1.2 = 1392.0

Output:
Final Bill Amount: ₹ 1392.0
'''
