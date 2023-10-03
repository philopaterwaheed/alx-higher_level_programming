#!/usr/bin/python3
import random
number = random.randint(-10, 10)
msg = None
if number > 0:
    msg = "positive"
elif number < 0:
    msg = "negative"
else:
    msg = "zero"
print(f"{number} is {msg}")
