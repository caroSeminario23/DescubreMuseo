import requests

class ExtraccionDatos:
    def __init__(self, url):
        self.url = url

    def obtener_museo(self, id_museo):
        respuesta = requests.get(f"{self.url}/get_museo/{id_museo}")

        if respuesta.status_code == 200:
            museo = respuesta.json()['data']
            return museo
        else:
            print(f"Error al obtener el museo {id_museo}", respuesta.json()['message'])
            return None
        
    def obtener_categoria_museo(self, id_categoria, id_museo):
        respuesta = requests.get(f"{self.url}/get_categoria_museo/{id_categoria}/{id_museo}")

        if respuesta.status_code == 200:
            categoria = respuesta.json()['data']
            return categoria
        else:
            print(f"Error al obtener la categoria {id_categoria}/{id_museo}", respuesta.json()['message'])
            return None
        
    def obtener_dia_atencion(self, id_museo, id_dia):
        respuesta = requests.get(f"{self.url}/get_dia_atencion/{id_museo}/{id_dia}")

        if respuesta.status_code == 200:
            dia_atencion = respuesta.json()['data']
            return dia_atencion
        else:
            print(f"Error al obtener el dia de atencion {id_museo}/{id_dia}", respuesta.json()['message'])
            return None
        
    def obtener_dia_concurrido(self, id_museo, id_dia):
        respuesta = requests.get(f"{self.url}/get_dia_concurrido/{id_museo}/{id_dia}")

        if respuesta.status_code == 200:
            dia_concurrido = respuesta.json()['data']
            return dia_concurrido
        else:
            print(f"Error al obtener el dia concurrido {id_museo}/{id_dia}", respuesta.json()['message'])
            return None
        
def extraer_json_por_museo(id_museo):
    url = "http://localhost:5000"
    extraccion = ExtraccionDatos(url)

    data_museo = extraccion.obtener_museo(id_museo)
    data_categorias = []
    dias_atencion = []
    dias_concurridos = []

    for i in range(1, 5):
        categoria = extraccion.obtener_categoria_museo(i, id_museo)
        if categoria:
            data_categorias.append(categoria['categoria']['nombre'])

    for i in range(1, 8):
        dia_atencion = extraccion.obtener_dia_atencion(id_museo, i)
        dia_concurrido = extraccion.obtener_dia_concurrido(id_museo, i)
        
        # Guardar en un arreglo los dias de atencion y concurridos (solo los nombres)
        if dia_atencion:
            dias_atencion.append(dia_atencion['dia']['nombre'])
        if dia_concurrido:
            dias_concurridos.append(dia_concurrido['dia']['nombre'])
    
    # Guardar los dias de dia_atencion en un diccionario que tenga como clave
    # los dias de la semana y como valor True o False si el museo atiende o no
    data_dia_atencion = {
        "Lunes": "Lunes" in dias_atencion,
        "Martes": "Martes" in dias_atencion,
        "Miercoles": "Miércoles" in dias_atencion,
        "Jueves": "Jueves" in dias_atencion,
        "Viernes": "Viernes" in dias_atencion,
        "Sabado": "Sabado" in dias_atencion,
        "Domingo": "Domingo" in dias_atencion
    }

    # Guardar los dias de dia_concurrido en un diccionario que tenga como clave
    # los dias de la semana y como valor True o False si el museo es concurrido o no
    data_dia_concurrido = {
        "Lunes": "Lunes" in dias_concurridos,
        "Martes": "Martes" in dias_concurridos,
        "Miercoles": "Miércoles" in dias_concurridos,
        "Jueves": "Jueves" in dias_concurridos,
        "Viernes": "Viernes" in dias_concurridos,
        "Sabado": "Sabado" in dias_concurridos,
        "Domingo": "Domingo" in dias_concurridos
    }
    
    return data_museo, data_categorias, data_dia_atencion, data_dia_concurrido

def main():
    id_museo = 1
    data_museo, data_categorias, data_dia_atencion, data_dia_concurrido = extraer_json_por_museo(id_museo)
    print(data_museo)
    print(data_categorias)
    print(data_dia_atencion)
    print(data_dia_concurrido)

if __name__ == "__main__":
    main()