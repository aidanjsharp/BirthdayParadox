from numpy .random import seed
from numpy .random import randint


def main():
    # Use a breakpoint in the code line below to debug your script.
    days = []
    matched = False
    while matched == False:
        rDay = randDay()
        matched = checkDay(rDay, days)
        days.append(rDay)

    print("Found a match on day", rDay, "!")
    print("days:")
    print(days)

    tries = len(days)
    print("This took", tries, "tries.")


def checkDay(rDay,days):
    for day in days:
        if day == rDay:
            return True
    return False

def randDay():
    return randint(1, 366)







main()
