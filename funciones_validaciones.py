import csv
from datos_consola import console

#Validación de que la variable contenga un string
def validar_pais(pais_buscado):
    if pais_buscado.replace(" ","").isalpha():
        pais_buscado = str(pais_buscado)
    else:
        console.print("[advertencia]Incorrecto, debe ingresar el nombre de un país[/advertencia]")

#Validación de busqueda de país exacta
def validacion_exacta(pais_buscado):

    #Se abre el archivo csv para lectura
    with open("paises.csv", "r", newline="", encoding="utf-8") as archivo:
        lectura = csv.DictReader(archivo)

        #Bucle para leer linea por linea
        for linea in lectura:

            #Si el país buscado se encuentra en el archivo csv, se imprime su respectiva información
            if pais_buscado in linea.values():
                console.print(f"""[titulo]Nombre: {linea["Nombre"]}[/titulo]
                        [info]Población: {linea["Población"]}[/info]
                        [exito]Superficie: {linea["Superficie"]}[/exito]
                        [opcion]Continente: {linea["Continente"]}[/opcion]""")
                
            else:
                continue
            if not pais_buscado in linea.values():
                console.print("[advertencia]El nombre ingrsado no se encuentra en el archivo[/advertencia]")


#Validacion de busqueda de país de forma parcial
def validacion_parcial(pais_buscado):

    #Se abre el archivo csv para lectura
    with open("paises.csv", "r", newline="", encoding="utf-8") as archivo:
        lectura = csv.DictReader(archivo)

        #Bucle for para leer cada linea del archivo
        for linea in lectura:
            
            #Asignar a una variable el dato de la linea actual
            paises = linea["Nombre"]

            #Si el string ingresado esta en el nombre del pais se muestran sus datos
            if pais_buscado in paises:
                console.print(f"""[titulo]Nombre: {linea["Nombre"]}[/titulo]
                        [info]Población: {linea["Población"]}[/info]
                        [exito]Superficie: {linea["Superficie"]}[/exito]
                        [opcion]Continente: {linea["Continente"]}[/opcion]""")

