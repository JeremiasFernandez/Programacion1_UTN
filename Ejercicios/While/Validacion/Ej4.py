'''
Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.
'''

print(" ")
Color = input("Ingrese su color (Por favor usar mayusculas): ")

while Color != "Rojo" and Color != "Verde" and Color != "Azul":
    print("Error, tus colores son malimos")
    Color = input("Ingresá un color válido: ")


print("Bien, su color ingresado es: ", Color)

