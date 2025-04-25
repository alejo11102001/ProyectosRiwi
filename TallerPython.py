from tabulate import tabulate

compras = []
continuar = True
print("\n===============================================\nBienvenido al sistema de registro de compras\n===============================================")
while continuar:
# Aqui hacemos la solicitud de datos e ingreso de ellos a la lista, ademas de las validaciones para que el usuario no ingrese algo erroneo
    while True: 
            name_Product = input("\nIngrese nombre de producto: ")
            if name_Product.isalpha():
                break
            else:
                print("\nEl nombre del producto no puede contener numeros ni caracteres especiales.") 
    while True:    
            number_product = (input("\nDigite la cantidad de productos a comprar: "))
            if number_product.isdigit():
                number_product = int(number_product)
                break
            else:
                print("\nLa cantidad de productos no puede contener letras ni caracteres especiales.")
    while True:
            unit_Price = (input("\nDigite precio unitario: "))
            if unit_Price.isdigit():
                unit_Price = float(unit_Price)
                break
            else:
                print("\nEl valor no puede contener letras ni caracteres especiales.")   
    while True:
        try:
            percentage_number = float(input("\nDigite el valor del descuento (%): "))
            if 0 <= percentage_number <= 100:
                break 
            else:
                print("\nEl valor del porcentaje no puede contener letras ni caracteres especiales.")
        except ValueError:
            print("\nPor favor digite un valor valido")

    compra = [name_Product, number_product, unit_Price, percentage_number]
    compras.append(compra)

    valor = input("\n¿Deseas continuar ingresando compras?: S()si N()no: ")
# Aqui estamos haciendo todos los calculos y asignado los valores a las variables para mostrar al usuario
    if valor == "N" or valor == "n":
        continuar = False 
        print("\nGracias por tu compra aqui tienes tu factura")

        tabla = []
        total_price  = 0
        
        for i, product in enumerate(compras):
            name_Product, number_product, unit_Price, percentage_number = product
            subtotal = unit_Price * number_product
            percentage = (subtotal * percentage_number )/100
            subtotal_price = subtotal - percentage
            total_price += subtotal_price
# A partir de aca estamos creando todo el enterno de la tabla, la que el usuario va a visualizar
            tabla.append([i+1, name_Product, number_product, f"${unit_Price:.2f}", percentage_number, f"${subtotal_price:.2f}"])

        encabezado = ["#", "Producto", "Cantidad", "Precio Unitario", "Descuento (%)", "Total Producto"]
        print(tabulate(tabla, headers=encabezado, tablefmt="pretty"))

        print(f"\n{'Total de la factura:':<63} ${total_price:.2f}")