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

#Mostrar la información básica de los museos recomendados
def mostrar_informacion_basica(id_museos_recomendados):
    museos_info = obtener_museos_recomendados(id_museos_recomendados)
    print("Información básica de los museos recomendados:")
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