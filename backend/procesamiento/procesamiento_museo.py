import json
data = {
    "accesibilidad": True,#accesibilidad ->18
    "anexo": None,
    "direccion": "Calle Retiro 160 - Miraflores",
    "distrito": {
        "nombre": "Miraflores"#distrito ->2
    },
    "email": "info@museoamano.org",#email ->25
    "estacionamiento": True,#estacionamiento ->20
    "ha_fin": "17:00:00",#ha_fin ->5
    "ha_inicio": "10:00:00",#ha_inicio ->4
    "hc_fin": "14:00:00",#hc_fin ->7
    "hc_inicio": "12:00:00",#hc_inicio ->6
    "id_distrito": 9,
    "id_museo": 1,#id_museo ->1
    "n_atracciones_prox": 295,#n_atracciones_prox ->23
    "n_restaurantes_prox": 2229,#n_restaurantes_prox ->22
    "nombre": "Museo Textil Precolombino: AMANO",
    "notas": None,
    "pag_facebook": "",#pag_facebook ->27
    "pag_instagram": "https://www.instagram.com/museoamano/",#pag_instagram ->28
    "pag_tiktok": "https://www.tiktok.com/@museoamano",#pag_tiktok ->29
    "permiso_foto": True,#permiso_foto ->19
    "puntaje_resena": "4.7",#puntaje_resena ->3
    "reserva_entrada": False,#reserva_entrada ->12
    "servicio_biblioteca": False,#servicio_biblioteca ->16
    "servicio_cafeteria": True,#servicio_cafeteria ->14
    "servicio_guiado": True,#servicio_guiado ->15
    "servicio_restaurante": True,#servicio_restaurante ->13
    "sitio_web": "www.museoamano.org",#sitio_web ->26
    "tarifa_ancianos": "25.00",#tarifa_ancianos ->10
    "tarifa_discapacitados": "35.00",#tarifa_discapacitados ->11
    "tarifa_ninos": "15.00",#tarifa_ninos ->9
    "tarifa_normal": "35.00",#tarifa_normal ->8
    "telefono": "4412909",#telefono ->24
    "venta_objetos": True,#venta_objetos ->17
    "visita_virtual": False#visita_virtual ->21
}

data_categoria = {
    "Temático": True,
    "Arqueológico": False,
    "Arte": True,
    "Histórico": False
}

data_dia_atencion = {
    "Lunes": True,
    "Martes": True,
    "Miercoles": True,
    "Jueves": True,
    "Viernes": False,
    "Sabado": False,
    "Domingo": False
}
data_dia_concurrido = {
    "Lunes": True,
    "Martes": True,
    "Miercoles": True,
    "Jueves": True,
    "Viernes": False,
    "Sabado": False,
    "Domingo": False
}

