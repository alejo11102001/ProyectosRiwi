#En estos ciclos while se estan validando que el usuario no digite numeros negativos, ni letras en vez de numeros y en caso de hacerlo se le indica al usuario el error
    while True: 
     try:
         unit_Price = float(input("Digite precio unitario: "))
         if (unit_Price <  0): 
             print("Digite un numero valido para precio unitario") 
         else:
             break 
     except ValueError:
         print("Por favor digite un valor valido")  
    while True:
     try:
         number_product = int(input("Digite la cantidad de productos a comprar: "))
         if (number_product < 0):
             print("Digite un numero valido para cantidad de productos")
         else:
             break 
     except ValueError:
         print("Por favor digite un valor valido")   
    while True:
     try:
         percentage_number = float(input("Digite el valor del descuento: "))
         if not(0 <= percentage_number  <= 100):
             print("Digite un numero valido para el porcentaje de descuento")
         else:
             break 
     except ValueError:
         print("Por favor digite un valor valido")
# Aqui se estan haciendo todas las operaciones pertinentes para mostrar al usuario el resultado
    subtotal = unit_Price * number_product
    percentage = (subtotal * percentage_number )/100
    total_price = subtotal - percentage
    
    print(f"El producto a comprar es {name_Product} y el valor total de la compra es {total_price}")