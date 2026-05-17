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
    
    for tareas in todas_las_tareas:
        print(f'\nId: {tareas.id}')
        print(f'Descripcion: {tareas.description}')
        print(f'Estado: {tareas.status}')
        print(f'Fecha de creacion: {tareas.createdAt}')
        print(f'Fecha de actualizacion: {tareas.updatedAt}\n')
    