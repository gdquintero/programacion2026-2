figura = input("Escriba una figura: ")

match figura:
    case "circulo":
        print("No tiene lados")
    case "triangulo":
        print("3 lados")
    case "cuadrado":
        print("4 lados")
    case "pentagono":
        print("5 lados")
    case _:
        print("Figura no reconocida")