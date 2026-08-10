#!/usr/bin/python3
def fizzbuzz():
    """Prints the numbers from 1 to 100.

    Multiples of 3 print Fizz.
    Multiples of 5 print Buzz.
    Multiples of both print FizzBuzz.
    """
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
