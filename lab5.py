def zadanie_3_1_1_12():
    year = int(input("Enter a year: "))
    if year < 1582:
        print("Not within the Gregorian calendar period")
    elif year % 4 != 0:
        print("common year")
    elif year % 100 != 0:
        print("leap year")
    elif year % 400 != 0:
        print("common year")
    else:
        print("leap year")


def zadanie_3_2_1_10():
    word = input("enter a word: ")
    word = word.upper()
    for w in word:
        if w not in ['A', 'E', 'I', 'O', 'U']:
            print(w)
        else:
            continue


def zadanie_3_2_1_11():
    word = input("enter a word: ")
    vowels = ['A', 'E', 'I', 'O', 'U']
    word = word.upper()
    word_without_vowels = ""
    for w in word:
        if w not in vowels:
            word_without_vowels += w
        else:
            continue
    print(word_without_vowels)

if __name__ == '__main__':
    zadanie_3_1_1_12()
    zadanie_3_2_1_10()
    zadanie_3_2_1_11()
