"""An exercise in remainders and boolean logic."""

__author__ = "haleygs@email.unc.edu"

# Prompt the user for an integer
    # When evenly divisible by 2, print "TAR"
    # When evenly divisible by 7, print "HEELS"
    # When evenly divisible by both 2 and 7, print "TAR HEELS"
    # When none of the conditions are met, print "CAROLINA"

input_value: int = int(input("Enter an int: "))
if input_value % 2 == 0 and input_value % 7 == 0:
    print("TAR HEELS")
else:
    if input_value % 2 == 0:
        print("TAR")
    else:
        if input_value % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")