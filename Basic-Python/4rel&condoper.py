# Problem Statement:
# Write a program to read four numbers and determine which one is the largest.
# Print the largest number with a meaningful message.

# Taking input values from user
a = int(input("FirstNo: "))
b = int(input("SecondNo: "))
c = int(input("ThirdNo: "))
d = int(input("FourthNo: "))

# Comparing numbers manually using conditions
if (a > b and a > c and a > d):
    print("a is the greatest number, which is {}".format(a))
elif (b > c and b > d):
    print("b is the greatest number, which is {}".format(b))
elif (c > d):
    print("c is the greatest number, which is {}".format(c))
else:
    print("d is the greatest number, which is {}".format(d))


# --------- Alternate Simple Method Using max() and Lambda ----------

# max_value = lambda x, y, z, w: max(x, y, z, w)
# result = max_value(a, b, c, d)
# print("Greatest number using lambda and max() is:", result)


# -------- Sample Inputs & Outputs --------

'''
Sample 1:
Input:
FirstNo: 12
SecondNo: 5
ThirdNo: 33
FourthNo: 7

Output:
c is the greatest number, which is 33
'''

'''
Sample 2:
Input:
FirstNo: 9
SecondNo: 21
ThirdNo: 4
FourthNo: 16

Output:
b is the greatest number, which is 21
'''
