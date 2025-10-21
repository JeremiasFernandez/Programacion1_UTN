import Main as m

def pedirEnteroEnRango(mensaje, minimo, maximo):
    while True:
        dato = input(mensaje).strip()
        try:
            n = int(dato)
            if minimo <= n <= maximo:
                return n
            print(f"⚠ Debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("⚠ Debe ser un número entero.")

if __name__ == "__main__":
    op = pedirEnteroEnRango("Elegí (1-8): ", 1, 8)
    print("Elegiste:", op)


def pedirTextoNoVacio():
    t = ""
    while not t:
        t = input(m.msg)
        if t:
            return t
        
        print("no se puede dejar vacio...")


def pedirOpcionDe(msg, opciones):
    mostrar = ", ".join(opciones)
    while True:
        op = input(f"{msg} ({mostrar}): ").strip().lower()
        for o in opciones:
            if op == o.lower():   # comparamos ignorando mayúsculas
                return op         # devolvemos lo que eligió (en minúsculas)
        print("⚠ Opción inválida.")
