from tarea import Tarea
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
    else: 
        for tarea in todas_las_tareas:
            print(f'\nId: {tarea.id}')
            print(f'Descripcion: {tarea.description}')
            print(f'Estado: {tarea.status}')
            print(f'Fecha de creacion: {tarea.createdAt}')
            print(f'Fecha de actualizacion: {tarea.updatedAt}\n')
    