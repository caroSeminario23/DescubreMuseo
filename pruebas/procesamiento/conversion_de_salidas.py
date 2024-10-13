# Recoger los datos generados por CLIPS
def recoger_recomendaciones(env):
    id_museos_recomendados = []
    for fact in env.facts():
        if fact.template.name == "recomendacion":
            id_museos_recomendados.append(fact['id_museo'])
    return id_museos_recomendados