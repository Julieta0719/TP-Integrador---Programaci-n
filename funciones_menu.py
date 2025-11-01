
import os
from funciones_validaciones import validar_pais, validacion_exacta, validacion_parcial
from funciones import menu_retorno
from datos_consola import console
from rich.theme import Theme
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
from rich.text import Text
from rich import box
from halo import Halo
from alive_progress import alive_bar
from loguru import logger
from rich.traceback import install
from prompt_toolkit import prompt as pt_prompt
from prompt_toolkit.completion import WordCompleter

color = Theme({
    "advertencia": "bold red",
    "info": "bold cyan",
    "exito": "bold green"
})
console = Console(theme=color)

install(show_locals=True)
if not os.path.exists("logs"):
    os.makedirs("logs")
logger.add("logs/actividad.log", rotation="500 KB", backtrace=True, diagnose=True)

def animacion(ani):
    def decoracion(*args, **kwargs):
        spinner = Halo(text='Cargando...', spinner= 'dots', color= 'cyan')
        spinner.start()
        try:
            r = ani(*args, **kwargs)
        finally:
            spinner.stop()
        return r
    return decoracion

def progreso(ani):
    def decoracion_p(*args, **kwargs):
        with alive_bar(4, title=f"Ejecutando {ani.__name__}...") as bar:
            r = None
            for _ in range(4):
                r = ani(*args, **kwargs)
                bar()
        return r
    return decoracion_p

def bienvenida():
    recepcion = Text("Sistema de gestion de paises", style="bold cyan")
    presentacion = Text("Desarrollado por Julieta Caceres characan y Matias Ezequiel Maigua", style= "italic yellow")
    panel = Panel(
        Align.center(recepcion + "\n" + presentacion),
        border_style= "bright_blue",
        padding=(1,3),
        title="[bold cyan]Bienvenido/a[/bold cyan]",
    )
    console.print(panel)


def tabla_menu(titulo, opciones):
    tabla = Table(title=titulo, box=box.ROUNDED, border_style="cyan")
    tabla.add_column("N", justify="center",style="bold yellow")
    tabla.add_column("Descripcion", justify="center",style="bold white")


    for i, opcion in enumerate(opciones,1):
        tabla.add_row(str(i),opcion)
    
    console.print(tabla)


#--------------------------------------------------------------------------------------------------------------------------        

#Función para limpiar la consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

bienvenida()

#--------------------------------------------------------------------------------------------------------------------------

#Funcion de la opcion 1 (Buscar un país por su nombre)
def buscar_pais():
    
    limpiar_consola()
    
    pais_buscado = input("Ingrese el nombre del país del que desea consultar su información: ").title().strip()
    
    #Guardar el retorno (True/False) de la funcion que valida el dato ingresado
    pais_valido = validar_pais(pais_buscado)

    #Si el dato ingresado no es valido se retorna para terminar la ejecucion de la funcion
    if not pais_valido:
        input("Presione enter para volver al menu principal")
        return

    #Se guarda el valor retornado (True/False) de la funcion de validacion exacta
    pais_encontrado = validacion_exacta(pais_buscado)

    #Si se retorna false de la validacion exacta, se buscan coincidencias en la funcion de validacion parcial
    if not pais_encontrado:
        validacion_parcial(pais_buscado)
    input("Presione enter para volver al menu principal")
    if input:
        limpiar_consola()
           
#--------------------------------------------------------------------------------------------------------------------------

#Funcion de la opcion 2 (Filtraciones)
def menu_filtraciones():

    #Importación de las funciones
    from funciones_filtrar import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
    while True:
        limpiar_consola()

        opciones = [
            "Filtrar pais por continente",
            "Filtrar paises por rango de poblacion",
            "Filtrar paises por rango de superficie"
        ]
        tabla_menu("Menu de Filtraciones", opciones)
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
                        console.print("[advertencia]La opción debe ser entre 1 y 3[/advertencia]")      
                else:
                    console.print("[advertencia]Incorrecto, ingrese una opcion valida[/advertencia]")
        if menu_retorno():
            limpiar_consola()
            break

#--------------------------------------------------------------------------------------------------------------------------

#Funcion de la opcion 3 (Ordenamiento)
def menu_ordenamiento():

    #Importación de las funciones
    from funciones_ordenar import ordenar_paises, ordenar_poblacion, ordenar_superficie
    while True:
        limpiar_consola()

        opciones = [
            "Ordenar países alfabeticamente",
            "Ordenar población de menor a mayor",
            "Ordenar superficie de forma ascendente"
        ]
        tabla_menu("Menu de ordenamientos", opciones)
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
                        console.print("[advertencia]La opción debe ser entre 1 y 3[/advertencia]")
                else:
                    console.print("[advertencia]Incorrecto debe ingresar una opción valida[/advertencia]")
        if menu_retorno():
            limpiar_consola()
            break

#-----------------------------------------------------------------------------------------------------------------------------------------------

#Funcion de la opción 4 (Estadísticas)
def menu_estadisticas():

    #Imporcion de las funciones
    from funciones_estadisticas import buscar_menor_poblacion, buscar_mayor_poblacion, promedio_poblaciones, promedio_superficies, contar_pais_por_continente
    while True:
        limpiar_consola()

        opciones = [
            "País con mayor y menor población",
            "Promedio de todas las poblaciones",
            "Promedio de todas las superficies",
            "Cantidad de países por continente",
        ]

        tabla_menu("Menu de Promedios", opciones)
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
                        console.print("[advertencia]La opción debe ser entre 1 y 4[/advertencia]")
                else:
                    console.print("[advertencia]Incorrecto, debe ingresar una opción valida[/advertencia]")   
        if menu_retorno():
            limpiar_consola()
            break    

#--------------------------------------------------------------------------------------------------------------------------

#Función del menú
def preguntar_opcion():

    limpiar_consola()
    bienvenida()
    #Bucle while para consultar el número cuantas veces sea necesario (si se ingresa mal)
    menu_flag: bool = True
    while menu_flag:
        limpiar_consola()

        opciones = [
            " Buscar un país por su nombre",
            " Filtrar países",
            " Ordenar países", 
            " Mostrar estadísticas",
            " Salir"
        ]

        tabla_menu("Menu Principal", opciones)
        

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
                console.print(Panel.fit("---Gracias por usar el programa!---", style="bold green"))
                menu_flag = False
            else:
                console.print()
        else:
            console.print("[advertencia]La opción debe ser un número entre 1 y 4[/advertencia]")
            menu_flag = True

