import requests

#Obtener los museos recomendados (información básica)
def obtener_museos_recomendados(id_museos_recomendados):
    museos_info = []

    for id_museo in id_museos_recomendados:
        response = requests.get(f'http://localhost:5000/museo_routes/get_museo/{id_museo}')
        if response.status_code == 200:
            data = response.json().get('data', {})
            museo_info = {
                'nombre': data.get('nombre'),
                'distrito': data.get('distrito', {}).get('nombre'),
                'direccion': data.get('direccion')
            }
            museos_info.append(museo_info)
        else:
            print(f'Error al obtener el museo con id {id_museo}: {response.json().get("message")}')
    
    return museos_info

'''
[
    {
        'nombre': 'Museo Nacional de Arqueología',
        'distrito': 'San Borja',
        'direccion': 'Av. Javier Prado Este 2465, San Borja 15021'
    },
    {
        'nombre': 'Museo de Arte de Lima',
        'distrito': 'Lima',
        'direccion': 'Paseo Colón 125, Parque de la Exposición, Lima 15046'
    }
]
'''

def mostrar_opciones_museos_recomendados(id_museos_recomendados):
    museos_info = obtener_museos_recomendados(id_museos_recomendados)
    print("\n=====================================")
    print("          MUSEOS RECOMENDADOS          ")
    print("=====================================")
    for i, museo in enumerate(museos_info):
        print(f"{i + 1}. {museo['nombre']} - {museo['distrito']} - {museo['direccion']}")
    # Opción para salir
    print(f"{len(museos_info) + 1}. No deseo ver más información.")
    print("=====================================")
    print("Si desea más detalle sobre uno de estos museos, digite el número correspondiente o, en todo caso, la opción de salida (3).")
    opcion_usuario = input("Opción: ").strip()

    while not opcion_usuario.isdigit() or 1 > int(opcion_usuario) or int(opcion_usuario) > len(museos_info)+2:
        print("Opción inválida. Intente nuevamente.")
        opcion_usuario = input("Opción: ").strip() # Eliminar espacios en blanco al inicio y al final
    
    opcion_usuario = int(opcion_usuario)
    if opcion_usuario == len(museos_info) + 1:
        print("Gracias por su preferencia. Disfrute su visita.")
    else:
        id_museo = id_museos_recomendados[opcion_usuario - 1]
        mostrar_informacion_completa_museo(id_museo)

        print("Gracias por su preferencia. Disfrute su visita.")



def mostrar_informacion_completa_museo(id_museo):
    response = requests.get(f'http://localhost:5000/museo_routes/get_museo/{id_museo}')
    if response.status_code == 200:
        data = response.json().get('data', {})
        categorias_museo = buscar_categoria_asociada_al_museo(id_museo)
        print("\n===========================================")
        print(f"Información completa del museo recomendado\n")
        # Mostrar toda la información del museo línea por línea
        '''for key, value in data.items():
            print(f"{key}: {value}")'''
        mostrar_detalle_organizado(data, categorias_museo)
        
        print("\nInformación completa de museo.")
    else:
        print(f'Error al obtener el museo con id {id_museo}: {response.json().get("message")}')

def buscar_categoria_asociada_al_museo(id_museo):
    categorias = []
    for i in range(1, 5):
        try:
            respuesta = requests.get(f'http://localhost:5000/categoria_museo_routes/get_categoria_museo/{i}/{id_museo}')
            respuesta.raise_for_status()
            categoria = respuesta.json()['data']
            categorias.append(categoria['categoria']['nombre'])
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error de conexión: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Error en la solicitud: {err}")
    return categorias

