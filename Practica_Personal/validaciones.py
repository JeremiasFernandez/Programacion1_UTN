"""Funciones de validación y obtención de datos para el sistema de inventario."""
from typing import Iterable


def pedir_entero_positivo(mensaje: str, permitir_cero: bool = False) -> int:
    """Solicita un entero positivo al usuario.

    Args:
        mensaje: Texto a mostrar al solicitar el valor.
        permitir_cero: Si es ``True`` se admite el valor cero como válido.

    Returns:
        Entero positivo ingresado por el usuario.
    """
    while True:
        dato = input(mensaje).strip()
        if not dato:
            print("⚠️ Debe ingresar un número.")
            continue
        if dato.startswith("+"):
            dato = dato[1:]
        if not dato.isdigit():
            print("⚠️ Ingrese solo dígitos.")
            continue
        numero = int(dato)
        if numero == 0 and not permitir_cero:
            print("⚠️ El valor debe ser mayor a cero.")
            continue
        if numero < 0:
            print("⚠️ El número no puede ser negativo.")
            continue
        return numero


def pedir_float_positivo(mensaje: str) -> float:
    """Solicita un número decimal positivo."""
    while True:
        dato = input(mensaje).strip().replace(",", ".")
        if not dato:
            print("⚠️ Debe ingresar un valor numérico.")
            continue
        try:
            numero = float(dato)
        except ValueError:
            print("⚠️ Formato inválido. Ingrese solo números.")
            continue
        if numero <= 0:
            print("⚠️ El número debe ser mayor que cero.")
            continue
        return numero


def pedir_texto_no_vacio(mensaje: str) -> str:
    """Solicita un texto no vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("⚠️ Este campo no puede quedar vacío.")


def pedir_opcion(mensaje: str, opciones_validas: Iterable[str]) -> str:
    """Solicita al usuario elegir una opción dentro de las opciones válidas."""
    opciones_normalizadas = {op.lower(): op for op in opciones_validas}
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in opciones_normalizadas:
            return opciones_normalizadas[respuesta]
        print(f"⚠️ Opción inválida. Elija entre: {', '.join(opciones_validas)}")
