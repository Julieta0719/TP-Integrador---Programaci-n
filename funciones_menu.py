def mostrar_menu():
    
    print("------------------------------------")
    print(" Menú de gestión de datos de países")
    print("------------------------------------\n" \
    " Opciones interactivas:")

    print("------------------------------------\n" \
    " [1]: Buscar un país por su nombre\n" \
    " [2]: Filtrar países\n" \
    " [3]: Ordenar países\n" \
    " [4]: Mostrar estadísticas\n"
    " [5]: Salir\n" 
    "------------------------------------")

def preguntar_opcion():
    
    #Bucle while para consultar el número cuantas veces sea necesario (si se ingresa mal)
    menu_flag: bool = True
    while menu_flag:

        opcion = input("Por favor, ingrese el número de la opción de la que desea interactuar: ")

        if opcion.isdigit() and opcion.strip() != "" and opcion in ["1","2","3","4","5"]:
            opcion = int(opcion)
            #Opción 1
            if opcion == 1:
                pass

            #Opción 2
            elif opcion == 2:
                pass

            #Opción 3
            elif opcion == 3:
                pass

            #Opción 4
            elif opcion == 4:
                pass
                
            #Opción 5
            elif opcion == 5:
                print("Saliendo...")
                menu_flag = False
            else:
                print()
        else:
            print("La opcion debe ser un numero entre 1 y 4")
            menu_flag = True

