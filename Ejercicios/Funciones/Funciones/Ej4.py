'''
Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 
'''
# Hago la funcion
def areaRectangulo(b, h):
    area = b * h
    return area

# Agarro los datos del area
b = float(input("Ingresá la base del rectángulo: "))
h = float(input("Ingresá la altura del rectángulo: "))


# Resultado
resultado = areaRectangulo(b, h)
print("El área del rectángulo es:", resultado)