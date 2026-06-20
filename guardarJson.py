from tarea import Tarea
from datetime import datetime
import json
"""
Esta funcion se encarga de guardar las tareas digitadas por el usuario

NOTA: LA funcion lo guarda ningun objeto generado por el programa, solo transforma los datos de cada objeto
a un diccionario.
"""
def guardarArchivo(todas_las_tareas):

    if not todas_las_tareas:
        print("\nNo hay tareas registradas...")
    else: 
        nombre_archivo = "mis_tareas.json"
        #esta lista va a guardar los datos json de cada tarea registrada
        tareas_para_guardar = []
        for tarea in todas_las_tareas:
            #se crea un diccionario simple con los datos de cada tarea
            datos_tarea = {
                "id": tarea.id,
                "descripcion": tarea.description,
                "estado": tarea.status,
                "fecha_creacion": str(tarea.createdAt),
                "fecha_actualizacion": str(tarea.updatedAt)
            }
            #se agrega a la nueva lista los datos de diccionario de los objetos
            tareas_para_guardar.append(datos_tarea)
        
        #guardando en archivo
        with open(nombre_archivo,"w",encoding="utf-8") as archivo:
            json.dump(tareas_para_guardar,archivo,indent=4,ensure_ascii=False)
            
        print(f"Tareas guardadas...... se guardaron {len(todas_las_tareas)} tareas.")


"""
Esta funcion se carga los datos guardados en archivos JSON
"""
def cargarArchivo():
    nombre_archivo = "mis_tareas.json"

    try:
        with open (nombre_archivo,"r",encoding="utf-8") as archivo:
            tareas_guardadas = json.load(archivo)

        print(f"\n Se cargaron {len(tareas_guardadas)} tareas registradas\n\n")
        return tareas_guardadas
    except FileNotFoundError:
        print("\n No hay tareas registradas aun.......")
        return []