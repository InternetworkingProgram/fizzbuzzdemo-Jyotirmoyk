# -*- coding: utf-8 -*-
"""FizzBuzz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Af4Oql42MBNYQgtUpbC132ju89iJDBj0
"""

# Ref: https://www.w3resource.com/python-exercises/python-conditional-exercise-10.php

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)