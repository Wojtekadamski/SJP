import xprint as xprint

kilometers = 12.25
miles = 7.38

miles_to_kilometers = kilometers / 0.621371
kilometers_to_miles = miles * 0.621371
def zad1():
    print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
    print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

if __name__ == "__main__":

    vals = [0,1,2]
    vals.insert(0,1)
    del vals[1]


    print(vals)