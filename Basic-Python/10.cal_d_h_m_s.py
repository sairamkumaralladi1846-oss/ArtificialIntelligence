# Problem Statement:
# Write a program that converts a given number of seconds into the format:
# Days, Hours, Minutes, and Seconds.
# Only include a time component if it is greater than zero.

# Taking total seconds as input
sec = int(input("Seconds: "))

# Variable to hold the formatted output
out = ""

# Converting seconds step by step
if sec >= (24 * 60 * 60):
    out += "{} Days ".format(sec // (24 * 60 * 60))
    sec = sec % (24 * 60 * 60)

if sec >= (60 * 60):
    out += "{} Hours ".format(sec // (60 * 60))
    sec = sec % (60 * 60)

if sec >= 60:
    out += "{} Minutes ".format(sec // 60)
    sec = sec % 60

if sec > 0:
    out += "{} Seconds".format(sec)

# Display output
print(out)


# -------- Sample Inputs & Outputs --------

'''
Sample 1:
Input:
Seconds: 90061

Breakdown:
90061 = 1 Day + 1 Hour + 1 Minute + 1 Second

Output:
1 Days 1 Hours 1 Minutes 1 Seconds
'''

'''
Sample 2:
Input:
Seconds: 3665

Breakdown:
3665 = 1 Hour + 1 Minute + 5 Seconds

Output:
1 Hours 1 Minutes 5 Seconds
'''

'''
Sample 3:
Input:
Seconds: 59

Output:
59 Seconds
'''

