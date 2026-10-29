from ipaddress import summarize_address_range

print ("Zadanie 1a:")

suma = 0
for i in range (2,101,2):
     suma += i
print (suma)

print ("Zadanie 1b:")
x = 0
for i in range (1,101):
     x += i ** 2
print (x)

print ("Zadanie 1c:")
v = 0
for i in range (1,64):
     x += 2 ** i
print (x)
