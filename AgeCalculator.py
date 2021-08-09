# AgeCalculator

#datetime (inbuilt in python)
from datetime import date

# global varibales
currentYear = date.today().year

# function to calculate the age (currentYear, whenBorn)
def ageCalculator(currentYear, whenBorn):
    return currentYear - whenBorn

#loop for taking in input
while True:
    whenBorn = int(input("What year were you born?"))

    print(f"{ageCalculator(currentYear,whenBorn = whenBorn)}")
