#funcion menu
def menu():
    """
    Muestra el menu al usuario y devuelve la opcion digitada en formato int
    """
    print("\n Calculadora de figuras geometricas")
    print("1. Calcular area del cuadrado")
    print("2. Calcular area del circulo")
    print("3. Calcular area del triangulo")
    print("4. Calcular area del trapecio")
    print("5. Calcular area del hexagono")
    print("6. Calcular area del trapecio_isosceles")
    print("7. Calcular area del triangulo_equilatero")
    print("8. Calcular area del rombo")
    print("9 Salir")
    op = int(input("Digite la opción: "))
    return op

#funcion solicitar datos
def datos_cuadrado():
    """
    Solicitar el lado del cuadrado y lo transforma y retorna float
    """
    lado = float(input("Digite el lado: "))
    return lado

#funcion solicitar datos
def datos_circulo():
    """
    Solicitar el radio del circulo y lo transforma y retorna float
    """
    radio = float(input("Digite el radio: "))
    return radio

#funcion solicitar datos
def datos_triangulo():
    """
    Solicitar base y altura del triangulo y lo transforma y retorna float base y altura
    """
    base = float(input("Digite la base: "))
    altura = float(input("Digite la altura: "))
    return base,altura

def datos_trapecio():
    base1 = float(input("Digite la base_1: "))
    base2 = float(input("Digite la base_2: "))
    altura = float(input("Digite la altura: "))
    return base1,base2,altura

def datos_hexagono():
    lado = float(input("Digite el lado: "))
    return lado

def datos_trapecio_isosceles():
    basemayor = float(input("Digite la base mayor: "))
    basemenor = float(input("Digite la base menor: "))
    altura = float(input("Digite la altura: "))
    return basemayor,basemenor,altura

def datos_triangulo_equilatero():
    lado = float(input("Digite el lado: "))
    return lado

def datos_rombo():
    diagonal1 = float(input("Digite la diagonal1: "))
    diagonal2 = float(input("Digite la diagonal2: "))
    return diagonal1,diagonal2
    
    

#Funcion mostrar datos
def mostrar_cuadrado(area):
    """
    Muestra el area del cuadrado al usuario final
    """
    print(f"El area del cuadrado es {area} mts^2")

def mostrar_circulo(area):
    """
    Muestra el area del circulo al usuario final
    """
    print(f"El area del circulo es {area} mts^2")

def mostrar_triangulo(area):
    """
    Muestra el area del triangulo al usuario final
    """
    print(f"El area del triangulo es {area} mts^2")
    
def mostrar_trapecio(area):
    print(f"El area del tapecio es {area} mts^2")
    
def mostrar_hexagono(area):
    print(f"El area del hexagono es {area} mts^2")
    
def mostrar_trapecio_isosceles(area):
    print(f"El area del trapecio isosceles es {area} mts^2")
    
def mostrar_triangulo_equilatero(area):
    print(f"El area del triangulo equilatero es {area} mts^2")
    
def mostrar_rombo(area):
    print(f"El area del rombo es {area} mts^2")
