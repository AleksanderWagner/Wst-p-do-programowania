suma = 0
n = input("Wpisz ile liczb: ")
for i in range(1, n+1):
    a = int(input("Wpisz liczbę rzeczywistą: "))
    suma += ((-1)**(i+1)) * a
