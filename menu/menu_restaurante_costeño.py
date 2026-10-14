import os

# Limpiar pantalla
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menus

# Menu principal

def mostrar_menu_principal():
    limpiar()
    print("MENU PRINCIPAL")
    print("1. Entradas")
    print("2. Plato fuerte")
    print("3. Postres")
    print("4. Bebidas")
    print("0. Salir")

# Entradas

def mostrar_menu_entradas():
    limpiar()
    print("======= Entradas =======")
    print("1. Ceviche de chicharron")
    print("2. Picada mixta")
    print("3. Fritos y horneados")
    print("4. Chips de platano con queso")
    print("0. Volver al menu principal")

# Plato fuerte

def mostrar_menu_fuerte():
    limpiar()
    print("======= Plato fuerte =======")
    print("1. Sopa de mondongo")
    print("2. Mote de queso")
    print("3. Pescado y arroz de coco")
    print("4. Salchipapa")
    print("0. Volver al menu principal")

def mostrar_menu_postres():
    limpiar()
    print("======= Postres =======")
    print("1. Matrimonio bocadillo con queso")
    print("2. Arroz con leche")
    print("3. Brownie con helado")
    print("4. Alegria")
    print("0. Volver al menu principal")

def mostrar_menu_bebidas():
    limpiar()
    print("======= Bebidas =======")
    print("1. Agua")
    print("2. Gaseosas")
    print("3. Cerveza")
    print("4. Jugos naturales")
    print("0. Volver al menu principal")

# Funcionalidades de los menus

def menu_entradas():
    while True:
        mostrar_menu_entradas()
        op = int(input("Elige una opcion: "))

        if op == 1:
            print("Precio: 16500")
            input("\nPresione Enter para continuar...")
        elif op == 2:
            print("Precio: 32000")
            input("\nPresione Enter para continuar...")
        elif op == 3:
            print("Precio: 5000")
            input("\nPresione Enter para continuar...")
        elif op == 4:
            print("Precio: 8000")
            input("\nPresione Enter para continuar...")
        elif op == 0:
            break
        else:
            print("Opcion invalida")
            input("\nPresiona Enter para continuar...")

def menu_fuerte():
    while True:
        mostrar_menu_fuerte()
        op = int(input("Elige una opcion: "))

        if op == 1:
            print("Precio: 35000")
            input("\nPresione Enter para continuar...")
        elif op == 2:
            print("Precio: 28000")
            input("\nPresione Enter para continuar...")
        elif op == 3:
            print("Precio: 50000")
            input("\nPresione Enter para continuar...")
        elif op == 4:
            print("Precio: 25000")
            input("\nPresione Enter para continuar...")
        elif op == 0:
            break
        else:
            print("Opcion invalida")
            input("\nPresiona Enter para continuar...")

def menu_postres():
    while True:
        mostrar_menu_postres()
        op = int(input("Elige una opcion: "))

        if op == 1:
            print("Precio: 15000")
            input("\nPresione Enter para continuar...")
        elif op == 2:
            print("Precio: 15000")
            input("\nPresione Enter para continuar...")
        elif op == 3:
            print("Precio: 25000")
            input("\nPresione Enter para continuar...")
        elif op == 4:
            print("Precio: 8000")
            input("\nPresione Enter para continuar...")
        elif op == 0:
            break
        else:
            print("Opcion invalida")
            input("\nPresiona Enter para continuar...")

def menu_bebidas():
    while True:
        mostrar_menu_bebidas()
        op = int(input("Elige una opcion: "))

        if op == 1:
            print("Precio: 15000")
            input("\nPresione Enter para continuar...")
        elif op == 2:
            print("Precio: 5000")
            input("\nPresione Enter para continuar...")
        elif op == 3:
            print("Precio: 7000")
            input("\nPresione Enter para continuar...")
        elif op == 4:
            print("Precio: 12000")
            input("\nPresione Enter para continuar...")
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
        menu_entradas()
    elif op == 2:
        menu_fuerte()
    elif op == 3:
        menu_postres()
    elif op == 4:
        menu_bebidas()
    elif op == 0:
        print("Hasta luego :) ")
        break
    else:
        print("Opcion invalida")
        input("\nPresiona Enter para continuar...")
