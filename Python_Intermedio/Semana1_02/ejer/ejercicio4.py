# assert: Para agregar una condición que de no cumplirse nos de un error.

def valor(mensaje):
    x = input(mensaje).strip()
    return x

def calcular_descuento(precio, porcentaje):
    try:
        precio = float(precio)
        porcentaje = float(porcentaje)

        assert precio>0, "El precio debe ser mayor a 0"
        assert 0 <= porcentaje <= 100, "Porcentaje fuera del rango permitido"
        descuento = (precio*porcentaje)/100
        return precio - descuento
    except ValueError:
        print("ERROR, el precio y el porcentaje de descuento del producto deben ser valores reales")
        return None
    except AssertionError as e:
        print("Error de validación de datos")
        print(f"{e}")
        return None
    except Exception as e:
        print("Error no previsto")
        print(f"{e}")
        return None
    



precio = valor("Ingrese el precio del producto(precio>0): ")
porcentaje = valor("Ingrese el porcentaje de descuento del producto(0<=porcentaje<=100): ")

resultado = calcular_descuento(precio, porcentaje)
if(resultado is not None):
    print(f"Resultado = {resultado}")
