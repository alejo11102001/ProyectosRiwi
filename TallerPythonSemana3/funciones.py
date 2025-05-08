from tabulate import tabulate
import re
products = {}

def add_product():
    while True: 
        name_product = input("\nIngrese nombre del producto: ").strip()
        if re.match(r'^[\w\s%]+$', name_product) and re.search(r'[a-zA-Z]', name_product):
            break
        else:
            print("\nEl nombre del producto debe contener letras, y puede incluir números, espacios y el símbolo %. No se permiten solo números o símbolos.")
    while True:    
        amount_product = (input("\nDigite la cantidad de productos: "))
        if amount_product.isdigit():
            amount_product = int(amount_product)
            break
        else:
            print("\nLa cantidad de productos no puede contener letras ni caracteres especiales, tampoco negativos.")
    while True:
        unit_Price = (input("\nDigite precio unitario del producto: "))
        if unit_Price.replace(".", "", 1).isdigit():
            unit_Price = float(unit_Price)
            break
        else:
            print("\nEl valor no puede contener letras ni caracteres especiales, tampoco negativos.")   

    products[name_product] = {
                "Cantidad": amount_product,
                "Precio unitario": unit_Price
            }
    
def search_products():
    while True:
        search_product = input("\nIngrese el nombre del producto que quiere buscar: ").lower()
        if search_product == "":
            print("\033[91m\nEl nombre no puede estar vacío. Por favor ingrésalo nuevamente.\033[0m")
            continue
        find = False
        if search_product in products:
            data_book = products[search_product]
            table = [[search_product, data_book["Cantidad"], data_book["Precio unitario"]]]
            print(tabulate(table, headers=["Nombre", "Cantidad", "Precio unitario"], tablefmt="pretty"))
            find = True
            break
        if not find:
            print("\033[91m\nNo se encontró ningún producto con ese nombre. Intenta nuevamente.\033[0m")
        else:
            break 

def update_product():
    while True:
        update = input("\nIngrese el nombre del producto que quiere actualizar: ")
        if update in products:
            print(f"\nActualizando producto: {update}")

            while True:
                new_amount = input("\nIngrese nuevo precio del producto (Enter para dejar igual): ")
                if new_amount == "":
                    break
                elif new_amount.replace(".", "", 1).isdigit():
                    products[update]["Precio unitario"] = float(new_amount)
                    break
                else:
                    print("\033[91m\nPrecio inválido, digite valor valido\033[0m")
            print("\033[92m\nProducto actualizado correctamente.\033[0m")
            print(products)
            break
        else:
            print("\033[91m\nEste producto no existe en el inventario.\033[0m")