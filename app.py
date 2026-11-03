print("==============================")
print(" ===== GESTOR DE TAREAS =====")
print("==============================")

selecion = 0
tareas = []

while selecion != 5:
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        print()
        selecion =  int(input("Seleccione una opcion: "))
        print()

        if selecion == 1:   
            if not tareas:
                print("No existen tareas actualmente.")
                print()
            else:
                print("Tareas actuales:")
                for numero, tarea in enumerate(tareas, start=1):
                    if tarea["completada"]:
                        print(f"{numero}. {tarea['descripcion']} [Completada]")
                    else:
                        print(f"{numero}. {tarea['descripcion']} [Pendiente]")
                        print()

        elif selecion == 2:
            descripcion = input("Escriba la nueva tarea: ")

            tarea = {
                "descripcion": descripcion,
                "completada": False
            }

            
            tareas.append(tarea)
            print("Tarea agregada correctamente!!!")
            print()


        elif selecion == 3:
            if not tareas:
                print("No existen tareas para completar.")
                print()
            else:
                print("Seleccione la tarea que quiere completar:")

                for numero, tarea in enumerate(tareas, start=1):
                    print(f"{numero}. {tarea['descripcion']}")
                
                completar_tarea = int(input("Selecione el numero de la tarea a completar:"))
                print()
                if completar_tarea < 1 or completar_tarea > len(tareas):
                    print("El numero de tarea ingresado no es valido.")
                    print()
                else:
                    indice = completar_tarea - 1
                    tareas[indice]["completada"] = True
                    print("¡Tarea completada correctamente!")
                    print()


        elif selecion == 4:
            if not tareas:
                print("No existen tareas para eliminar.")
                print()
            else:                
                print("Selecione que tarea quiere eliminar:")
                print()
                for numero, tarea in enumerate(tareas, start=1):
                    if tarea["completada"]:
                        print(f"{numero}. {tarea['descripcion']} [Completada]")
                    else:
                        print(f"{numero}. {tarea['descripcion']} [Pendiente]")           
                print()

                eliminar_tarea = int(input("Sellecione el numero de la tarea que desea eliminar:"))

                if eliminar_tarea < 1 or eliminar_tarea > len(tareas):
                    print("El numero de tarea ingresado no es valido.")
                    print()
                else:
                    indice = eliminar_tarea - 1
                    tareas.pop(indice)
                    print("Tarea eliminada correctamente.")
                    print()



        elif selecion == 5: 
            print("¡¡¡Gracias por usar mi programa!!!")
