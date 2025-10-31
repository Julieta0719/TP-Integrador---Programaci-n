
import os
from funciones_validaciones import validar_pais, validacion_exacta, validacion_parcial

#Función para limpiar la consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


#Funcion de la opcion 1 (Buscar un país por su nombre)
def buscar_pais():

    limpiar_consola()

    pais_buscado = input("Ingrese el nombre del país del que desea consultar su información: ").capitalize()
    validar_pais(pais_buscado)
    validacion_exacta(pais_buscado)
    validacion_parcial(pais_buscado)



#Funcion de la opcion 2 (Filtraciones)
def menu_filtraciones():

    #Importación de las funciones
    from funciones_filtrar import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie

    limpiar_consola()

    print("""             ---------------------------------------------
                      ---Menú de Filtraciones---             
             ---------------------------------------------
              [1]: Filtrar país por continente
              [2]: Filtrar países por rango de población
              [3]: Filtrar países por rango de superficie
             ---------------------------------------------
             """)
    #Bucle while del menú
    filtraciones_flag: bool = True
    while filtraciones_flag:

            opcion_filtracion = input("Ingrese el número de la opción para filtrar: ")

            if opcion_filtracion.isdigit() and opcion_filtracion.strip() != "":
                opcion_filtracion = int(opcion_filtracion)

                if opcion_filtracion >=1 and opcion_filtracion <=3:

                    if opcion_filtracion == 1:

                        filtrar_por_continente()
                        filtraciones_flag = False
        
                    elif opcion_filtracion == 2:

                        filtrar_por_poblacion()
                        filtraciones_flag = False

                    elif opcion_filtracion == 3:
                        filtrar_por_superficie()
                        filtraciones_flag = False
                    else:
                        break
                else:
                    print("La opción debe ser entre 1 y 3")      
            else:
                print("Incorrecto, ingrese una opcion valida")


#Funcion de la opcion 3 (Ordenamiento)
def menu_ordenamiento():

    #Importación de las funciones
    from funciones_ordenar import ordenar_paises, ordenar_poblacion, ordenar_superficie

    limpiar_consola()

    print("""             ---------------------------------------------
                      ---Menú de Ordenamiento---             
             ---------------------------------------------
              [1]: Ordenar países alfabeticamente
              [2]: Ordenar población de menor a mayor
              [3]: Ordenar superficie de forma ascendente
             ---------------------------------------------
             """)
    #Bucle while del menú
    ordenamiento_flag: bool = True
    while ordenamiento_flag:

            opcion_ordenamiento = input("Ingrese el número de la opción para ordenar: ")

            if opcion_ordenamiento.isdigit() and opcion_ordenamiento.strip() != "":
                opcion_ordenamiento = int(opcion_ordenamiento)

                if opcion_ordenamiento >=1 and opcion_ordenamiento <=3:

                    if opcion_ordenamiento == 1:

                        ordenar_paises()
                        ordenamiento_flag = False
        
                    elif opcion_ordenamiento == 2:

                        ordenar_poblacion()
                        ordenamiento_flag = False

                    elif opcion_ordenamiento == 3:
                        ordenar_superficie()
                        ordenamiento_flag = False
                    else:
                        break
                else:
                    print("La opción debe ser entre 1 y 3")
            else:
                print("Incorrecto debe ingresar una opción valida")


#Funcion de la opción 4 (Estadísticas)

def menu_estadisticas():

    #Imporcion de las funciones
    from funciones_estadisticas import buscar_menor_poblacion, buscar_mayor_poblacion, promedio_poblaciones, promedio_superficies, contar_pais_por_continente

    limpiar_consola()

    print("""             ---------------------------------------------
                      ---Menú de Estadísticas---             
             ---------------------------------------------
              [1]: País con mayor y menor población
              [2]: Promedio de todas las poblaciones
              [3]: Promedio de todas las superficies
              [4]: Cantidad de países por continente
             ---------------------------------------------
             """)
    #Bucle while del menú
    estadisticas_flag: bool = True
    while estadisticas_flag:

            opcion_estadisticas = input("Ingrese el número de la opción para consultar estadisticas: ")

            if opcion_estadisticas.isdigit() and opcion_estadisticas.strip() != "":
                opcion_estadisticas = int(opcion_estadisticas)

                if opcion_estadisticas >=1 and opcion_estadisticas <=4:

                    if opcion_estadisticas == 1:
                        
                        buscar_menor_poblacion()
                        buscar_mayor_poblacion()
                        estadisticas_flag = False
        
                    elif opcion_estadisticas == 2:

                        promedio_poblaciones()
                        estadisticas_flag = False

                    elif opcion_estadisticas == 3:
                        promedio_superficies()
                        estadisticas_flag = False

                    elif opcion_estadisticas == 4:
                        contar_pais_por_continente()
                        estadisticas_flag = False
                    else:
                        break
                else:
                    print("La opción debe ser entre 1 y 4")
            else:
                print("Incorrecto, debe ingresar una opción valida")       

#Función del menú
def preguntar_opcion():

    limpiar_consola()

    #Bucle while para consultar el número cuantas veces sea necesario (si se ingresa mal)
    menu_flag: bool = True
    while menu_flag:

        print("--------------------------------------")
        print("  Menú de gestión de datos de países")
        print("--------------------------------------\n" \
        " Opciones interactivas:")

        print("--------------------------------------\n" \
        " [1]: Buscar un país por su nombre \n" \
        " [2]: Filtrar países               \n" \
        " [3]: Ordenar países               \n" \
        " [4]: Mostrar estadísticas         \n"
        " [5]: Salir                        \n" 
        "--------------------------------------")

        opcion = input("Por favor, ingrese el número de la opción de la que desea interactuar: ")

        #Validación del dato ingresado
        if opcion.isdigit() and opcion.strip() != "" and opcion in ["1","2","3","4","5"]:
            opcion = int(opcion)
            
            if opcion == 1:

                buscar_pais()

            elif opcion == 2:

                menu_filtraciones()

            elif opcion == 3:

                menu_ordenamiento()

            elif opcion == 4:
                
                menu_estadisticas()
                
                
            elif opcion == 5:
                print("---Gracias por usar el programa!---")
                menu_flag = False
            else:
                print()
        else:
            print("La opción debe ser un número entre 1 y 4")
            menu_flag = True

