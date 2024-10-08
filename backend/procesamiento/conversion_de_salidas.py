# Recoger los datos generados por CLIPS
id_museos_recomendados = []
for fact in env.facts():
    if fact.template.name == "recomendacion":
        id_museos_recomendados.append(fact['id_museo'])
        