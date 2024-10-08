from flask import json
import requests

class ExtraccionDatos:
    def __init__(self, url):
        self.url = url

    def obtener_museo(self, id_museo):
        try:
            respuesta = requests.get(f"{self.url}/museo_routes/get_museo/{id_museo}")
            respuesta.raise_for_status()  # Verifica si hubo un error HTTP
            museo = respuesta.json()['data']
            return museo
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error de conexión: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Error en la solicitud: {err}")
        return None
        
    def obtener_categoria_museo(self, id_categoria, id_museo):
        try:
            respuesta = requests.get(f"{self.url}/categoria_museo_routes/get_categoria_museo/{id_categoria}/{id_museo}")
            respuesta.raise_for_status()
            categoria = respuesta.json()['data']
            return categoria
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error de conexión: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Error en la solicitud: {err}")
        return None
        
    def obtener_dia_atencion(self, id_museo, id_dia):
        try:
            respuesta = requests.get(f"{self.url}/dia_atencion_routes/get_dia_atencion/{id_museo}/{id_dia}")
            respuesta.raise_for_status()
            dia_atencion = respuesta.json()['data']
            return dia_atencion
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error de conexión: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Error en la solicitud: {err}")
        return None
        
    def obtener_dia_concurrido(self, id_museo, id_dia):
        try:
            respuesta = requests.get(f"{self.url}/dia_concurrido_routes/get_dia_concurrido/{id_museo}/{id_dia}")
            respuesta.raise_for_status()
            dia_concurrido = respuesta.json()['data']
            return dia_concurrido
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error de conexión: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Error en la solicitud: {err}")
        return None
        
def extraer_json_por_museo(id_museo):
    url = "http://localhost:5000"
    extraccion = ExtraccionDatos(url)

    museo = extraccion.obtener_museo(id_museo)
    categorias = []
    dias_atencion = []
    dias_concurridos = []

    # Obtener las categorías del museo
    for i in range(1, 5):
        categoria = extraccion.obtener_categoria_museo(i, id_museo)
        if categoria:
            categorias.append(categoria['categoria']['nombre'])

    # Guardar las categorías en un diccionario
    data_categorias = {
        "Temático": "Temático" in categorias,
        "Arqueológico": "Arqueológico" in categorias,
        "Arte": "Arte" in categorias,
        "Histórico": "Histórico" in categorias
    }

    # Obtener los días de atención y los días concurridos
    for i in range(1, 8):
        dia_atencion = extraccion.obtener_dia_atencion(id_museo, i)
        dia_concurrido = extraccion.obtener_dia_concurrido(id_museo, i)

        if dia_atencion:
            dias_atencion.append(dia_atencion['dia']['nombre'])
        if dia_concurrido:
            dias_concurridos.append(dia_concurrido['dia']['nombre'])
    
    # Guardar los días de atención en un diccionario
    data_dia_atencion = {
        "Lunes": "Lunes" in dias_atencion,
        "Martes": "Martes" in dias_atencion,
        "Miércoles": "Miércoles" in dias_atencion,
        "Jueves": "Jueves" in dias_atencion,
        "Viernes": "Viernes" in dias_atencion,
        "Sábado": "Sabado" in dias_atencion,
        "Domingo": "Domingo" in dias_atencion
    }

    # Guardar los días concurridos en un diccionario
    data_dia_concurrido = {
        "Lunes": "Lunes" in dias_concurridos,
        "Martes": "Martes" in dias_concurridos,
        "Miércoles": "Miércoles" in dias_concurridos,
        "Jueves": "Jueves" in dias_concurridos,
        "Viernes": "Viernes" in dias_concurridos,
        "Sábado": "Sabado" in dias_concurridos,
        "Domingo": "Domingo" in dias_concurridos
    }
    
    return museo, data_categorias, data_dia_atencion, data_dia_concurrido

def main():
    id_museo = 2
    data_museo, data_categorias, data_dia_atencion, data_dia_concurrido = extraer_json_por_museo(id_museo)
    print(data_museo)
    print(data_categorias)
    print(data_dia_atencion)
    print(data_dia_concurrido)

    # Guardar en archivos JSON
    with open('backend/procesamiento/archivos_JSON/data_museo.json', 'w') as file:
        json.dump(data_museo, file, indent=4)

    with open('backend/procesamiento/archivos_JSON/data_categorias.json', 'w') as file:
        json.dump(data_categorias, file, indent=4)

    with open('backend/procesamiento/archivos_JSON/data_dia_atencion.json', 'w') as file:
        json.dump(data_dia_atencion, file, indent=4)

    with open('backend/procesamiento/archivos_JSON/data_dia_concurrido.json', 'w') as file:
        json.dump(data_dia_concurrido, file, indent=4)

    print("Datos guardados correctamente")

if __name__ == "__main__":
    main()