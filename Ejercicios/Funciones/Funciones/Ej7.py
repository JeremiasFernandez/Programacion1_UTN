'''
Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, 
False en caso contrario.

'''

numero = int(input("di un num jej: "))

def parImpar(num):

    if num % 2 == 0:
        print("el numero es par")
        return True
    else:
        print("el numero es impar")
        return False

    
esPar = parImpar(numero)
print("ay benjamin benjamin: ", esPar)