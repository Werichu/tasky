from alta import darAlta
from actualizar import actualizarTarea
from mostrarTodo import mostrarTodo
from tareasHechas import tareasHechas
from tareasPendientes import tareasPendientes
from baja import darBaja
from guardarJson import guardarArchivo, cargarArchivo

def main(): 
    #variable que controla el menu de opciones
    opcion = 1

    #carga los datos del archivo json
    tareas_cargadas = cargarArchivo()  # esta variable carga diccionarios
    
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
        print('===== Tasky =====')
        print('[1.] Registrar tarea\n[2.] modificar estado de la tarea\n[3.] Mostrar todo\n[4.] Mostrar tareas hechas')
        print('[5.] Mostrar tareas pendientes\n[6.] borrar tareas\n[7.] Guardar tareas')
        print('[0.] Salir')
        opcion = int(input('>>>>> opcion: '))

        if opcion == 1:
            #todas las tareas que registre el usuario  y retorne la funcion se van a guardar en esta variable
            tareasNuevas = darAlta()
            #cuando el usuario vuelva a llamar la funcion "darAlta" los nuevos registros se guardan en una lista global
            todas_las_tareas.extend(tareasNuevas)

        elif opcion == 2:
            actualizarTarea(todas_las_tareas)
        elif opcion == 3:
            mostrarTodo(todas_las_tareas)
        elif opcion == 4:
            tareasHechas(todas_las_tareas)
        elif opcion == 5:
            tareasPendientes(todas_las_tareas)
        elif opcion == 6:
            #la lista: "todas_las_tareas" guarda la nueva lista de tareas generada al borrar un elemento de la lista
            todas_las_tareas = darBaja(todas_las_tareas)
        elif opcion == 7:
            guardarArchivo(todas_las_tareas)
        elif opcion == 0:
            guardarArchivo(todas_las_tareas)
            print('Byteees!!!!')
        else: 
            print('Error, opcion no valida.....')

if __name__ == "__main__":
    main()