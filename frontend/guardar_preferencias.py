def generar_hecho_preferencia_clips(preferencias):
    # Crear el formato de hecho para CLIPS
    hecho_clips = f"""
    (deffacts inicial
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
    return hecho_clips

def guardar_hecho_preferencia_clips(hecho_clips, archivo='backend/base_hechos/hecho2.clp'):
    with open(archivo, 'w', encoding='utf-8') as file:
        file.write(hecho_clips)
    print(f"\nHecho guardado en {archivo}")

# Suponiendo que tienes el diccionario de preferencias
preferencias = {
    'distrito_especificado': 'Lima',
    'dia_especificado': 'Lunes',
    'hora_especificada': '10:00',
    'categoria_especificada': 'Arqueología',
    'concurrencia': 'Alta',
    'tarifa_usuario': 'Media',
    'resena_usuario': '4.5',
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
    'cantidad_rest_cerca': '3',
    'cantidad_atrac_cerca': '2'
}

# Generar el hecho en formato CLIPS
hecho_clips = generar_hecho_preferencia_clips(preferencias)

# Guardar el hecho en un archivo .clp
guardar_hecho_preferencia_clips(hecho_clips)
