from Operaciones import area_cuadrado,area_circulo,area_triangulo,area_trapecio,area_hexagono,area_trapecio_isosceles,area_triangulo_equilatero,area_rombo,base1,base2,datos_hexagono,mostrar_hexagono,basemayor,basemenor
from Interfaz import menu,datos_cuadrado,datos_circulo,datos_triangulo,datos_trapecio,mostrar_circulo,mostrar_cuadrado,mostrar_triangulo,mostrar_trapecio,
#variables menu
CUADRADO = 1
CIRCULO = 2
TRIANGULO = 3
TRAPECIO = 4
HEXAGONO = 5
TRAPECIO_ISOSCELES = 6
TRIANGULO_EQUILATERO = 7
ROMBO = 8
SALIR = 9

opcion = 0

while opcion != SALIR:
    #Opcion menu
    opcion = menu()
    if opcion == CUADRADO:
        #Llamar la funcion de solicitar datos
        lado = datos_cuadrado()
        #Llamae a area
        area = area_cuadrado(lado)
        #Llamar a mostrar datos
        mostrar_cuadrado(area)
    elif opcion == CIRCULO:
        #Llamar la funcion de solicitar datos
        radio = datos_circulo()
        #Llamae a area
        area = area_circulo(radio)
        #Llamar a mostrar datos
        mostrar_circulo(area)
    elif opcion == TRIANGULO:
        #Llamar la funcion de solicitar datos
        base,altura = datos_triangulo()
        #Llamae a area
        area = area_triangulo(base,altura)
        #Llamar a mostrar datos
        mostrar_triangulo(area)
        
    elif opcion == TRAPECIO:
        base1,base2,altura == datos_trapecio()
        area = area_trapecio (base1,base2,altura)
        mostrar_trapecio(area)
         
    elif opcion == HEXAGONO:
        lado = datos_hexagono()
        area = area_hexagono(lado)
        mostrar_hexagono (area)
        
    elif opcion == TRAPECIO_ISOSCELES
         basemayor,basemenor,altura
        
        
    elif opcion == SALIR:
        print("Gracias por utilizar la calculadora de figuras geometricas!!!")       
    else:
        print("Opción Erronea!!!") 
    
    
    #stated