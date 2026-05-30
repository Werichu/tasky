from alta import darAlta
from actualizar import actualizarTarea
from mostrarTodo import mostrarTodo
from tareasHechas import tareasHechas
from tareasPendientes import tareasPendientes
from baja import darBaja
def main(): 
    opcion = 1

    #lista global que acumula todas las tareas registradas por el usuario
    todas_las_tareas = []

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
            print("proximamente.......")
        elif opcion == 0:
            print('Byteees!!!!')
        else: 
            print('Error, opcion no valida.....')

if __name__ == "__main__":
    main()