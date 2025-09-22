import random

altura = int(input("Ingrese la altura del jugador en cm: "))

# Determinar la posición
if altura < 160:
    posicion = "Base"
elif 160 <= altura <= 179:
    posicion = "Escolta"
elif 180 <= altura <= 199:
    posicion = "Alero"
else:
    posicion = "Ala-Pívot o Pívot"

print(f"El jugador con {altura} cm juega de {posicion}.")

nota = int(input("ingrese una nota: "))

if nota >= 6 and nota <= 10:
    print(f"Promoción directa, la nota es: {nota}")
elif nota >= 4 and nota <= 5:
    print(f"Aprobado, la nota es: {nota}")
elif nota >= 1 and nota <= 3:
    print(f"Desaprobado, la nota es: {nota}")
