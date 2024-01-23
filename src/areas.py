from math import pi, pow


def calcular_area_rectangulo(base: float, altura: float) -> float:
    """
    PRE: Base y altura deben ser números positivos.
    POST: Devuelve el área del rectángulo.
    """
    return round(base * altura, 2)


def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    PRE: Base y altura deben ser números positivos.
    POST: Devuelve el área del triángulo.
    """
    return round(base * altura / 2, 2)


def calcular_area_circulo(radio: float) -> float:
    """
    PRE: Radio debe ser un número positivo.
    POST: Devuelve el área del círculo.
    """
    return round(pi * pow(radio, 2), 2)
