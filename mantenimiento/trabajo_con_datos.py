# Nota: Puedo mejorar el código añadiendo una funcion que me devuelva la posición que ocupa un diccionario en la lista.
# EL CODIGO DE ESTE ARCHIVO ESTÁ PENSADO PARA SER REUTILZADO EN LO QUE SERÍA UN MÓDULO DE TECNICOS.

#Función para comprobar que el código del equipo o del técnico  no se repite.


def comprobar_codigo(nombre_lista, numero_codigo):    # recibe como argumento la lista de diccionario que se quiere comprobar, y el código que se quiere verificar existencia.
    
    for c_odigo in nombre_lista:
        if c_odigo["codigo"]==numero_codigo:
            
            return 1                                   # retorna valor 1 si el código está en la lista.
        else:
            continue



# FUNCION para buscar equipo o técnico por nombre


def buscar_por_nombre(nombre_lista, nombre):     #recibe como argumento una lista de diccionarios y el nombre a buscar en la lista
    i=0
    dato_equipo= []
    for b_nombre in nombre_lista:
        if b_nombre["nombre"]== nombre:
            i+=1
            dato_equipo.append(b_nombre["codigo"])
    if i>0:
        print(f"exiten {i} códigos asiciados a {nombre}")
        for c_codigo in dato_equipo:
            print(c_codigo)
    else:
        print("No existe el nombre solicitado")
    

# Función que busca un nombre por código en una lista de diccionarios

def buscar_por_codigo(nombre_lista, a_codigo):                    #Recibe como argumento una lista de diccionarios y el código a buscar en la lista
    for c_odigo in nombre_lista:
        if c_odigo["codigo"]==a_codigo:
            print(f"El nombre asociado al {a_codigo} es:  {c_odigo["nombre"]}")
        else:
            print(f"No existe ningún nombre asociado al código {a_codigo}")


# Función para eliminar un diccionario de una lista por código

def eliminar_por_codigo(nombre_lista, e_codico):
    eliminado= "False"
    for c_codigo in nombre_lista:
        if c_codigo["codigo"]== e_codico:
            nombre_lista.remove(c_codigo)
            eliminado="True"
            print(f"{e_codico} fue eliminado")
            break
    if eliminado== "False":
        print("cpodigo no encontrado")





# Función para imprimir una lista de diccionarios
def  imprimir_lista_diccionarios(listado):
    print("Nombre:        Código:")
    for diccionario in listado:
        print(f"{diccionario["nombre"]}:  {diccionario["codigo"]} ")
