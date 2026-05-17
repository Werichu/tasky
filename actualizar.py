from datetime import date
from datetime import datetime
from tarea import Tarea

def actualizarTarea(todas_las_tareas):
    
    idBuscar = int(input('Digite una id para modificar el estado de la tarea: '))

    for tarea in todas_las_tareas:
        if idBuscar == tarea.id:
            print(f"{tarea.description}")

            estado = input('digite un nuevo estado de la tarea(Pendiente / En proceso / Hecha): ')
            tarea.status = estado
            tarea.updatedAt = datetime.today()
            break
        else:
            print(f"Error, no existe una id con el numero: {idBuscar}")
