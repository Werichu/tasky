from tarea import Tarea
from misc import limpiarPantalla, getchr #archivo que guarda funciones auxiliares
'''
Esta funcion se encarga de mostrar todas las tareas registradas por el usuario, independientemente 
si estan hechas o no

Funcionamiento:

1. La funcion recibe como parametro la lista de objetos de todas las tareas digitadas por el usuario
2. mediante un ciclo for usamos la variable tareas como acceso a todos los atributos de la clase "Tarea"
pudiendo mostrar mediante los getters todos los atributos de la clase
'''

def mostrarTodo(todas_las_tareas):
    #si no hay tareas registradas se mostrara este mensaje
    if not todas_las_tareas:
        print("\nNo hay tareas registradas...")
        print(getchr("Presione cualquier tecla para continuar....."))
        return
    
    print("▁"*90)
    print(f"{'ID':<5} | {'Estado':<12} | {'Fecha de creacion':<20} | {'Fecha actualiz.':<20} | {'Descripcion'}")
    print("▁"*90)
    
    for tarea in todas_las_tareas:
        print(f"{tarea.id:<5} | {tarea.status:<12} | {str(tarea.createdAt)[:19]:<20} | {str(tarea.updatedAt)[:19]:<20} | {tarea.description}")
        print("▁"*90)
    print(getchr("Presione cualquier tecla para continuar....."))
    