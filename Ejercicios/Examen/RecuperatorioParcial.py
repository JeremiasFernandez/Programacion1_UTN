import csv
import os

ARCHIVO_CSV = "alumnos.csv"
ARCHIVO_TXT = "informe.txt"



def validarEntero(promptTxt, minVal, maxVal):
    while True:
        try:
            val = int(input(promptTxt))
            if minVal <= val <= maxVal:
                return val
            else:
                print(f"Debe estar entre {minVal} y {maxVal}.")
        except ValueError:
            print("Error 404")




def cargarEstudiantes():
    alumnos = []

    if os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, newline='', encoding='utf-8') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                try:

                    notaVal = int(row["nota"])
                    cond = row.get("condicion") or ("Promocionado" if notaVal >= 7 else ("Aprobado" if notaVal >= 4 else "Desaprobado"))
                    leg = row.get("legajo", "-")
                    alumnos.append({
                        "legajo": leg,
                        "nombre": row["nombre"],
                        "nota": notaVal,
                        "condicion": cond
                    })

                except:
                    pass

    if alumnos:
        opc = ""
        while opc not in ["R", "A"]:
            opc = input("quiere reemplazar (R) los datos existentes o Agregar (A) nuevos registros?: ").upper()

        if opc == "R":
            alumnos = []
            print("Remplazo exitoso")
        else:
            print("Se agrego exitosamente")

    cant = validarEntero("Cuantos estudiantes quiere ingresar? ", 1, 1000)

    for idx in range(cant):

        leg = input(f"Legajo del estudiante #{idx+1}: ").strip()
        while not leg or any(a.get("legajo") == leg for a in alumnos):
            leg = input("Legajo vacío o repetido. Reingrese: ").strip()


        nom = input(f"Ingrese nombre del estudiante #{idx+1}: ").strip()
        while not nom:
            nom = input("Nombre no puede estar vacio. Reingrese: ").strip()
        notaVal = validarEntero(f"Ingrese nota de {nom} (0 a 10): ", 0, 10)


        cond = "Promocionado" if notaVal >= 7 else ("Aprobado" if notaVal >= 4 else "Desaprobado")

        alumnos.append({"legajo": leg, "nombre": nom, "nota": notaVal, "condicion": cond})

   
    with open(ARCHIVO_CSV, "w", newline='', encoding='utf-8') as fh:

        camposList = ["legajo", "nombre", "nota", "condicion"]
        writer = csv.DictWriter(fh, fieldnames=camposList)
        writer.writeheader()
        for alum in alumnos:
            writer.writerow(alum)


    print("\n Datos guadados y caragados")

    return alumnos

# Mostramos el listado de estudiantes guarrdados

def mostrarEstudiantes(alumnos):
    print("\n------ LISTADO DE ESTUDIANTES ------\n")
    for alum in alumnos:
        print(f"Legajo: {alum['legajo']} | {alum['nombre']:<15} | nota: {alum['nota']} | {alum['condicion']}")
    print("\n------------------------------------")



# Buscamos a un estudiante por el nombre o el legajo

def buscarEstudiante(alumnos):
    nomBuscado = input("Ingrese el nombre del estudiante a buscar: ").strip().lower()
    hallado = False
    for alum in alumnos:
        if alum["nombre"].lower() == nomBuscado:
            print(f" Estudiante encontrado: {alum['nombre']} - Nota: {alum['nota']}")
            hallado = True
            break
    if not hallado:
        print(" Estudiante no encontrado.")


# Armamos las estadisticas

def calcularEstadisticas(alumnos):
    notasList = [e["nota"] for e in alumnos]
    prom = sum(notasList) / len(notasList)
    aprob = len([n for n in notasList if n >= 4])   
    desaprob = len(notasList) - aprob
    mejorNota = max(notasList)
    peorNota = min(notasList)

    print("\n------ ESTADÍSTICAS DE TU CURSO ------")
    print(f"Promedio general: {prom:.2f}")
    print(f"Aprobados: {aprob}")
    print(f"Desaprobados: {desaprob}")
    print(f"Nota más alta: {mejorNota}")
    print(f"Nota más baja: {peorNota}")
    print("------------------------------------")


# Hacemos el array 

def ordenarEstudiantes(alumnos):
    orden = ""
    while orden not in ["ASC", "DESC"]:
        orden = input("Como le gustaria ordenar? (ASC/DESC): ").strip().upper()
    
    copiaLista = alumnos.copy()
    copiaLista.sort(key=lambda x: x["nota"], reverse=(orden == "DESC"))

    print(f"\n--- Lista ordenada por nota ({orden}) ---")
    for alum in copiaLista:
        print(f"Nombre: {alum['nombre']:<15} | Nota: {alum['nota']}")
    print("--------------------------------------------")


# Aca generamos un informe

