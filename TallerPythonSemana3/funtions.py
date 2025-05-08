from tabulate import tabulate  # Importa la librería para mostrar tablas en consola

products = {}  # Diccionario para almacenar los productos con su nombre como clave

def add_product_funtion(name_product, amount_product, price_product):
    # Agrega un producto al inventario
    products[name_product] = {
        "Cantidad": amount_product,  # Almacena la cantidad del producto
        "Precio unitario": price_product  # Almacena el precio por unidad del producto
    }
    print(f"\033[92m\nProducto '{name_product}' agregado correctamente.\033[0m")

def search_products_funtion(search_product):
    # Busca un producto por su nombre en el inventario
    while True:
        if search_product in products:
            # Si el producto se encuentra, muestra sus detalles
            data_inventary = products[search_product]
            table = [[
                f"\033[94m{search_product}\033[0m",  # Nombre del producto
                f"\033[93m{data_inventary['Cantidad']:,.2f}\033[0m",  # Cantidad del producto
                f"\033[92m${data_inventary['Precio unitario']:,.2f}\033[0m"  # Precio unitario
            ]]
            # Muestra la información del producto encontrado en formato tabla
            print("\n\033[96mProducto encontrado:\033[0m")
            print(tabulate(table, headers=["\033[95mNombre\033[0m", "\033[95mCantidad\033[0m", "\033[95mPrecio\033[0m"], tablefmt="pretty"))
            break

def update_product_funtion(update):
    # Permite actualizar el precio de un producto existente
    while True:
        new_amount = input("\nIngrese nuevo precio del producto (Enter para dejar igual): ")
        if new_amount == "":
            # Si no se ingresa nada, se mantiene el precio actual
            print("\033[92m\nEl precio quedo igual al anterior.\033[0m")
            break
        elif new_amount.replace(".", "", 1).isdigit():
            # Si el nuevo precio es válido, se actualiza el precio del producto
            products[update]["Precio unitario"] = float(new_amount)
            print("\033[92m\nProducto actualizado correctamente.\033[0m")
            break
        else:
            # Si el precio no es válido, se muestra un mensaje de error
            print("\033[91m\nPrecio inválido, digite valor valido\033[0m")

def eliminate_product_funtion(product_eliminate):
    # Elimina un producto del inventario
    if product_eliminate in products:
        # Si el producto existe, lo elimina del diccionario
        products.pop(product_eliminate)
        print(f"\033[92m\nEl producto '{product_eliminate}' ha sido eliminado correctamente\033[0m")
        if len(products) == 0:
            # Si no hay productos restantes, muestra un mensaje
            print("\033[93m\nYa no hay más productos registrados.\033[0m")
    else:
        # Si el producto no existe en el inventario, muestra un mensaje de error
        print("\033[91m\nEl producto no existe en el inventario.\033[0m")

def calculation_function(products):
    # Calcula el valor total del inventario
    total_multiplication = lambda p: p["Cantidad"] * p["Precio unitario"]  # Multiplica cantidad por precio
    total_calculation = sum(total_multiplication(p) for p in products.values())  # Suma todos los valores
    # Muestra el valor total calculado
    print(f"\033[92mTotal: ${total_calculation:,.2f}\033[0m")

def show_all_products():
    # Muestra todos los productos en inventario
    table = []
    for name, data in products.items():
        # Crea una lista de productos con su nombre, cantidad y precio
        table.append([f"\033[94m{name}\033[0m", f"\033[93m{data['Cantidad']}\033[0m", f"\033[92m${data['Precio unitario']:,.2f}\033[0m"])
    # Imprime todos los productos en formato tabla
    print(tabulate(table, headers=["\033[95mNombre\033[0m", "\033[95mCantidad\033[0m", "\033[95mPrecio\033[0m"], tablefmt="pretty"))

def return_to_menu_or_exit():
    # Pregunta si el usuario quiere regresar al menú o salir del sistema
    while True:
        option_out = input("\033[93m\n¿Deseas volver al menú inicial?: S()si N()no:\033[0m")
        if option_out == "s":
            return False  # Regresa al menú
        elif option_out == "n":
            print("\033[93mSaliendo del sistema...\033[0m")
            exit()  # Sale del sistema
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_funtion_product():
    # Pregunta si el usuario desea seguir ingresando productos
    while True:
        output_menu = input("\033[93m\n¿Deseas continuar ingresando productos?: S()si N()no:\033[0m")
        if output_menu == "n":
            return return_to_menu_or_exit()  # Regresa al menú
        elif output_menu == "s":
            return True  # Continúa ingresando productos
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_funtion_search():
    # Pregunta si el usuario desea seguir buscando productos
    while True:
        search_again = input("\033[93m\n¿Deseas buscar otro producto?: S()si N()no: \033[0m")
        if search_again == "n":
            return return_to_menu_or_exit()  # Regresa al menú
        elif search_again == "s":
            return True  # Continúa buscando productos
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_funtion_update():
    # Pregunta si el usuario desea seguir actualizando productos
    while True:
        output_update = input("\033[93m\n¿Deseas actualizar otro producto? S(si) N(no): \033[0m")
        if output_update == "n":
            return return_to_menu_or_exit()  # Regresa al menú
        elif output_update == "s":
            return True  # Continúa actualizando productos
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_funtion_remove():
    # Pregunta si el usuario desea seguir eliminando productos
    while True:
        output_remove = input("\033[93m\n¿Deseas eliminar otro producto? S(si) N(no): \033[0m")
        if output_remove == "n":
            return return_to_menu_or_exit()  # Regresa al menú
        elif output_remove == "s":
            return True  # Continúa eliminando productos
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def empty_list():
    # Verifica si la lista de productos está vacía
    if not products:
        print("\033[91m\nNo hay productos registrados en el inventario.\033[0m")
        return True  # Indica que la lista está vacía
    return False  # La lista tiene productos
