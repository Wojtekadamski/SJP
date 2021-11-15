kilometers = 12.25
miles = 7.38
PLN_VALUE =3.95
miles_to_kilometers = kilometers / 0.621371
kilometers_to_miles = miles * 0.621371

def zad1():
    print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
    print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

def usd_pln_conv(amm):
     return amm/PLN_VALUE

def x_y_eq():
    x = 0
    # hardcode your test data here
    x = float(x)
    y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
    return print("y =", y)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tmp=int(input())
    print('wydano:',tmp)

    print('otrzymano',round(usd_pln_conv(tmp),2 ))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
