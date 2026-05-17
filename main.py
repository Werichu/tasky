from alta import darAlta
from actualizar import actualizarTarea
def main(): 
    opcion = 1

    #lista global que acumula todas las tareas registradas por el usuario
    todas_las_tareas = []

    while opcion != 0:
        print('===== Tasky =====')
        print('[1.] Registrar tarea\n[2.] modificar estado de la tarea\n[3.] Borrar tarea\n[4.] Guardar')
        print('[5.] Mostrar todo\n[6.] Mostrar no relizadas\n[7.] Mostrar tareas pendientes')
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
            print("proximamente..........")
        elif opcion == 4:
            print("proximamente..........")
        elif opcion == 5:
            print("proximamente..........")
        elif opcion == 6:
            print("proximamente..........")
        elif opcion == 0:
            print('Byteees!!!!')
        else: 
            print('Error, opcion no valida.....')

if __name__ == "__main__":
    main()