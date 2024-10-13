import clips

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
    ids = range(2, 4) #Hasta 40
    # Cargar varios hechos identificados por su ID
    for id in ids:
        hechos_path = f"pruebas/hechos2/museo_{id}.clp"
        try:
            env.load(hechos_path)
            print(f"Hecho de museo {id} cargado con éxito.")
            
            for fact in env.facts():
                print(fact)
            print("===============================")
        except Exception as e:
            print(f"Error al cargar hecho {id}: {e}")
    #env.reset()

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