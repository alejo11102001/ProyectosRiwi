compras = []
continuar = True
total_factura = 0
print("\n===============================================\nBienvenido al sistema de registro de compras\n===============================================")
while continuar:

    name_Product = input("\nIngrese nombre de producto: ")
    number_product = int(input("Digite la cantidad de productos a comprar: "))
    unit_Price = float(input("Digite precio unitario: "))
    percentage_number = float(input("Digite el valor del descuento: "))

    compra = [name_Product, number_product, unit_Price, percentage_number]
    compras.append(compra)

    valor = input("\n¿Deseas continuar ingresando compras?: S()si N()no: ")
    print("\n Gracias por tu compra aqui tienes tu factura")
    if valor == "N" or valor == "n":
        continuar = False 
        subtotal = unit_Price * number_product
        percentage = (subtotal * percentage_number )/100
        total_price = subtotal - percentage

        total_factura += total_price
    else:
        for i in range(len(compras)):
            print(f"\n{i+1}. {compras[i][0]}, {compras[i][1]}, {compras[i][2]}, {compras[i][3]}")
        print(f"\nTotal de todas las compras: ${total_factura}")
    

