rzedy = int(input("Podaj liczbę rzędów: "))

for i in range(1, rzedy + 1):
    krzesla = int(input(f"Podaj liczbę krzeseł w rzędzie {i}: "))
    print(f"Rząd {i}: {krzesla} krzeseł")