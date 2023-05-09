#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modulus = abs(number) % 10
if (modulus > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, modulus))
elif (modulus < 6) and (modulus != 0):
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, modulus))
else:
    print("Last digit of {} is {} and is 0".format(number, modulus))
