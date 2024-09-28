# Web Mapping Project

Este proyecto de **Web Mapping** utiliza diversas tecnologías para crear y visualizar mapas interactivos en archivos HTML, basándose en la información de volcanes, como su latitud, longitud y otros datos relevantes.

## Tecnologías utilizadas

1. **Python**:
   - Utilizado como lenguaje principal para manipulación de datos y generación de mapas interactivos.
   
2. **pandas**:
   - Librería poderosa para análisis de datos. Se utiliza para procesar y organizar la información de los volcanes (como latitud, longitud, elevación, etc.) que se carga desde archivos de texto o CSV.
   
3. **folium**:
   - Librería para generar mapas interactivos que se guardan en archivos HTML. Nos permite representar fácilmente ubicaciones geográficas (como volcanes) en un mapa visual.
   
4. **Jupyter Notebook**:
   - Herramienta utilizada para ejecutar y probar el código, además de realizar análisis de datos.
   
5. **Git y GitHub**:
   - Control de versiones: Para gestionar el desarrollo del proyecto y almacenar los cambios en un repositorio remoto en GitHub.

## Estructura del proyecto

- **Map1.html**: Archivo generado con el mapa interactivo que contiene marcadores de diferentes volcanes.
- **volcanes_extendido.csv**: Archivo CSV que contiene la información de varios volcanes, como nombre, ubicación, elevación, tipo de volcán, latitud y longitud.
- **main.py**: Script principal que utiliza `folium` y `pandas` para procesar los datos de los volcanes y generar el mapa.
- **README.md**: Descripción del proyecto (este archivo).

## Instrucciones de uso

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/Antoniomorales17/Web_Mapping.git
