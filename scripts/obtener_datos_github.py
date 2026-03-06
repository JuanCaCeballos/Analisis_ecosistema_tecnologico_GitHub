import requests
import pandas as pd
import time

# Parámetros de la consulta
URL_BASE = "https://api.github.com/search/repositories"
PARAMS = {
    "q": "stars:>5000",
    "sort": "stars",
    "order": "desc",
    "per_page": 100
}
CABECERAS = {
    "Accept": "application/vnd.github.v3+json"
}

# Lista para almacenar los datos
repositorios = []

# GitHub limita el número de resultados por página y el total de páginas
for pagina in range(1, 6):  # 5 páginas x 100 repositorios = 500 repositorios
    print(f"Descargando página {pagina}...")
    PARAMS["page"] = pagina
    respuesta = requests.get(URL_BASE, params=PARAMS, headers=CABECERAS)
    if respuesta.status_code != 200:
        print(f"Error en la descarga: {respuesta.status_code}")
        break
    datos = respuesta.json()["items"]
    for repo in datos:
        repositorios.append({
            "nombre": repo["name"],
            "lenguaje": repo["language"],
            "estrellas": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "watchers": repo["watchers_count"],
            "fecha_creacion": repo["created_at"],
            "fecha_actualizacion": repo["updated_at"]
        })
    time.sleep(1)  # Espera para evitar límites de la API

# Crear DataFrame
print("Transformando datos en DataFrame...")
df = pd.DataFrame(repositorios)

# Limpieza de datos
print("Limpiando datos...")
df["lenguaje"].fillna("Desconocido", inplace=True)

# Guardar CSV
import os
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(directorio_actual, "../datos/repositorios_populares.csv")
df.to_csv(ruta_csv, index=False)
print(f"Datos guardados en {ruta_csv}")

# Fin del script
print("Proceso finalizado.")
