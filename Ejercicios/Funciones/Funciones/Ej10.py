'''
Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

'''

import math
def primates(numero):

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

while True:

    n = int(input("numerin: "))

    if primates(n) == True:
        print("es primo jeje")

    else: 
        print("Es falsiño jeje")
