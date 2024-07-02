from os import system
from datos import lista


def mostrar_datos(lista: list):
    # Definir anchos de columnas
    col_widths = {
        'pregunta': 60,
        'a': 10,
        'b': 15,
        'c': 15,
        'correcta': 10
    }
    
    # Crear encabezado
    claves = lista[0].keys()
    encabezado = " | ".join(f"{clave:<{col_widths[clave]}}" for clave in claves)
    print(encabezado)
    print("-" * len(encabezado))
    
    # Crear filas de datos
    for datos in lista:
        fila = " | ".join(f"{str(datos[clave]):<{col_widths[clave]}}" for clave in claves)
        print(fila)
                
    #mostrar_datos(lista)            
                
def crear_sub_listas(lista: list) -> list:
    """ 
        1-Esta función (crear_sub_listas) recorre cada elemento en la lista original y extrae la pregunta, las opciones y la respuesta correcta, guardándolas en una sub-lista.
        2-Cada sub-lista contiene la pregunta, las tres opciones (a, b, c) y la respuesta correcta.
        3-La función devuelve la lista de sub-listas, que luego se almacena en la variable sub_listas.
    """   
    sub_listas = []
    for registro in lista:
        sub_lista = [
            registro['pregunta'],
            registro['a'],
            registro['b'],
            registro['c'],
            registro['correcta']
        ]
        sub_listas.append(sub_lista) #El método .append() en Python se utiliza para agregar un elemento al final de una lista.
    return sub_listas

# Llamada a la función y almacenamiento del resultado
sub_listas = crear_sub_listas(lista)

# Imprimir las sub-listas para verificar el resultado
# Para ver las sub listas en consola
""" for sub_lista in sub_listas: 
    print(sub_lista) """
                
                
