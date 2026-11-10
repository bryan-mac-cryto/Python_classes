'''
Ejercicio 1: Conversión segura a entero
Escribe una función pedir_entero(texto) que intente convertir texto a int.
* Si la conversión funciona, debe devolver el número.
* Si ocurre un ValueError, debe imprimir "Error: La cadena no es un número entero válido" y devolver None.
''' 

def convertir(x):
    return int(x)

numero = input("Ingrese un número: ")
try:
    convertir(numero)
except(ValueError):
    print("Error en el valor ingresado")
print(numero)
