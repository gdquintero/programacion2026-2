a = 17
b = a % 5
c = a // b + b ** 3
d = c - a
clave = []

if a > c and not d < 0:
    clave.append("W")
    a = a - c
elif a % b == 1 or c // a > 1:
    clave.append("Q")
    b = b + d
    if b > 0 and c % 4 == 0:
        clave.append(c)
        c = c // 3

if a > b > d:
    if c > 5:
        clave.append("#")
    elif c == 5 and (a + b) % 3 == 0:
        clave.append("m")
        clave.append(c)
        d = a - 3 * c
    else:
        clave.append(c - a)
    if d > 0 or a // 0 == 1:
        clave.append(a * d)
        clave.append("!")
print(clave)