def es_float(string: str) -> bool:
    """
    PRE:
    POST: Devuelve True si el string ingresado es casteable a float.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def ingresar_float_positivo(mensaje: str) -> float:
    """
    PRE:
    POST: Devuelve un número float positivo (mayor o igual que 0).
    """
    numero = input(mensaje)
    while not (es_float(numero) and float(numero) >= 0):
        numero = input("La entrada no es válida. Ingrese nuevamente: ")
    return float(numero)
