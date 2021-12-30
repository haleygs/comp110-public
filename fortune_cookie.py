"""Program that outputs one of at least four random fortunes."""

__author__ = "haleygs@email.unc.edu"

# Import randint function from the random library
from random import randint

def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


some_int: int = randint(1, 4)


def fortune_cookie() -> str:
    """Returns a random fortune."""
    if some_int == 1:
        return "You can make your own happiness!"
    else:
        if some_int == 2:
            return "Your ability for accomplishment will follow with success."
        else:
            if some_int == 3:
                return "Jealousy doesn't open doors, it closes them!"
            else:
                return "A new voyage will fill your life with untold memories."


# Special dunder variable __name__ for "starting" the program when run as a module.
if __name__ == "__main__":
    main()
