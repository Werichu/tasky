from .tarea import Tarea
from .misc import limpiarPantalla, getchr #archivo que guarda funciones auxiliares
'''
Esta funcion elimina una tarea por ID
Funcionamiento:

1. se recibe la lista de objetos registrada por el usuario
2. se valida si hay tareas registradas 
3. si hay tareas registradas se le pregunta al usuario la ID de la tarea a eliminar
4. mediante un ciclo for enumeramos la lista de objetos con una variable auxiliar "i" y la funcion "enumerate"
dandonos esta simbologia

    ID(i)      tarea
    1          .....
    2          .....

5. Cuando la tarea es encontrada usamos el metodo "pop" con el indice de la lista para eliminar un objeto registrado
dentro de la lista, devolviendo la funcion, la lista de objetos modificada 

'''

def darBaja(todas_las_tareas):
    #si la lista esta vacia, mostrara este mensaje
    if not todas_las_tareas: 
        print("\nNo hay tareas registradas....")
    else:
        idBuscar = int(input("Digite la id de la tarea a eliminar: "))
        for i, tarea in  enumerate(todas_las_tareas):
            if idBuscar == tarea.id:
                todas_las_tareas.pop(i)
                
                print(f"se elimino la tarea con el id: {idBuscar}")
                print(getchr("Presione cualquier tecla para continuar....."))
                return todas_las_tareas
            
        else: print(f"\n>>>>>> Error, no existe una id con el numero: {idBuscar}")
        print(getchr("Presione cualquier tecla para continuar....."))
        
        return todas_las_tareas