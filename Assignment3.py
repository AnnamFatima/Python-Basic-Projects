'''
#Task 1: Calculate Factorial Using a Function 
#Problem Statement: Write a Python program that:
#1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
#2.   Returns the calculated factorial.
#3.   Calls the function with a sample number and prints the output.


def factorial(n):
    if n < 2: #because facorial of 0and 1 will be 1
        return 1
    else:
        return n * (factorial (n-1))

result = factorial(5)
print (result)
'''

#Task 2: Using the Math Module for Calculations
 #Problem Statement: Write a Python program that:
#1.   Asks the user for a number as input.
#2.   Uses the math module to calculate the:
#o   Square root of the number
#o   Natural logarithm (log base e) of the number
#o   Sine of the number (in radians)
#3.   Displays the calculated results.

'''import math

num = int(input("Enter a number : "))
#adding squareroot
square_root = math.sqrt(num)

#adding natural log
if num > 0:
    natural_log = math.log(num)
else:
    natural_log = "Not defined for 0 and negative numbers."

# Sin in radius 
Sine_value = math.sin(num)

print(f"\nSquare root of {num} = {square_root: }")
print(f"Natural log {num} = {natural_log}")
print(f"Sine of {num} = {Sine_value: }")
'''