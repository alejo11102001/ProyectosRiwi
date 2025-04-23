usuarios = []
continuar = True

while continuar:
    nombre = input("ingresa el nombre: ")
    usuarios.append([nombre])
    print(usuarios)
    valor = input("deseas continuar: S()si N(no)")
    if (valor == "N"):
        continuar = False


#registrar usuarios, con un menu que se puedan hacer las operaciones basicas, nombre, apellido, correo, edad, que el correo no se repita