'''
Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos 
y devolver el número más grande.

'''


def numerazo(a, b, c):
    m = a
    if b > m:
        m = b

    if c > m:
        m = c
    return m

lista = [8, 2, 42]


resultado = numerazo(*lista)


    
print("el numero mas grande es", resultado)
print(" ")



def benji():
    for i in range (0, len(lista)):
        if i == 0:
            maximo = lista [i]
        elif lista [i] > maximo:
            maximo = lista [i]
    return maximo

print("el numero mas grande es", benji())
