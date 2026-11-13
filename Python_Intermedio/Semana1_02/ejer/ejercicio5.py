'''
if edad < 18:
    raise ValueError("Debes ser mayor de 18)
'''
# Ahora con ese raise si la edad es menor a 18 entonces nos dará en ValueError. Ahora los ValueError abarca nuestra condición


def procesar_transferencia(saldo_origen, saldo_destino, monto):
    try:
        saldo_origen = float(saldo_origen)
        saldo_destino = float(saldo_destino)
        monto = float(monto)
        total = saldo_origen + saldo_destino

        assert monto>0, "Error, ingrese un monto valido"
        assert saldo_origen-monto>=0, "Error, saldo insuficiente"

        total = saldo_origen + saldo_destino
        nuevo_origen = saldo_origen - monto
        nuevo_destino = saldo_destino + monto

        assert total == nuevo_destino + nuevo_origen, "Error, el salto total no cuadra"

        return nuevo_origen, nuevo_destino
    
    except ValueError:
        print("Ingrese valores reales")
        return None
    except AssertionError as e:
        print(f"Error de validación: {e}")
        return None
    except Exception as e:
        print("Error no previsto")
        return None

    
saldo_origen = input("Ingrese el saldo de origen: ")
saldo_destino = input("Ingrese el saldo de destino: ")
monto = input("Ingrese el monto: ")

resultado = procesar_transferencia(saldo_origen, saldo_destino, monto)
if resultado is not None:
    
    #print(resultado)   --> nos da (valor1, valor2)

    saldo_origen, saldo_destino = resultado
    print(f"saldo_origen: {saldo_origen}")
    print(f"saldo_destino: {saldo_destino}")
