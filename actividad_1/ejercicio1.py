a = 12378
b = 3054

num1, num2 = a, b

r = a % b

while r != 0:
    a = b
    b = r
    r = a % b

print(f"mcd({num1},{num2}) = {b}")
