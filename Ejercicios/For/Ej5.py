'''Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
número 0. Mostrar la suma y el promedio de todos los números. '''

suma= 0
contador = 0

for i in range (11):
    numero = float(input(f"Ingrese el número {i + 1} (0 para terminar): "))

    if numero == 0:
        break

    suma =+ numero
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"\nSuma de los números: {suma}")
    print(f"Promedio de los números: {promedio}")
else:
    print("\nNo se ingresaron números.")