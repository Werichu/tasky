from tarea import Tarea

def tareasHechas(todas_las_tareas):
    
    #si la lista esta vacia mostrara este mensaje:
    if not todas_las_tareas:
        print("\nNo hay tareas registradas....")
        
    else:
        for tarea in todas_las_tareas:
            if tarea.status == "Hecho":
                print(f'\nId: {tarea.id}')
                print(f'Descripcion: {tarea.description}')
                print(f'Estado: {tarea.status}')
                print(f'Fecha de creacion: {tarea.createdAt}')
                print(f'Fecha de actualizacion: {tarea.updatedAt}\n')
            else: print("Error, no hay tareas registreadas con el estado 'Hecho'\n")