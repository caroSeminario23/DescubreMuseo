def generar_hecho_museo_clips(museo):
    # Crear el formato del hecho para CLIPS usando la información del museo
    hecho_clips = f"""
    (deffacts museo_datos
        (museo
            (id_museo {museo['id_museo']})
            (distrito {museo['distrito']})
            (puntaje_resena {museo['puntaje_resena']})
            (ha_inicio {museo['ha_inicio']})
            (ha_fin {museo['ha_fin']})
            (hc_inicio {museo['hc_inicio']})
            (hc_fin {museo['hc_fin']})
            (tarifa_normal {museo['tarifa_normal']})
            (tarifa_ninos {museo['tarifa_ninos']})
            (tarifa_ancianos {museo['tarifa_ancianos']})
            (tarifa_discapacitados {museo['tarifa_discapacitados']})
            (reserva_entrada {museo['reserva_entrada']})
            (servicio_restaurante {museo['servicio_restaurante']})
            (servicio_cafeteria {museo['servicio_cafeteria']})
            (servicio_guiado {museo['servicio_guiado']})
            (servicio_biblioteca {museo['servicio_biblioteca']})
            (venta_objetos {museo['venta_objetos']})
            (accesibilidad {museo['accesibilidad']})
            (permiso_foto {museo['permiso_foto']})
            (estacionamiento {museo['estacionamiento']})
            (visita_virtual {museo['visita_virtual']})
            (n_restaurantes_prox {museo['n_restaurantes_prox']})
            (n_atracciones_prox {museo['n_atracciones_prox']})
            (telefono {museo['telefono']})
            (email {museo['email']})
            (sitio_web {museo['sitio_web']})
            (pag_facebook {museo['pag_facebook']})
            (pag_instagram {museo['pag_instagram']})
            (pag_tiktok {museo['pag_tiktok']})
            (categoria {" ".join(museo['categoria'].split())})
            (dia_atencion {" ".join(museo['dia_atencion'].split())})
            (dia_concurrido {" ".join(museo['dia_concurrido'].split())})
        )
    )
    """
    return hecho_clips


def guardar_hecho_museo_clips(hecho_clips, archivo='backend/base_hechos/museo_simplificado.clp'):
    with open(archivo, 'w', encoding='utf-8') as file:
        file.write(hecho_clips)
    print(f"\nHecho guardado en {archivo}")

def guardar_hecho_museo_clipsID(hecho_clips, dir_archivo, id_museo):
    archivo = f'{dir_archivo}/museo_{id_museo}.clp'
    with open(archivo, 'w', encoding='utf-8') as file:
        file.write(hecho_clips)
    print(f"\nHecho guardado en {archivo}")


# Datos del museo como ejemplo
museo = {
    "id_museo": 2,
    "distrito": "\"Barranco\"",
    "puntaje_resena": 4.3,
    "ha_inicio": 10,
    "ha_fin": 19,
    "hc_inicio": 16,
    "hc_fin": 18,
    "tarifa_normal": 12.0,
    "tarifa_ninos": 6.0,
    "tarifa_ancianos": 6.0,
    "tarifa_discapacitados": 12.0,
    "reserva_entrada": "FALSE",
    "servicio_restaurante": "FALSE",
    "servicio_cafeteria": "TRUE",
    "servicio_guiado": "TRUE",
    "servicio_biblioteca": "FALSE",
    "venta_objetos": "TRUE",
    "accesibilidad": "TRUE",
    "permiso_foto": "TRUE",
    "estacionamiento": "TRUE",
    "visita_virtual": "FALSE",
    "n_restaurantes_prox": 1822,
    "n_atracciones_prox": 230,
    "telefono": "TRUE",
    "email": "TRUE",
    "sitio_web": "TRUE",
    "pag_facebook": "TRUE",
    "pag_instagram": "TRUE",
    "pag_tiktok": "TRUE",
    "categoria": "\"Arte\"",
    "dia_atencion": "\"Martes\" \"Miércoles\" \"Jueves\" \"Viernes\" \"Domingo\"",
    "dia_concurrido": ""
}

# Generar y guardar el hecho de CLIPS
hecho_clips = generar_hecho_museo_clips(museo)

# Guardar el hecho en un archivo
guardar_hecho_museo_clips(hecho_clips)
