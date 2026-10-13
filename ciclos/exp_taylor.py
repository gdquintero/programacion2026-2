import math

n = 10
x = 0.5
suma = 0

for k in range(n+1):
    suma = suma + (x**k) / math.factorial(k)


print("Valor exacto: ", math.exp(x))
print("Valor aproximado: ", suma)