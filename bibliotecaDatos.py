from os import system
from datos import lista
import json
        
                
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

# Función para leer puntajes y mostrar los tres primeros en orden descendente
def obtener_top_puntajes(criterio: str= "DESC"):
    try:
        with open('D:\Desktop\Curso_de_ingreso_PYTHON\proramacion_1\preparacion\juego_2\puntajes.json', 'r') as archivo:
            puntajes = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    # Ordenamiento por burbuja
    for i in range(len(puntajes) - 1):
        for j in range(i + 1, len(puntajes)):
            if criterio == "DESC":
                if puntajes[i]["puntaje"] < puntajes[j]["puntaje"]:
                    # Intercambiar
                    puntajes[i], puntajes[j] = puntajes[j], puntajes[i]

    # Retornar los tres primeros puntajes
    return puntajes[:3]

# Función para guardar puntaje en archivo JSON
def agregar_puntaje(nombre, puntaje):
    datos = {'nombre': nombre, 'puntaje': puntaje}
    
    # Leer el contenido existente del archivo
    #Si el archivo no existe (FileNotFoundError) o si hay un error en la decodificación JSON (json.JSONDecodeError), inicializar puntajes como una lista vacía:
    try:
        with open('D:\Desktop\Curso_de_ingreso_PYTHON\proramacion_1\preparacion\juego_2\puntajes.json', 'r') as archivo:
            puntajes = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        puntajes = []

    # Agregar el nuevo puntaje a la lista
    puntajes.append(datos)

    # Escribir la lista actualizada de puntajes en el archivo
    with open('D:\Desktop\Curso_de_ingreso_PYTHON\proramacion_1\preparacion\juego_2\puntajes.json', 'w') as archivo:
        json.dump(puntajes, archivo, indent=4)
        

