import os
import logging

def cargar_hechos_museos(env):
    # Configurar logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Directorio que contiene los archivos de hechos
    directorio_hechos = "pruebas/hechos/"
    
    # Contador de hechos cargados exitosamente
    hechos_cargados = 0
    
    # Iterar sobre todos los archivos en el directorio
    for archivo in os.listdir(directorio_hechos):
        if archivo.startswith("museo_") and archivo.endswith(".clp"):
            ruta_completa = os.path.join(directorio_hechos, archivo)
            try:
                env.load(ruta_completa)
                hechos_cargados += 1
                logging.info(f"Hecho de museo {archivo} cargado con éxito.")
            except Exception as e:
                logging.error(f"Error al cargar hecho {archivo}: {e}")

    logging.info(f"Total de hechos de museos cargados: {hechos_cargados}")

    # Verificar si se cargaron todos los hechos esperados
    if hechos_cargados < 38:  # Asumiendo que esperas 38 museos (del 2 al 39)
        logging.warning(f"Se esperaban 38 hechos, pero solo se cargaron {hechos_cargados}.")

    return hechos_cargados