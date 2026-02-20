'''

registrar equipo (nombre y código)
consultar equipo (por nombre o por código, el nombre se puede repetir, el código no)
eliminar equipo

LO MISMO PARA LOS TECNICOS.
'''
from equipos import *


print("\n BIEMVENIDO AL SOFTWARE DE GESTION DE MANTENIMINETO \n")

while True:

    #   AGREGAR MODULO TIME PARA DARLE UNOS SEGUNDOS ANTES DE QUE SE MUESTREN LAS OPCIONES

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


    opcion= int (input())

    if opcion ==1:
        consultar_equipo()

    elif opcion==2:
        agregar_equipo()

    elif opcion==3:
        eliminar_equipo()  
    
    elif opcion==4:
        mostrar_equipos() 
    
    elif opcion==5:
        print ("esta función está en desarrollo...")
    
    elif opcion==6:
        print ("esta función está en desarrollo...")
    
    elif opcion==7:
        print ("esta función está en desarrollo...")
    
    elif opcion==8:
        break
    else:
        print("el valor agregado no es válido")  
    
