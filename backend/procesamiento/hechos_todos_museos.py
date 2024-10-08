from extraer_datos_bd import extraer_json_por_museo
from simplificar_museo import simplificar_un_museo
from convertir_museo_hecho import generar_hecho_museo_clips, guardar_hecho_museo_clipsID
from flask import json

def convertir_museos_hechos():
    for i in range(1, 40):
        data_museo, data_categorias, data_dia_atencion, data_dia_concurrido = extraer_json_por_museo(i)
        print(data_museo)
        print(data_categorias)
        print(data_dia_atencion)
        print(data_dia_concurrido)
        print("")

        # Guardar en archivos JSON
        with open(f'backend/procesamiento/archivos_JSON/data_museo.json', 'w') as file:
            json.dump(data_museo, file, indent=4)

        with open(f'backend/procesamiento/archivos_JSON/data_categorias.json', 'w') as file:
            json.dump(data_categorias, file, indent=4)

        with open(f'backend/procesamiento/archivos_JSON/data_dia_atencion.json', 'w') as file:
            json.dump(data_dia_atencion, file, indent=4)

        with open(f'backend/procesamiento/archivos_JSON/data_dia_concurrido.json', 'w') as file:
            json.dump(data_dia_concurrido, file, indent=4)

        print(f"Datos guardados correctamente para el museo {i}")

        print("\nSimplificando datos...")
        simplificar_un_museo()

        # Leer un archivo JSON
        with open('backend/procesamiento/archivos_JSON/museo_simplificado.json', 'r') as file:
            data_museo_simplificado = json.load(file)

        # Crear diccionario para el archivo JSON
        dicc_museo_simplificado = data_museo_simplificado

        # Generar el hecho de CLIPS para el museo
        hecho_museo = generar_hecho_museo_clips(dicc_museo_simplificado)

        # Guardar el hecho en un archivo CLIPS
        print("\nGuardando hecho en archivo CLIPS...")
        guardar_hecho_museo_clipsID(hecho_museo, 'backend/base_hechos/hechos_museos', i)