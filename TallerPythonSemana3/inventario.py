from funciones import *

def add_product():
    while True:
        name_product = input("\nIngrese nombre del producto: ").strip()
        if name_product != "" and any(c.isalpha() for c in name_product):
            break
        else:
            print("\nEl nombre debe contener al menos una letra.")

    while True:
        amount_product = input("\nDigite la cantidad de productos: ")
        if amount_product.isdigit():
            amount_product = int(amount_product)
            break
        else:
            print("\nDebe ser un número entero válido.")

    while True:
        unit_Price = input("\nDigite precio unitario del producto: ")
        if unit_Price.replace(".", "", 1).isdigit():
            unit_Price = float(unit_Price)
            break
        else:
            print("\nDebe ser un número válido.")

    add_product_funtion(name_product, amount_product, unit_Price)

def search_products():
    while True:
        search_product = input("\nIngrese el nombre del producto que quiere buscar: ").lower()
        if search_product == "":
            print("\033[91m\nEl nombre no puede estar vacío. Por favor ingrésalo nuevamente.\033[0m")
            continue
        if not search_product in products:
            print("\033[91m\nNo se encontró ningún producto con ese nombre. Intenta nuevamente.\033[0m")
        else:
            break 
    search_products_funtion(search_product)

def update_product():
    while True:
        update = input("\nIngrese el nombre del producto que quiere actualizar: ")
        if update in products:
            print(f"\nActualizando producto: {update}")
            break
        else:
            print("\033[91m\nEste producto no existe en el inventario.\033[0m")
    update_product_funtion(update)

def eliminate_product():
    if len(products) == 0:
        print("\033[91m\nNo hay productos registrados\033[0m")
    else:
        while True:       
            product_eliminate = input("\nIngrese el nombre del producto que quiere eliminar: ")

            eliminate_product_funtion(product_eliminate)
            break

def calculation():
    calculation_function(products)

while True:
    print("\033[96m\n===============================================\nBienvenido al sistema de inventario\n===============================================\033[0m")
    print("\033[93mPor favor seleccione una opción:\033[0m")
    print("\n1.) Añadir produto")
    print("2.) Buscar producto")
    print("3.) Actualizar producto")
    print("4.) Eliminar producto")
    print("5.) Calcular inventario")
    print("6.) Mostrar inventario")
    print("7.) Salir")

    option = input("\n\033[93mElije la opción que deseas: \033[0m")

    if option == "1":
        add_product()
    elif option == "2":
        search_products()
    elif option == "3":
        update_product()
    elif option == "4":
        eliminate_product()
    elif option == "5":
        calculation()
    elif option == "6":
        print("Tabla")
    elif option == "7":
        print("\nSaliendo...")
        print("\nVuelva pronto")
        break
    else:
        print("Opción inválida.")

#consultar productos
##buscar producto por nombre => detalle de precio y cantidad
##Si el producto no está en el inventario, se debe notificar adecuadamente

#actualizar precios
## actualizar mediante el nombre del producto

# Eliminar productos:
## El programa debe permitir al usuario eliminar productos del inventario de manera segura

# Calcular el valor total del inventario:
## El programa debe calcular el valor total de los productos en inventario y mostrarlo al usuario
## Para ello, utilizarás una función anónima (lambda) que facilite este cálculo.