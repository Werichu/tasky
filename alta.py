from datetime import date
from datetime import datetime
from tarea import Tarea

'''
En esta funcion damos de alta las tareas registradas por el usuario, mediante un listado de objetos
'''
def darAlta():
    #variables de la lista y la id de la tarea
    listadoTareas=[]
    id=1;

    while True:
        descripcion = input("\nDigite su descripcion: ")
        estado = input("Digite el estado de la tarea (No realizado / En progreso / Realizado): ")
        fechaCreacion = datetime.today()
        fechaActualizacion = datetime.today()
        print(f'\n >>>>>> tarea registrada con el id: {id}')
        
        #se crea un nuevo objeto tarea con los parametros del usuario y esta se aniade a la lista
        nuevaTarea = Tarea(id,descripcion,estado,fechaCreacion,fechaActualizacion)
        listadoTareas.append(nuevaTarea)
        id+=1

        #siempre preguntamos si desea continuar registrando tareas
        continuar = input("Desea agregar otra tarea? (S/n): ")
        if continuar.lower() != 's':
            break
    #al final la funcion retorna todas las tareas que el usuario agrego
    return listadoTareas 