def mostrar_detalle_organizado(data, categorias):
    print("NOMBRE: ", data.get('nombre'))

    if len(categorias) > 0:
        print("CATEGORÍAS: ", ', '.join(categorias))

    print("DISTRITO: ", data.get('distrito', {}).get('nombre'))
    print("DIRECCIÓN: ", data.get('direccion'))

    print("HORARIO DE ATENCION: ", data.get('ha_inicio'), " - ", data.get('ha_fin'))
    if data.get('hc_inicio') != None and data.get('hc_fin') != None:
        print("HORARIO CONCURRENCIA: ", data.get('hc_inicio'), " - ", data.get('hc_fin'))

    print("PUNTAJE DE RECOMENDACIÓN: ", data.get('puntaje_resena'))

    print("PRECIO DE TARIFA REGULAR: ", data.get('tarifa_normal'))
    if data.get('tarifa_ninos') != None:
        print("PRECIO DE TARIFA DE NIÑOS: ", data.get('tarifa_ninos'))
    if data.get('tarifa_ancianos') != None:
        print("PRECIO DE TARIFA DE ADULTOS MAYORES: ", data.get('tarifa_ancianos'))
    if data.get('tarifa_discapacitados') != None:
        print("PRECIO DE TARIFA DE DISCAPACITADOS: ", data.get('tarifa_discapacitados'))
    
    if data.get('reserva_entrada') == True:
        print("RESERVA DE ENTRADA: Sí")
    else:
        print("RESERVA DE ENTRADA: No")
        
    if data.get('servicio_restaurante') == True:
        print("SERVICIO DE RESTAURANTE: Sí")
    else:
        print("SERVICIO DE RESTAURANTE: No")

    if data.get('servicio_cafeteria') == True:
        print("SERVICIO DE CAFETERÍA: Sí")
    else:
        print("SERVICIO DE CAFETERÍA: No")

    if data.get('servicio_guiado') == True:
        print("SERVICIO DE GUIADO: Sí")
    else:
        print("SERVICIO DE GUIADO: No")
    
    if data.get('servicio_biblioteca') == True:
        print("SERVICIO DE BIBLIOTECA: Sí")
    else:
        print("SERVICIO DE BIBLIOTECA: No")
    
    if data.get('venta_objetos') == True:
        print("VENTA DE OBJETOS: Sí")
    else:
        print("VENTA DE OBJETOS: No")

    if data.get('accesibilidad') == True:
        print("OPCIONES DE ACCESIBILIDAD PARA PERSONAS CON DISCAPACIDAD: Sí")
    else:
        print("OPCIONES DE ACCESIBILIDAD PARA PERSONAS CON DISCAPACIDAD: No")
    
    if data.get('permiso_fotos') == True:
        print("PERMISO DE TOMAR FOTOS: Sí")
    else:
        print("PERMISO DE TOMAR FOTOS: No")

    if data.get('estacionamiento') == True:
        print("ESTACIONAMIENTO DISPONIBLE: Sí")
    else:
        print("ESTACIONAMIENTO DISPONIBLE: No")

    if data.get('visita_virtual') == True:
        print("VISITA VIRTUAL DISPONIBLE: Sí")
    else:
        print("VISITA VIRTUAL DISPONIBLE: No")

    if data.get('email') != None:
        print("EMAIL: ", data.get('email'))

    if data.get('telefono') != None:
        print("TELÉFONO DE CONTACTO: ", data.get('telefono'))
    
    if data.get('anexo') != None:
        print("ANEXO: ", data.get('anexo'))

    if data.get('sitio_web') != None:
        print("PÁGINA WEB: ", data.get('sitio_web'))

    if data.get('pag_facebook') != None:
        print("PÁGINA DE FACEBOOK: ", data.get('pag_facebook'))

    if data.get('pag_instagram') != None:
        print("PÁGINA DE INSTAGRAM: ", data.get('pag_instagram'))
    
    if data.get('pag_tiktok') != None:
        print("PÁGINA DE TIKTOK: ", data.get('pag_tiktok'))

    if data.get('n_restaurantes_prox') != None:
        print("NÚMERO DE RESTAURANTES CERCANOS: ", data.get('n_restaurantes_prox'))

    if data.get('n_atracciones_prox') != None:
        print("NÚMERO DE ATRACCIONES CERCANAS: ", data.get('n_atracciones_prox'))

    if data.get('notas') != None:
        print("NOTAS ADICIONALES: ", data.get('notas'))

#Mostrar la información básica de los museos recomendados
def mostrar_informacion_basica(id_museos_recomendados):
    museos_info = obtener_museos_recomendados(id_museos_recomendados)
    print("\nInformación básica de los museos recomendados:")
    for museo in museos_info:
        print(museo)

#Llamada a funcion mostrar info basica y Preguntar al usuario si desea ver la información completa de los museos recomendados
def preguntar_y_mostrar_informacion_completa(id_museos_recomendados):
    mostrar_informacion_basica(id_museos_recomendados)
    
    respuesta = input("¿Desea ver toda la información de los museos? (1 para sí, 2 para no): ").strip()
    
    if respuesta == '1':
        for id_museo in id_museos_recomendados:
            response = requests.get(f'http://localhost:5000/get_museo/{id_museo}')
            if response.status_code == 200:
                print(f"Información completa de los museos recomendados\n")
                data = response.json().get('data', {})
                print(data)
            else:
                print(f'Error al obtener el museo con id {id_museo}: {response.json().get("message")}')
    else:
        print("Proceso de recomendacion terminado.")