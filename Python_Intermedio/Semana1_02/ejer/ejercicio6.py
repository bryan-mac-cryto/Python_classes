# Usando raise
# ASSERT se utiliza para testear y detectar bugs, mientras que RAISE para comprobar la entrada de datos y demás

def procesar_compra(saldo_usuario, stock_producto, precio_unitario, cantidad):
    
    saldo_usuario = float(saldo_usuario)
    stock_producto = int(stock_producto)
    precio_unitario = float(precio_unitario)
    cantidad = int(cantidad)
    if cantidad <= 0 or precio_unitario <= 0 or saldo_usuario < 0:
        raise ValueError("Los datos numéricos son invalidos")
    if cantidad > stock_producto:
        raise ValueError("Error, no hay suficiente inventario disponible")

    total_a_pagar = precio_unitario * cantidad

    if total_a_pagar > saldo_usuario:
        raise ValueError("Error, saldo insuficiente")

    nuevo_saldo = saldo_usuario - total_a_pagar
    nuevo_stock = stock_producto - cantidad

    return nuevo_saldo, nuevo_stock

saldo_usuario = input("Ingrese el saldo del usuario: ")
stock_producto = input("Ingrese el stock del producto: ")
precio_unitario = input("Ingrese el precio unitario")
cantidad = input("Ingrese la cantidad: ")

try:
    nuevo_saldo, nuevo_stock = procesar_compra(saldo_usuario, stock_producto, precio_unitario, cantidad)
    print(f"Nuevo saldo: {nuevo_saldo}")
    print(f"Nuevo stock: {nuevo_stock}")
except ValueError as e:
    print(e)    
    