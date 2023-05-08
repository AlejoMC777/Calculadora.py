#Importar libreria
import math

#Funciones
def area_cuadrado(lado):
    """
    Calcula el area del cuadrado y retorna una variable
    que se llama area en formato float
    """
    area = lado*lado
    return area

def area_circulo(radio):
    """
    Calcula el area del circulo y retorna una variable
    que se llama area en formato float
    """
    area = math.pi*radio**2
    return area

def area_triangulo(base,altura):
    """
    Calcula el area del triangulo y retorna una variable
    que se llama area en formato float
    """
    area = (base*altura)/2
    return area

def area_trapecio(base1, base2, altura):
    area_trapecio = ((base1 + base2) / 2) * altura
    return area_trapecio
"""
    Calcula el area del trapecio y retorna una variable
    que se llama area en formato float
    """

def area_hexagono(lado):
    area_hexagono = (3 * math.sqrt(3) / 2) * lado**2
    return area_hexagono
"""
    Calcula el area del hexagono y retorna una variable
    que se llama area en formato float
    """
def area_trapecio_isosceles(base_mayor, base_menor, altura):
    area_trapecio_isosceles = ((base_mayor + base_menor) / 2) * altura
    return area_trapecio_isosceles
"""
    Calcula el area del trapecio_isosceles y retorna una variable
    que se llama area en formato float
    """
def area_triangulo_equilatero(lado):
    area_triangulo_equilatero = (math.sqrt(3) / 4) * lado**2
    return area_triangulo_equilatero

def area_rombo(diagonal1, diagonal2):
    area_rombo = (diagonal1 * diagonal2) / 2
    return area_rombo

