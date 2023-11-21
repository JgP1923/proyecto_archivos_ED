from FuncionesAdministrador import *
from InterfazAdministrador import *

#Pruebas

#Mostrar la ruta del directorio de prueba
directorio_actual = os.getcwd()
nombre_carpeta = "Prueba_Proyecto"
ruta_carpeta_deseada = os.path.join(directorio_actual, nombre_carpeta)

#crear archivo
nombre_archivo = "hola2.txt"
prueba_crear_archivo = os.path.join(ruta_carpeta_deseada, nombre_archivo)

#eliminar archivo
prueba_eliminar_archivo =  os.path.join(ruta_carpeta_deseada, nombre_archivo)

#crear directorio
nombre_directorio = "3"
prueba_crear_directorio =  os.path.join(ruta_carpeta_deseada, nombre_directorio)

#eliminar directorio
prueba_eliminar_directorio = os.path.join(ruta_carpeta_deseada, nombre_directorio)

#renombrar archivo
nombre_renombrar_archivo = "hola3.txt"
nuevo_nombre_archivo = "hola4.txt"
prueba_renombrar_archivo = os.path.join(ruta_carpeta_deseada, nombre_renombrar_archivo)

#renombrar directorio
nombre_renombrar_directorio = "3"
nombre_nuevo_directorio = "4"
prueba_renombrar_directorio = os.path.join(ruta_carpeta_deseada, nombre_renombrar_directorio)



#Menu del administrador de archivos Para pruebas, debe hacerse estas funciones desde La interfaz grafica

def menu():
    while True:
        print("Bienvenido al administrador de archivos")
        print("1. Crear Archivo")
        print("2. Crear directorio")
        print("3. Eliminar archivo")
        print("4. Eliminar directorio")
        print("5. Renombrar archivo")
        print("6. Renombrar directorio")
        print("7. Mostrar el arbol de directorios")
        print("8. Abrir administrador de archivos graficamente") 
        print("9. Salir")

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            crear_archivo(prueba_crear_archivo)
            print("\n")
            pass
        elif opcion == 2:
            crear_directorio(prueba_crear_directorio)
            print("\n")
            pass
        elif opcion == 3:
            eliminar_archivo(prueba_eliminar_archivo)
            print("\n")
            pass
        elif opcion == 4:
            eliminar_directorio(prueba_eliminar_directorio)
            print("\n")
            pass
        elif opcion == 5:
            renombrar_archivo(prueba_renombrar_archivo, nuevo_nombre_archivo)
            print("\n")
            pass
        elif opcion == 6:
            renombrar_directorio(prueba_renombrar_directorio, nombre_nuevo_directorio)
            print("\n")
            pass
        elif opcion == 7:
            imprimir_arbol(construir_arbol_directorio(ruta_carpeta_deseada))
            pass
        elif opcion == 8:
            interfaz()
            break
        elif opcion == 9:
            print("Hasta pronto")
            break
        else:
            print("Opcion invalida")

# Ejecución del menú
menu()

