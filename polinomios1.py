import numpy as np

n = int(input("Grado del primer polinomio: "))
m = int(input("Grado del segundo polinomio: "))

p = np.zeros(n+1)
q = np.zeros(m+1)

print("\nCoeficientes de primer polinomio")
for i in range(n+1):
    p[i] = float(input(f"Escriba coeficiente p({i}): "))

print("\nCoeficientes de segundo polinomio")

for i in range(m+1):
    q[i] = float(input(f"Escriba coeficiente q({i}): "))

if n >= m:
    for i in range(m+1):
        p[i] = p[i] + q[i]

    print(p)
else:
    for i in range(n+1):
        q[i] = p[i] + q[i]

    print(q)
