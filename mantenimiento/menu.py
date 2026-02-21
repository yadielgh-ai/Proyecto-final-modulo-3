

#   *** En esta instacia se muestra el menú tanto para equipos como para técnicos. En esta versión se concidera suficiente como ejercicio
#       del módulo, la lo referente a los equipos, por lo que lo referente a los técnicos se realizará mientras avance el curso  


import time
from .equipos import *


def mostrar_menu():
    print("\n BIEMVENIDO AL SOFTWARE DE GESTION DE MANTENIMINETO \n")

    while True:
        

        time.sleep(2) # Da dos segundos antes de cargar las opciones nuevamente para identificar bien la respuesta o resultado anterior
        

        print("""        
            Escoja una de las siguientes opciones:
            1: Consultar equipo 
            2: Registrar equipo 
            3: Eliminar equipo
            4: Ver listado de equipos  
            5: Consultar técnico
            6: Agregar técnico
            7: Eliminar técnico 
            8: Salir 

        """)


        opcion= input()

        if opcion =="1":
            consultar_equipo()

        elif opcion=="2":
            agregar_equipo()

        elif opcion=="3":
            eliminar_equipo()  
        
        elif opcion=="4":
            mostrar_equipos() 
        
        elif opcion=="5":
            print ("esta función está en desarrollo...")   # estas tres opciones se seguirán implementando a medida que avance el curso.
        
        elif opcion=="6":
            print ("esta función está en desarrollo...")
        
        elif opcion=="7":
            print ("esta función está en desarrollo...")
        
        elif opcion=="8":
            break
        else:
            print("El valor agregado no es válido")  
        