'''
Desafío: Encuesta Tecnológica en UTN Technologies

UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo 
en Python, con el objetivo de revolucionar el mercado.

Las tecnologías en evaluación son:

 🔹 Inteligencia Artificial (IA)
 🔹 Realidad Virtual/Aumentada (RV/RA)
 🔹 Internet de las Cosas (IOT)

Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados 
con el propósito de analizar ciertas métricas.

🔹 Recolección de Datos

Cada empleado encuestado deberá proporcionar la siguiente información:

 ✔️ Nombre
 ✔️ Edad (debe ser 18 años o más)
 ✔️ Género (Masculino, Femenino, Otro)
 ✔️ Tecnología elegida (IA, RV/RA, IOT)

El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.

🔹 Análisis de Datos
A partir de las respuestas, se deben calcular las siguientes métricas:
1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años 
(inclusive).
2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
Su género no sea Femenino 
Su edad está entre los 33 y 40 años.
3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.


🔹 Requisitos del Programa
 ✔️ Los datos deben solicitarse y validarse correctamente.
 ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
 ✔️ Presentar los resultados de manera clara y organizada.

'''

# Desafío: Encuesta Tecnológica en UTN Technologies

print("=== Encuesta Tecnológica en UTN Technologies ===")

# Contadores y acumuladores
contador = 0
hombres_iot_ia_25_50 = 0
grupo2_total = 0
grupo2_no_ia = 0
mayor_hombre_edad = -1
mayor_hombre_nombre = ""
mayor_hombre_tecnologia = ""

while contador < 10:
    print(f"\nEmpleado #{contador + 1}")

    # Validar nombre
    nombre = input("Ingrese su nombre: ").strip()
    while nombre == "":
        nombre = input("El nombre no puede estar vacío. Intente nuevamente: ").strip()

    # Validar edad
    edad_str = input("Ingrese su edad (mayor o igual a 18): ").strip()
    while not edad_str.isdigit() or int(edad_str) < 18:
        edad_str = input("Edad inválida. Debe ser un número mayor o igual a 18: ").strip()
    edad = int(edad_str)

    # Validar género
    genero = input("Ingrese su género (Masculino / Femenino / Otro): ").strip().capitalize()
    while genero not in ("Masculino", "Femenino", "Otro"):
        genero = input("Opción inválida. Ingrese Masculino, Femenino u Otro: ").strip().capitalize()

    # Validar tecnología
    tecnologia = input("Ingrese la tecnología (IA / RV/RA / IOT): ").strip().upper()
    while tecnologia not in ("IA", "RV/RA", "IOT"):
        tecnologia = input("Opción inválida. Ingrese IA, RV/RA o IOT: ").strip().upper()

    # 1️⃣ Hombres entre 25 y 50 que votaron IOT o IA
    if genero == "Masculino" and 25 <= edad <= 50 and tecnologia in ("IOT", "IA"):
        hombres_iot_ia_25_50 += 1

    # 2️⃣ Grupo de no femeninos y edad entre 33 y 40
    if genero != "Femenino" and 33 <= edad <= 40:
        grupo2_total += 1
        if tecnologia != "IA":
            grupo2_no_ia += 1

    # 3️⃣ Hombre de mayor edad
    if genero == "Masculino" and edad > mayor_hombre_edad:
        mayor_hombre_edad = edad
        mayor_hombre_nombre = nombre
        mayor_hombre_tecnologia = tecnologia

    contador += 1

# Calcular porcentaje del punto 2
if grupo2_total > 0:
    porcentaje_no_ia = (grupo2_no_ia / grupo2_total) * 100
else:
    porcentaje_no_ia = 0

# Mostrar resultados
print("\n=== RESULTADOS ===")
print(f"Hombres (25-50) que votaron IOT o IA: {hombres_iot_ia_25_50}")
if grupo2_total == 0:
    print("No hubo empleados que cumplan las condiciones del grupo 2.")
else:
    print(f"Porcentaje de empleados que NO votaron IA (no femeninos, edad 33-40): {porcentaje_no_ia:.2f}%")
if mayor_hombre_edad == -1:
    print("No se registraron empleados masculinos.")
else:
    print(f"Hombre de mayor edad: {mayor_hombre_nombre} ({mayor_hombre_edad} años) – Votó: {mayor_hombre_tecnologia}")
