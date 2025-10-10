'''
Escribe una función que calcule el área de un círculo. La función debe recibir el radio como 
'''

import math  # para usar el valor de π (pi)

def areaCirculo(radio):
    area = math.pi * (radio ** 2)
    return area

radio = float(input("Ingresá el radio del círculo: "))
resultado = areaCirculo(radio)
print("El área del círculo es:", resultado)