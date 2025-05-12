from functions import * # import functions

# function for add products
def add_product():
    while True:
        name_product = input("\nDigite nombre del producto: ").strip()
        if name_product != "" and any(c.isalpha() for c in name_product):
            break
        else:
            print("\033[93m\nEl nombre debe contener al menos una letra.\033[0m")
    while True:
        amount_product = input("\nDigite la cantidad de producto: ")
        if amount_product.isdigit():
            amount_product = int(amount_product)
            break
        else:
            print("\033[93m\nDebe ser un número entero válido.\033[0m")
    while True:
        price_product = input("\nDigite el precio del producto: ")
        if price_product.replace(".", "", 1).isdigit():
            price_product = float(price_product)
            break
        else:
            print("\033[93m\nDebe ser un número válido.\033[0m")
    add_product_function(name_product, amount_product, price_product)

# function for search products
def search_product():
    while True:
        search_name = input("\nDigite nombre de producto a buscar: ").lower()
        if search_name == "":
            print("\033[93m\nEl nombre no puede estar vacío. Por favor ingrésalo nuevamente.\033[0m")
            continue
        if not search_name in inventary:
            print("\033[93m\nNo se encontró ningún producto con ese nombre. Intenta nuevamente.\033[0m")
        else:
            break
    search_product_function(search_name)

# function for update products
def update_product():
    while True:
        update_name = input("\nDigite producto a actualizar: ")
        if update_name in inventary:
            break
        else:
            print("\033[93m\nEste producto no existe en el inventario.\033[0m")
    update_product_function(update_name)

# function for eliminate products
def eliminate_product():
    while True:
        eliminate_name = input("\nDigite nombre de producto a eliminar: ")
        if eliminate_name in inventary:
            eliminate_product_function(eliminate_name)
            break
        else:
            print("\033[93m\nEste producto no existe en el inventario.\033[0m")

# function for add initials products
add_initials_products()

# initial menu
while True:
    print("\033[96m\n===============================================\nBienvenido al sistema de inventario\n===============================================\033[0m")
    print("\033[93mPor favor seleccione una opción:\033[0m")
    print("\n1.) Añadir producto")
    print("2.) Buscar producto")
    print("3.) Actualizar producto")
    print("4.) Eliminar producto")
    print("5.) Calcular inventario")
    print("6.) Mostrar inventario")
    print("7.) Salir")

    option = int(input("\n\033[93mElije la opción que deseas: \033[0m"))

# diferents options to choose for the user
    match option:
        case 1:
            while True:
                add_product() #call the function
                if not advance_function_product(): #call the function
                    break
        case 2:
            while True:
                if empty_list(): #call the function
                    break
                search_product() #call the function
                if not advance_function_search(): #call the function
                    break
        case 3:
            while True:
                if empty_list(): #call the function
                    break
                update_product() #call the function
                if not advance_function_update(): #call the function
                    break            
        case 4:
            while True:
                if empty_list(): #call the function
                    break
                eliminate_product() #call the function
                if not advance_function_remove(): #call the function
                    break
        case 5:
            calculation_function() #call the function
            return_to_menu_or_exit() #call the function
        case 6:
            if empty_list(): #call the function
                return_to_menu_or_exit() #call the function
            else:
                show_all_products() #call the function
                return_to_menu_or_exit() #call the function
        case 7:
            print("\n\033[93mSaliendo del sistema...\033[0m")
            print("\n\033[93mVuelva pronto\033[0m")
            break