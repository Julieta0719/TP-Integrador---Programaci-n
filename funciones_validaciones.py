import csv

#Validación de que la variable contenga un string
def validar_pais(pais_buscado):
    if pais_buscado.replace(" ","").isalpha():
        pais_buscado = str(pais_buscado)
    else:
        print("Incorrecto, debe ingresar el nombre de un país")

#Validación de busqueda de país exacta
def validacion_exacta(pais_buscado):

    #Se abre el archivo csv para lectura
    with open("paises.csv", "r", newline="", encoding="utf-8") as archivo:
        lectura = csv.DictReader(archivo)

        #Bucle para leer linea por linea
        for linea in lectura:

            #Si el país buscado se encuentra en el archivo csv, se imprime su respectiva información
            if pais_buscado in linea.values():
                print(f"""Nombre: {linea["Nombre"]}
                        Población: {linea["Población"]}
                        Superficie: {linea["Superficie"]}
                        Continente: {linea["Continente"]}""")
                
            else:
                continue
            if not pais_buscado in linea.values():
                print("El nombre ingrsado no se encuentra en el archivo")


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
                print(f"""Nombre: {linea["Nombre"]}
                        Población: {linea["Población"]}
                        Superficie: {linea["Superficie"]}
                        Continente: {linea["Continente"]}""")

