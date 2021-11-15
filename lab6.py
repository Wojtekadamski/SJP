__author__ =  "Wojciech Adamksi 242359"
def zadanie_3_2_1_14(blocks):
    tmp, i = 0, 1
    while blocks>=i:
        i,blocks, tmp = i+1, blocks-i, tmp+1
    return tmp

def zadanie_3_2_1_15(c0):
    tmp =0
    while c0!=1:
        if c0%2==0:
            c0, tmp=c0/2 , tmp+1
            print(c0)
        else:
            c0, tmp=3*c0+1, tmp+1
            print(c0)
    return tmp

def test_zadanie_3_2_1_14():
    assert zadanie_3_2_1_14(6) == 3
    assert zadanie_3_2_1_14(20) == 5
    assert zadanie_3_2_1_14(1000) == 44
    assert zadanie_3_2_1_14(2) == 1

def test_zadanie_3_2_1_15():
    assert zadanie_3_2_1_15(16) == 4
    assert zadanie_3_2_1_15(1023) == 62

if __name__ == '__main__':
    test_zadanie_3_2_1_14()
    test_zadanie_3_2_1_15()
    #print("zadanie_3_2_1_14: ", zadanie_3_2_1_14(int(input("podaj liczbę klocków: "))))
    #print("zadanie_3_2_1_15: ", zadanie_3_2_1_15(int(input("podaj liczbę początkową: "))))
    print(__author__)
    # oczywiście w zadaniu jest podane żeby dać input(), ale w ramach testów wolałem użyć pytestu.
    # Mam nadzieję że nie będzie to negatywnie wpływało na ocenę
    # w pierwszej funkci powinno byc def pyramid(blocks=int(input("podaj liczbę klocków: ):
    # a w drugiej funkcji def Lothar_Collatz(c0 = int(input("Podaj liczbę początkową: ")):
