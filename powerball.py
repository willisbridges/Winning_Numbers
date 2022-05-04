import numpy as np
import random

# This file holds a python function to determine what numbers I'll play in Powerball this week

def numbers():
    ''' input next drawing date and receive a list of WINNING NUMBERS!!!! '''
    white_numbers = [random.randint(1, 69) for p in range(0, 5)]
    red_number = [random.randint(1, 29)]

    winning_numbers = white_numbers + red_number

    return winning_numbers

numbers = numbers()

print(numbers)