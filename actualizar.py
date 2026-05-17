from datetime import date
from datetime import datetime
from tarea import Tarea
'''
Esta funcion se encarga de actualizar el estado de las tareas que el usuario haya registrado.

Funcionamiento: 

1. La funcion recibe como parametro una lista de objetos de 'todas las tareas' que el usuario a registrado
2. Se pregunta el id de una tarea a modificar
3. Mediante un for y con una variable auxiliar iteramos dentro de la lista, y si encuentra una tarea con la misma id
se cumplira el condicional y podremos acceder tanto a la descripcion de la tarea como a la modificacion del estado y fecha (actualizada automaticamente por el sistema)

'''

def actualizarTarea(todas_las_tareas):
    
    idBuscar = int(input('Digite una id para modificar el estado de la tarea: '))
# tarea es una variable auxiliar que nos permite modificar los atributos directamente mediante los setters y getters
    for tarea in todas_las_tareas:
        if idBuscar == tarea.id:
            print(f"Descripcion: {tarea.description}")

            estado = input('digite un nuevo estado de la tarea(Pendiente / En proceso / Hecho): ')
            print('\n>>>>>> tarea modificada......')
            tarea.status = estado
            tarea.updatedAt = datetime.today()
    else:
        print(f"\n>>>>>> Error, no existe una id con el numero: {idBuscar}")
