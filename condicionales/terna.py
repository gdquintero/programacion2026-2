a = int(input("Escriba a: "))
b = int(input("Escriba b: "))
c = int(input("Escriba c: "))

cond1 = a**2 + b**2 == c**2
cond2 = a**2 + c**2 == b**2
cond3 = b**2 + c**2 == a**2

if cond1 or cond2 or cond3:
    print("Los numeros forman una terna pitagorica")
else:
    print("Los numeros NO forman una terna pitagorica")