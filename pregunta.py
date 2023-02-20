"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    d = {"cluster": [], "cantidad_de_palabras_clave": [], 
    "porcentaje_de_palabras_clave": [], "principales_palabras_clave": []}
    with open("clusters_report.txt") as fh:
        for _ in range(4):
            next(fh)
        principales_palabras_clave = str()
        for line in fh:
            cluster = line[3:5].strip(" ")
            if cluster.isdigit():
                d["cluster"].append(int(cluster))

            cantidad_de_palabras_clave = line[9:12].strip(" ")
            if cantidad_de_palabras_clave.isdigit():
                d["cantidad_de_palabras_clave"].append(int(cantidad_de_palabras_clave))

            porcentaje_de_palabras_clave = line[25:31].strip(" ").rstrip(" %").replace(",", ".")
            if porcentaje_de_palabras_clave.replace(".", "", 1).isdigit():
                d["porcentaje_de_palabras_clave"].append(float(porcentaje_de_palabras_clave))

            principales_palabras_clave += line[41:]
            if line.strip().endswith(".") or line.strip().endswith("control"):
                principales_palabras_clave = principales_palabras_clave.replace("\n", "")
                principales_palabras_clave = principales_palabras_clave.replace(".", "")
                principales_palabras_clave = principales_palabras_clave.replace("     ", " ")
                principales_palabras_clave = principales_palabras_clave.replace("    ", " ")
                principales_palabras_clave = principales_palabras_clave.replace("   ", " ")
                principales_palabras_clave = principales_palabras_clave.replace("  ", " ")
                d["principales_palabras_clave"].append(principales_palabras_clave.strip())
                principales_palabras_clave = str()

    df = pd.DataFrame(d)
    return df