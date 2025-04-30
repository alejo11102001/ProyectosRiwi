# Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
# Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada

# 90 - 100	A	Excelente
# 80 - 89	B	Muy Bueno
# 70 - 79	C	Bueno
# 60 - 69	D	Suficiente / Aprobado
# 0 - 59	F	Insuficiente / Reprobado

# 1. evaluar calificacion
# 2. calcular promedio
# 3. contar calificacion
# 4. Verificar calificaciones
lista_notas = []
menu = True


while menu:
    continuar = True
    try:
        print("\033[96m\n===============================================\nBienvenido al sistema de calculo y evaluo de notas \n===============================================\033[0m")
        print("\033[93mPor favor seleccione una opción:\033[0m")
        print("\n1.) Evaluar calificacion")
        print("2.) Calcular promedio")
        print("3.) Contar calificacion")
        print("4.) Verificar calificaciones")
        while True:
            opcion = int(input("\n\033[96mElije la opción que deseas: \033[0m"))
        
            if opcion < 1 or opcion > 4:
                print("\nIngrese una opción valida")
            break

        if opcion == 1:
            while continuar:
                while True:
                    try:
                        calificacion = float(input("\nIngrese nota (0-100): "))
                        if calificacion < 0 or calificacion > 100:
                            print("\n\033[91mIngrese una nota valida\033[0m")
                        else:
                            if calificacion <= 59:
                                print("\n\033[91mInsuficiente/Reprobado\033[0m")
                                break
                            elif calificacion >= 60 and calificacion <= 69:
                                print("\n\033[93mSuficiente/Aprobado\033[0m")
                                break
                            elif calificacion >= 70 and calificacion <= 79:
                                print("\n\033[92mBueno/Aprobado\033[0m")
                                break
                            elif calificacion >= 80 and calificacion <= 89:
                                print("\n\033[92mMuy bueno/Aprobado\033[0m")
                                break
                            else:
                                print("\n\033[92mExcelente/Aprobado\033[0m")
                                break
                    except ValueError:
                        print("\n\033[91mNo puede digitar letras ni caracteres especiales, digite valor valido\033[0m")
                while continuar:
                    continuar_validando = input("\033[93m\n¿Deseas continuar evaluando notas?: S()si N()no:\033[0m").lower()
                    if continuar_validando.lower() == "n":
                        continuar = False
                        while True:
                            salida = input("\033[93m\n¿Deseas volver al menu inicial?: S()si N()no:\033[0m").lower()
                            if salida.lower() == "s":
                                break
                            elif salida.lower() == "n":
                                menu = False
                                break 
                            else:
                                print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
                        break
                    elif continuar_validando.lower() == "s":
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
        # Calcular el promedio:
        # Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
        # Calcular y mostrar el promedio de las calificaciones en la lista
        elif opcion == 2:
            while continuar:
                promedio = 0
                while True:
                    try:
                        calificaciones = (input("\nIngrese todas las calificaciones para el promedio: "))
                        notes = calificaciones.split(',')

                        for nota in notes:
                            lista_notas.append(float(nota))
                        print(f"\n{lista_notas}")

                        promedio = sum(lista_notas) / len(lista_notas)
                        print("\nPromedio:", promedio)
                        break
                    except ValueError:
                        print("\n\033[91mNo puede digitar letras ni caracteres especiales, digite valor valido\033[0m")
                while continuar:
                    continuar_validando = input("\033[93m\n¿Deseas calcular otro promedio?: S()si N()no:\033[0m").lower()
                    if continuar_validando.lower() == "n":
                        continuar = False
                        while True:
                            salida = input("\033[93m\n¿Deseas volver al menu inicial?: S()si N()no:\033[0m").lower()
                            if salida.lower() == "s":
                                break
                            elif salida.lower() == "n":
                                menu = False
                                break 
                            else:
                                print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
                        break
                    elif continuar_validando.lower() == "s":
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

        # Contar calificaciones mayores:
        # Preguntar al usuario por un valor específico
        # Contar cuántas calificaciones en la lista son mayores que este valor
        elif opcion == 3:
            nota_especifica = float(input("\nIngresa una nota específica: "))

            indice = 0
            canti_mayor = 0

            while indice < len(lista_notas):
                if lista_notas[indice] > nota_especifica:
                    canti_mayor += 1
                indice += 1

            print(f"\nCantidad de notas mayores que {nota_especifica}: {canti_mayor}")


        # Verificar y contar calificaciones específicas:
        # Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
        # Calcular y mostrar el promedio de las calificaciones en la lista
        elif opcion == 4:

            nota_buscar = int(input("\n¿Qué calificación deseas buscar?: "))

            contador = 0
            encontrado = False

            for nota in lista_notas:
                if nota != nota_buscar:
                    continue
                contador += 1
                encontrado = True

            if encontrado:
                print(f"\nLa calificación {nota_buscar} aparece {contador} veces.")
            else:
                print(f"\nLa calificación {nota_buscar} no se encuentra en la lista.")
    except ValueError:
        print("\nNo puede digitar letras ni caracteres especiales, digite valor valido")