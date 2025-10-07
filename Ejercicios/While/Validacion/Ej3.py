'''
Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
'''

nota = int(input("Ingresá una nota (1 a 10): "))

while nota < 1 or nota > 10:
    print("Error: la nota debe estar entre 1 y 10.")
    nota = int(input("Ingresá una nota válida: "))

print("Nota ingresada correctamente:", nota)
