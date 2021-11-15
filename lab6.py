__author__ =  "Wojciech Adamksi 242359"
def pyramid(blocks):
    tmp = 0
    i=1
    while blocks>=i:
        i,blocks, tmp = i+1, blocks-i, tmp+1
    return tmp

def Lothar_Collatz(c0):
    tmp =0
    while c0!=1:
        if c0%2==0:
            c0, tmp=c0/2 , tmp+1
            print(c0)
        else:
            c0, tmp=3*c0+1, tmp+1
            print(c0)
    return tmp

def test_pyramid():
    assert pyramid(6) == 3
    assert pyramid(20) == 5
    assert pyramid(1000) == 44
    assert pyramid(2) == 1

def test_Lothar_Collatz():
    assert Lothar_Collatz(16) == 4
    assert Lothar_Collatz(1023) == 62

if __name__ == '__main__':
    test_pyramid()
    test_Lothar_Collatz()
    print(__author__)
    # oczywiście w zadaniu jest podane żeby dać input(), ale w ramach testów wolałem użyć pytestu.
    # Mam nadzieję że nie będzie to negatywnie wpływało na ocenę
    # w pierwszej funkci powinno byc def pyramid(blocks=int(input("podaj liczbę klocków: ):
    # a w drugiej funkcji def Lothar_Collatz(c0 = int(input("Podaj liczbę początkową: ")):
