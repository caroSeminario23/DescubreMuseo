import clips

#Función para cargar los clips
def cargar_clips():
    env = clips.Environment()
    cargar_templates(env)
    cargar_reglas_intermedias(env)
    cargar_hechos_preferencias_usuario(env)
    env.reset() # Resetear el entorno para asegurar que los deffacts se apliquen
    env.run()
    guardar_hechos(env, "backend/base_hechos/hechos_intermedios.clp")
    return env

#backend/base_conocimiento/templates/completo.clp
def cargar_templates(env):
    # Cargar la plantilla desde un archivo externo
    plantilla_path = "backend/base_conocimiento/templates/completo.clp"
    try:
        env.load(plantilla_path)
        print("Plantilla cargada con éxito.")
    except Exception as e:
        print(f"Error al cargar plantilla: {e}")

#backend/base_conocimiento/rules/reglas_intermedias.clp
def cargar_reglas_intermedias(env):
    # Cargar las reglas intermedias desde un archivo externo
    reglas_intermedias_path = "backend/base_conocimiento/rules/reglas_intermedias.clp"
    try:
        env.load(reglas_intermedias_path)
        print("Reglas intermedias cargadas con éxito.")
    except Exception as e:
        print(f"Error al cargar reglas intermedias: {e}")

def cargar_hechos_preferencias_usuario(env):
    # Cargar el hecho desde un archivo externo
    hechos_path = "backend/base_hechos/preferencia_usuario.clp"
    try:
        env.load(hechos_path)
        print("Hecho de preferencias de usuario cargado con éxito.")
    except Exception as e:
        print(f"Error al cargar hechos: {e}")

def guardar_hechos(env, file_path):
    # Obtener todos los hechos del entorno
    hechos = env.facts()
    with open(file_path, 'w') as file:
        file.write("(deffacts hechos_guardados\n")
        for hecho in hechos:
            file.write(f"  {hecho}\n")
        file.write(")\n")
    print(f"Hechos guardados en {file_path}")

if __name__ == '__main__':
    env = cargar_clips()

    '''print("\n\n\nHechos antes de ejecucion:")
    for fact in env.facts():
        print(fact)
    env.run()'''

    # Imprimir los hechos
    print("\n\n\nHechos despues de ejecucion:")
    for fact in env.facts():
        print(fact)