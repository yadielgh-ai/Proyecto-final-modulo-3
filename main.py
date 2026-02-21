'''
Proyecto de Gestión de mantenimiento. 
Gestión de máquinas y técnicos: este proyecto permite realizar registro y consultar los técnicos y máquinas de una empresa
En esta primera versión solo se trabajará con las máquimas o equipos
Esta versión permite:
- consultar la existencia de un equipo por código o por nombre.
- agregar un nuevo equipo
- eliminar un equipo solo con la introducción del código del equipo.
- ver el listado completo de los equipos existentes.
- Importante resaltar que más de un equipo puede tener el mismo nombre, pero solo un código, es decir, los nombres se pueden repetir, los códigos no.


Autor: Yadiel González
'''
from mantenimiento.menu import *    # importando menu para ejecutarlo desde main.

def main():
    mostrar_menu()




if __name__ == "__main__":
    main()