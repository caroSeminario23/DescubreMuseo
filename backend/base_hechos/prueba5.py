import clips

# Inicializar el entorno de CLIPS
env = clips.Environment()

# Cargar la plantilla desde un archivo externo
plantilla_path = "C:/Users/carolina/Documents/VS Code/DescubreMuseo/backend/base_hechos/plantilla.clp"
try:
    env.load(plantilla_path)
    print("Plantilla cargada con éxito.")
except Exception as e:
    print(f"Error al cargar plantilla: {e}")

# Mostrar las plantillas cargadas
print("Plantillas cargadas:")
for template in env.templates():
    print(f"Template: {template.name}")
    for slot in template.slots:
        print(f"  Slot: {slot.name}")

# Cargar el hecho desde un archivo externo
hechos_path = "C:/Users/carolina/Documents/VS Code/DescubreMuseo/backend/base_hechos/hecho.clp"
try:
    env.load(hechos_path)
    print("Hechos cargados con éxito.")
except Exception as e:
    print(f"Error al cargar hechos: {e}")

# Listar los hechos para verificar
print("Hechos cargados:")
for fact in env.facts():
    print(fact)

# Ejecutar el motor de inferencia
env.run()

# Listar todos los hechos en el entorno
print("Todos los hechos en el entorno:")
for fact in env.facts():
    print(fact)
