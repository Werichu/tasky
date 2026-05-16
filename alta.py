from tarea import Tarea
'''
Esta funcion se encarga de dar de alta las tareas registradas por el usuario
creandoce un nuevo objeto en el proceso y guardandose dentro de una lista, cuando el usuario deja de registrar
tareas, la funcion retorna la lista de todos los registros para ser trabajados en otras funciones
'''
def darAlta():   
    ListaTareas=[]
    id=1
    
    while True:
        
        descripcion=input("Digite una descripcion: ")
        estatus=input("Digite el estado de la tarea: ")
        fechaCreacion = '---'
        fechaActualizacion='---'
        
        nuevaTarea=Tarea(id,descripcion,estatus,fechaCreacion,fechaActualizacion)
        ListaTareas.append(nuevaTarea)
        id+=1
        
        continuar = input("Quieres agregar una nueva tarea? (S/n): ")
        if continuar.lower() != 's':
            break
        
    return ListaTareas

