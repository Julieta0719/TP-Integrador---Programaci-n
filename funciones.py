import requests
import csv
import json


def obtener_datos(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()

        datos = respuesta.json()
        return datos

    except requests.exceptions.RequestException as a:
        print(f" Error al conectar con la API: {a}")
        return []

    except json.JSONDecodeError:
        print("Error al convertir la respuesta a JSON.")
        return []
    
def validar_datos(paises):
    paises_validos = []

    for pais in paises:
        try:
            nombre = pais["name"]["common"]
            poblacion = pais.get("population")
            superficie = pais.get("area")
            continente = pais["continents"][0]

            if not nombre or not isinstance(poblacion, (int, float)) or not isinstance(superficie, (int, float)):
                continue

            paises_validos.append({
                "nombre": nombre,
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente
            })

        except (KeyError, IndexError, TypeError):
            continue

    return paises_validos

def formatear_datos(paises):
    encabezado = ["Nombre", "Población", "Superficie", "Continente"]
    filas = [encabezado]

    for pais in paises:
        fila = [
            pais["nombre"],
            pais["poblacion"],
            pais["superficie"],
            pais["continente"]
        ]
        filas.append(fila)

    return filas

def guardar_en_csv(datos_pais, datos):
    try:
        with open(datos_pais, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(datos)
        print(f"Archivo '{datos_pais}' guardado correctamente.")

    except IOError as a:
        print(f"Error al escribir el archivo CSV: {a}")



def csv_a_lista(datos_pais):
    
    paises = []
    try:
        with open(datos_pais, mode="r",newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Normalizar y convertir
                try:
                    nombre = fila.get("Nombre", "").strip()
                    poblacion = int(fila.get("Población", "0").replace(",", "").strip())
                    superficie = float(fila.get("Superficie", "0").replace(",", "").strip())
                    continente = fila.get("Continente", "").strip()

                    # Omitir filas sin nombre
                    if not nombre:
                        continue

                    pais = {
                        "Nombre": nombre,
                        "Población": poblacion,
                        "Superficie": superficie,
                        "Continente": continente
                    }
                    paises.append(pais)
                except (ValueError, TypeError):
                    # Si falla la conversión numérica, saltar esa fila
                    continue
        return paises
    except FileNotFoundError:
        print("Archivo no encontrado:", datos_pais)
        return []
