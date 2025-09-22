'''
Ejercicio 1:

A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot

'''

# Aqui pondremos valor a la altura del usuario

altura = int(input("Ingrese la altura del jugador en cm: "))

# Aqui determinamos la posicion del usaurio
if altura < 160:
    posicion = "Base"
elif 160 <= altura <= 179:
    posicion = "Escolta"
elif 180 <= altura <= 199:
    posicion = "Alero"
else:
    posicion = "Ala Pívot o Pívot"

# Y para finalizar pondremos el print

print(f"El jugador con {altura} cm juega de {posicion}.")

