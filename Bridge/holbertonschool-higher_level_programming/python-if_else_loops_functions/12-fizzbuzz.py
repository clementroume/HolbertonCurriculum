#!/usr/bin/python3
# Define the function FizzBuzz
def fizzbuzz():
    # Loop through numbers from 1 to 100
    for i in range(1, 101):
        # If divisible by both 3 and 5, print 'FizzBuzz'
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        # If divisible by 3, print 'Fizz'
        elif i % 3 == 0:
            print("Fizz", end=" ")
        # If divisible by 5, print 'Buzz'
        elif i % 5 == 0:
            print("Buzz", end=" ")
        # Otherwise, print the number itself
        else:
            print(i, end=" ")
