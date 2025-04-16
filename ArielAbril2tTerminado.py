
def Mcmenu():

    print("\nGestión de tareas pendientes")
    print("1: Añadir una tarea")
    print("2: Ver todas las tareas")
    print("3: Marcar una tarea como completada")
    print("4: Salir")

def cipote_funcion():
    tareas = []

    while True:
        
        Mcmenu()
        opcion = input("Selecciona una opción: ")

        
        
        
        if opcion == "1":
            nueva_tarea = input("Escribe la descripción de la tarea: ")
            tareas.append(nueva_tarea)
            print("¡Tarea añadida exitosamente!")
        
        
        
        
        elif opcion == "2":
            print("\nLista de tareas pendientes:")
            if len(tareas) == 0:
                print("No hay tareas pendientes.")
            else:
                for idx, tarea in enumerate(tareas, start=1):
                    print(f"{idx}. {tarea}")
        
        
        
        
        ######################el comando "\n" salta el dialogo y lo divide en 2 partes
        elif opcion == "3":
            print("\nLista de pendientes:")
            if len(tareas) == 0:
                print("No hay tareas que marcar como completadas.")
            else:
                for idx, tarea in enumerate(tareas, start=1):
                    print(f"{idx}. {tarea}")
                num_tarea = input("Escribe el número de la tarea completada: ")
                if num_tarea.isdigit():
                    num_tarea = int(num_tarea)
                    if 1 <= num_tarea <= len(tareas):
                        tareas.pop(num_tarea - 1)
                        print("Tarea completada y eliminada exitosamente")
                    else:
                        print("EROR 505 -/COMANDO/ inválido. (mete un numero decente please)")
                else:
                    print("Mete un numero decente please")
        
        
        
        
        elif opcion == "4":
            print("Gracias por usar el Cipoteprograma!")
            break
#################Rompe el bucle de la cipotefuncion
        else:
            print("elija un numero decente please")
################Llama a la cipotefuncion
cipote_funcion()

