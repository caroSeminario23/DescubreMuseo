import requests

#Obtener los museos recomendados (información básica)
def obtener_museos_recomendados(id_museos_recomendados):
    museos_info = []

    for id_museo in id_museos_recomendados:
        response = requests.get(f'http://localhost:5000/get_museo/{id_museo}')
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
    print("Si desea más detalle sobre uno de estos museos, digite el número correspondiente.")
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
    response = requests.get(f'http://localhost:5000/get_museo/{id_museo}')
    if response.status_code == 200:
        data = response.json().get('data', {})
        print(f"Información completa del museo recomendado\n")
        # Mostrar toda la información del museo línea por línea
        for key, value in data.items():
            print(f"{key}: {value}")
        
        print("\nInformación completa de museo.")
    else:
        print(f'Error al obtener el museo con id {id_museo}: {response.json().get("message")}')

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