data = {
    "accesibilidad": True,
    "anexo": None,
    "direccion": "Calle Retiro 160 - Miraflores",
    "distrito": {
        "nombre": "Miraflores"
    },
    "email": "info@museoamano.org",
    "estacionamiento": True,
    "ha_fin": "17:00:00",
    "ha_inicio": "10:00:00",
    "hc_fin": "14:00:00",
    "hc_inicio": "12:00:00",
    "id_distrito": 9,
    "id_museo": 1,
    "n_atracciones_prox": 295,
    "n_restaurantes_prox": 2229,
    "nombre": "Museo Textil Precolombino: AMANO",
    "notas": None,
    "pag_facebook": "",
    "pag_instagram": "https://www.instagram.com/museoamano/",
    "pag_tiktok": "https://www.tiktok.com/@museoamano",
    "permiso_foto": True,
    "puntaje_resena": "4.7",
    "reserva_entrada": False,
    "servicio_biblioteca": False,
    "servicio_cafeteria": True,
    "servicio_guiado": True,
    "servicio_restaurante": True,
    "sitio_web": "www.museoamano.org",
    "tarifa_ancianos": "25.00",
    "tarifa_discapacitados": "35.00",
    "tarifa_ninos": "15.00",
    "tarifa_normal": "35.00",
    "telefono": "4412909",
    "venta_objetos": True,
    "visita_virtual": False
}

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

# Convertir el valor de telefono a entero
#data["telefono"] = int(data["telefono"])

# Convertir los valores booleanos especificados a cadenas en mayúsculas
boolean_keys = [
    "accesibilidad", "estacionamiento", "permiso_foto", "reserva_entrada",
    "servicio_biblioteca", "servicio_cafeteria", "servicio_guiado",
    "servicio_restaurante", "venta_objetos", "visita_virtual"
]

for key in boolean_keys:
    data[key] = "TRUE" if data[key] else "FALSE"

# Convertir el diccionario en un arreglo de pares clave-valor
data_array = list(data.items())

print(data_array)