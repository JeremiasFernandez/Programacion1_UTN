'''
Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. 
Tendrá intentos indeterminados.
'''

print(" ")

intentos = 0

while intentos < 3:
    clave = "skibidi"
    
    print("Solo hay 3 intentos")

    ponerClave = input("Ingrese la clave: " )

    if ponerClave == clave:
        print("¡Contraseña correcta!")
        break

    else:
        print("Contraseña incorrecta, vuelva a probar")
        intentos += 1

if intentos == 3: 
    print("Se acabaron las chances chaval")