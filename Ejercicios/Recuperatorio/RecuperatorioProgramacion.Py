import csv
import os

ARCHIVO_CSV = "alumnos.csv"
ARCHIVO_FILTRADOS = "filtrados.csv"
ARCHIVO_TXT = "informe.txt"




# Aca validamos si el numero entra enn el rango
def validar_entero(prompt, minimo, maximo):
    while True:
        try:

            valor = int(input(prompt))
            if minimo <= valor <= maximo:
                return valor
            
            else:
                print(f"Debe estar entre {minimo} y {maximo}.")

        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

# Funcion de condicion
def calcular_condicion(nota):
    if nota >= 6:
        return "Promocionado!!!"
    elif nota >= 4:
        return "Aprobado"
    else:
        return "Desaprobado"


# Aca agregamos a los estudiantes nuevos
def cargar_estudiantes():
    estudiantes = []

    # Si existe el archivo, cargarlo
    if os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, newline='', encoding='utf-8') as f:     # abre

            lector = csv.DictReader(f)
            for fila in lector:
                estudiantes.append({
                    "legajo": int(fila["legajo"]),
                    "nombre": fila["nombre"],
                    "nota": int(fila["nota"]),
                    "condicion": fila["condicion"]
                })

        f.close() # cierra 

    # Si hay datos, preguntar si se reemplazan o agregan
    if estudiantes:
        print("Se detectó un archivo con información de alumnos.")
        eleccion = ""

        while eleccion not in ["R", "A"]:
            eleccion = input("desea Reemplazar (R) o Agregar (A) nuevos registros?: ").upper()

        if eleccion == "R":
            estudiantes = []
            print("se reemplazarán los datos existentes.")

        else:
            print("se agregarán nuevos registros.")

    n = validar_entero("cuántos estudiantes desea ingresar?: ", 1, 1000)

    for i in range(n):
        print(f"\n--- Estudiante #{i+1} ---")
        legajo = validar_entero("Ingrese su legajo (1000-9999): ", 1000, 9999)
        nombre = input("Ingrese nombre: ").strip()

        while not nombre:
            nombre = input("Nombre no puede estar vacío. Reingrese: ").strip()
        nota = validar_entero("Ingrese nota (0-10): ", 0, 10)
        condicion = calcular_condicion(nota)
        estudiantes.append({

            "legajo": legajo,
            "nombre": nombre,
            "nota": nota,
            "condicion": condicion
        })

    # guardar todo en CSV
    with open(ARCHIVO_CSV, "w", newline='', encoding="utf-8") as f:
        campos = ["legajo", "nombre", "nota", "condicion"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(estudiantes)
    f.close()

    print(" ")
    print("Datos cargados y guardados correctamente.")
    return estudiantes


def mostrar_estudiantes(estudiantes):
    print("\n------ LISTADO DE ESTUDIANTES ------\n")

    for e in estudiantes:
        print(f"Legajo: {e['legajo']} | Nombre: {e['nombre']:<15} | Nota: {e['nota']} | Condición: {e['condicion']}")

    print("\n------------------------------------")


def buscar_estudiante(estudiantes):
    while True:
        dato = input("Ingrese nombre o legajo del estudiante: ").strip().lower()
        encontrado = None

        for e in estudiantes:
            if e["nombre"].lower() == dato or str(e["legajo"]) == dato:
                encontrado = e
                break

        if encontrado:
            print(f"\nEstudiante encontrado:")
            print(f"Legajo: {encontrado['legajo']} | Nombre: {encontrado['nombre']} | Nota: {encontrado['nota']} | Condición: {encontrado['condicion']}")
            break

        else:
            print("Estudiante no encontrado. Intente de nuevo.")


def calcular_estadisticas(estudiantes):
    notas = [e["nota"] for e in estudiantes]
    promedio_general = sum(notas) / len(notas)

    total = len(estudiantes)
    promo = len([e for e in estudiantes if e["condicion"] == "Promocionado"])
    aprob = len([e for e in estudiantes if e["condicion"] == "Aprobado"])
    desap = len([e for e in estudiantes if e["condicion"] == "Desaprobado"])

    mejor = max(estudiantes, key=lambda e: e["nota"])
    peor = min(estudiantes, key=lambda e: e["nota"])

    promedio_promocionados = (
        sum([e["nota"] for e in estudiantes if e["condicion"] == "Promocionado"]) / promo
        if promo > 0 else 0
    )

    print("\n------ ESTADÍSTICAS ------")
    print(f"Promedio general: {promedio_general:.2f}")
    print(f"Promocionados: {promo} ({promo*100/total:.1f}%)")
    print(f"Aprobados: {aprob} ({aprob*100/total:.1f}%)")
    print(f"Desaprobados: {desap} ({desap*100/total:.1f}%)")
    print(f"Mejor nota: {mejor['nota']} (Alumno: {mejor['nombre']})")
    print(f"Peor nota: {peor['nota']} (Alumno: {peor['nombre']})")
    print(f"Promedio de promocionados: {promedio_promocionados:.2f}")
    print("--------------------------")




def ordenar_estudiantes(estudiantes):
    campo = ""

    while campo not in ["nombre", "nota"]:
        campo = input("¿Desea ordenar por 'nombre' o 'nota'?: ").strip().lower()
    orden = ""

    while orden not in ["ASC", "DESC"]:
        orden = input("¿Orden ascendente (ASC) o descendente (DESC)?: ").strip().upper()


    copia = estudiantes.copy()
    copia.sort(key=lambda x: x[campo].lower() if campo == "nombre" else x[campo], reverse=(orden == "DESC"))


    print(f"\n--- Lista ordenada por {campo} ({orden}) ---")


    for e in copia:
        print(f"Legajo: {e['legajo']} | Nombre: {e['nombre']:<15} | Nota: {e['nota']} | Condición: {e['condicion']}")
    print("--------------------------------------------")




def filtrar_por_condicion(estudiantes):
    condicion = ""
    while condicion not in ["Promocionado", "Aprobado", "Desaprobado"]:
        condicion = input("Ingrese condición a filtrar (Promocionado/Aprobado/Desaprobado): ").capitalize()

    filtrados = [e for e in estudiantes if e["condicion"] == condicion]

    if not filtrados:
        print(f"No hay estudiantes con condición '{condicion}'.")
    else:
        print(f"\n--- Estudiantes {condicion} ---")
        for e in filtrados:
            print(f"Legajo: {e['legajo']} | Nombre: {e['nombre']} | Nota: {e['nota']}")
        print("--------------------------------")

        guardar = input("¿Desea guardar este resultado en filtrados.csv? (S/N): ").upper()
        if guardar == "S":
            with open(ARCHIVO_FILTRADOS, "w", newline='', encoding="utf-8") as f:
                campos = ["legajo", "nombre", "nota", "condicion"]
                escritor = csv.DictWriter(f, fieldnames=campos)
                escritor.writeheader()
                escritor.writerows(filtrados)
            print("Archivo 'filtrados.csv' guardado correctamente.")



def generar_informe(estudiantes):
    total = len(estudiantes)
    notas = [e["nota"] for e in estudiantes]
    promedio = sum(notas) / total
    promo = len([e for e in estudiantes if e["condicion"] == "Promocionado"])
    aprob = len([e for e in estudiantes if e["condicion"] == "Aprobado"])
    desap = len([e for e in estudiantes if e["condicion"] == "Desaprobado"])
    mejor = max(estudiantes, key=lambda e: e["nota"])
    peor = min(estudiantes, key=lambda e: e["nota"])
    prom_promo = (
        sum([e["nota"] for e in estudiantes if e["condicion"] == "Promocionado"]) / promo
        if promo > 0 else 0
    )



    informe = (
        "INFORME FINAL DEL CURSO\n"
        "------------------------------\n"
        f"Cantidad total de estudiantes: {total}\n"
        f"Promedio general: {promedio:.2f}\n"
        f"Promocionados: {promo} ({promo*100/total:.1f}%)\n"
        f"Aprobados: {aprob} ({aprob*100/total:.1f}%)\n"
        f"Desaprobados: {desap} ({desap*100/total:.1f}%)\n"
        f"Mejor nota: {mejor['nota']} (Alumno: {mejor['nombre']})\n"
        f"Peor nota: {peor['nota']} (Alumno: {peor['nombre']})\n"
        f"Promedio de promocionados: {prom_promo:.2f}\n"
        "------------------------------\n"
    )



    print("\n" + informe)
    with open(ARCHIVO_TXT, "w", encoding="utf-8") as f:
        f.write(informe)
    print("Informe guardado en 'informe.txt'.")



def menu():
    estudiantes = []
    cargado = False

    if os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                estudiantes.append({
                    "legajo": int(fila["legajo"]),
                    "nombre": fila["nombre"],
                    "nota": int(fila["nota"]),
                    "condicion": fila["condicion"]
                })
        if estudiantes:
            cargado = True

 # --------------------- Menu -----------------------------#

    while True:
        print("\n======= MENÚ PRINCIPAL =======")
        print("1) Cargar datos de estudiantes")
        print("2) Mostrar listado de estudiantes")
        print("3) Buscar estudiante")
        print("4) Calcular estadísticas")
        print("5) Ordenar y mostrar")
        print("6) Filtrar por condición")
        print("7) Generar informe resumen")
        print("8) Salir")
        print("==============================")

        opcion = input("Seleccione una opción: ")

 # ---------------------     -----------------------------#

        # Algoritmo del menu

        if opcion == "1":
            estudiantes = cargar_estudiantes()
            cargado = True

        elif opcion == "2" and cargado:
            mostrar_estudiantes(estudiantes)

        elif opcion == "3" and cargado:
            buscar_estudiante(estudiantes)

        elif opcion == "4" and cargado:
            calcular_estadisticas(estudiantes)

        elif opcion == "5" and cargado:
            ordenar_estudiantes(estudiantes)

        elif opcion == "6" and cargado:
            filtrar_por_condicion(estudiantes)

        elif opcion == "7" and cargado:
            generar_informe(estudiantes)

        elif opcion == "8":
            print("\nGracias por usar el programa. ¡Hasta luego!")
            break

        else:
            print("Opción inválida o no disponible. Cargue los datos primero.")



if __name__ == "__main__":
    menu()
