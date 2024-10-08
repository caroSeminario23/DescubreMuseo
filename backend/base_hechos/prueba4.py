import clips

# Inicializar el entorno de CLIPS
env = clips.Environment()

# Cargar la plantilla desde un archivo externo
plantilla_path = "C:/Users/carolina/Documents/VS Code/DescubreMuseo/backend/base_hechos/plantilla.clp"
env.load(plantilla_path)

'''# Mostrar las plantillas cargadas
for template in env.templates():
    print(f"Template: {template.name}")
    for slot in template.slots:
        print(f"  Slot: {slot.name}")'''

# Cargar el hecho desde un archivo externo
hechos_path = "C:/Users/carolina/Documents/VS Code/DescubreMuseo/backend/base_hechos/hecho.clp"
env.load(hechos_path)

'''# Ejecutar el motor de inferencia
env.run()'''

# Listar los hechos para verificar
for fact in env.facts():
    print(fact)