from validaciones import ingresar_float_positivo
from perimetros import calcular_perimetro_circulo, calcular_perimetro_rectangulo
from areas import calcular_area_triangulo, calcular_area_rectangulo, calcular_area_circulo

# Constantes.
RECTANGULO = "1"
TRIANGULO = "2"
CIRCULO = "3"
SALIR = "4"


def imprimir_mensaje_inicial() -> None:
    """
    PRE:
    POST: Imprime el menú de opciones válidas.
    """
    print("Calculadora de áreas y perímetros.\n")
    print("1. Rectángulo\n2. Triángulo\n3. Círculo\n4. Salir\n")


def ingresar_base_altura(figura: str) -> tuple[float, float]:
    """
    PRE:
    POST: Devuelve la base y altura de la figura (ambas positivas).
    """
    base = ingresar_float_positivo(f"Ingrese la base del {figura}: ")
    altura = ingresar_float_positivo(f"Ingrese la altura del {figura}: ")
    return base, altura


def procesar_opcion(opcion: str) -> None:
    """
    PRE:
    POST: Ejecuta la opción ingresada o un mensaje de error en caso de no ser válida.
    """
    if opcion == RECTANGULO:
        base, altura = ingresar_base_altura("rectángulo")
        print(f"El perímetro del rectángulo es {calcular_perimetro_rectangulo(base, altura)}.")
        print(f"El área del rectángulo es {calcular_area_rectangulo(base, altura)}.")
    elif opcion == TRIANGULO:
        base, altura = ingresar_base_altura("triángulo")
        print(f"El área del triángulo es {calcular_area_triangulo(base, altura)}.")
    elif opcion == CIRCULO:
        radio = ingresar_float_positivo("Ingrese el radio del círculo: ")
        print(f"El perímetro del círculo es {calcular_perimetro_circulo(radio)}.")
        print(f"El área del círculo es {calcular_area_circulo(radio)}.")
    elif opcion != SALIR:
        print("La opción ingresada no es válida.")


def main():
    imprimir_mensaje_inicial()
    opcion = ""
    while opcion != SALIR:
        opcion = input("Ingrese una opción: ")
        procesar_opcion(opcion)


if __name__ == "__main__":
    main()
