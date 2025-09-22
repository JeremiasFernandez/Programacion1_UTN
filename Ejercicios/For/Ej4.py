''' Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

# 	5 x 0 = 0
# 	5 x 1  = 5
# 	5 x 2 = 10
# 	5 x 3  = 15  '''


num= int(input("Ingresa un numero: "))

print("Inicio de la tabla de multiplicacion:")

for i in range (1, 11):
    resultado= num * i
    print(f"{num} x {i} = {resultado}")

print("Tabla finalizada con exito")

