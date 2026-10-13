def factorial(n):
    fact = 1

    for i in range(1,n+1):
        fact = fact * i

    return fact

def coef_bin(n,k):
    return factorial(n) // (factorial(k) * factorial(n-k))

print(coef_bin(3,2))