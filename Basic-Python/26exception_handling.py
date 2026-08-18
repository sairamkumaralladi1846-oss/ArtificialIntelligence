x = input("Enter a number: ")

# answer = 10 / int(x)  # This line may raise a ZeroDivisionError or ValueError if x is not a valid integer

try:
    answer = 10 / int(x) 
except ZeroDivisionError:
    print("zero value is not allowed. Please enter a non-zero integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
else:
    print("The answer is: {}".format(answer))
finally:
    print("Execution completed.")