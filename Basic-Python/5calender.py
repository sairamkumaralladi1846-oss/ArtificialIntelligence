# Problem Statement:
# A user enters the starting day of a month and a date number.
# Write a program to calculate and print the weekday of the given date.

# Taking inputs from user
first_day = input("First day of the month: ")
req_date = int(input("Required date (1-31): "))

# Mapping days to numeric values for easier calculation
days_dict = {
    "Monday": 0, "Tuesday": 1, "Wednesday": 2, 
    "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6
}

# Formula to calculate the weekday index
req_digit = (req_date - 1 + days_dict[first_day]) % 7

# Finding and printing the matching day
for key, value in days_dict.items():
    if value == req_digit:
        print("Day on that date:", key)


# -------- Alternative Simple Method Using List --------
# first_day = input("Enter first day: ")
# date = int(input("Enter date: "))
# list_days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# req = (date + list_days.index(first_day) - 1) % 7
# print("Day on that date:", list_days[req])


# -------- Sample Input & Output --------

'''
Sample 1:
Input:
First day of the month: Monday
Required date (1-31): 5

Output:
Day on that date: Friday
'''

'''
Sample 2:
Input:
First day of the month: Thursday
Required date (1-31): 1

Output:
Day on that date: Thursday
'''
