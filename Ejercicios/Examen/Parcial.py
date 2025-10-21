import Validacion as v


ROJO = "\033[91m"
VERDE = "\033[92m"
AZUL = "\033[94m"
RESET = "\033[0m"
NEGRITA = "\033[1m"

def mostrar_menu():
    print(f"\n{NEGRITA}{AZUL}===== MENÚ INVENTARIO ====={RESET}")
    print(f"{VERDE}1){RESET} Cargar alumnos")
    print(f"{VERDE}2){RESET} Mostrar listado de estudiantes")
    print(f"{VERDE}3){RESET} Buscar estudiante")
    print(f"{VERDE}4){RESET} Calcular Estadísticas")
    print(f"{VERDE}5){RESET} Ordenar")
    print(f"{VERDE}6){RESET} Generar informe resumen")
    print(f"{ROJO}8){RESET} Salir")
    print(f"{AZUL}============================={RESET}")
    print("")
   


def __main__():

    dts = False
    while True:

        # Imprime el menu
        mostrar_menu()
        opcion= int(input("Elige una opcion (1-8): "))
        
        match opcion:
            case 1:
                v.cargarEquipos()
                break

            case 2:
                v.listadoEstudiantes()
        
            case 3:
                v.buscarAlumno()

            case 4:
                v.estadisticas()

            case 5:
                print("nose")
                

__main__()
