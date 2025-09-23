while True:

    # Ingresa la nota
    nota = float(input("Ingrese su nota: "))

    # Resultados especiales

    if nota == 10:
        print("RESULTADO PERFECTO!!")


    elif nota in [9.99, 9.98]:
        while True:
            estado = input("Estas triste? (Y/N): ")

            if estado.lower() in ["y", "yes", "si", "s"]:
                print("mal ahi")
                break

            elif estado.lower() in ["n", "no"]:
                print("bueno deberias")
                break

            else:
                print("Invalido, respondiste cualquiera")
            
    elif nota == 9.11:
        print("Hola si, esta llamando a emergencias, ¿Cual es su problema?")

    elif nota == 9.12:
        print("moriste en madrid")

    elif nota == 6.66:
        print("nota insana")

    elif nota == 0:
        print("menudo fraca jaja")
        
    # Notas generales

    elif nota > 10:
        print("... ¿Como?")

    elif nota > 7:
        print("Promocionaste")
    elif nota > 4:
        print("Aprobaste")
    elif nota < 4:
        print("Desaprobaste")

    else:
        print("pusiste cualquiera")
    print()


