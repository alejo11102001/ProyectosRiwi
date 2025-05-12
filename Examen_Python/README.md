# Sistema de Inventario en Python

Este proyecto es un sistema de gestión de inventario por consola que permite registrar, buscar, actualizar, eliminar, mostrar y calcular el valor total de los productos almacenados.

---

## Archivos del Proyecto

- `inventary_index.py`: Archivo principal que contiene el menú y controla la interacción del usuario.
- `funtions.py`: Contiene todas las funciones relacionadas con la lógica del inventario.
- `inventary`: Diccionario global donde se almacenan los productos.

---

## Funcionalidades

- **Añadir productos**: Registro de nombre, cantidad y precio.
- **Buscar productos**: Consulta individual por nombre con formato tabular.
- **Actualizar productos**: Modificación del precio de un producto existente.
- **Eliminar productos**: Eliminación de productos registrados por nombre.
- **Calcular inventario**: Muestra el valor total del inventario en pesos colombianos.
- **Mostrar inventario**: Despliegue en tabla de todos los productos registrados.
- **Control de flujo**: Permite repetir operaciones o volver al menú principal tras cada acción.

---

## Ejemplo de Uso

===============================================
Bienvenido al sistema de inventario
===============================================
1.) Añadir produto
2.) Buscar producto
3.) Actualizar producto
4.) Eliminar producto
5.) Calcular inventario
6.) Mostrar inventario
7.) Salir

Elije la opción que deseas: 

## Requisitos

- Python 3.6 o superior

- Biblioteca externa tabulate
