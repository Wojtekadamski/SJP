from signal import pause


class lab3:
    # zadanie 2.6.1.10
    def it_val(x = float(input("Enter value for x: "))):
        return "y = ", 1 / (x + (1 / (x + (1 / (x + (1 / x))))))
    # zadanie 2.6.1.11
    def duration(hour=int(input("Starting time (hours): ")), mins=int(input("Starting time (minutes): ")),
        dura=int(input("Event duration (minutes): "))):
        return int(((hour + dura / 60 + mins / 60)) % 24), ":", (mins + dura) % 60
    # zadanie eportal
    def lokata(percentage=0.015, duration=int(input("Podaj czas trwania lokaty ")),
           income_value=int(input("podaj wartość wpłaconych pieniędzy: "))):
           tmp = float(income_value * (float(1 + float(percentage))) ** duration)
           return "podaj czas trawania lokaty: ", duration, "\nPodaj wartość wpłaconych pieniędzy: ", income_value,"\nTwoje saldo będzie wynosić: ", round(tmp, 2), " PLN\n", "Twój zysk to: ",round(tmp - income_value, 2), " PLN"
if __name__ == "__main__":
    print(lab3.it_val())
    print("----------------------------")
    print(lab3.duration())
    print("----------------------------")
    print(lab3.lokata())