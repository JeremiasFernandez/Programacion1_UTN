'''
Diseña una función que calcule la potencia de un número. 
La función debe recibir la base y el exponente como argumentos y devolver el resultado.
'''

def potenciaEpica(base, exponente):
    return base ** exponente
    

while True:

    b = int(input("Ingrese el numero: "))
    e = int(input("Ingrese el exponente: "))

    print("El resultadin es... prrrr: ", potenciaEpica(b, e))

    if b == 666:
        print(" ")
        print("Ya lo cerraste epico chispa")
        break
