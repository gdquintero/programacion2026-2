import math

n = 10
x = 5
cosx = 0

for k in range(n):
    cosx = cosx + ((-1)**k) * (x**(2*k)) / math.factorial(2*k)

print("Valor exacto: ", math.cos(x))
print("Valor Aproximado: ", cosx)