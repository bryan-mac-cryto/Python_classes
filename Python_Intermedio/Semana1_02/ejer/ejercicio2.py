# .strip(): Sirve para eliminar caracateres no deseados en los extremos de una palabra(cadena)
# EJEMPLO:    ip = input("\nIngrese IP del objetivo (o 'salir'): ").strip()

# .split(): Sirve para cortar los datos de una cadena por los espacios, se puede hacer .split(",") y será por comas
# EJEMPLO:    lista = entrada.split()

# .append(): Sirve para agregar elementos al final
# EJEMPLO     lista.append(80)

# .lower(): Convierte una cadena str a minúsculas
# EJEMPLO:     entrada = entrada.lower()

def Buscar_elemento(lista, indice):
    try:
        indice = int(indice)
    except ValueError:
        print("El indice debe ser un numero entero")
        return None
    try:
        return lista[indice]
    except IndexError:
        print(f"Indice {indice} fuera de limites")





print("Creando una lista")

entrada = input("Ingrese los datos separados por espacios: ")


lista = [int(x) for x in entrada.split()]
'''
EQUIVALENTE A HACER ESTO:
lista = []
for x in entrada.split():
    lista.append(int(x))
'''
indice = input("Ingrese un indice para buscar el elemento en esa posición: ")

resultado = Buscar_elemento(lista, indice)
if resultado is not None:
    print(f"Elemento en la posición {indice}:  {Buscar_elemento(lista, indice)}")

