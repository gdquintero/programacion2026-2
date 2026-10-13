x1 = float(input("x1: "))
y1 = float(input("y1: "))
r1 = float(input("r1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
r2 = float(input("r2: "))

d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
s = r1 + r2
t = abs(r1 - r2)

if d == 0:
    print("Concentricas")
elif d < t:
    print("Una interior a la otra sin contacto")
elif abs(d - t) <= 0:
    print("Tangentes interiores")
elif d < s:
    print("Secantes")
elif abs(d - s) <= 0:
    print("Tangentes exteriores")
else:
    print("Exteriores")