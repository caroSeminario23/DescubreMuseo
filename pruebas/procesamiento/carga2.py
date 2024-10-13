import clips
import os

#Función para cargar los clips
def cargar_clips():
    env = clips.Environment()
    cargar_templates(env)
    cargar_reglas_intermedias(env)
    cargar_regla_general(env)
    cargar_hechos_museos(env)
    cargar_hechos_preferencias_usuario(env)
    env.reset() # Resetear el entorno para asegurar que los deffacts se apliquen
    return env

def cargar_templates(env):
    # Cargar la plantilla desde un archivo externo
    plantilla_path = "pruebas/templates/completo.clp"
    try:
        env.load(plantilla_path)
        print("Plantilla cargada con éxito.")
    except Exception as e:
        print(f"Error al cargar plantilla: {e}")

def cargar_regla_general(env):
    # Cargar la regla general desde un archivo externo
    regla_general_path = "pruebas/reglas/regla_a_prueba2.clp"
    try:
        env.load(regla_general_path)
        print("Regla general cargada con éxito.")
    except Exception as e:
        print(f"Error al cargar regla general: {e}")

def cargar_reglas_intermedias(env):
    # Cargar las reglas intermedias desde un archivo externo
    reglas_intermedias_path = "pruebas/reglas/reglas_intermedias.clp"
    try:
        env.load(reglas_intermedias_path)
        print("Reglas intermedias cargadas con éxito.")
    except Exception as e:
        print(f"Error al cargar reglas intermedias: {e}")

def cargar_hechos_preferencias_usuario(env):
    # Cargar el hecho desde un archivo externo
    hechos_path = "pruebas/hechos/preferencia_usuario.clp"
    try:
        env.load(hechos_path)
        print("Hecho de preferencias de usuario cargado con éxito.")
    except Exception as e:
        print(f"Error al cargar hechos: {e}")

def cargar_hechos_museos(env):
    # Directorio que contiene los archivos de hechos
    directorio_hechos = "pruebas/hechos2/"
    
    # Contador de hechos cargados exitosamente
    hechos_cargados = 0

    # Iterar sobre todos los archivos en el directorio
    for archivo in os.listdir(directorio_hechos):
        if archivo.startswith("museo_") and archivo.endswith(".clp"):
            ruta_completa = os.path.join(directorio_hechos, archivo)
            try:
                env.load(ruta_completa)
                hechos_cargados += 1
                print(f"Hecho de museo {archivo} cargado con éxito.")
            except Exception as e:
                print(f"Error al cargar hecho {archivo}: {e}")

    print(f"Total de hechos de museos cargados: {hechos_cargados}")


if __name__ == "__main__":
    env = cargar_clips()

    print("\n\nHechos antes de ejecucion:")
    for fact in env.facts():
        print(fact)
    print("===============================")

    env.run()

    # Imprimir los hechos
    print("\n\nHechos despues de ejecucion:")
    for fact in env.facts():
        print(fact)
    print("===============================")