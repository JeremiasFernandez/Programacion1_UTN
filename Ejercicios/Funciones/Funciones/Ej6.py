'''
Crea una función que verifique si un número dado es par o impar. 
La función debe imprimir un mensaje indicando si el número es par o impar.

'''
numero = int(input("di un num jej: "))

def parImpar(num):

    if num % 2 == 0:
        print("el numero es par")
    else:
        print("el numero es impar")
    
parImpar(numero)
print("ay benjamin benjamin: ", numero)