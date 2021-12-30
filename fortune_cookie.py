"""Program that outputs one of at least four random fortunes."""

__author__ = "haleygs@email.unc.edu"

# Import randint function from the random library
from random import randint

print("Your fortune cookie says... ")

some_int: int = randint(1, 4)

if some_int == 1:
    print("You can make your own happiness.")
else:
    if some_int == 2:
        print("Your ability for accomplishment will follow with success.")
    else: 
        if some_int == 3:
            print("Jealousy doesn't open doors, it closes them.")
        else:
            print("A new voyage will fill your life with untold memories.")

print("Now, go spread positive vibes!")