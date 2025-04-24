usuarios = []
continuar_menu = True
encontrado = True

while continuar_menu:
    try:    
        continuar = True
        print("\n===============================================\nBienvenido al sistema de registro de estudiantes \n===============================================")
        print("Por favor seleccione una opción: ")
        print("\n1.) Agregar usuario")
        print("2.) Mostrar listado de usuarios")
        print("3.) Eliminar usuario")
        print("4.) Actualizar datos de usuario")

        opcion = int(input("\nElije la opción que deseas: "))
        
        if opcion == 1:
            while continuar:
                nombre = input("\nIngresa el nombre: ")
                apellido = input("Ingresa el apellido: ")
                correo = input("Ingresa el correo: ")
                edad = int(input("Ingresa la edad: "))

                usuario = [nombre, apellido, correo, edad]
                usuarios.append(usuario)

                valor = input("\n¿Deseas continuar ingresando usuario?: S()si N()no: ")
                if valor == "N" or valor == "n":
                    salida = input("\n¿Deseas volver al menu inicial?: S()si N()no: ")
                    if salida == "S" or salida == "s":
                        break
                    else:
                        continuar = False  
        elif opcion == 2:
            if len(usuarios) == 0:
                print("\nNo hay usuarios registrados")
            else:
                for i in range(len(usuarios)):
                    print(f"\n{i+1}. {usuarios[i][0]}, {usuarios[i][1]}, {usuarios[i][2]}, {usuarios[i][3]} años")
                salida = input("\n¿Deseas volver al menu inicial?: S()si N()no: ")
                if salida == "N" or salida == "n":
                    break
                else:
                    continuar = False  
        elif opcion == 3:
            if len(usuarios) == 0:
                print("\nNo hay usuarios registrados")
            else:
                usuario_eliminado = input("\nIngrese el nombre del usuario que deseas eliminar: ")
                for usuario in usuarios:
                    if usuario[0] == usuario_eliminado:
                        usuarios.remove(usuario)
                        print("\nEl usuario ha sido eliminado correctamente")
                        break
                else:
                    print("\nEl usuario no se encontro en la base de datos") 
                salida = input("\n¿Deseas volver al menu inicial?: S()si N()no: ")
                if salida == "N" or salida == "n":
                    break
                else:
                    continuar = False   
        elif opcion == 4:
            try:
                if len(usuarios) == 0:
                    print("\nNo hay usuarios registrados")
                else:
                    for i in range(len(usuarios)):
                        print(f"{i+1}. {usuarios[i][0]}, {usuarios[i][1]}, {usuarios[i][2]}, {usuarios[i][3]} años")
                    num_tabla = int(input("\nIngrese el numero del usuario que quiere actualizar: ")) - 1
                
                    if 0 <= num_tabla < len(usuarios):
                        print(f"\nActualizando usuario: {usuarios[num_tabla][0]}")
                        usuarios[num_tabla][0] = input("\nIngrese nuevo nombre (Enter para dejarlo asi): ")
                        usuarios[num_tabla][1] = input("\nIngrese nuevo apellido (Enter para dejarlo asi): ")
                        usuarios[num_tabla][2] = input("\nIngrese nuevo correo (Enter para dejarlo asi): ")
                        usuarios[num_tabla][3] = int(input("\nIngrese nueva edad (Enter para dejarlo asi): "))
                        print("\nUsuario actualizado")
                    else:
                        print("\nNumero de usuario invalido")
                    if salida == "N" or salida == "n":
                        break
                    else:
                        continuar = False
            except ValueError:
                print("\nEL valor es incorrecto ingrese un valor valido")
        else:
            print("\nOpción no valida por favor dijite la correcta")
    except ValueError:
        print("\nIngrese una opción valida")