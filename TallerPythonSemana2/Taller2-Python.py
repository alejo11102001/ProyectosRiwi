# Lista para almacenar las notas ingresadas por el usuario
lista_notas = []
menu = True

# Bucle principal del menú
while menu:
    continuar = True
    try:
        # Menú de opciones principal
        print("\033[96m\n===============================================\nBienvenido al sistema de calculo y evaluo de notas \n===============================================\033[0m")
        print("\033[93mPor favor seleccione una opción:\033[0m")
        print("\n1.) Evaluar calificación") 
        print("2.) Calcular promedio")    
        print("3.) Contar calificación")   
        print("4.) Verificar calificaciones") 

        # Validación de entrada del usuario (opción del menú)
        while True:
            try:
                opcion = int(input("\n\033[96mElije la opción que deseas: \033[0m"))
                if opcion < 1 or opcion > 4:
                    print("\nIngrese una opción válida")
                    continue
                break
            except ValueError:
                print("\n\033[91mPor favor ingrese un número entre 1 y 4.\033[0m")

        # ---------------- Opción 1: Evaluar calificación ----------------
        if opcion == 1:
            while continuar:
                while True:
                    try:
                        # Ingreso y validación de una nota individual
                        calificacion = float(input("\nIngrese nota (0-100): "))
                        if calificacion < 0 or calificacion > 100:
                            print("\n\033[91mIngrese una nota válida\033[0m")
                        else:
                            # Clasificación de la nota según su rango
                            if calificacion <= 59:
                                print("\n\033[91mInsuficiente/Reprobado\033[0m")
                            elif calificacion <= 69:
                                print("\n\033[93mSuficiente/Aprobado\033[0m")
                            elif calificacion <= 79:
                                print("\n\033[92mBueno/Aprobado\033[0m")
                            elif calificacion <= 89:
                                print("\n\033[92mMuy bueno/Aprobado\033[0m")
                            else:
                                print("\n\033[92mExcelente/Aprobado\033[0m")
                            break
                    except ValueError:
                        print("\n\033[91mNo puede digitar letras, espacios en blanco ni caracteres especiales, digite valor válido\033[0m")

                # Confirmar si desea continuar evaluando notas
                while continuar:
                    continuar_validando = input("\033[93m\n¿Deseas continuar evaluando notas?: S()si N()no:\033[0m").lower()
                    if continuar_validando == "n":
                        continuar = False
                        # Confirmar si desea volver al menú principal
                        while True:
                            salida = input("\033[93m\n¿Deseas volver al menú inicial?: S()si N()no:\033[0m").lower()
                            if salida == "s":
                                break
                            elif salida == "n":
                                menu = False
                                break
                            else:
                                print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
                        break
                    elif continuar_validando == "s":
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

        # ---------------- Opción 2: Calcular promedio ----------------
        elif opcion == 2:
            while continuar:
                while True:
                    try:
                        # Ingreso de múltiples notas separadas por coma
                        calificaciones = input("\nIngrese todas las calificaciones para el promedio separadas con una (,): ")
                        notas = calificaciones.split(',')
                        lista_notas = []
                        for nota in notas:
                            nota_float = float(nota.strip())
                            if nota_float < 0 or nota_float > 100:
                                raise ValueError("\n\033[91mNota fuera de rango\033[0m")
                            lista_notas.append(nota_float)

                        # Cálculo del promedio
                        print(f"\n{lista_notas}")
                        promedio = sum(lista_notas) / len(lista_notas)
                        print("\n\033[92mPromedio:\033[0m", promedio)
                        break
                    except ValueError:
                        print("\n\033[91mSolo se permiten números entre 0 y 100 separados por comas.\033[0m")

                # Confirmar si desea calcular otro promedio
                while continuar:
                    continuar_validando = input("\033[93m\n¿Deseas calcular otro promedio?: S()si N()no:\033[0m").lower()
                    if continuar_validando == "n":
                        continuar = False
                        while True:
                            salida = input("\033[93m\n¿Deseas volver al menú inicial?: S()si N()no:\033[0m").lower()
                            if salida == "s":
                                break
                            elif salida == "n":
                                menu = False
                                break
                            else:
                                print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
                        break
                    elif continuar_validando == "s":
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

        # ---------------- Opción 3: Contar calificaciones mayores que una ----------------
        elif opcion == 3:
            # Verifica que haya notas disponibles
            if not lista_notas:
                print("\n\033[91mNo hay calificaciones disponibles. Ingrese calificaciones primero.\033[0m")
                continue

            while continuar:
                while True:
                    try:
                        # Ingreso de la nota de referencia
                        nota_especifica = float(input("\nIngresa la nota que quiere buscar: "))
                        if nota_especifica < 0 or nota_especifica > 100:
                            print("\033[91m\nLa nota debe estar entre 0 y 100. Inténtalo de nuevo.\033[0m")
                            continue

                        # Conteo de notas mayores a la ingresada
                        canti_mayor = sum(1 for nota in lista_notas if nota > nota_especifica)
                        print(f"\n\033[92mCantidad de notas mayores que {nota_especifica} son: {canti_mayor}\033[0m")
                        break
                    except ValueError:
                        print("\n\033[91mNo puede digitar letras ni caracteres especiales, digite valor válido\033[0m")

                # Confirmar si desea seguir buscando
                while continuar:
                    continuar_validando = input("\033[93m\n¿Deseas seguir buscando?: S()si N()no:\033[0m").lower()
                    if continuar_validando == "n":
                        continuar = False
                        while True:
                            salida = input("\033[93m\n¿Deseas volver al menú inicial?: S()si N()no:\033[0m").lower()
                            if salida == "s":
                                break
                            elif salida == "n":
                                menu = False
                                break
                            else:
                                print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
                        break
                    elif continuar_validando == "s":
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

        # ---------------- Opción 4: Verificar cuántas veces aparece una calificación ----------------
        elif opcion == 4:
            # Verifica que haya notas disponibles
            if not lista_notas:
                print("\n\033[91mNo hay calificaciones disponibles. Ingrese calificaciones primero.\033[0m")
                continue

            while continuar:
                while True:
                    try:
                        nota_buscar = float(input("\n¿Qué calificación deseas buscar?: "))
                        if nota_buscar < 0 or nota_buscar > 100:
                            print("\033[91m\nLa nota debe estar entre 0 y 100. Inténtalo de nuevo.\033[0m")
                            continue

                        # Conteo de veces que aparece la nota en la lista
                        contador = lista_notas.count(nota_buscar)
                        if contador:
                            print(f"\033[92m\nLa calificación {nota_buscar} aparece {contador} veces.\033[0m")
                        else:
                            print(f"\033[91m\nLa calificación {nota_buscar} no se encuentra en la lista.\033[0m")
                        break
                    except ValueError:
                        print("\033[91m\nSolo puedes ingresar números entre 0 y 100.\033[0m")

                # Confirmar si desea seguir buscando
                while continuar:
                    continuar_validando = input("\033[93m\n¿Deseas seguir buscando?: S()si N()no:\033[0m").lower()
                    if continuar_validando == "n":
                        continuar = False
                        while True:
                            salida = input("\033[93m\n¿Deseas volver al menú inicial?: S()si N()no:\033[0m").lower()
                            if salida == "s":
                                break
                            elif salida == "n":
                                menu = False
                                break
                            else:
                                print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")
                        break
                    elif continuar_validando == "s":
                        break
                    else:
                        print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

    except ValueError:
        print("\n\033[91mNo puede digitar letras, espacio en blanco ni caracteres especiales, digite valor válido\033[0m")
