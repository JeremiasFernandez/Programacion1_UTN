'''
Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
'''

def pedirNum():
    numero = float(input("Ingresa el numerin chavalin: "))
    return numero

n = pedirNum()
print("Ingresaste el numero: ", n)