'''
Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.
'''

print(" ")

while True:
    clave = "skibidi"
    ponerClave = input("Ingrese la clave: ")

    if ponerClave == clave:
        print("¡Contraseña correcta!")
        break

    else:
        print("Contraseña incorrecta, vuelva a probar")