def procesar_datos(data, data_categoria, data_dia_atencion, data_dia_concurrido):
    # Extraer y convertir los valores de ha_fin, ha_inicio, hc_fin, hc_inicio
    data["ha_fin"] = int(data["ha_fin"][:2])
    data["ha_inicio"] = int(data["ha_inicio"][:2])
    data["hc_fin"] = int(data["hc_fin"][:2])
    data["hc_inicio"] = int(data["hc_inicio"][:2])

    # Convertir los valores de email, pag_facebook, pag_instagram, pag_tiktok, sitio_web a booleanos en mayúsculas
    data["email"] = "TRUE" if data["email"] else "FALSE"
    data["pag_facebook"] = "TRUE" if data["pag_facebook"] else "FALSE"
    data["pag_instagram"] = "TRUE" if data["pag_instagram"] else "FALSE"
    data["pag_tiktok"] = "TRUE" if data["pag_tiktok"] else "FALSE"
    data["sitio_web"] = "TRUE" if data["sitio_web"] else "FALSE"
    data["telefono"] = "TRUE" if data["telefono"] else "FALSE"

    # Convertir los valores de puntaje_resena, tarifa_ancianos, tarifa_discapacitados, tarifa_ninos, tarifa_normal a float
    data["puntaje_resena"] = float(data["puntaje_resena"])
    data["tarifa_ancianos"] = float(data["tarifa_ancianos"])
    data["tarifa_discapacitados"] = float(data["tarifa_discapacitados"])
    data["tarifa_ninos"] = float(data["tarifa_ninos"])
    data["tarifa_normal"] = float(data["tarifa_normal"])

    # Convertir los valores booleanos especificados a cadenas en mayúsculas
    boolean_keys = [
        "accesibilidad", "estacionamiento", "permiso_foto", "reserva_entrada",
        "servicio_biblioteca", "servicio_cafeteria", "servicio_guiado",
        "servicio_restaurante", "venta_objetos", "visita_virtual"
    ]

    for key in boolean_keys:
        data[key] = "TRUE" if data[key] else "FALSE"

    # Crear un nuevo diccionario con las claves en el orden especificado
    ordered_data = {
        "id_museo": data["id_museo"],  # 1
        "distrito": f'"{data["distrito"]["nombre"]}"',  # 2
        "puntaje_resena": data["puntaje_resena"],  # 3
        "ha_inicio": data["ha_inicio"],  # 4
        "ha_fin": data["ha_fin"],  # 5
        "hc_inicio": data["hc_inicio"],  # 6
        "hc_fin": data["hc_fin"],  # 7
        "tarifa_normal": data["tarifa_normal"],  # 8
        "tarifa_ninos": data["tarifa_ninos"],  # 9
        "tarifa_ancianos": data["tarifa_ancianos"],  # 10
        "tarifa_discapacitados": data["tarifa_discapacitados"],  # 11
        "reserva_entrada": data["reserva_entrada"],  # 12
        "servicio_restaurante": data["servicio_restaurante"],  # 13
        "servicio_cafeteria": data["servicio_cafeteria"],  # 14
        "servicio_guiado": data["servicio_guiado"],  # 15
        "servicio_biblioteca": data["servicio_biblioteca"],  # 16
        "venta_objetos": data["venta_objetos"],  # 17
        "accesibilidad": data["accesibilidad"],  # 18
        "permiso_foto": data["permiso_foto"],  # 19
        "estacionamiento": data["estacionamiento"],  # 20
        "visita_virtual": data["visita_virtual"],  # 21
        "n_restaurantes_prox": data["n_restaurantes_prox"],  # 22
        "n_atracciones_prox": data["n_atracciones_prox"],  # 23
        "telefono": data["telefono"],  # 24
        "email": data["email"],  # 25
        "sitio_web": data["sitio_web"],  # 26
        "pag_facebook": data["pag_facebook"],  # 27
        "pag_instagram": data["pag_instagram"],  # 28
        "pag_tiktok": data["pag_tiktok"]  # 29
    }

    # Agregar las categorías con valor True al nuevo diccionario
    categorias_true = [key for key, value in data_categoria.items() if value]
    ordered_data["categoria"] =  "".join([f'"{cat}"' for cat in categorias_true])

    # Agregar los días de atención con valor True al nuevo diccionario
    dias_atencion_true = [key for key, value in data_dia_atencion.items() if value]
    ordered_data["dia_atencion"] = "".join([f'"{dia}"' for dia in dias_atencion_true])

    # Agregar los días concurridos con valor True al nuevo diccionario
    dias_concurrido_true = [key for key, value in data_dia_concurrido.items() if value]
    ordered_data["dia_concurrido"] ="".join([f'"{dia}"' for dia in dias_concurrido_true])


    return ordered_data

# Llamar a la función y mostrar el resultado
ordered_data = procesar_datos(data, data_categoria, data_dia_atencion, data_dia_concurrido)
# Guardar el resultado en un archivo JSON
with open('resultado.json', 'w', encoding='utf-8') as f:
    json.dump(ordered_data, f, ensure_ascii=False, indent=4)

print("Datos guardados en resultado.json")

# Leer el archivo JSON y mostrar su contenido
#with open('resultado.json', 'r', encoding='utf-8') as f:
#    data = json.load(f)
#    print(json.dumps(data, ensure_ascii=False, indent=4))
    