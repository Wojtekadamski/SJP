def zad_3_4_1_13():
    beatles = []
    print("step 1:", beatles)
    beatles.append("John Lennon")
    beatles.append("Paul McCartney")
    beatles.append("George Harrison")
    print("step 2:", beatles)

    for elem in ["Stu Sutcliffe", "Pete Best"]:
        beatles.append(elem)
    print("step 3:", beatles)

    del beatles[3:]
    print("step 4:", beatles)

    beatles.insert(0, "Ringo Starr")
    print("step 5:", beatles)
    print("the Fab", len(beatles))


def zad_3_9_1_9(myList):
    return list(dict.fromkeys(myList))


def zad_3_9_1_9_rev2(myList):
    temp = []
    for elem in myList:
        if elem not in temp:
            temp.append(elem)
    return temp


zad_3_9_1_9_rev3 = lambda x: list(dict.fromkeys(x))


def test_zad_3_9_1_9_rev2():
    assert zad_3_9_1_9_rev2([1, 2, 4, 4, 1, 4, 2, 6, 2, 9]) == [1, 2, 4, 6, 9]


def test_zad_3_9_1_9():
    assert zad_3_9_1_9([1, 2, 4, 4, 1, 4, 2, 6, 2, 9]) == [1, 2, 4, 6, 9]


def test_zad_3_9_1_9_rev3():
    assert zad_3_9_1_9_rev3([1, 2, 4, 4, 1, 4, 2, 6, 2, 9]) == [1, 2, 4, 6, 9]


if __name__ == '__main__':
    # zad_3_4_1_13()
    test_zad_3_9_1_9_rev2()
    test_zad_3_9_1_9()
    test_zad_3_9_1_9_rev3()
