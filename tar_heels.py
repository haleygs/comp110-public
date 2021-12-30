"""An exercise in remainders and boolean logic."""

__author__ = "haleygs@email.unc.edu"

# Prompt the user for an integer
    # When evenly divisible by 2, print "TAR"
    # When evenly divisible by 7, print "HEELS"
    # When evenly divisible by both 2 and 7, print "TAR HEELS"
    # When none of the conditions are met, print "CAROLINA"

def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(some_int: int) -> str:
    """Returns an str statement, depending on which conditions are met."""
    if some_int % 2 == 0 and some_int % 7 == 0:
        return "TAR HEELS"
    else:
        if some_int % 2 == 0:
            return "TAR"
        else:
            if some_int % 7 == 0:
                return "HEELS"
            else:
                return "CAROLINA"


if __name__ == "__main__":
    main()
