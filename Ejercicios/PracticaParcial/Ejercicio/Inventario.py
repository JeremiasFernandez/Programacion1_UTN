# inventario.py
from Validaciones import pedirEnteroEnRango, pedirTextoNoVacio, pedirOpcionDe, pedirFloatPositivo

CATEGORIAS = ["router", "pc", "notebook", "impresora"]
ESTADOS = ["funcional", "fuera de servicio"]

def proximoId(equipos):
    if not equipos:
        return 1

def pedir_equipo(equipos):
    e = {}
    e["id"] = proximoId(equipos)
    e["nombre"] = pedirTextoNoVacio("Nombre del equipo: ")
    e["categoria"] = pedirOpcionDe("Categoría", CATEGORIAS)
    e["estado"] = pedirOpcionDe("Estado", ESTADOS)
    e["valor"] = pedirFloatPositivo("Valor ($): ")
    return e

def opcion1cargar(equipos):
    n = pedirEnteroEnRango("¿Cuántos equipos querés cargar? (1-999): ", 1, 999)
    for i in range(n):
        print("\n--- Nuevo equipo ---")
        equipos(pedir_equipo(equipos))
    print(f"\n✔ Cargaste {n} equipo(s). Total: {len(equipos)}")
