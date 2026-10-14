import numpy as np
import os

# Limpiar pantalla
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Definir un vector
def leer_vector(n):
    x = np.zeros(n)

    for i in range(n):
        x[i] = float(input(f"Componente {i+1}: "))

    return x

# Definir una matriz
def leer_matriz(m,n):
    matriz = np.zeros((m,n))

    for i in range(m):
        for j in range(n):
            matriz[i,j] = float(input(f"Componente {i+1,j+1}: "))

    return matriz

# Menus

def mostrar_menu_principal():
    limpiar()
    print("MENU PRINCIPAL")
    print("1. Operaciones aritmeticas")
    print("2. Operaciones con vectores")
    print("3. Operaciones con matrices")
    print("0. Salir")

def mostrar_menu_operaciones_aritmeticas():
    limpiar()
    print("Operaciones aritmeticas")
    print("1. Adicion de dos numeros")
    print("2. Multiplicacion de dos numeros")
    print("3. Potencia de un numero")
    print("0. Volver al menu principal")

def mostrar_menu_operaciones_vectores():
    limpiar()
    print("Operaciones con vectores")
    print("1. Adicion de dos vectores")
    print("2. Producto punto de dos vectores")
    print("3. Producto cruz de dos vectores")
    print("0. Volver al menu principal")

def mostrar_menu_operaciones_matrices():
    limpiar()
    print("Operaciones con matrices")
    print("1. Adicion de dos matrices")
    print("2. Multiplicacion de dos matrices")
    print("3. Transpuesta de una matriz")
    print("0. Volver al menu principal")

# Operaciones aritmeticas

def menu_aritmetica():
    while True:
        mostrar_menu_operaciones_aritmeticas()
        op = int(input("Elige una opcion: "))

        if op == 1:
            a = float(input("Numero 1: "))
            b = float(input("Numero 2: "))

            print(f"La adicion es {a+b}")
            input("\nPresiona Enter para continuar...")

        elif op == 2:
            a = float(input("Numero 1: "))
            b = float(input("Numero 2: "))

            print(f"La multiplicacion es {a*b}")
            input("\nPresiona Enter para continuar...")

        elif op == 3:
            b = float(input("Base: "))
            n = float(input("Exponente: "))
            print(f"{b} elevado a la {n} es {b**n}")
            input("\nPresiona Enter para continuar...")

        elif op == 0:
            break

        else:
            print("Opcion invalida")
            input("\nPresiona Enter para continuar...")

# Operaciones con vectores

def menu_vectores():
    while True:
        mostrar_menu_operaciones_vectores()
        op = int(input("Elige una opcion: "))

        if op == 1:
            n = int(input("Dimension de los vectores: "))

            print("\nComponentes del primer vector")
            x = leer_vector(n)

            print("\nComponentes del segundo vector")
            y = leer_vector(n)

            print(f"La adicion de los vectores es {x+y}")
            input("\nPresiona Enter para continuar...")

            del x
            del y

        elif op == 2:
            n = int(input("Dimension de los vectores: "))

            print("\nComponentes del primer vector")
            x = leer_vector(n)

            print("\nComponentes del segundo vector")
            y = leer_vector(n)

            print(f"El producto interno de los vectores es {x @ y}")
            input("\nPresiona Enter para continuar...")

            del x
            del y

        elif op == 3:
            print("\nComponentes del primer vector")
            x = leer_vector(3)

            print("\nComponentes del segundo vector")
            y = leer_vector(3)

            print(f"El producto cruz de los vectores es {np.cross(x,y)}")
            input("\nPresiona Enter para continuar...")

            del x
            del y

        elif op == 0:
            break

        else:
            print("Opcion invalida")
            input("\nPresiona Enter para continuar...")


# Operaciones con matrices

def menu_matrices():
    while True:
        mostrar_menu_operaciones_matrices()
        op = int(input("Elige una opcion: "))

        if op == 1:
            m = int(input("Numero de filas: "))
            n = int(input("Numero de columnas: "))

            print("\nComponentes de la primera matriz")
            A = leer_matriz(m,n)

            print("\nComponentes de la segunda matriz")
            B = leer_matriz(m,n)

            print(f"La adicion de las matrices es {A+B}")
            input("\nPresiona Enter para continuar...")

            del A
            del B

        elif op == 2:
            m = int(input("m: "))
            n = int(input("n: "))
            p = int(input("p: "))

            print("\nComponentes de la primera matriz")
            A = leer_matriz(m,n)

            print("\nComponentes de la segunda matriz")
            B = leer_matriz(n,p)

            print(f"La multiplicacion de las matrices es {A@B}")
            input("\nPresiona Enter para continuar...")

            del A
            del B

        elif op == 3:
            m = int(input("m: "))
            n = int(input("n: "))

            print("\nComponentes de la primera matriz")
            A = leer_matriz(m,n)

            print(f"La transpuesta de la matriz es \n \n {np.transpose(A)}")
            input("\nPresiona Enter para continuar...")

            del A

        elif op == 0:
            break

        else:
            print("Opcion invalida")
            input("\nPresiona Enter para continuar...")

# Menu principal
while True:
    mostrar_menu_principal()
    op = int(input("Elige una opcion: "))

    if op == 1:
        menu_aritmetica()
    elif op == 2:
        menu_vectores()
    elif op == 3:
        menu_matrices()
    elif op == 0:
        print("Hasta luego :) ")
        break
    else:
        print("Opcion invalida")
        input("\nPresiona Enter para continuar...")



