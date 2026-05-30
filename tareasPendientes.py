from tarea import Tarea
#la funcion recibe como argunento todas las tareas digitadas por el usuario
def tareasPendientes(todas_las_tareas):
    
    #si la lista esta vacia mostrara este mensaje:
    if not todas_las_tareas:
        print("\nNo hay tareas registradas....")
        
    else:
        #se crea el objeto tarea y se itera dentro de la lista de objetos
        for tarea in todas_las_tareas:
            if tarea.status == "Pendiente":
                print(f'\nId: {tarea.id}')
                print(f'Descripcion: {tarea.description}')
                print(f'Estado: {tarea.status}')
                print(f'Fecha de creacion: {tarea.createdAt}')
                print(f'Fecha de actualizacion: {tarea.updatedAt}\n')
            else: print("Error, no hay tareas registreadas con el estado 'Pendiente'\n")