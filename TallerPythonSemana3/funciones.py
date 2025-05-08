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
            data_book = products[search_product]
            table = [[search_product, data_book["Cantidad"], data_book["Precio unitario"]]]
            print(tabulate(table, headers=["Nombre producto", "Cantidad", "Precio unitario"], tablefmt="pretty"))
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
    print(f"\nEl valor total del inventario es: ${total_calculation}")

