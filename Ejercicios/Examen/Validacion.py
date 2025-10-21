import csv

def cargarEquipos():
    import csv

    f = open("alumnos.csv", "a", encoding="utf-8")

    while True:
        nombre = input("Ingresa el nombre (Enter para salir): ")
        if nombre == "":
            break
        nota = input("Ingresa la nota del 1 al 10: ")
        f.write(f"{nombre},{nota}\n")

    f.close()



def listadoEstudiantes():
    f = open("alumnos.csv", "r") # abre

    print("-------------------------")
    for linea in f:
        linea = linea.strip()
        if linea == " ": 
            continue
        nombre, nota = linea.split(",", 1)
        print(f"Nombre: {nombre}\t| Nota: {nota}")
        print("-------------------------")

    f.close() # cierra jejje

def buscarAlumno():
    buscado = input("Nombre a buscar: ").strip().lower()
    existe = False

    f = open("alumnos.csv", "r", encoding="utf-8")

    for linea in f:
        linea = linea.strip()
        if not linea:
            continue
        nombre = linea.split(",", 1)[0]

        if nombre.strip().lower() == buscado:
            existe = True
            break

    f.close()

    print("Existe" if existe else "No existe")
