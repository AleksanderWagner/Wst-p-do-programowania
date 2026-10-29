#punkty = 100
#if punkty > 80 and punkty <= 100:
 #    print("Ocena 5")
#else:
   #  print("Ocena mniejsza niż 4,5")

   #  czas=60

  #   if punkty > 90 or czas < 70:
  #       print("Egzamin zaliczony")
  #   else:
    #     print("Egzamin do poprawy")

       #  temperatura = eval(input("Podaj temperature w st cels:"))
      #   temp_fahr = 9/5*temperatura+32

       #  if temp_fahr < 32:
       #      print("woda zamarza")

     #   if temp_fahr > 212:
     #   print("Temperatura wrzenia")

      #  rok = eval(input("Podaj rok do sprawdzenia"))
      #  if rok%100==0 and rok%400==0
      #      print("To jest rok przestepny")
      #  elif rok%100 ==0 and rok%400 ==0
       #     print("To nie jest rok przestepny")
      #  elif rok % 4 ==0 :
     #   else:
       #     print("To nie jest rok przestepny")

#from random import randint

#liczba=randint(a=1, b=10)
#losuj = eval(input("Podaj liczbe od 1 do 10"))
#print("Wylosowana liczba :", liczba)
#if losuj == liczba:
   # print("Zgadłeś")
#else:
  #  print("Przegrałeś")

#waga= float(input("Podaj wagę w kg"))
#wzrost= float(input("Podaj wzrost w m"))
#BMI= waga / (wzrost ** 2)
#if BMI < 18.5:
 #   print("masz niedowage")
#elif BMI > 18.6 or BMI <= 24.9:
 #   print("Waga prawidlowa")
#elif BMI < 25 or BMI >= 29.9:
 #   print("nadwaga")
#elif BMI > 30:
 #   print("otyłość")


#liczba= eval(input("Podaj liczbe calkowita"))
#if liczba > 0 and liczba%2 == 0:
 #   print("Liczba jest parzysta i dodatnia")
#else:
 #   print("Nie spełnia obu warunków")
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))

najmniejsza = a
najwieksza = a

if b < najmniejsza:
    najmniejsza = b

if c < najmniejsza:
    najmniejsza = c

if b > najwieksza:
    najwieksza = b

if c > najwieksza:
    najwieksza = c

print("Najmniejsza liczba:", najmniejsza)
print("Największa liczba:", najwieksza)