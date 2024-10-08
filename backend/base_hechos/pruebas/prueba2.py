import clips

# Leer el archivo de plantillas
def read_templates(filename):
    with open(filename, 'r') as file:
        return file.read()

# Crear un entorno de CLIPS
environment = clips.Environment()

# Leer y construir las plantillas desde un archivo
templates = read_templates(r'C:\Users\carolina\Documents\VS Code\DescubreMuseo\backend\base_conocimiento\rules\templates.clp')
environment.build(templates)

# Leer y mostrar las plantillas
for template in environment.templates():
    print(f"Template: {template.name}")
    for slot in template.slots:
        print(f"  Slot: {slot.name}, Type: {slot.type}")