nombre_producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))

subtotal = precio * cantidad

print("\n--- RESUMEN DE COMPRA ---")
print(f"Producto: {nombre_producto}")
print(f"Precio unitario: ${precio:.0f}")
print(f"Cantidad: {cantidad}")
print(f"Total: ${subtotal:.0f}")
