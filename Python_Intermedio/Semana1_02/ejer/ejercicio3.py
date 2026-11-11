print("CALCULADORA")
print("Escribe 'salir' en cualquier momento para cerrar")

def ingresar(mensaje):
    valor = input(mensaje).strip()
    if valor.lower() == 'salir':
        return None;
    return valor

def operacion(a, b, operador):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("ERROR, ambos valores deben ser números reales")
        return None

    try:
        if operador == '+':
            return a + b
        elif operador == '-':
                return a - b
        elif operador == '*':
                return a * b
        elif operador == '/':
                 return a / b
        else:
             print(f"Error: El operador {operador} no es válido")
             return None
    except ZeroDivisionError:
         print("Error no se puede dividir entre 0")
         return None
    except Exception as e:
         print("Error no previsto")
         return None

while True:
    a = ingresar("Ingrese el primer número(a): ")

    if(a==None):
        break

    operador = ingresar("Ingrese la operación('+', '-', '*', '/'): ")
    if(operador==None):
         break

    b = ingresar("Ingrese el segundo numero(a): ")
    if(b==None):
         break

    resultado = operacion(a, b, operador)
    if(resultado is not None):
            print(f"RESULTADO: {resultado}")
print("Saliendo de la calculadora ...")