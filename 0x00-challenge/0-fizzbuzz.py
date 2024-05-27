#!/usr/bin/python3
""" FizzBuzz
"""
import sys

def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return

    result = [
        "FizzBuzz" if i % 15 == 0 else
        "Fizz" if i % 3 == 0 else
        "Buzz" if i % 5 == 0 else
        str(i)
        for i in range(1, n + 1)
    ]
    print(" ".join(result))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
