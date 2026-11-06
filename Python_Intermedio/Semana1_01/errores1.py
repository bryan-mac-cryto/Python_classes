# Ejemplo de un error de sintaxis
'''
if 3.14157 > 1.2
    print("Una aproximacion de pi es mayor que 1.2")
'''
# Corrección (le faltaba : en el if)
if 3.14157 > 1.2:
    print("Una aproximacion de pi es mayor que 1.2\n")



# Otro ejemplo de un error de sintaxis
'''
a = 23
b = 12
c = 9
d = 3.21
resultado = a+b * (c*d))
print(resultado)
'''
# Corrección (le faltaba '(' en la asignación de resultado)
a = 23
b = 12
c = 9
d = 3.21
resultado = (a+b * (c*d))
print(resultado)


# Otro ejemplo de error de sintaxis (utilización de una palabra reservada como variable)
'''
def = 10
'''

# Para obtener la lista de palabras reservadas
help("keywords")


# Indectación inconsistente (o sangría)
'''
if True:
    print("Hola")
        print("Mundo")
'''
# Corrección
if True:
    print("Hola")
    print("Mundo")

# Error lógico
'''
def promedio(lista):
    suma = 0.0
    for x in lista:
        suma -= x
    return suma/len(lista)-1
'''

# Ejemplo corregido
def promedio(lista):
    suma = 0.0
    for x in lista:
        suma += x  # 1. Sumamos cada elemento
    return suma / len(lista)  # 2. Dividimos entre la cantidad total de elementos