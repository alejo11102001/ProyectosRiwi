from functions import *  # Importa todas las funciones definidas en el archivo 'funtions.py'

def add_product():
    # Función para agregar un producto al inventario
    while True:
        # Solicita el nombre del producto y verifica que contenga al menos una letra
        name_product = input("\nIngrese nombre del producto: ").strip()
        if name_product != "" and any(c.isalpha() for c in name_product):
            break
        else:
            print("\033[91m\nEl nombre debe contener al menos una letra.\033[0m")

    while True:
        # Solicita la cantidad del producto y verifica que sea un número entero válido
        amount_product = input("\nDigite la cantidad de productos: ")
        if amount_product.isdigit():
            amount_product = int(amount_product)
            break
        else:
            print("\033[91m\nDebe ser un número entero válido.\033[0m")

    while True:
        # Solicita el precio unitario del producto y verifica que sea un número válido
        unit_Price = input("\nDigite precio unitario del producto: ")
        if unit_Price.replace(".", "", 1).isdigit():
            unit_Price = float(unit_Price)
            break
        else:
            print("\033[91m\nDebe ser un número válido.\033[0m")

    # Llama a la función para agregar el producto con la información proporcionada
    add_product_function(name_product, amount_product, unit_Price)

def search_products():
    # Función para buscar un producto en el inventario
    while True:
        # Solicita el nombre del producto a buscar y verifica que no esté vacío
        search_product = input("\nIngrese el nombre del producto que quiere buscar: ").lower()
        if search_product == "":
            print("\033[91m\nEl nombre no puede estar vacío. Por favor ingrésalo nuevamente.\033[0m")
            continue
        if not search_product in products:
            # Si no se encuentra el producto, muestra un mensaje de error
            print("\033[91m\nNo se encontró ningún producto con ese nombre. Intenta nuevamente.\033[0m")
        else:
            break
    # Llama a la función que realiza la búsqueda del producto en el inventario
    search_products_function(search_product)

def update_product():
    # Función para actualizar el precio de un producto
    while True:
        # Solicita el nombre del producto a actualizar
        update = input("\nIngrese el nombre del producto que quiere actualizar: ")
        if update in products:
            # Si el producto existe, se procede con la actualización
            print(f"\033[93m\nActualizando producto: {update}\033[0m")
            break
        else:
            # Si el producto no existe, muestra un mensaje de error
            print("\033[91m\nEste producto no existe en el inventario.\033[0m")
    # Llama a la función que realiza la actualización del producto
    update_product_function(update)

def eliminate_product():
    # Función para eliminar un producto del inventario
    while True:
        # Solicita el nombre del producto a eliminar
        product_eliminate = input("\nIngrese el nombre del producto que quiere eliminar: ")
        if product_eliminate in products:
            # Si el producto existe, se elimina del inventario
            eliminate_product_function(product_eliminate)
            break
        else:
            # Si el producto no existe, muestra un mensaje de error
            print("\033[91m\nEste producto no existe en el inventario.\033[0m")

def calculation():
    # Función para calcular el valor total del inventario
    calculation_function(products)

# Menú principal del sistema
while True:
    # Muestra el menú con las opciones disponibles
    print("\033[96m\n===============================================\nBienvenido al sistema de inventario\n===============================================\033[0m")
    print("\033[93mPor favor seleccione una opción:\033[0m")
    print("\n1.) Añadir producto")
    print("2.) Buscar producto")
    print("3.) Actualizar producto")
    print("4.) Eliminar producto")
    print("5.) Calcular inventario")
    print("6.) Mostrar inventario")
    print("7.) Salir")

    # Solicita al usuario que elija una opción
    option = input("\n\033[93mElije la opción que deseas: \033[0m")

    if option == "1":
        # Si elige la opción de agregar producto, ejecuta la función correspondiente
        while True:
            add_product()
            if not advance_function_product():
                break
    elif option == "2":
        # Si elige la opción de buscar producto, ejecuta la función correspondiente
        while True:
            if empty_list():
                break
            search_products()
            if not advance_function_search():
                break
    elif option == "3":
        # Si elige la opción de actualizar producto, ejecuta la función correspondiente
        while True:
            if empty_list():
                break
            update_product()
            if not advance_function_update():
                break
    elif option == "4":
        # Si elige la opción de eliminar producto, ejecuta la función correspondiente
        while True:
            if empty_list():
                break
            eliminate_product()
            if not advance_function_remove():
                break
    elif option == "5":
        # Si elige la opción de calcular inventario, ejecuta la función correspondiente
        calculation()
        return_to_menu_or_exit()
    elif option == "6":
        # Si elige la opción de mostrar inventario, ejecuta la función correspondiente
        if empty_list():
            return_to_menu_or_exit()
        else:
            show_all_products()
            return_to_menu_or_exit()
    elif option == "7":
        # Si elige la opción de salir, termina el programa
        print("\n\033[93mSaliendo del sistema...\033[0m")
        print("\n\033[92mVuelva pronto\033[0m")
        break
    else:
        # Si la opción es inválida, muestra un mensaje de error
        print("\n\033[91mOpción inválida.\033[0m")
