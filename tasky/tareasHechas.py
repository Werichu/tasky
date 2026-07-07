from tarea import Tarea
from misc import limpiarPantalla, getchr #archivo que guarda funciones auxiliares

def tareasHechas(todas_las_tareas):

    #creamos una lista que guarde las tareas con el estado "realizado"
    tareas_realizadas = [tareas for tareas in todas_las_tareas if tareas.status == "Realizado"]

    #si no hay ninguna tarea registrada
    if not todas_las_tareas:
        print("\nNo hay tareas registradas....")
        print(getchr("Presione cualquier tecla para continuar....."))
        return
    #si no hay ninguna tarea con el estado "Realizado"
    if not tareas_realizadas:
        print("Error, no hay tareas registreadas con el estado 'Realizado'\n")
        print(getchr("Presione cualquier tecla para continuar....."))
        return
        
    print("▁"*90)
    print(f"{'ID':<5} | {'Estado':<12} | {'Fecha de creacion':<20} | {'Fecha actualiz.':<20} | {'Descripcion'}")
    print("▁"*90)

    #el objeto tarea itera en la variable "tareas_realizadas" mostrando las tareas que contengan ese estado
    for tarea in tareas_realizadas:
        print(f"{tarea.id:<5} | {tarea.status:<12} | {str(tarea.createdAt)[:19]:<20} | {str(tarea.updatedAt)[:19]:<20} | {tarea.description}")
        print("▁"*90)
    print(getchr("Presione cualquier tecla para continuar....."))