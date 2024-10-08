from flask import json
from procesamiento_museo import procesar_datos

def simplificar_un_museo():
    # Leer los archivos JSON
    with open('backend/procesamiento/archivos_JSON/data_museo.json', 'r') as file:
        data_museo = json.load(file)

    with open('backend/procesamiento/archivos_JSON/data_categorias.json', 'r') as file:
        data_categorias = json.load(file)

    with open('backend/procesamiento/archivos_JSON/data_dia_atencion.json', 'r') as file:
        data_dia_atencion = json.load(file)

    with open('backend/procesamiento/archivos_JSON/data_dia_concurrido.json', 'r') as file:
        data_dia_concurrido = json.load(file)

    # Crear diccionarios para cada archivo JSON
    json_museo = data_museo
    json_categorias = data_categorias
    json_dia_atencion = data_dia_atencion
    json_dia_concurrido = data_dia_concurrido

    # Guardar el diccionario resultante en un archivo JSON
    museo_simplificado = procesar_datos(json_museo, json_categorias, json_dia_atencion, json_dia_concurrido)

    # Impresión de los datos simplificados
    print(museo_simplificado)

    # Guardar el resultado en un archivo JSON
    with open('backend/procesamiento/archivos_JSON/museo_simplificado.json', 'w', encoding='utf-8') as f:
        json.dump(museo_simplificado, f, ensure_ascii=False, indent=4)

    print("Datos guardados en museo_simplificado.json")

if __name__ == "__main__":
    simplificar_un_museo()