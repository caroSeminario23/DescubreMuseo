import clips

# Definir una plantilla de hechos
DEFTEMPLATE_STRING = """
(deftemplate persona
    (slot nombre (type STRING))
    (slot apellido (type STRING))
    (slot fecha_nacimiento (type SYMBOL)))
"""

# Definir una regla
DEFRULE_STRING = """
(defrule saludo
    "Saludar a una nueva persona."
    (persona (nombre ?nombre) (apellido ?apellido))
    =>
    (printout t "Hola " ?nombre " " ?apellido crlf))
"""

# Crear un entorno de CLIPS
environment = clips.Environment()

# Construir las plantillas y reglas en el entorno
environment.build(DEFTEMPLATE_STRING)
environment.build(DEFRULE_STRING)

# Crear un hecho basado en la plantilla
template = environment.find_template('persona')
hecho = template.assert_fact(nombre='Juan', apellido='Pérez', fecha_nacimiento=clips.Symbol('01/01/1980'))

# Ejecutar las reglas
environment.run()