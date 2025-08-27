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

nota = random.randint(1, 10)

if nota >= 6:
    print("Promoción directa, la nota es {nota}.")
elif nota in [4, 5]:
    print("Aprobado, la nota es {nota}.")
else:
    print("Desaprobado, la nota es {nota}.")
