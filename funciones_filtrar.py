import csv
from funciones_menu import limpiar_consola, tabla_menu
from funciones import menu_retorno
from datos_consola import console


#--------------------------------------------------------------------------------------------------------------------------

#Funcion de filtrado por continente (Opcion 1 del menu de filtración)
def filtrar_por_continente():
    continentes = {
        1: ("Africa", ["Africa"]),
        2: ("America", ["North America", "South America"]),
        3: ("Asia", ["Asia"]),
        4: ("Europa", ["Europe"]),
        5: ("Oceania", ["Oceania"])
    }
    while True:
        limpiar_consola()
        opciones = []
        for datos in continentes.values():
            nombre_continente = str(datos[0]) 
            opciones.append(nombre_continente)
        tabla_menu("Filtrar Continentes", opciones)
        opcion = input("Ingrese la opcion que desee: ").strip()

        if not opcion.isdigit():
            console.print("[advertencia]La opcion no es valida[/advertencia]")
            continue

        opcion = int(opcion)
        if opcion not in continentes:
            console.print("[advertencia]La opcion no corresponde a ningun Continente")
            continue

        opcion_continente, datos = continentes[opcion]
        console.print(f"[titulo]---Paises de {opcion_continente}---[/titulo]")

        with open("paises.csv","r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["Continente"].strip() in datos:
                    console.print(f"[opcion]{fila['Nombre'].strip()}[/opcion]")
        
        if menu_retorno():
            limpiar_consola()
            break


#--------------------------------------------------------------------------------------------------------------------------

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
                    console.print(f"[titulo]{linea['Nombre']}[/titulo] --> [opcion]{poblacion}[/opcion]")
            except (TypeError,ValueError):
                console.print("[advertencia]Los limites de rango no son validos, debe ingresar un entero positivo[/advertencia]")
                break

#-------------------------------------------------------------------------------------------------------------------------------------

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
                    console.print(f"[titulo]{linea['Nombre']}[/titulo] --> [exito]{superficie}[/exito]")
            except (TypeError, ValueError):
                console.print("[advertencia]Datos de rango incorrectos[/advertencia]")