import math


def zad1_pktc():
    counter = 0
    n = abs(int(input("Ile chcesz wpisać liczb: ")))
    for i in range(n):
        a = abs(int(input("Wpisz liczbę naturalną: ")))
        if a % 2 == 0 and math.sqrt(a) % 2 == 0:
            counter += 1
    print(counter)


def zad1_pktd():
    counter = 0
    n = abs(int(input("Ile chcesz wpisać liczb: ")))

    first = abs(int(input("Wpisz liczbę naturalną: ")))
    second = abs(int(input("Wpisz liczbę naturalną: ")))

    for i in range(2, n):
        third = abs(int(input("Wpisz liczbę naturalną: ")))
        if second < (first + third):
            counter += 1
        first = second
        second = third


def main():
    # zad1_pktc()
    zad1_pktd()


main()