import math

x = 10
eps = 1e-12
k = 0
iter = 0
max_iter = 10

term = (x**(2*k + 1)) / math.factorial(2*k + 1)
sinx = ((-1)**k) * term

while abs(term) >= eps and iter < max_iter:
    k = k + 1
    iter = iter + 1
    term = (x**(2*k + 1)) / math.factorial(2*k + 1)
    sinx = sinx + ((-1)**k) * term

print("Valor exacto: ", math.sin(x))
print("Valor Aproximado: ", sinx, " con ",k," iteraciones.")