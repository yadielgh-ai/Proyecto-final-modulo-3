'''
Trabajo con el quipamiento
'''

from trabajo_con_datos import *

lista_equipos= []


# función para agregar un equipo a la lista de equipos, será agregado solo nombre y código
def agregar_equipo():
    nombre = input("introduzca el nombre del equipo:  ")
    while True:                                            #lazo para comprobar que no se repita el código.
        codigo = input("introduzca el código del equipo:  ")  #el código del equipo puede ser alfanumérico
        if comprobar_codigo(lista_equipos, codigo)==1:      #llamada a la función para verificar presencia de código
            print(f"El código {codigo} ya se encuentra asignado")
            opcion = int(input(" Digite 1 para intentarlo de nuevo, digite otro valor para cancelar"))
            if opcion== 1:
                continue
            else:
                return 0
        else:
            equipo= {
                "nombre": nombre,
                "codigo": codigo
            }

            lista_equipos.append(equipo)
            print(f"El equipo {nombre} con código {codigo} se ha agregado correctamente ")
            return 1

# funcion para consultar un equipo específico, permite buscar por código o por nombre.
def consultar_equipo():
    print(""" 
        Marque la opción deseada:
        1: Buscar por nombre
        2: Buscar por código
        3: Cancelar
    """)

    opcion= int(input())
    if opcion==1:
        nombre_equipo= input("Introduzca el nombre del equipo:  ")
        buscar_por_nombre(lista_equipos, nombre_equipo)
    if opcion==2:
        codigo_equipo= input("Introduzca el código del equipo:  ")
        buscar_por_codigo(lista_equipos, codigo_equipo)


def eliminar_equipo():
    print(" Solo se pueden eliminar equipos por el código ")
    delete_codigo= input("introduzca el código del equipo a eliminar:  ")
    eliminar_por_codigo(lista_equipos, delete_codigo)


# Función para mostrar todos los equipos disponibles
def mostrar_equipos (): 
    if lista_equipos:
        print("Los disponibles son los siguientes:  ")
        imprimir_lista_diccionarios(lista_equipos)             # Llamada a función para imprimir listas
    else:
        print("No existen equipos para mostrar")


    # Lazo para revizar que el código del equipo no se repita
    # implementar una función a parte que revise en la lista con diccionarios que el código no se repite, la podré utilizar para 
    # equipos y técnicos. Pasarle como argumentos el código y el nombre de la lista. 
    # me parece que se puede hacer una función para insertar un diccionario en una lista, como argumentos el diccionario y el nombre (duda con esta funcion)
    # poner esas funciones en otro archivo que se llame trabajo con datos o algo así.
