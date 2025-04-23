usuarios = []
continuar_menu = True
encontrado = True

while continuar_menu:

    print("\nBienvenido al sistema de registro")
    print("Por favor seleccione una opción: ")
    print("1.) Agregar usuario")
    print("2.) Mostrar listado de usuarios")
    print("3.) Eliminar usuario")
    print("4.) Actualizar datos de usuario")

    opcion = int(input("\nOpción del 1-4: "))
    
    if (opcion == 1):
        continuar = True
        while continuar:
            nombre = input("\nIngresa el nombre: ")
            apellido = input("ingresa el apellido: ")
            correo = input("ingresa el correo: ")
            edad = int(input("ingresa la edad: "))

            usuario = [nombre, apellido, correo, edad]
            usuarios.append(usuario)

            valor = input("\ndeseas continuar: S()si N()no: ")
            if (valor == "N" or valor == "n"):
                salida = input("\ndeseas volver al menu inicial: S()si N()no: ")
                if (salida == "S" or salida == "s"):
                    break
                else:
                    continuar = False  
                    continuar_menu = False
    elif (opcion == 2):
        print(usuarios)
    elif (opcion == 3):
        usuario_eliminado = input("Ingrese el nombre del usuario que deseas eliminar: ")
        for usuario in usuarios:
            if usuario[0] == usuario_eliminado:
                usuarios.remove(usuario)
                print("EL usuario ha sido eliminado correctamente")
                break
        else:
            print("El usuario no se encontro en la base de datos")    
    elif (opcion == 4):
        usuario_actualizado = input("Ingrese el nombre del usuario que deseas actualizar")
        for usuario in usuarios:
            if usuario[0] == usuario_actualizado:
                nombre_nuevo = input("Ingrese nuevo nombre: ")
                apellido_nuevo = input("Ingrese nuevo apellido: ")
                correo_nuevo = input("Ingrese nuevo correo: ")
                edad_nuevo = int(input("Ingrese nueva edad: "))
    else:
        print("Opción no valida por favor dijite la correcta")