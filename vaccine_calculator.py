"""Vaccine calculator exercise as a structured program."""

__author__ = "haleygs@email.unc.edu"

from datetime import datetime, timedelta


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))

    # Call days_to_target and store result in a variable.
    days_to_vaccination: int = days_to_target(population, doses, doses_per_day, target) 
    # Call future_date and store result in a variable.
    date_to_vaccination: str = future_date(days_to_vaccination)
    # Print the expected output using the variables above.
    print("We will reach " + str(target) + "% vaccination in " + str(days_to_vaccination) + " days, which falls on " + (date_to_vaccination) + ".")


# Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Returns the number of days left until the target population is vaccinated."""
    percent: float = (target / 100)
    percent_population: int = round(percent * population)
    already_vaccinated: float = (doses / 2)
    need_vaccine: int = round(percent_population - already_vaccinated)
    days: float = (doses_per_day / 2) 
    days_left: int = round(need_vaccine / days)
    return days_left


# Define future_date function
def future_date(days_left: int) -> str:
    """Returns the date for which the target population will be vaccinated."""
    today: datetime = datetime.today()
    future_days: timedelta = timedelta(days_left)
    date: datetime = today + future_days
    return (date.strftime("%B %d, %Y"))


if __name__ == "__main__":
    main()