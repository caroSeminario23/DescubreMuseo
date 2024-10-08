import clips

# Iniciar el entorno de CLIPS
env = clips.Environment()

# Definir la plantilla en CLIPS
env.build("""
(deftemplate preferencias_usuario
    (slot distrito_especificado)
    (slot dia_especificado)
    (slot hora_especificada)
    (slot categoria_especificada)
    (slot concurrencia)
    (slot tarifa_usuario)
    (slot resena_usuario)
    (slot descuento_ninos)
    (slot descuento_ancianos)
    (slot descuento_discapacitados)
    (slot comida_disponible)
    (slot reserva_usuario)
    (slot estacionamiento_usuario)
    (slot venta_objetos_usuario)
    (slot permiso_foto_usuario)
    (slot accesibilidad_usuario)
    (slot servicio_guiado_usuario)
    (slot visita_virtual_usuario)
    (slot servicio_biblioteca_usuario)
    (slot presencia_redes_sociales)
    (slot existencia_medios_comunicacion)
    (slot sitio_web_existe)
    (slot cantidad_rest_cerca)
    (slot cantidad_atrac_cerca)
)
""")

# Recoger las preferencias del usuario en un diccionario (como lo tienes)
preferencias = {
    'distrito_especificado': 'Lima',
    'dia_especificado': 'Lunes',
    'hora_especificada': '10:00',
    'categoria_especificada': 'Arte',
    'concurrencia': 'Alta',
    'tarifa_usuario': 'Media',
    'resena_usuario': 4.5,
    'descuento_ninos': 'si',
    'descuento_ancianos': 'no',
    'descuento_discapacitados': 'si',
    'comida_disponible': 'no',
    'reserva_usuario': 'no',
    'estacionamiento_usuario': 'si',
    'venta_objetos_usuario': 'si',
    'permiso_foto_usuario': 'si',
    'accesibilidad_usuario': 'si',
    'servicio_guiado_usuario': 'no',
    'visita_virtual_usuario': 'no',
    'servicio_biblioteca_usuario': 'no',
    'presencia_redes_sociales': 'si',
    'existencia_medios_comunicacion': 'si',
    'sitio_web_existe': 'si',
    'cantidad_rest_cerca': 3,
    'cantidad_atrac_cerca': 2
}

# Insertar el hecho en CLIPS usando el diccionario
fact_string = f"""
(assert
    (preferencias_usuario
        (distrito_especificado {preferencias['distrito_especificado']})
        (dia_especificado {preferencias['dia_especificado']})
        (hora_especificada {preferencias['hora_especificada']})
        (categoria_especificada {preferencias['categoria_especificada']})
        (concurrencia {preferencias['concurrencia']})
        (tarifa_usuario {preferencias['tarifa_usuario']})
        (resena_usuario {preferencias['resena_usuario']})
        (descuento_ninos {preferencias['descuento_ninos']})
        (descuento_ancianos {preferencias['descuento_ancianos']})
        (descuento_discapacitados {preferencias['descuento_discapacitados']})
        (comida_disponible {preferencias['comida_disponible']})
        (reserva_usuario {preferencias['reserva_usuario']})
        (estacionamiento_usuario {preferencias['estacionamiento_usuario']})
        (venta_objetos_usuario {preferencias['venta_objetos_usuario']})
        (permiso_foto_usuario {preferencias['permiso_foto_usuario']})
        (accesibilidad_usuario {preferencias['accesibilidad_usuario']})
        (servicio_guiado_usuario {preferencias['servicio_guiado_usuario']})
        (visita_virtual_usuario {preferencias['visita_virtual_usuario']})
        (servicio_biblioteca_usuario {preferencias['servicio_biblioteca_usuario']})
        (presencia_redes_sociales {preferencias['presencia_redes_sociales']})
        (existencia_medios_comunicacion {preferencias['existencia_medios_comunicacion']})
        (sitio_web_existe {preferencias['sitio_web_existe']})
        (cantidad_rest_cerca {preferencias['cantidad_rest_cerca']})
        (cantidad_atrac_cerca {preferencias['cantidad_atrac_cerca']})
    )
)
"""

# Ejecutar el comando assert en el entorno CLIPS
env.eval(fact_string)

# Ejecutar el motor de inferencia
env.run()

# Listar los hechos para verificar que se haya insertado correctamente
for fact in env.facts():
    print(fact)
