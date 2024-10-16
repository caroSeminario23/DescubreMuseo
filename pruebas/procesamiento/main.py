from pruebas.procesamiento.cargar_un_hecho import cargar_clips

id_museos_recomendados = []
for i in range(2, 4):
    # Cargar los clips
    env = cargar_clips(i)

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

    # Recoger los datos generados por CLIPS
    for fact in env.facts():
        if fact.template.name == "recomendacion":
            id_museos_recomendados.append(fact['id_museo'])

print(id_museos_recomendados)