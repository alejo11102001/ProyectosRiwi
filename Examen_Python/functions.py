from tabulate import tabulate # import tabulate to table

inventary = {} # create a diccionary

# function for add initials products
def add_initials_products():
    add_product_function("manzanas", 6, 3000)
    add_product_function("bananas", 5, 3000)
    add_product_function("naranjas", 4, 4000)
    add_product_function("leche", 8, 6000)
    add_product_function("pan", 10, 2000)

# function for add products
def add_product_function(name_product, amount_product, price_product):
    inventary[name_product] = {
        "Amount" : amount_product,
        "Price" : price_product
    }
    print(f"\033[92m\nProducto '{name_product}' agregado correctamente.\033[0m")

# function for search products
def search_product_function(search_name):
    while True:
        if search_name in inventary:
            data_inventary = inventary[search_name]
            table = [[
                f"\033[94m{search_name}\033[0m",
                f"\033[93m{data_inventary['Amount']:,.2f}\033[0m",  
                f"\033[92m${data_inventary['Price']:,.2f}\033[0m"
            ]]
            print("\n\033[96mProducto encontrado:\033[0m")
            print(tabulate(table, headers=["\033[95mNombre\033[0m", "\033[95mCantidad\033[0m", "\033[95mPrecio\033[0m"], tablefmt="pretty"))
            break

# function for update products
def update_product_function(update_name):
    while True:
        new_price = input("\nIngrese nuevo precio del producto (Enter para dejar igual): ")
        if new_price == "":
            print("\033[93m\nEl precio quedo igual al anterior.\033[0m")
            break
        elif new_price.replace(".", "", 1).isdigit():
            inventary[update_name]["Price"] = float(new_price)
            print("\033[92m\nProducto actualizado correctamente.\033[0m")
            break
        else:    
            print("\033[91m\nPrecio inválido, digite valor valido\033[0m")

# function for eliminate products
def eliminate_product_function(eliminate_name):
    if eliminate_name in inventary:
        inventary.pop(eliminate_name)
        print(f"\033[92m\nProducto '{eliminate_name}' eliminado correctamente.\033[0m")
        if len(inventary) == 0:
            print("\033[93m\nYa no hay más productos registrados.\033[0m")
    else:
        print(f"\033[93m\nProducto '{eliminate_name}' no se encuentra en el inventario.\033[0m")

# function for calculate total inventary
def calculation_function():
    total_calculation = sum(product["Amount"] * product["Price"] for product in inventary.values())  
    print(f"\033[92m\nTotal inventario: ${total_calculation:,.2f}\033[0m")

# function for show all products of diccionary in a table
def show_all_products():
    table = []
    for name, data in inventary.items():
        table.append([f"\033[94m{name}\033[0m", f"\033[93m{data['Amount']}\033[0m", f"\033[92m${data['Price']:,.2f}\033[0m"])
    print(tabulate(table, headers=["\033[95mNombre\033[0m", "\033[95mCantidad\033[0m", "\033[95mPrecio\033[0m"], tablefmt="pretty"))

# function for return menu or exit
def return_to_menu_or_exit():
    while True:
        option_out = input("\033[93m\n¿Deseas volver al menú inicial?: S()si N()no:\033[0m")
        if option_out == "s":
            return False  
        elif option_out == "n":
            print("\033[93mSaliendo del sistema...\033[0m")
            exit()  
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

# function for continue in the action 
def advance_function_product():
    while True:
        output_menu = input("\033[93m\n¿Deseas continuar ingresando productos?: S()si N()no:\033[0m")
        if output_menu == "n":
            return return_to_menu_or_exit()  
        elif output_menu == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

# function for continue in the action 
def advance_function_search():
    while True:
        search_again = input("\033[93m\n¿Deseas buscar otro producto?: S()si N()no: \033[0m")
        if search_again == "n":
            return return_to_menu_or_exit()
        elif search_again == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

# function for continue in the action 
def advance_function_update():
    while True:
        output_update = input("\033[93m\n¿Deseas actualizar otro producto? S(si) N(no): \033[0m")
        if output_update == "n":
            return return_to_menu_or_exit()  
        elif output_update == "s":
            return True 
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

# function for continue in the action 
def advance_function_remove():
    while True:
        output_remove = input("\033[93m\n¿Deseas eliminar otro producto? S(si) N(no): \033[0m")
        if output_remove == "n":
            return return_to_menu_or_exit() 
        elif output_remove == "s":
            return True
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

# function for check amount products in the diccionary
def empty_list():
    if not inventary:
        print("\033[91m\nNo hay productos registrados en el inventario.\033[0m")
        return True
    return False