from alta import darAlta
from actualizar import actualizarTarea
from mostrarTodo import mostrarTodo
from tareasHechas import tareasHechas
from tareasNorealizadas import tareasNorealizadas
from tareasPendientes import tareasPendientes
from baja import darBaja
from guardarJson import guardarArchivo,cargarArchivo

def main(): 
    opcion = 1
    #carga los datos del archivo json
    tareas_cargadas = cargarArchivo()  # esta variable carga el archivo de diccionarios
    
    #conversion de los diccionarios a objetos Tarea
    todas_las_tareas = []
    for tarea_dict in tareas_cargadas:
        from tarea import Tarea
        from datetime import datetime
        
        #estas variables convienrten las fechas de string a datetime
        fecha_creacion = datetime.strptime(tarea_dict["fecha_creacion"], "%Y-%m-%d %H:%M:%S.%f")
        fecha_actualizado = datetime.strptime(tarea_dict["fecha_actualizacion"], "%Y-%m-%d %H:%M:%S.%f")
        
        #crear objeto Tarea
        tarea = Tarea(
            tarea_dict["id"],
            tarea_dict["descripcion"],
            tarea_dict["estado"],
            fecha_creacion,
            fecha_actualizado
        )
        #se aniaden a la lista 
        todas_las_tareas.append(tarea)

    while opcion != 0:
        print("""\
               ░██████████                      ░██                  
                   ░██                          ░██                  
                   ░██     ░██████    ░███████  ░██    ░██░██    ░██ 
                   ░██          ░██  ░██        ░██   ░██ ░██    ░██ 
                   ░██     ░███████   ░███████  ░███████  ░██    ░██ 
                   ░██    ░██   ░██         ░██ ░██   ░██ ░██   ░███ 
                   ░██     ░█████░██  ░███████  ░██    ░██ ░█████░██ 
                                                                 ░██ 
                                                            ░███████
        """)  
        print('[1.] Registrar tarea\n[2.] modificar estado de la tarea\n[3.] Mostrar todo\n[4.] Mostrar tareas realizadas')
        print('[5.] Mostrar tareas no realizadas\n[6.] Mostrar tareas en progreso\n[7.] borrar tareas')
        print('[0.] Salir')
        entrada = input('>>> opcion: ')
        
        if entrada.isdigit():
            opcion = int(entrada)

            if opcion == 1:
                #calculacion del siguiente id
                siguiente_id = obtener_sig_id(todas_las_tareas)

                tareasNuevas= darAlta(siguiente_id) #pasa al ultimo id si hay alguna tarea disponible
                todas_las_tareas.extend(tareasNuevas)

            elif opcion == 2:
                actualizarTarea(todas_las_tareas)
            elif opcion == 3:
                mostrarTodo(todas_las_tareas)
            elif opcion == 4:
                tareasHechas(todas_las_tareas)
            elif opcion == 5:
                tareasNorealizadas(todas_las_tareas)
            elif opcion == 6:
                tareasPendientes(todas_las_tareas)
            elif opcion == 7:
                #la lista: "todas_las_tareas" guarda la nueva lista de tareas generada al borrar un elemento de la lista
                todas_las_tareas = darBaja(todas_las_tareas)
            elif opcion == 0:
                guardarArchivo(todas_las_tareas)
                print('Byteees!!!!')
            else: print('Error, opcion no valida.....')
        else: print('Error, digite solo numeros.......')

#Funcion miscelanea para calcular id

def obtener_sig_id(tareas):
#calcular el siguiente id disponible
    if not tareas:
        return 1
    #si ya hay una tarea ocupando el id, devolvera el siguiente espacio
    return max(tarea.id for tarea in tareas) + 1

if __name__ == "__main__":
    main()