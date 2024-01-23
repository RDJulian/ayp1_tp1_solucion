from math import pi


def calcular_perimetro_rectangulo(base: float, altura: float) -> float:
    """
    PRE: Base y altura deben ser números positivos.
    POST: Devuelve el perímetro del rectángulo.
    """
    return round((base + altura) * 2, 2)


def calcular_perimetro_circulo(radio: float) -> float:
    """
    PRE: Radio debe ser un número positivo.
    POST: Devuelve el perímetro del círculo.
    """
    return round(pi * radio * 2, 2)
