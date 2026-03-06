# Análisis del Ecosistema Tecnológico a partir de GitHub

## Descripción del proyecto

En este proyecto analizo tendencias del ecosistema tecnológico utilizando datos de repositorios públicos de GitHub. La idea es explorar qué lenguajes dominan los repositorios más populares, cómo se distribuye la popularidad de los proyectos y qué tecnologías tienen mayor crecimiento.El objetivo es simular un caso real de análisis de datos, desde la obtención de los datos hasta la generación de insights y visualizaciones.



## Origen de los datos

Los datos se obtienen a partir de la API de GitHub, consultando repositorios públicos con más de 5000 estrellas.Para cada repositorio se extrae información como:

- nombre del repositorio  
- lenguaje principal  
- número de estrellas  
- forks  
- watchers  
- fecha de creación  
- fecha de última actualización  

Estos datos se procesan y se guardan en un dataset para su posterior análisis.


## Flujo del proyecto

El flujo de trabajo del proyecto es el siguiente:

- GitHub API 
- Script de ingesta de datos (Python)  
- Limpieza y estructuración del dataset  
- Análisis exploratorio de datos  
- Visualizaciones e insights


## Como ejecutar el proyecto 

- Clonar este repositorio
- instalar las dependencias (pip install -r requirements.txt)
- Ejecutar el script para obtener los datos
- Abrir el notebook para explorar el análisis

