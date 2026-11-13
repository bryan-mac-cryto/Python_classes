# Usando EXCEPCIONES PERSONALIZADAS. Se puede formar bucles como en este ejemplo,
# aunque aún no estoy seguro de que tan práctico sea su uso.

class SaldoInsuficienteError(Exception):
    pass
class StockInsuficienteError(Exception):
    pass

def procesar_compra(saldo_usuario, stock_producto, precio_unitario, cantidad):
    
    saldo_usuario = float(saldo_usuario)
    stock_producto = int(stock_producto)
    precio_unitario = float(precio_unitario)
    cantidad = int(cantidad)

    if cantidad <= 0 or precio_unitario <= 0 or saldo_usuario < 0 or stock_producto < 0:
        raise ValueError("Los datos numéricos son invalidos")
    
    if cantidad > stock_producto:
        raise StockInsuficienteError("Error, no hay suficiente inventario disponible")


    total_a_pagar = precio_unitario * cantidad

    if total_a_pagar > saldo_usuario:
        faltante = total_a_pagar - saldo_usuario
        raise SaldoInsuficienteError(f"Error, saldo insuficiente. Faltante: S/. {faltante:.2f}")

    nuevo_saldo = saldo_usuario - total_a_pagar
    nuevo_stock = stock_producto - cantidad

    return nuevo_saldo, nuevo_stock

saldo_usuario = input("Ingrese el saldo del usuario: ").strip()
stock_producto = input("Ingrese el stock del producto: ").strip()
precio_unitario = input("Ingrese el precio unitario: ").strip()
cantidad = input("Ingrese la cantidad: ").strip()

while True:
    try:
        nuevo_saldo, nuevo_stock = procesar_compra(saldo_usuario, stock_producto, precio_unitario, cantidad)
        print(f"Operacion exitosa. Nuevo saldo: S/.{nuevo_saldo:.2f} | Nuevo stock: {nuevo_stock} ")
        break

    except SaldoInsuficienteError as e:
        print(e)
        opcion = input("¿Desea recargar saldo ahora para completar la compra? (s/n): ")
        if opcion.lower() == "s":
            try:
                agregado = input("Ingrese el monto extra: ").strip()
                agregado = float(agregado)

                if(agregado<=0):
                    raise ValueError("Monto ingresado invalido")
                else:
                    saldo_usuario = float(saldo_usuario) + agregado
            except ValueError as e:
                print(e)
                break
        else:
            print("Compra cancelada por el usuario")
            break

    except StockInsuficienteError as e:
        print(e)
        opcion = input("¿Desea corregir la cantidad ahora para completar la compra? (s/n): ")
        if opcion.lower() == "s":
            try:
                cantidad = int(input("Ingrese la cantidad corregida").strip())
                if(cantidad > int(stock_producto) or cantidad == 0):
                    raise ValueError("No se ingreso una cantidad valida")
            except ValueError as e:
                print(e)
                break
        else:
            print("Compra cancelada")
            break

    except ValueError as e:
        print(e)    
        break
        