import csv
from funciones_menu import limpiar_consola
from funciones import menu_retorno
from datos_consola import console


#Funcion de filtrado por continente (Opcion 1 del menu de filtración)
def filtrar_por_continente():
    while True:
        limpiar_consola()

        print("""             -----------------------------------
                        ---Continentes---             
                -----------------------------------
                [1]: África
                [2]: América
                [3]: Asia
                [4]: Europa
                [5]: Oceanía
                -----------------------------------
                """)

        opcion_continente = input("Ingrese la opción del continente: ")

        #Validar la opción
        if opcion_continente.isdigit() and opcion_continente.strip() != "":
            opcion_continente = int(opcion_continente)
        else:
            console.print("[advertencia]La opción del continente no es valida[/advertencia]")
            continue

        #Diccionario con key de las opciones y value de los continentes
        continentes = {1: ["Africa"], 2: ["North America", "South America"], 3:["Asia"], 4: ["Europe"], 5: ["Oceania"]}

        #Si la opcion esta en el diccionario de continentes se guarda en una variable la opcion(int) ingresada como el nombre del continente
        if opcion_continente in continentes:
            continente_elegido = continentes[opcion_continente]
        
            if opcion_continente == 1:
                console.print("[titulo]---Países de África---[/titulo]")

                #Abrir el archivo csv en modo de lectura
                with open("paises.csv", "r", encoding="utf-8") as archivo:
                    lectura = csv.DictReader(archivo)

                    #Bucle para leer linea por linea
                    for fila in lectura:

                        #Si el continente de la fila actual coincide con el diccionario de continentes en el indice del continente seleccionado se imprime el país
                        if fila["Continente"].strip() in continentes[opcion_continente]:
                            console.print(f"[opcion]{fila["Nombre"].strip()}[/opcion]")


            elif opcion_continente == 2:
                console.print("[titulo]---Países de América---[/titulo]")
                
                with open("paises.csv", "r", encoding="utf-8") as archivo:
                    lectura = csv.DictReader(archivo)

                    for fila in lectura:

                        if fila["Continente"].strip() in continentes[opcion_continente]:
                            console.print(f"[opcion]{fila["Nombre"].strip()}[/opcion]")

            elif opcion_continente == 3:
                console.print("[titulo]---Países de Asia---[/titulo]")

                with open("paises.csv", "r", encoding="utf-8") as archivo:
                    lectura = csv.DictReader(archivo)

                    for fila in lectura:

                        if fila["Continente"].strip() in continentes[opcion_continente]:
                            console.print(f"[opcion]{fila["Nombre"].strip()}[/opcion]")

            elif opcion_continente == 4:
                console.print("[titulo]---Países de Europa---[/titulo]")

                with open("paises.csv", "r", encoding="utf-8") as archivo:
                    lectura = csv.DictReader(archivo)

                    for fila in lectura:

                        if fila["Continente"].strip() in continentes[opcion_continente]:
                            console.print(f"[opcion]{fila["Nombre"].strip()}[/opcion]")

            elif opcion_continente == 5:
                console.print("---Países de Oceanía---")
                #Abrir el archivo csv en modo de lectura
                with open("paises.csv", "r", encoding="utf-8") as archivo:
                    lectura = csv.DictReader(archivo)

                    for fila in lectura:

                        if fila["Continente"].strip() in continentes[opcion_continente]:
                            console.print(f"[opcion]{fila["Nombre"].strip()}[/opcion]")

            else:
                console.print("[advertencia]La opción del continente no es valida[/advertencia]")
                continue
        else:
            console.print("[advertencia]La opción no corresponde a ningún continente[/advertencia]")
            continue
        
        if menu_retorno():
            limpiar_consola()
            break



#Funcion de filtrado por rango de población (Opcion 2 del menu de filtración)
def filtrar_por_poblacion():

    #Pedir los limites de rango
    rango_minimo = input("Ingrese el límite de rango mínimo de la población: ")
    rango_maximo = input("Ingrese el límite de rango máximo de la población: ")

    #Validación de los rangos ingresados
    if (rango_minimo.isdigit() and rango_minimo.strip() != "") and (rango_maximo.isdigit() and rango_maximo.strip() != ""):

        #Convertir a int
        rango_minimo = int(rango_minimo)
        rango_maximo = int(rango_maximo)
        print(" ")
    else:
        console.print("[advertencia]Incorrecto[/advertencia]")
        return

    #Abrir el archivo csv para lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        lectura = csv.DictReader(archivo)

        #Bucle para leer linea por linea
        for linea in lectura:

            #Asignar a una variable el número de población en la linea actual
            poblacion = int(linea["Población"].replace(",","").strip())

            try:
                #Si la poblacion es mayor o igual al rango min, y la poblacion es menor o igual al rango max, se imprime
                if poblacion >= rango_minimo and poblacion <= rango_maximo:
                    console.print(f"[titulo]{linea["Nombre"]}[/titulo]  |  [opcion]{poblacion}[/opcion]")
            except (TypeError,ValueError):
                console.print("[advertencia]Los limites de rango no son validos, debe ingresar un entero positivo[/advertencia]")
                break


#Funcion de filtrado por rango de superficie (Opcion 3 del menu de filtración)
def filtrar_por_superficie():

    #Pedir los limites de rango
    rango_minimo = input("Ingrese el límite de rango mínimo de la superficie: ")
    rango_maximo = input("Ingrese el límite de rango máximo de la superficie: ")

    #Validación de los rangos
    if (rango_minimo.replace(".","",1).isdigit()) and (rango_maximo.replace(".","",1).isdigit()):

        #Convertir a float
        rango_minimo = float(rango_minimo)
        rango_maximo = float(rango_maximo)
        print(" ")
    else:
        console.print("[advertencia]Los limites de los rangos no son validos, debe ingresar decimales[/advertencia]")
        return
        

    #Abrir el archivo csv para lectura
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        lectura = csv.DictReader(archivo)

        #Bucle para leer linea por linea
        for linea in lectura:

            #Asignar a una variable el número de población en la linea actual
            superficie = float(linea["Superficie"].replace(",","").strip())
            try:

                #Si la poblacion es mayor o igual al rango min, y la poblacion es menor o igual al rango max, se imprime
                if superficie >= rango_minimo and superficie <= rango_maximo:
                    console.print(f"[titulo]{linea["Nombre"]}[/titulo]  |  [exito]{superficie}[/exito]")
            except (TypeError, ValueError):
                console.print("[advertencia]Datos de rango incorrectos[/advertencia]")