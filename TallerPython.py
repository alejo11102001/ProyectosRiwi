from tabulate import tabulate

compras = []
continuar = True
print("\n===============================================\nBienvenido al sistema de registro de compras\n===============================================")
while continuar:

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
    compras.append(compra) #investigar nueva forma de agregar un registro

    valor = input("\n¿Deseas continuar ingresando compras?: S()si N()no: ")
    # text-transform: lowercase.css
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

            tabla.append([i+1, name_Product, number_product, f"${unit_Price:.2f}", percentage_number, f"${subtotal_price:.2f}"])

        encabezado = ["#", "Producto", "Cantidad", "Precio Unitario", "Descuento (%)", "Total Producto"]
        print(tabulate(tabla, headers=encabezado, tablefmt="pretty")) #como se llama el uso de la importancion

        print(f"\n{'Total de la factura:':<63} ${total_price:.2f}")