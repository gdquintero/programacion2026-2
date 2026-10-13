def arctan(x):
    eps = 1e-4
    k = 0
    term = x**(2*k + 1) / (2*k + 1)
    atan = term

    while abs(term) >= eps:
        k = k + 1
        term = x**(2*k + 1) / (2*k + 1)
        atan = atan + ((-1)**k) * term

    return atan


print("Valor exacto: ", math.atan(0.5))
print("Valor aproximado: ",arctan(0.5))