def generarInforme(alumnos):
    totalAlu = len(alumnos)
    notasList = [e["nota"] for e in alumnos]
    prom = sum(notasList) / totalAlu
    aprob = len([e for e in alumnos if e["nota"] >= 4])  #
    desaprob = totalAlu - aprob
    mejorAlu = max(alumnos, key=lambda e: e["nota"])
    peorAlu = min(alumnos, key=lambda e: e["nota"])

    informeTxt = (

        "INFORME FINAL DEL CURSO\n"
        "-------------------------\n"
        f"Cantidad total de estudiantes: {totalAlu}\n"
        f"Promedio general: {prom:.2f}\n"
        f"Aprobados: {aprob}\n"
        f"Desaprobados: {desaprob}\n"
        f"Mejor nota: {mejorAlu['nota']} (Alumno: {mejorAlu['nombre']})\n"
        f"Peor nota: {peorAlu['nota']} (Alumno: {peorAlu['nombre']})\n"
        "-------------------------\n"
    )

    print("\n" + informeTxt)

    with open(ARCHIVO_TXT, "w", encoding="utf-8") as fh:
        fh.write(informeTxt)

    print(f" Informe guardado en '{ARCHIVO_TXT}'.")



def filtrarPorCondicion(alumnos):
    valids = {"promocionado": "Promocionado", "aprobado": "Aprobado", "desaprobado": "Desaprobado"}
    condSel = ""
    while condSel not in valids:
        condSel = input("Condición (Promocionado/Aprobado/Desaprobado): ").strip().lower()

    condFinal = valids[condSel]
    filtrados = [a for a in alumnos if a.get("condicion") == condFinal]

    print("\n------ FILTRADOS ------\n")
    if filtrados:
        for a in filtrados:
            leg = a.get("legajo", "-")
            nom = a.get("nombre", "-")
            nota = a.get("nota", "-")
            cond = a.get("condicion", "-")
            print(f"Legajo: {leg} | Nombre: {nom:<15} | Nota: {nota} | Condición: {cond}")
    else:
        print("No hay estudiantes con esa condición.")
    print("\n-----------------------")

    guardar = ""
    while guardar not in ["S", "N"]:
        guardar = input("¿Guardar resultado en 'filtrados.csv'? (S/N): ").strip().upper()

    if guardar == "S":
        with open("filtrados.csv", "w", newline="", encoding="utf-8") as fh:
            campos = ["legajo", "nombre", "nota", "condicion"]
            writer = csv.DictWriter(fh, fieldnames=campos)
            writer.writeheader()
            for a in filtrados:
                writer.writerow({
                    "legajo": a.get("legajo", ""),
                    "nombre": a.get("nombre", ""),
                    "nota": a.get("nota", ""),
                    "condicion": a.get("condicion", "")
                })
        print("Guardado en 'filtrados.csv'.")




def menu():
    alumnos = []
    cargadoOk = False

    if os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, newline='', encoding='utf-8') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                try:

                    notaVal = int(row["nota"])
                    cond = row.get("condicion") or ("Promocionado" if notaVal >= 7 else ("Aprobado" if notaVal >= 4 else "Desaprobado"))
                    leg = row.get("legajo", "-")
                    alumnos.append({
                        "legajo": leg,
                        "nombre": row["nombre"],
                        "nota": notaVal,
                        "condicion": cond
                    })

                except:
                    pass
        if alumnos:
            cargadoOk = True


    # ------------------ menu ---------------------
    while True:
        print("\n  MENÚ DE TUS ESTUDIANTES  ")
        print("1) Cargar datos de estudiantes")
        print("2) Mostrar listado de estudiantes")
        print("3) Buscar estudiante")
        print("4) Calcular estadísticas")
        print("5) Ordenar y mostrar")
        print("6) Filtrar por condición")      # === AGREGADO ===
        print("7) Generar informe resumen")    # (renumerado)
        print("8) Salir")                      # (renumerado)
        print("==========================")
    # ------------------ menu ---------------------

        opcionSel = input("Seleccione una opción: ")

    # sistema del menu
        match opcionSel:
            case "1":
                alumnos = cargarEstudiantes()
                cargadoOk = True

            case "2" | "3" | "4" | "5" | "6" | "7":
                if cargadoOk:
                    match opcionSel:
                        case "2":
                            mostrarEstudiantes(alumnos)
                        case "3":
                            buscarEstudiante(alumnos)
                        case "4":
                            calcularEstadisticas(alumnos)
                        case "5":
                            ordenarEstudiantes(alumnos)
                        case "6":
                            filtrarPorCondicion(alumnos)   # === AGREGADO ===
                        case "7":
                            generarInforme(alumnos)
                else:
                    print("Primero debe cargar los datos.")

            case "8":
                print("Gracias por la visita :)")
                break

            case _:
                print("Opción errónea !!")



# EJECUTAR FINALMENTE EL PROGRAMA

if __name__ == "__main__":
    menu()


#Nombe = Jeremias Fernandez
#DNI = 46098893
#print("Saludos")

