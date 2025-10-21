
import Variables as c
import Validaciones as v


def mostrar_menu():
    print(f"\n{c.NEGRITA}{c.AZUL}===== MENÚ INVENTARIO ====={c.RESET}")
    print(f"{c.VERDE}1){c.RESET} Cargar equipos")
    print(f"{c.VERDE}2){c.RESET} Mostrar inventario")
    print(f"{c.VERDE}3){c.RESET} Buscar equipo por nombre")
    print(f"{c.VERDE}4){c.RESET} Estadísticas")
    print(f"{c.VERDE}5){c.RESET} Filtrar por categoría")
    print(f"{c.VERDE}6){c.RESET} Ordenar por valor (ASC/DESC)")
    print(f"{c.VERDE}7){c.RESET} Generar informe")
    print(f"{c.ROJO}8){c.RESET} Salir")
    print(f"{c.AZUL}============================={c.RESET}")


def main():
    datos_cargados = False

    while True:
        mostrar_menu()
        opcion = v.pedirEnteroEnRango("Elegí una opción (1-8): ", 1, 8)
    
        match opcion:
            case 1:
                print("Opción 1: 'Cargar equipos' (a implementar).")
                datos_cargados = True

            case 2 | 3 | 4 | 5 | 6 | 7:
                if datos_cargados == False:
                    print("Primero debés cargar/leer datos (Opción 1).")
                    continue
                print(f"Opción {opcion}: pendiente de implementar.")

            case 2:
                opcion2()

            case 8:
                print("¡Gracias por usar el sistema!")
                break

            case _:
                print("Opción inválida.")

if __name__ == "__main__":
    main()
