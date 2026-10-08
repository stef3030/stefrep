Values = [1,2,3,4,5,6,7,8,9,10]
import random

# Generates a random integer between 1 and 10 (includes both 1 and 10)
num = random.randint(1, 10)
number_game = input ("guess a number 1-10:")
if number_game== random.randint(1, 10):
    print(num)
