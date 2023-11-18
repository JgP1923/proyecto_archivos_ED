import os
from EstructuraAdmisnistrador import Nodo

#Imprimir el arbol como si fueran los directorios de un sistema operativo

def imprimir_arbol(nodo, nivel=0):
        prefijo = "|   " * nivel + "|-- " if nivel > 0 else ""
        tipo = " [Directorio]" if nodo.es_directorio else ""
        print(prefijo + nodo.nombre + tipo)

        for hijo in nodo.hijos:
            imprimir_arbol(hijo, nivel + 1)
            
#Identifica si la ruta es un archivo o un directorio y los agrega al arbol de directorios
           
def construir_arbol_directorio(ruta_directorio):
    nodo_directorio = Nodo(ruta_directorio, es_directorio=True)

    # Obtener la lista de archivos y carpetas en el directorio
    lista_contenido = os.listdir(ruta_directorio)

    for item_nombre in lista_contenido:
        item_ruta = os.path.join(ruta_directorio, item_nombre)

        if os.path.isdir(item_ruta):
            # Si es un directorio, construir recursivamente su subárbol
            hijo_directorio = construir_arbol_directorio(item_ruta)
            nodo_directorio.agregar_hijo(hijo_directorio)
        else:
            # Si es un archivo, agregarlo como hijo
            hijo_archivo = Nodo(item_nombre)
            nodo_directorio.agregar_hijo(hijo_archivo)

    return nodo_directorio

#Funciones del administrador de archivos

#Funcion para eliminar un archivo de una ruta especifica
def eliminar_archivo(ruta_archivo):
    if os.path.isfile(ruta_archivo):
        os.remove(ruta_archivo)
        print(f"El archivo de la ruta {ruta_archivo} se ha eliminado correctamente")
    else:
        print("No se puede eliminar el archivo porque no existe")
        
#Funcion para eliminar un directorio de una ruta especifica        
def eliminar_directorio(ruta_directorio):
    if os.path.isdir(ruta_directorio):
        os.rmdir(ruta_directorio)
        print(f"El directorio de la ruta {ruta_directorio} se ha eliminado correctamente")
    else:
        print("No se puede eliminar el directorio porque no existe")        

#Funcion para renombrar un archivo de una ruta especifica
def renombrar_archivo(ruta_archivo, nuevo_nombre):
    if os.path.isfile(ruta_archivo):
        directorio_original = os.path.dirname(ruta_archivo)
        nueva_ruta = os.path.join(directorio_original, nuevo_nombre)

        os.rename(ruta_archivo, nueva_ruta)
        print(f"El archivo se ha renombrado correctamente a {nuevo_nombre}")
    else:
        print("No se puede renombrar el archivo porque no existe")

#Funcion para renombrar un directorio de una ruta especifica
def renombrar_directorio(ruta_directorio, nuevo_nombre):
    if os.path.isdir(ruta_directorio):
        directorio_padre = os.path.dirname(ruta_directorio)
        nueva_ruta = os.path.join(directorio_padre, nuevo_nombre)

        os.rename(ruta_directorio, nueva_ruta)
        print(f"El directorio se ha renombrado correctamente a {nuevo_nombre}")
    else:
        print("No se puede renombrar el directorio porque no existe")
        
#Funcion para crear un directorio en una ruta especifica
def crear_archivo(ruta_archivo):
    if os.path.isfile(ruta_archivo):
        print("El archivo ya existe")
    else:
        archivo = open(ruta_archivo, "w")
        archivo.close()
        print(f"El archivo en la ruta {ruta_archivo} se ha creado correctamente")
        
#Funcion para crear un directorio en una ruta especifica        
def crear_directorio(ruta_directorio):
    if os.path.isdir(ruta_directorio):
        print("El directorio ya existe")
    else:
        os.mkdir(ruta_directorio)
        print(f"El directorio en la ruta {ruta_directorio} se ha creado correctamente")
        
        