from random import random # generates random numbers
import math

print(random())

num_float= 34.5
print(f"actual float is {num_float}")
print(math.ceil(num_float)) # Ceil Rounds up the value
print(math.floor(num_float)) # Floor Rounds down

# Pyhton Modules
import os
import datetime, sys

working_directory = os.getcwd()
print(working_directory)

print(os.cpu_count())
print(datetime.date.today)
print(sys.path)
