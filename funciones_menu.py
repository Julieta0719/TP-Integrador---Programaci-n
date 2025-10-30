def mostrar_menu():
    
    print("--------------------------------------")
    print("  Menú de gestión de datos de países")
    print("--------------------------------------\n" \
    " Opciones interactivas:")

    print("------------------------------------\n" \
    "| [1]: Buscar un país por su nombre |\n" \
    "| [2]: Filtrar países               |\n" \
    "| [3]: Ordenar países               |\n" \
    "| [4]: Mostrar estadísticas         |\n"
    "| [5]: Salir                        |\n" 
    "------------------------------------")

from funciones_validaciones import validar_pais, validacion_exacta, validacion_parcial

#Funcion de la opcion 1 (Buscar un país por su nombre)
def buscar_pais():

    pais_buscado = input("Ingrese el nombre del país del que desea consultar su información: ").capitalize()
    validar_pais(pais_buscado)
    validacion_exacta(pais_buscado)
    validacion_parcial(pais_buscado)


#Funcion de la opcion 2 (Filtraciones)
def menu_filtraciones():
    print("""             ---------------------------------------------
                      ---Menú de Filtraciones---             
             ---------------------------------------------
              [1]: Filtrar país por continente
              [2]: Filtrar países por rango de población
              [3]: Filtrar países por rango de superficie
             ---------------------------------------------""")


def preguntar_opcion():
    
    #Bucle while para consultar el número cuantas veces sea necesario (si se ingresa mal)
    menu_flag: bool = True
    while menu_flag:

        opcion = input("Por favor, ingrese el número de la opción de la que desea interactuar: ")

        #Validación del dato ingresado
        if opcion.isdigit() and opcion.strip() != "" and opcion in ["1","2","3","4","5"]:
            opcion = int(opcion)
            
            if opcion == 1:
                print("---Buscar país por nombre---")

                buscar_pais()

            elif opcion == 2:
                print("---Filtraciones---")

                menu_filtraciones()

            elif opcion == 3:
                print("---Ordenamiento---")

                #ordenar_paises()
                #menu_ordenamiento()

            elif opcion == 4:
                print("---Estadísticas---")

                #buscar_mayor_poblacion()
                #buscar_menor_poblacion()
                #promedio_poblaciones()
                #promedio_superficies()
                #contar_pais_por_continente()
                
            elif opcion == 5:
                print("---Gracias por usar el programa!---")
                menu_flag = False
            else:
                print()
        else:
            print("La opcion debe ser un numero entre 1 y 4")
            menu_flag = True

