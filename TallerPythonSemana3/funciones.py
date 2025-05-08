from tabulate import tabulate

products = {}

def add_product_funtion(name_product, amount_product, price_product):
    products[name_product] = {
        "Cantidad": amount_product,
        "Precio unitario": price_product
    }
    print(f"\033[92m\nProducto '{name_product}' agregado correctamente.\033[0m")
    
def search_products_funtion(search_product):
    while True:
        if search_product in products:
            data_inventary = products[search_product]
            table = [[
                f"\033[94m{search_product}\033[0m", 
                f"\033[93m{data_inventary['Cantidad']}\033[0m", 
                f"\033[92m${data_inventary['Precio unitario']:.2f}\033[0m"
            ]]
            print("\n\033[96mProducto encontrado:\033[0m")
            print("\033[96m" + "="*50 + "\033[0m")
            print(tabulate(table, headers=[
                "\033[95mNombre del producto\033[0m", 
                "\033[95mCantidad\033[0m", 
                "\033[95mPrecio unitario\033[0m"
            ], tablefmt="pretty"))
            print("\033[96m" + "="*50 + "\033[0m")
            break

def update_product_funtion(update):
    while True:
        new_amount = input("\nIngrese nuevo precio del producto (Enter para dejar igual): ")
        if new_amount == "":
            print("\033[92m\nEl precio quedo igual al anterior.\033[0m")
            break
        elif new_amount.replace(".", "", 1).isdigit():
            products[update]["Precio unitario"] = float(new_amount)
            print("\033[92m\nProducto actualizado correctamente.\033[0m")
            break
        else:
            print("\033[91m\nPrecio inválido, digite valor valido\033[0m")

def eliminate_product_funtion(product_eliminate):
    if product_eliminate in products:
        products.pop(product_eliminate)
        print(f"\033[92m\nEl producto '{product_eliminate}' ha sido eliminado correctamente\033[0m")
        if len(products) == 0:
            print("\033[93m\nYa no hay más productos registrados.\033[0m")
    else:
        print("\033[91m\nEl producto no existe en el inventario.\033[0m")

def calculation_function(products):
    total_multiplication = lambda p: p["Cantidad"] * p["Precio unitario"]
    total_calculation = sum(total_multiplication(p) for p in products.values())
    print("\n\033[96mCálculo del valor total del inventario:\033[0m")
    print("\033[92m" + "="*50 + "\033[0m")
    print(f"\033[1;92mTotal: ${total_calculation:.2f}\033[0m")
    print("\033[92m" + "="*50 + "\033[0m")

def show_all_products():
    if not products:
        print("\033[91m\nNo hay productos registrados en el inventario.\033[0m")
        return
    table = []
    for name, data in products.items():
        table.append([
            f"\033[94m{name}\033[0m",
            f"\033[93m{data['Cantidad']}\033[0m",
            f"\033[92m${data['Precio unitario']:.2f}\033[0m" 
            ])
    print("\n\033[96mInventario actual:\033[0m")
    print("\033[96m" + "="*50 + "\033[0m")
    print(tabulate(table, headers=[
        "\033[95mNombre del producto\033[0m",
        "\033[95mCantidad\033[0m",
        "\033[95mPrecio unitario\033[0m"
        ], tablefmt="pretty"))
    print("\033[96m" + "="*50 + "\033[0m")

def return_to_menu_or_exit():
    while True:
        option_out = input("\033[93m\n¿Deseas volver al menú inicial?: S()si N()no:\033[0m")
        if option_out == "s":
            return False
        elif option_out == "n":
            print("\n\033[93mSaliendo del sistema...\033[0m")
            exit()
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_funtion_product():
    while True:
        output_menu = input("\033[93m\n¿Deseas continuar ingresando productos?: S()si N()no:\033[0m")
        if output_menu == "n":
            return return_to_menu_or_exit()
        elif output_menu == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_funtion_search():
    while True:
        search_again = input("\033[93m\n¿Deseas buscar otro producto?: S()si N()no: \033[0m")
        if search_again == "n":
            return return_to_menu_or_exit()
        elif search_again == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_funtion_update():
    while True:
        output_update = input("\033[93m\n¿Deseas actualizar otro producto? S(si) N(no): \033[0m")
        if output_update == "n":
            return return_to_menu_or_exit()
        elif output_update == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_funtion_remove():
    while True:
        output_remove = input("\033[93m\n¿Deseas eliminar otro producto? S(si) N(no): \033[0m")
        if output_remove == "n":
            return return_to_menu_or_exit()
        elif output_remove == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")