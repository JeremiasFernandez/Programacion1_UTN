'''
1) Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”.

a) Si es invierno: solo se viaja a Bariloche.
b) Si es verano: se viaja a Mar del plata y Cataratas.
c) Si es otoño: se viaja a todos los lugares.
d) Si es primavera: se viaja a todos los lugares menos Bariloche.

'''

destino = input("¿A qué destino deseas viajar?: ")
estacion = input("Ingrese la estación del año: ")

match estacion:
    case "invierno":
        if destino == "Bariloche":
            print("Se viaja")
        else:
            print("No se viaja")

    case "verano" :
        if destino == "Mar del plata" or destino == "Cataratas":
            print("Se viaja")
        else:
            print("No se viaja")

    case "otoño": 
        print("Se viaja")
        
    case "primavera":
        if destino != "Bariloche":
            print("Se viaja")
        else:
            print("No se viaja")