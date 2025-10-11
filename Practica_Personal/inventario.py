"""Módulo con funciones para gestionar el inventario de equipos tecnológicos."""
from __future__ import annotations

import csv
import os
from typing import Dict, List

from Practica_Personal.validaciones import (
    pedir_entero_positivo,
    pedir_float_positivo,
    pedir_opcion,
    pedir_texto_no_vacio,
)

EQUIPOS_CSV = "equipos.csv"
INFORME_TXT = "informe_inventario.txt"
CATEGORIAS = ("router", "pc", "notebook", "impresora")
ESTADOS = ("funcional", "fuera de servicio")

Equipo = Dict[str, object]


def leer_equipos_desde_csv(ruta_archivo: str = EQUIPOS_CSV) -> List[Equipo]:
    """Lee los equipos almacenados en el archivo CSV."""
    if not os.path.exists(ruta_archivo):
        return []

    equipos: List[Equipo] = []
    with open(ruta_archivo, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                equipo = {
                    "id": int(fila["id"]),
                    "nombre": fila["nombre"],
                    "categoría": fila["categoría"],
                    "estado": fila["estado"],
                    "valor": float(fila["valor"]),
                }
            except (ValueError, KeyError):
                print("⚠️ Se encontró una fila inválida en el archivo y será ignorada.")
                continue
            equipos.append(equipo)
    return equipos


def guardar_equipos_en_csv(equipos: List[Equipo], ruta_archivo: str = EQUIPOS_CSV) -> None:
    """Guarda la lista de equipos en el archivo CSV."""
    with open(ruta_archivo, "w", newline="", encoding="utf-8") as archivo:
        campos = ("id", "nombre", "categoría", "estado", "valor")
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for equipo in equipos:
            escritor.writerow(equipo)


def obtener_siguiente_id(equipos: List[Equipo]) -> int:
    """Devuelve el próximo identificador disponible."""
    if not equipos:
        return 1
    return max(int(equipo["id"]) for equipo in equipos) + 1


def opcion_cargar_equipos(equipos: List[Equipo]) -> bool:
    """Permite cargar nuevos equipos y almacenarlos en memoria y en el CSV."""
    print("\n=== Carga de equipos ===")
    cambios = False
    if os.path.exists(EQUIPOS_CSV) and equipos:
        decision = pedir_opcion(
            "Ya hay datos cargados. ¿Desea reemplazarlos o agregar nuevos? (reemplazar/agregar): ",
            ("reemplazar", "agregar"),
        )
        if decision == "reemplazar":
            equipos.clear()
            print("Inventario reiniciado. Puede cargar nuevos equipos.")
            cambios = True
    elif os.path.exists(EQUIPOS_CSV) and not equipos:
        # Si el archivo existe pero la lista está vacía se cargan automáticamente los datos.
        equipos.extend(leer_equipos_desde_csv())
        print("Se cargaron los datos existentes desde el archivo.")

    cantidad = pedir_entero_positivo("¿Cuántos equipos desea ingresar? ", permitir_cero=True)
    if cantidad == 0:
        if cambios:
            guardar_equipos_en_csv(equipos)
        print("No se agregaron nuevos equipos.")
        return cambios

    siguiente_id = obtener_siguiente_id(equipos)
    for numero in range(1, cantidad + 1):
        print(f"\nEquipo #{numero}")
        nombre = pedir_texto_no_vacio("Nombre: ")
        categoria = pedir_opcion(
            f"Categoría ({', '.join(CATEGORIAS)}): ", CATEGORIAS
        )
        estado = pedir_opcion(
            f"Estado ({', '.join(ESTADOS)}): ", ESTADOS
        )
        valor = pedir_float_positivo("Valor estimado: $")
        equipos.append(
            {
                "id": siguiente_id,
                "nombre": nombre,
                "categoría": categoria,
                "estado": estado,
                "valor": valor,
            }
        )
        siguiente_id += 1
        cambios = True

    guardar_equipos_en_csv(equipos)
    print("\n✅ Equipos guardados correctamente.")
    return cambios


def opcion_mostrar_inventario(equipos: List[Equipo]) -> None:
    """Muestra todos los equipos registrados."""
    print("\n=== Inventario de equipos ===")
    if not equipos:
        print("No hay equipos cargados.")
        return

    linea = "-" * 50
    for equipo in equipos:
        print(linea)
        print(f"ID: {equipo['id']}")
        print(f"Nombre: {equipo['nombre']}")
        print(f"Categoría: {equipo['categoría']}")
        print(f"Estado: {equipo['estado']}")
        print(f"Valor: ${equipo['valor']:.2f}")
    print(linea)


def opcion_buscar_equipo(equipos: List[Equipo]) -> None:
    """Busca un equipo por nombre ignorando mayúsculas y minúsculas."""
    criterio = pedir_texto_no_vacio("Ingrese el nombre del equipo a buscar: ")
    criterio_normalizado = criterio.lower()
    for equipo in equipos:
        if equipo["nombre"].lower() == criterio_normalizado:
            print("\nEquipo encontrado:")
            opcion_mostrar_inventario([equipo])
            return
    print("\n⚠️ No se encontró un equipo con ese nombre.")


def obtener_estadisticas(equipos: List[Equipo]) -> Dict[str, object]:
    """Calcula estadísticas sobre los equipos cargados."""
    if not equipos:
        return {
            "total": 0,
            "promedio_valor": 0.0,
            "fuera_servicio": 0,
            "mas_caro": None,
            "mas_barato": None,
        }

    total = len(equipos)
    suma_valores = sum(float(eq["valor"]) for eq in equipos)
    promedio = suma_valores / total if total else 0.0
    fuera_servicio = sum(1 for eq in equipos if eq["estado"].lower() == "fuera de servicio")
    mas_caro = max(equipos, key=lambda eq: float(eq["valor"]))
    mas_barato = min(equipos, key=lambda eq: float(eq["valor"]))
    return {
        "total": total,
        "promedio_valor": promedio,
        "fuera_servicio": fuera_servicio,
        "mas_caro": mas_caro,
        "mas_barato": mas_barato,
    }


def opcion_mostrar_estadisticas(equipos: List[Equipo]) -> None:
    """Muestra las estadísticas del inventario."""
    stats = obtener_estadisticas(equipos)
    if stats["total"] == 0:
        print("\n⚠️ No hay datos para mostrar estadísticas.")
        return

    print("\n=== Estadísticas ===")
    print(f"Equipos totales: {stats['total']}")
    print(f"Promedio de valor: ${stats['promedio_valor']:.2f}")
    print(f"Fuera de servicio: {stats['fuera_servicio']}")
    mas_caro = stats["mas_caro"]
    mas_barato = stats["mas_barato"]
    if mas_caro:
        print(
            f"Más caro: ${mas_caro['valor']:.2f} (Nombre: {mas_caro['nombre']})"
        )
    if mas_barato:
        print(
            f"Más barato: ${mas_barato['valor']:.2f} (Nombre: {mas_barato['nombre']})"
        )


def opcion_filtrar_por_categoria(equipos: List[Equipo]) -> None:
    """Muestra los equipos que pertenecen a una categoría específica."""
    categoria = pedir_opcion(
        f"Ingrese la categoría a filtrar ({', '.join(CATEGORIAS)}): ", CATEGORIAS
    )
    filtrados = [eq for eq in equipos if eq["categoría"].lower() == categoria.lower()]
    if not filtrados:
        print("\n⚠️ No se encontraron equipos para esa categoría.")
        return
    opcion_mostrar_inventario(filtrados)


def opcion_ordenar_por_valor(equipos: List[Equipo]) -> None:
    """Muestra la lista ordenada por valor sin modificar la original."""
    criterio = pedir_opcion("Ordenar por valor (ASC/DESC): ", ("asc", "desc"))
    reverso = criterio.lower() == "desc"
    ordenados = sorted(equipos, key=lambda eq: float(eq["valor"]), reverse=reverso)
    opcion_mostrar_inventario(ordenados)


def opcion_generar_informe(equipos: List[Equipo]) -> None:
    """Genera y muestra un informe de inventario en formato de texto."""
    stats = obtener_estadisticas(equipos)
    if stats["total"] == 0:
        print("\n⚠️ No hay datos para generar el informe.")
        return

    mas_caro = stats["mas_caro"]
    mas_barato = stats["mas_barato"]
    contenido = [
        "INFORME GENERAL DE INVENTARIO",
        "-----------------------------",
        f"Equipos totales: {stats['total']}",
        f"Promedio de valor: {stats['promedio_valor']:.2f}",
        f"Fuera de servicio: {stats['fuera_servicio']}",
        f"Más caro: ${mas_caro['valor']:.2f} (Nombre: {mas_caro['nombre']})" if mas_caro else "Más caro: N/A",
        f"Más barato: ${mas_barato['valor']:.2f} (Nombre: {mas_barato['nombre']})" if mas_barato else "Más barato: N/A",
        "-----------------------------",
    ]
    with open(INFORME_TXT, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(contenido))

    print("\n=== Informe generado ===")
    for linea in contenido:
        print(linea)


def mostrar_menu() -> str:
    """Muestra el menú principal y devuelve la opción elegida."""
    menu = (
        "\n==============================\n"
        "Gestión de Inventario\n"
        "==============================\n"
        "1. Cargar equipos\n"
        "2. Mostrar inventario\n"
        "3. Buscar equipo\n"
        "4. Estadísticas\n"
        "5. Filtrar por categoría\n"
        "6. Ordenar por valor\n"
        "7. Generar informe\n"
        "8. Salir\n"
    )
    print(menu)
    return pedir_opcion("Seleccione una opción: ", tuple(str(i) for i in range(1, 9)))


def ejecutar_programa() -> None:
    """Ejecuta el bucle principal del programa."""
    equipos = leer_equipos_desde_csv()
    datos_cargados = bool(equipos)
    cambios_realizados = False

    if datos_cargados:
        print("Se cargaron los datos existentes desde el archivo CSV.")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            if opcion_cargar_equipos(equipos):
                datos_cargados = True
                cambios_realizados = True
        elif opcion == "2":
            if datos_cargados:
                opcion_mostrar_inventario(equipos)
            else:
                print("⚠️ Debe cargar o leer el archivo antes de usar esta opción.")
        elif opcion == "3":
            if datos_cargados:
                opcion_buscar_equipo(equipos)
            else:
                print("⚠️ Debe cargar o leer el archivo antes de usar esta opción.")
        elif opcion == "4":
            if datos_cargados:
                opcion_mostrar_estadisticas(equipos)
            else:
                print("⚠️ Debe cargar o leer el archivo antes de usar esta opción.")
        elif opcion == "5":
            if datos_cargados:
                opcion_filtrar_por_categoria(equipos)
            else:
                print("⚠️ Debe cargar o leer el archivo antes de usar esta opción.")
        elif opcion == "6":
            if datos_cargados:
                opcion_ordenar_por_valor(equipos)
            else:
                print("⚠️ Debe cargar o leer el archivo antes de usar esta opción.")
        elif opcion == "7":
            if datos_cargados:
                opcion_generar_informe(equipos)
            else:
                print("⚠️ Debe cargar o leer el archivo antes de usar esta opción.")
        elif opcion == "8":
            if cambios_realizados:
                guardar_equipos_en_csv(equipos)
                print("Cambios guardados en el archivo CSV.")
            print("¡Hasta luego! 👋")
            break


if __name__ == "__main__":
    ejecutar_programa()
