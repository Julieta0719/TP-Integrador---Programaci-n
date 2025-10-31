
import os
from funciones import obtener_datos, validar_datos, formatear_datos, guardar_en_csv
from datos_consola import console
def main():
    datos_pais = "paises.csv"

    # Verificamos si el CSV ya existe
    if os.path.exists(datos_pais):
        console.print(f"[info]El archivo '{datos_pais}' ya existe.[/info]")
        console.print("[advertencia]Se omite la descarga desde la API.[/advertencia]")
        return 
    url = "https://restcountries.com/v3.1/all?fields=name,area,continents,population,translations"
    datos_api = obtener_datos(url)

    if not datos_api:
        console.print("[advertencia]No se pudieron obtener datos de la API.[/advertencia]")
        return

    paises_validos = validar_datos(datos_api)
    datos_formateados = formatear_datos(paises_validos)
    guardar_en_csv("paises.csv", datos_formateados)
if __name__ == "__main__":
    main()


#Importación y llamado de funciones del menú
from funciones_menu import preguntar_opcion, limpiar_consola

limpiar_consola()

preguntar_opcion()